SELECT outcome_by_runs, city, season
FROM odi_matches
WHERE outcome_by_runs IS NOT NULL
ORDER BY outcome_by_runs DESC
LIMIT 10;

SELECT overs, COUNT(*) AS match_count
FROM odi_matches
WHERE overs IS NOT NULL
GROUP BY overs
ORDER BY match_count DESC;


SELECT city, COUNT(*) AS match_count
FROM odi_matches
WHERE city IS NOT NULL
GROUP BY city
ORDER BY match_count DESC
LIMIT 10;
    
        SELECT player_of_match, COUNT(*) AS awards_count
        FROM odi_matches
        WHERE player_of_match IS NOT NULL
        GROUP BY player_of_match
        ORDER BY awards_count DESC
        LIMIT 10;
   
   
        SELECT player_of_match, COUNT(*) AS wickets_count
        FROM odi_matches
        WHERE player_of_match IS NOT NULL
        GROUP BY player_of_match
        ORDER BY wickets_count DESC
        LIMIT 10;
    
	
        SELECT player_of_match, COUNT(*) AS awards_count
        FROM test_matches
        WHERE player_of_match IS NOT NULL
        GROUP BY player_of_match
        ORDER BY awards_count DESC
        LIMIT 10;
    
	
        SELECT city, COUNT(*) AS match_count
        FROM test_matches
        WHERE city IS NOT NULL
        GROUP BY city
        ORDER BY match_count DESC
        LIMIT 10;
    
	
        SELECT outcome_winner, COUNT(*) AS win_count
        FROM test_matches
        WHERE outcome_winner IS NOT NULL
        GROUP BY outcome_winner
        ORDER BY win_count DESC
        LIMIT 10;
    
	
        SELECT outcome_by_runs, city, season
        FROM test_matches
        WHERE outcome_by_runs IS NOT NULL
        ORDER BY outcome_by_runs DESC
        LIMIT 10;
    
	
        SELECT player_of_match, COUNT(*) AS awards_count
        FROM test_matches
        WHERE player_of_match IS NOT NULL
        GROUP BY player_of_match
        ORDER BY awards_count DESC
        LIMIT 10;
    
	
        SELECT player_of_match, COUNT(*) AS awards_count
        FROM t20_matches
        WHERE player_of_match IS NOT NULL
        GROUP BY player_of_match
        ORDER BY awards_count DESC
        LIMIT 10;
    
	
        SELECT outcome_winner, COUNT(*) AS win_count
        FROM t20_matches
        WHERE outcome_winner IS NOT NULL
        GROUP BY outcome_winner
        ORDER BY win_count DESC
        LIMIT 10;
    
	
        SELECT match_id, outcome_by_wickets, season
        FROM t20_matches
        WHERE outcome_by_wickets IS NOT NULL
        ORDER BY outcome_by_wickets ASC
        LIMIT 10;
   
   
        SELECT gender, COUNT(*) AS match_count
        FROM t20_matches
        GROUP BY gender
        ORDER BY match_count DESC;
    
