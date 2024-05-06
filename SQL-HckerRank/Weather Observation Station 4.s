/*
Enter your query here.
*/
select COUNT(CITY) -COUNT(DISTINCT (CITY))
from STATION