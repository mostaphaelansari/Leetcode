SELECT e2.unique_id, e1.name FROM Employees e1
LEFT JOIN EmployeeUNI e2 
ON e2.id = e1.id;