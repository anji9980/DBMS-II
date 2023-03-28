SELECT citation.id_1,b.citationid_2
FROM citation JOIN citation AS b
ON citation.citationid_2 =b.id_1