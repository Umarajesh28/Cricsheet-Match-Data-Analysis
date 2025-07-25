import os
import zipfile
import json
import pandas as pd
from multiprocessing import Pool

# Define directories
source_directory = r"C:\Users\user\Desktop\DS_Capstone_Projects\DS_Cricsheet_Match_Analysis\Final Submission\Scripts\cricket_downloads"
csv_directory = os.path.join(source_directory, "csv_files")

os.makedirs(csv_directory, exist_ok=True)

def extract_zip_files(zip_filepath, output_dir):
    """Extract a single zip file."""
    with zipfile.ZipFile(zip_filepath, 'r') as zip_file:
        extract_path = os.path.join(output_dir, os.path.splitext(os.path.basename(zip_filepath))[0])
        os.makedirs(extract_path, exist_ok=True)
        zip_file.extractall(extract_path)
        print(f"Extracted: {zip_filepath} to {extract_path}")
    return extract_path

def preprocess_dataframe(dataframe):
    """Clean and preprocess the DataFrame."""
    dataframe.columns = [
        col.replace('meta.', '')
           .replace('info.', '')
           .replace('outcome.', 'outcome_')
           .replace('event.', 'event_')
           .replace('officials.', 'officials_')
           .replace('.', '_')
           .replace('info.', '')
           .replace('registry.people.', '')
           .replace('players.', 'players_')
           .replace('.', '_')
        for col in dataframe.columns
    ]

    dataframe.columns = ['_'.join(col.split('.')[-2:]) for col in dataframe.columns]

    for col in dataframe.columns:
        dataframe[col] = dataframe[col].apply(lambda x: str(x) if isinstance(x, (list, dict)) else x)

    dataframe.fillna({
        'player_of_match': 'Unknown',
        'result': 'No Result'
    }, inplace=True)

    missing_value_threshold = 0.5 * len(dataframe)
    dataframe.dropna(axis=1, thresh=missing_value_threshold, inplace=True)

    dataframe.drop_duplicates(inplace=True)

    if 'dates' in dataframe.columns:
        dataframe['dates'] = pd.to_datetime(dataframe['dates'], errors='coerce')

    return dataframe

def process_json_file(json_filepath):
    """Process a single JSON file and return a cleaned DataFrame."""
    try:
        with open(json_filepath, 'r') as json_file:
            match_json = json.load(json_file)
            dataframe = pd.json_normalize(match_json)
            dataframe = preprocess_dataframe(dataframe)
            return dataframe
    except (json.JSONDecodeError, KeyError) as e:
        print(f"Error processing {json_filepath}: {e}")
        return pd.DataFrame()

def process_json_data(input_dir):
    """Process JSON files and return cleaned DataFrames for the match type."""
    json_filepaths = [
        os.path.join(input_dir, json_filename)
        for json_filename in os.listdir(input_dir)
        if json_filename.endswith(".json")
    ]

    # Process JSON files in parallel using multiprocessing Pool
    with Pool() as pool:
        match_dfs = pool.map(process_json_file, json_filepaths)

    return pd.concat(match_dfs, ignore_index=True) if match_dfs else pd.DataFrame()

if __name__ == "__main__":
    # Comment out ODI and Test sections
    for file in ["odis_json.zip", "t20s_json.zip", "tests_json.zip"]:
         # Step 1: Extract zip file
        zip_path = os.path.join(source_directory, file)
        if not os.path.exists(zip_path):
            print(f" File not found: {zip_path}")
            continue

        extracted_path = extract_zip_files(zip_path, source_directory)

        # Step 2: Process JSON files into a cleaned DataFrame
        cleaned_dataframe = process_json_data(extracted_path)

        # Step 3: Save the cleaned DataFrame as a CSV with a custom name
        csv_name = file.replace(".zip", ".csv")
        csv_filepath = os.path.join(csv_directory, csv_name)
        cleaned_dataframe.to_csv(csv_filepath, index=False)
        print(f"Saved {csv_name} to {csv_filepath}")

