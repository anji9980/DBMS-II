SELECT id_1,citationid_2,paper_title,year_of_publication,venue
FROM citation NATURAL JOIN research_paper WHERE research_paper.id=citation.citationid_2
ORDER BY id_1 ASC