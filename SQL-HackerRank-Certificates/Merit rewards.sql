/*
Enter your query below.
Please append a semicolon ";" at the end of the query
*/
SELECT e.employee_ID, e.name
FROM employee_information e
JOIN last_quarter_bonus l ON l.employee_ID = e.employee_ID
WHERE e.division LIKE 'HR'
AND l.bonus >= 5000
