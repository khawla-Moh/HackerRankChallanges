    /*
Enter your query below.
Please append a semicolon ";" at the end of the query
*/  

SELECT s.roll_number ,s.name
from student_information s
join examination_marks m ON s.roll_number=m.roll_number
GROUP BY m.roll_number
HAVING SUM(m.subject_one+m.subject_two+m.subject_three) <100;