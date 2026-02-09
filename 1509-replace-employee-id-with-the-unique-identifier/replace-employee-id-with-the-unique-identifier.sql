SELECT Emp.unique_id , E.name
FROM Employees E
LEFT JOIN EmployeeUNI Emp
ON E.id = Emp.id ;