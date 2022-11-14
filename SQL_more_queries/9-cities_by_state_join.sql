-- lists all cities contained in the database hbtn_0d_usa.
SELECT t1.id, t1.name, t2.name
FROM cities t1
LEFT JOIN states t2
ON t1.state_id = t2.id
ORDER BY t1.id ASC;
