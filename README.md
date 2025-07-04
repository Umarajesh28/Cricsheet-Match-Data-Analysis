# Cricsheet Match Data Analysis

This project involves end-to-end analysis of international cricket match data from Cricsheet.org. The analysis includes scraping, cleaning, structuring, querying, and visualizing data using Python, SQL, and Power BI.

## Project Objective

To analyze historical cricket match data (ODI, T20, Test) and extract insights related to player performance, team wins, match outcomes, and trends across formats using interactive dashboards.

## Tools and Technologies

| Tool          | Purpose                                      |
|---------------|----------------------------------------------|
| Python        | Web scraping (Selenium), JSON transformation (Pandas) |
| SQLite / SQL  | Database creation, querying, and analytics   |
| Power BI      | Interactive dashboards and visual storytelling |


## Data Source

Data is sourced from the public domain at [https://cricsheet.org](https://cricsheet.org), which provides structured JSON files for international cricket matches.

## Key Analysis Areas

### Player Analysis
- Top players based on Player of the Match awards
- Player trends across different match formats

### Team Performance
- Most successful teams across formats
- Win distribution across seasons

### Match Outcome Analysis
- Win type distribution (runs, wickets)
- Comparative analysis across formats

## Power BI Dashboard Overview

| Page | Title                      | Description |
|------|----------------------------|-------------|
| 1    | Match Overview             | Summary of total matches, match formats, seasons, cities |
| 2    | Player Performance         | Player of the Match awards and format-based player insights |
| 3    | Team Performance           | Team-wise win count and seasonal win patterns |
| 4    | Win/Loss Analysis          | Win types, win/loss trends across match formats |
| 5    | Key Highlights             | Summary KPIs for players, teams, win types, and match growth trends |

## Features

- Web scraping of JSON data using Selenium
- Transformation of nested JSON using Python
- Structured storage and querying with SQLite and SQL
- Rich, multi-page Power BI dashboard with slicers and visual variety
- Analysis focused on team trends, player performance, and match outcomes

## Deliverables

- Cleaned and transformed CSV files
- SQL queries for analysis
- Python notebooks and scripts
- Final `.pbix` Power BI dashboard
- Documentation and project explanation

## Author

Uma Rajesh  

## License

This project is intended for academic and learning purposes. The dataset used is open-source and available via Cricsheet.org.

