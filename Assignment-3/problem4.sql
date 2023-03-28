SELECT citationid_2, COUNT(*) as n FROM citation
GROUP BY citationid_2
ORDER BY n DESC
LIMIT 20;