SELECT citationid_2,id_1,paper_title,year_of_publication,venue
FROM citation NATURAL JOIN research_paper WHERE research_paper.id=citation.id_1
ORDER BY citationid_2 ASC