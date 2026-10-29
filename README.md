# Experiment No. 1

## Aim/Title
Design and Conversion of ER Diagrams to Relational Tables for Two Real-World Scenarios.

## Theory

An Entity-Relationship (ER) diagram is a visual representation of entities, their attributes, and relationships within a database. Introduced by Peter Chen in 1976, ER diagrams help design databases systematically before converting them into relational tables.

The main components of ER diagrams are entities, attributes, relationships, and keys. Entities are represented by rectangles, attributes by ovals, and relationships by diamonds. Primary key attributes are underlined. Relationships are classified as one-to-one (1:1), one-to-many (1:N), and many-to-many (M:N).

During ER-to-relational conversion, each entity becomes a table, and its attributes become columns. Primary keys uniquely identify records, while foreign keys establish relationships between tables. In a 1:N relationship, the primary key of the parent table is added as a foreign key to the child table. M:N relationships require an associative table containing foreign keys from both participating tables. Composite keys combine multiple attributes to uniquely identify records.

For example, a college database may contain Student, Course, and Enrollment tables. Enrollment connects students and courses using their respective identifiers.

## Algorithm

1. Identify two real-world scenarios, such as a bank and a college.
2. Identify entities and their attributes.
3. Select primary keys for each entity.
4. Determine relationships and cardinalities.
5. Draw ER diagrams using standard notation.
6. Convert each entity into a relational table.
7. Add foreign keys for 1:N relationships.
8. Create associative tables for M:N relationships.
9. Define composite keys wherever required.
10. Verify the resulting schemas and key constraints.

## Conclusion

Successfully designed ER diagrams for two real-world scenarios and converted them into relational tables using primary keys, foreign keys, and composite keys to maintain relationships and data integrity.

---

# Experiment No. 2

## Aim/Title
Performing SQL DDL and DML with Constraints.

## Theory

SQL (Structured Query Language) is used to create, modify, and manipulate relational databases. DDL (Data Definition Language) defines database structures, while DML (Data Manipulation Language) manages the data stored within them.

Common DDL commands include CREATE, ALTER, DROP, and TRUNCATE. For example, `CREATE DATABASE a1;` creates a database, while `USE a1;` selects it. The `ALTER TABLE` command modifies an existing table's structure. DML commands include INSERT, UPDATE, and DELETE, which allow users to add, modify, and remove records.

SQL constraints enforce rules to maintain data integrity. NOT NULL prevents null values, UNIQUE ensures uniqueness, DEFAULT supplies a predefined value, and CHECK validates specified conditions. PRIMARY KEY uniquely identifies each record and cannot contain NULL values. FOREIGN KEY establishes relationships between tables and maintains referential integrity.

For example, `PRIMARY KEY (empno)` uniquely identifies employees, while `CHECK (salary >= 0)` prevents negative salaries. Constraints can be specified during table creation or added later using ALTER TABLE. These features help maintain reliable, consistent, and valid database records.

## Algorithm

1. Create a database using `CREATE DATABASE`.
2. Select it using `USE`.
3. Create tables without constraints.
4. Create tables with appropriate constraints.
5. Insert sample records using INSERT.
6. Verify constraint behaviour.
7. Add or modify columns using ALTER TABLE.
8. Add or remove constraints as required.
9. Remove records using TRUNCATE.
10. Remove tables using DROP TABLE.

## Conclusion

Successfully performed SQL DDL and DML operations and applied constraints to maintain data integrity, enforce validation rules, establish relationships, and manage database structures effectively.

## SQL / Implementation Code

```sql
CREATE DATABASE a1;
USE a1;
CREATE TABLE student (
rollno INT,
name VARCHAR(30)
);
INSERT INTO student VALUES
(1, 'Amit'),
(2, 'Rahul'),
(3, 'Sneha');
CREATE TABLE emp (
empno INT,
ename VARCHAR(20) NOT NULL,
job VARCHAR(10) NOT NULL,
deptno INT,
sal DECIMAL(7,2),
experience INT,
CONSTRAINT emp_pk PRIMARY KEY (empno),
CONSTRAINT emp_ck_empno CHECK (empno > 100)
);
ALTER TABLE emp
ADD COLUMN email VARCHAR(50);
ALTER TABLE emp
MODIFY COLUMN job VARCHAR(12);
ALTER TABLE emp
ADD CONSTRAINT emp_ck_experience CHECK (experience >= 0);
ALTER TABLE emp
DROP COLUMN email;
CREATE TABLE dept (
deptno INT PRIMARY KEY,
dname VARCHAR(10),
loc VARCHAR(10)
);
CREATE TABLE employee (
empno INT,
ename VARCHAR(25) NOT NULL,
job VARCHAR(15),
mgr INT,joindate DATE,
salary DECIMAL(7,2),
comm DECIMAL(7,2),
deptno INT,
CONSTRAINT emp_fk_dept
FOREIGN KEY (deptno) REFERENCES dept(deptno)
);
ALTER TABLE employee
ADD CONSTRAINT emp_uk_empno UNIQUE (empno);
ALTER TABLE employee
ALTER COLUMN job SET DEFAULT 'Employee';
ALTER TABLE employee
ADD CONSTRAINT emp_ck_salary CHECK (salary >= 0);
INSERT INTO dept VALUES
(12, 'computer', 'pune'),
(13, 'IT', 'mumbai'),
(14, 'HR', 'delhi');
INSERT INTO employee
(empno, ename, job, mgr, joindate, salary, comm, deptno)
VALUES
(23, 'shiv', 'manager', 55, '2019-09-12', 30000.00, 55.00, 12),
(24, 'rahul', 'developer', 55, '2020-05-15', 35000.00, 100.00, 12),
(25, 'sneha', 'analyst', 56, '2021-03-20', 28000.00, 75.00, 13);
SELECT * FROM student;
SELECT * FROM dept;
SELECT * FROM employee;
INSERT INTO employee
(empno, ename, mgr, joindate, salary, comm, deptno)
VALUES
(26, 'amit', 55, '2022-01-10', 25000.00, 50.00, 14);
INSERT INTO employee
(empno, ename, job, mgr, joindate, salary, comm, deptno)
VALUES
(27, 'test', 'developer', 55, '2023-01-10', -5000.00, 50.00, 12);
TRUNCATE TABLE employee;
DROP TABLE employee;
DROP TABLE dept;
DROP TABLE emp;
DROP TABLE student;
```

---

# Experiment No. 3

## Aim/Title

To Perform the Following Database Operations:

- Viewing All Databases
- Viewing All Tables in a Database
- Updating/Deleting Records in a Table

## Theory

A database is a structured collection of data that can be accessed, managed, and updated efficiently. A Database Management System (DBMS), such as MySQL, PostgreSQL, or SQLite, provides facilities to manage databases and their records. SQL is the standard language used to perform database operations.

The `SHOW DATABASES;` command displays all databases available on a MySQL server. The `USE database_name;` command selects a particular database, while `SHOW TABLES;` lists its tables. To retrieve records from a table, the SELECT statement is used. For example, `SELECT * FROM student;` displays all records from the student table.

The UPDATE command modifies existing records. Its syntax is `UPDATE table_name SET column_name = value WHERE condition;`. The DELETE command removes selected records using `DELETE FROM table_name WHERE condition;`. The WHERE clause specifies which records should be affected. Without it, UPDATE may modify every record, while DELETE may remove every record. Therefore, conditions must be checked carefully before executing these commands to avoid unintended data loss and maintain database accuracy.

## Algorithm

1. Open a DBMS client.
2. Connect to the database server.
3. Execute `SHOW DATABASES;`.
4. Select a database using `USE database_name;`.
5. Execute `SHOW TABLES;`.
6. View records using `SELECT * FROM table_name;`.
7. Update records using the UPDATE command.
8. Delete selected records using the DELETE command.
9. Verify the changes using SELECT queries.

## Conclusion

Successfully performed database operations to view databases and tables, retrieve records, update existing data, and delete selected records using SQL commands and appropriate conditions.

## SQL / Implementation Code

```sql
CREATE DATABASE IF NOT EXISTS a1;
USE a1;
CREATE TABLE IF NOT EXISTS student (
rollno INT PRIMARY KEY,
name VARCHAR(30),
branch VARCHAR(20),
marks INT
);
INSERT INTO student (rollno, name, branch, marks) VALUES
(1, 'Amit', 'CSE', 78),
(2, 'Rahul', 'AIML', 85),
(3, 'Sneha', 'CSE', 91),
(4, 'Priya', 'AIML', 72),
(5, 'Rohan', 'CSE', 88);
SHOW DATABASES;
USE a1;
SHOW TABLES;
SELECT * FROM student;
UPDATE student
SET marks = 90
WHERE rollno = 2;
UPDATE student
SET branch = 'AIML', marks = 80
WHERE rollno = 4;
SELECT * FROM student;
DELETE FROM student
WHERE rollno = 5;
SELECT * FROM student;
```

---

# Experiment No. 4

## Aim/Title

To Perform the Following Database Operations:

- Altering a Table
- Dropping, Truncating, and Renaming Tables
- Backing Up and Restoring a Database

## Theory

SQL provides commands to modify database structures, remove data, rename tables, and perform backup and restoration operations. These operations are essential for database maintenance, structural modifications, and data recovery.

The ALTER TABLE command changes an existing table's structure without necessarily deleting its data. Columns can be added, modified, or removed using appropriate ALTER TABLE statements. For example, `ALTER TABLE student ADD email VARCHAR(50);` adds a new column.

The DROP TABLE command permanently removes a table and its structure, whereas TRUNCATE TABLE removes all records while retaining the table structure. The RENAME TABLE command changes an existing table's name. For example, `RENAME TABLE student TO student_details;` renames the table.

Database backups preserve data for recovery in case of accidental deletion or system failure. In MySQL, `mysqldump -u username -p database_name > backup_file.sql` creates a backup file. Restoration can be performed using `mysql -u username -p database_name < backup_file.sql`. These operations require careful execution, especially when deleting tables or modifying important database structures.

## Algorithm

1. Open a DBMS tool and connect to the database server.
2. Select the database using `USE database_name;`.
3. Modify table structures using ALTER TABLE.
4. Add, modify, or remove columns as required.
5. Remove all records using TRUNCATE TABLE.
6. Remove a table using DROP TABLE.
7. Rename a table using RENAME TABLE.
8. Create a database backup using mysqldump.
9. Restore the database using the backup file.
10. Verify the operations using appropriate SQL commands.

## Conclusion

Successfully performed table alteration, deletion, truncation, and renaming operations, along with database backup and restoration, demonstrating essential techniques for database maintenance and recovery.

## SQL / Implementation Code

```sql
CREATE DATABASE IF NOT EXISTS a1;
USE a1;
CREATE TABLE employee (
emp_id INT PRIMARY KEY,
emp_name VARCHAR(50),
department VARCHAR(30),
salary DECIMAL(10,2)
);
INSERT INTO employee VALUES
(1, 'Amit', 'CSE', 45000),
(2, 'Rahul', 'AIML', 50000),
(3, 'Sneha', 'CSE', 55000),
(4, 'Priya', 'HR', 40000);
SELECT * FROM employee;
ALTER TABLE employee
ADD COLUMN email VARCHAR(100);
ALTER TABLE employee
MODIFY COLUMN emp_name VARCHAR(60);
ALTER TABLE employee
DROP COLUMN email;
SELECT * FROM employee;
RENAME TABLE employee TO staff;
SELECT * FROM staff;
TRUNCATE TABLE staff;
SELECT * FROM staff;
INSERT INTO staff VALUES
(1, 'Amit', 'CSE', 45000),
(2, 'Rahul', 'AIML', 50000),
(3, 'Sneha', 'CSE', 55000);
SELECT * FROM staff;
RENAME TABLE staff TO employee;
SELECT * FROM employee;DROP TABLE employee;
SHOW TABLES;
Backup Command: mysqldump -u root -p a1 > a1_backup.sql
Restore Command: mysql -u root -p a1 < a1_backup.sql
```

---

# Experiment No. 5

## Aim/Title
Experiment: SQL Queries with Aggregate, Date, String, Math, and Set Operations

## Theory

SQL provides built-in functions and operators to retrieve, manipulate, summarize, and compare data efficiently. Aggregate functions calculate summary values from multiple records. COUNT() counts records, SUM() calculates totals, AVG() computes averages, while MAX() and MIN() identify maximum and minimum values.

The GROUP BY clause groups records based on common values, whereas HAVING filters groups according to specified conditions. For example, `SELECT discount, COUNT(*) FROM product GROUP BY discount HAVING COUNT(*) > 1;` displays discount groups containing more than one record.

Date functions such as DAY(), MONTH(), YEAR(), and DATEDIFF() extract date components or calculate differences between dates. String functions, including UPPER(), LOWER(), CONCAT(), SUBSTR(), and REPLACE(), manipulate textual data. Mathematical functions such as ROUND(), FLOOR(), CEILING(), POWER(), and SQRT() perform numerical calculations.

Set operators combine or compare the results of multiple SELECT queries. UNION combines results and removes duplicates, while INTERSECT returns common records and EXCEPT returns records present in the first result but absent from the second. The queries must have compatible column counts and corresponding data types. These functions simplify data analysis and reporting.

## Algorithm

1. Create a product table with suitable columns.
2. Insert sample product records.
3. Execute aggregate queries using COUNT(), SUM(), AVG(), MAX(), and MIN().
4. Group records using GROUP BY.
5. Filter grouped results using HAVING.
6. Execute date functions such as DAY() and DATEDIFF().
7. Apply string functions such as UPPER() and CONCAT().
8. Perform calculations using ROUND(), FLOOR(), and POWER().
9. Execute set operations such as UNION.
10. Examine and verify the query results.

## Conclusion

Successfully executed SQL queries using aggregate, date, string, mathematical, and set operations to summarize data, manipulate values, perform calculations, and combine query results effectively.

## SQL / Implementation Code

```sql
CREATE DATABASE a1;
USE a1;
CREATE TABLE product (
id INT PRIMARY KEY,
pname VARCHAR(50),
pprice DECIMAL(8,2),
discount INT,
created DATE
);
INSERT INTO product VALUES
(1, 'AMIT', 2000, 100, '2025-07-01'),
(2, 'CORNFLAKES', 800, 50, '2025-06-15'),
(3, 'PARLE', 90, 5, '2025-05-20'),
(4, 'NESTLE', 70, 2, '2025-04-10'),
(5, 'CADBURY', 100, 10, '2025-03-05');
SELECT * FROM product;
SELECT
COUNT(id) AS numProducts,
SUM(pprice) AS totalPrice,
AVG(pprice) AS avgPrice,
MAX(discount) AS maxDisc,
MIN(pprice) AS minPrice
FROM product;
SELECT
discount,
COUNT(*) AS cnt,
AVG(pprice) AS avgPrice
FROM product
GROUP BY discount
HAVING COUNT(*) > 1;
SELECT
DAY(created) AS day,
MONTH(created) AS month,
YEAR(created) AS year,
DATEDIFF(CURDATE(), created) AS daysOld
FROM product;
SELECT
UPPER(pname) AS upperName,
LOWER(pname) AS lowerName,
CONCAT(pname, '_2025') AS tag,SUBSTR(pname, 1, 3) AS prefix,
REPLACE(pname, 'PAR', 'KIT') AS replacedName
FROM product;
SELECT
ROUND(pprice * 0.9, 2) AS discountedPrice,
POWER(pprice, 2) AS priceSquared,
FLOOR(pprice / 100) * 100 AS floorHundred
FROM product;
SELECT pname
FROM product
WHERE discount > 50
UNION
SELECT pname
FROM product
WHERE pprice < 100;
SELECT pname
FROM product
WHERE discount >= 5
INTERSECT
SELECT pname
FROM product
WHERE pprice < 100;
SELECT pname
FROM product
WHERE discount >= 5
EXCEPT
SELECT pname
FROM product
WHERE pprice < 100;
SELECT
ROUND(AVG(pprice), 2) AS averagePrice,
ROUND(AVG(discount), 2) AS averageDiscount
FROM product;
```

---

# Experiment No. 6

## Aim/Title

Demonstrating SQL Join Queries – Inner, Outer, Left, and Right Joins.

## Theory

SQL JOIN combines rows from two or more tables based on related columns. Joins help retrieve meaningful information stored across multiple tables in a relational database.

An **Equi-Join or Inner Join** uses the equality operator (`=`) to retrieve records with matching values in both tables. A **Non-Equi Join** uses relational operators such as `<`, `>`, `<=`, and `>=` to match records based on conditions, such as salary ranges. A **Self-Join** joins a table with itself, for example, to associate employees with their managers.

Outer joins also retrieve unmatched records. A **Left Join** returns all records from the left table and matching records from the right table. A **Right Join** returns all records from the right table and matching records from the left table. A **Full Outer Join** returns matched and unmatched records from both tables.

Example syntax:

```sql
SELECT e.ename, d.dname
FROM emp e
INNER JOIN dept d
ON e.dept = d.deptno;
```

In database systems without direct Full Outer Join support, a combination of LEFT JOIN, RIGHT JOIN, and UNION can be used to simulate its behaviour.

## Algorithm

1. Connect to the database.
2. Create and populate the required tables.
3. Execute an Inner Join to retrieve matching records.
4. Perform a Non-Equi Join using range conditions.
5. Execute a Self-Join to relate employees and managers.
6. Perform a Left Join to retrieve all left-table records.
7. Perform a Right Join to retrieve all right-table records.
8. Simulate a Full Outer Join using UNION where required.
9. Execute complex queries involving employees, departments, and projects.
10. Verify and analyse the query results.

## Conclusion

Successfully implemented SQL joins, including inner, non-equi, self, left, right, and full outer joins, to combine related records and analyse data across multiple relational tables.

## SQL / Implementation Code

```sql
CREATE DATABASE a1;
USE a1;
CREATE TABLE dept (
deptno INT PRIMARY KEY,
dname VARCHAR(30),
loc VARCHAR(30)
);
CREATE TABLE emp (
empno INT PRIMARY KEY,
ename VARCHAR(30),
job VARCHAR(30),
mgr INT,
salary DECIMAL(10,2),
dept INT,
FOREIGN KEY (dept) REFERENCES dept(deptno)
);
CREATE TABLE salgrade (
grade INT PRIMARY KEY,
losal DECIMAL(10,2),
hisal DECIMAL(10,2)
);
INSERT INTO dept VALUES
(10, 'Accounts', 'Pune'),
(20, 'Research', 'Mumbai'),
(30, 'Sales', 'Delhi'),
(40, 'IT', 'Bangalore');
INSERT INTO emp VALUES
(101, 'Scott', 'Manager', NULL, 80000, 10),
(102, 'Amit', 'Developer', 101, 60000, 40),
(103, 'Rahul', 'Developer', 101, 55000, 40),
(104, 'Sneha', 'Analyst', 101, 45000, 20),
(105, 'Priya', 'Sales Executive', 101, 35000, 30),
(106, 'Rohan', 'Intern', 102, 20000, 40);
INSERT INTO salgrade VALUES
(1, 10000, 29999),
(2, 30000, 49999),
(3, 50000, 69999),
(4, 70000, 99999);
CREATE TABLE customers (
custID INT PRIMARY KEY,cust_name VARCHAR(50),
city VARCHAR(30)
);
CREATE TABLE orders (
orderID INT PRIMARY KEY,
custID INT,
order_date DATE,
amount DECIMAL(10,2),
FOREIGN KEY (custID) REFERENCES customers(custID)
);
INSERT INTO customers VALUES
(1, 'Customer A', 'Pune'),
(2, 'Customer B', 'Mumbai'),
(3, 'Customer C', 'Delhi'),
(4, 'Customer D', 'Nashik');
INSERT INTO orders VALUES
(101, 1, '2026-01-10', 5000),
(102, 2, '2026-01-15', 7500),
(103, 1, '2026-02-05', 3000),
(104, 3, '2026-02-20', 9000);
CREATE TABLE department (
DNO INT PRIMARY KEY,
DNAME VARCHAR(50),
MGRSSN INT
);
CREATE TABLE employee (
SSN INT PRIMARY KEY,
NAME VARCHAR(50),
DNO INT,
SALARY DECIMAL(10,2),
FOREIGN KEY (DNO) REFERENCES department(DNO)
);
CREATE TABLE project (
PNO INT PRIMARY KEY,
PNAME VARCHAR(50),
DNO INT,
FOREIGN KEY (DNO) REFERENCES department(DNO)
);
CREATE TABLE works_on (
SSN INT,
PNO INT,
HOURS DECIMAL(5,2),
PRIMARY KEY (SSN, PNO),
FOREIGN KEY (SSN) REFERENCES employee(SSN),FOREIGN KEY (PNO) REFERENCES project(PNO)
);
INSERT INTO department VALUES
(10, 'Accounts', 1001),
(20, 'Research', 1004),
(30, 'Sales', 1005),
(40, 'IT', 1002);
INSERT INTO employee VALUES
(1001, 'Scott', 10, 80000),
(1002, 'Amit', 40, 60000),
(1003, 'Rahul', 40, 55000),
(1004, 'Sneha', 20, 45000),
(1005, 'Priya', 30, 35000);
INSERT INTO project VALUES
(1, 'IoT', 40),
(2, 'Banking System', 10),
(3, 'Research Portal', 20),
(4, 'Sales Analytics', 30);
INSERT INTO works_on VALUES
(1002, 1, 20),
(1003, 1, 15),
(1001, 2, 10),
(1004, 3, 25),
(1005, 4, 30);
SELECT
e.empno,
e.ename,
e.dept,
d.deptno,
d.loc,
d.dname
FROM emp e
INNER JOIN dept d
ON e.dept = d.deptno;
SELECT
e.ename,
e.salary,
s.grade
FROM emp e
INNER JOIN salgrade s
ON e.salary >= s.losal
AND e.salary <= s.hisal;
SELECT
worker.ename AS employee,manager.ename AS manager
FROM emp worker
INNER JOIN emp manager
ON worker.mgr = manager.empno;
SELECT
o.orderID,
c.cust_name,
c.city
FROM orders o
LEFT JOIN customers c
ON o.custID = c.custID;
SELECT
o.orderID,
c.cust_name,
c.city
FROM orders o
RIGHT JOIN customers c
ON o.custID = c.custID;
SELECT
o.orderID,
c.cust_name,
c.city
FROM orders o
LEFT JOIN customers c
ON o.custID = c.custID
UNION
SELECT
o.orderID,
c.cust_name,
c.city
FROM orders o
RIGHT JOIN customers c
ON o.custID = c.custID;
SELECT DISTINCT p.PNO
FROM project p
JOIN department d
ON p.DNO = d.DNO
JOIN employee e
ON d.MGRSSN = e.SSN
WHERE e.NAME = 'Scott'
UNION
SELECT DISTINCT w.PNO
FROM project p
JOIN works_on w
ON p.PNO = w.PNO
JOIN employee e
ON w.SSN = e.SSNWHERE e.NAME = 'Scott';
SELECT
e.NAME,
1.1 * e.SALARY AS INCREASED_SALARY
FROM employee e
JOIN works_on w
ON e.SSN = w.SSN
JOIN project p
ON w.PNO = p.PNO
WHERE p.PNAME = 'IoT';
SELECT
SUM(e.SALARY) AS TOTAL_SALARY,
MAX(e.SALARY) AS MAX_SALARY,
MIN(e.SALARY) AS MIN_SALARY,
AVG(e.SALARY) AS AVG_SALARY
FROM employee e
JOIN department d
ON e.DNO = d.DNO
WHERE d.DNAME = 'Accounts';
SELECT
e.ename,
d.dname,
e.salary
FROM emp e
JOIN dept d
ON e.dept = d.deptno;
SELECT
d.dname,
COUNT(e.empno) AS employee_count,
AVG(e.salary) AS average_salary
FROM emp e
RIGHT JOIN dept d
ON e.dept = d.deptno
GROUP BY d.deptno, d.dname;
```

---

# Experiment No. 7

## Aim/Title

To perform SQL query that demonstrate following-Search conditions, Summary queries, Sub- queries, Subqueries- with IN clause, With EXISTS clause.

## Theory

SQL provides various techniques to retrieve and analyse database records efficiently. **Search conditions** filter records using the WHERE clause and comparison, logical, and pattern-matching operators. For example, `SELECT * FROM employees WHERE salary > 50000;` retrieves employees earning more than 50,000.

**Summary queries** use aggregate functions such as COUNT(), SUM(), AVG(), MAX(), and MIN() to calculate useful statistics. The GROUP BY clause groups records according to specified columns, enabling summaries such as average salary per department.

A **subquery** is a query nested inside another SQL query. It allows the outer query to use results obtained from the inner query. For example, `SELECT * FROM employees WHERE salary > (SELECT AVG(salary) FROM employees);` retrieves employees earning above the average salary.

The **IN clause** checks whether a value matches any value returned by a list or subquery. The **EXISTS clause** checks whether a subquery returns at least one row. It is particularly useful for correlated subqueries that refer to the outer query.

These techniques support complex filtering, data summarisation, and efficient retrieval of records based on multiple conditions.

## Algorithm

1. Connect to the database.
2. Execute search queries using the WHERE clause.
3. Apply comparison and logical operators to filter records.
4. Execute summary queries using aggregate functions.
5. Group records using GROUP BY.
6. Write a subquery to retrieve data using nested conditions.
7. Execute a query using the IN clause.
8. Execute a query using the EXISTS clause.
9. Display and verify the query results.

## Conclusion

Successfully executed SQL search conditions, summary queries, and subqueries using IN and EXISTS clauses to filter records, calculate statistics, and retrieve data efficiently.

## SQL / Implementation Code

```sql
CREATE DATABASE a1;
USE a1;
CREATE TABLE departments (
department_id INT PRIMARY KEY,
department_name VARCHAR(50),
location VARCHAR(50)
);
CREATE TABLE employees (
employee_id INT PRIMARY KEY,
employee_name VARCHAR(50),
salary DECIMAL(10,2),
department_id INT,
FOREIGN KEY (department_id) REFERENCES departments(department_id)
);
INSERT INTO departments VALUES
(1, 'IT', 'Pune'),
(2, 'HR', 'New York'),
(3, 'Finance', 'Mumbai'),
(4, 'Sales', 'New York'),
(5, 'Marketing', 'Delhi');
INSERT INTO employees VALUES
(101, 'Amit', 60000, 1),
(102, 'Rahul', 75000, 1),
(103, 'Sneha', 50000, 2),
(104, 'Priya', 65000, 2),
(105, 'Rohan', 45000, 3),
(106, 'Neha', 80000, 3),
(107, 'Karan', 55000, 4),
(108, 'Anjali', 70000, 4),
(109, 'Vikas', 40000, 5),
(110, 'Pooja', 90000, 1);
SELECT * FROM employees
WHERE salary > 60000
AND department_id = 1;
SELECT * FROM employees
WHERE salary >= 50000
AND salary <= 80000;
SELECT * FROM employees
WHERE employee_name LIKE 'A%';SELECT * FROM employees
WHERE department_id = 1
OR department_id = 2;
SELECT * FROM employees
WHERE NOT department_id = 3;
SELECT
COUNT(*) AS total_employees,
SUM(salary) AS total_salary,
AVG(salary) AS average_salary,
MAX(salary) AS maximum_salary,
MIN(salary) AS minimum_salary
FROM employees;
SELECT
department_id,
COUNT(*) AS employee_count,
SUM(salary) AS total_salary,
AVG(salary) AS average_salary,
MAX(salary) AS maximum_salary,
MIN(salary) AS minimum_salary
FROM employees
GROUP BY department_id;
SELECT
department_id,
COUNT(*) AS employee_count,
AVG(salary) AS average_salary
FROM employees
GROUP BY department_id
HAVING AVG(salary) > 60000;
SELECT *
FROM employees
WHERE salary > (
SELECT AVG(salary)
FROM employees
);
SELECT *
FROM employees
WHERE department_id IN (
SELECT department_id
FROM departments
WHERE location = 'New York'
);
SELECT *
FROM employees e
WHERE EXISTS (SELECT 1
FROM departments d
WHERE d.department_id = e.department_id
AND d.location = 'New York'
);
SELECT *
FROM employees e
WHERE EXISTS (
SELECT 1
FROM departments d
WHERE d.department_id = e.department_id
AND d.department_name = 'HR'
);
SELECT *
FROM employees
WHERE department_id IN (
SELECT department_id
FROM departments
WHERE department_name IN ('IT', 'Finance')
);
SELECT *
FROM employees e
WHERE EXISTS (
SELECT 1
FROM departments d
WHERE d.department_id = e.department_id
);
SELECT
e.employee_name,
e.salary,
d.department_name,
d.location
FROM employees e
JOIN departments d
ON e.department_id = d.department_id
WHERE e.salary > (
SELECT AVG(salary)
FROM employees
);
```

---

# Experiment No. 8

## Aim/Title

Write and execute PL/SQL stored procedure and function to perform a suitable task on the database. Demonstrate its use.

## Theory

PL/SQL is Oracle's procedural extension to SQL that supports variables, conditional statements, loops, and modular programming. It enables developers to implement business logic directly within the database.

A **stored procedure** is a named PL/SQL program unit that performs specific operations. It can accept input parameters and execute database modifications, calculations, or other tasks. For example, a procedure can increase employee salaries by a specified percentage.

A **function** is similar to a procedure but returns a value. Functions are useful for calculations and can be called from SQL queries when their operations and return types permit it.

In this experiment, a stored procedure named `IncreaseSalary` can update employee salaries according to a department identifier and percentage. A function named `GetAvgSalary` can calculate and return the average salary for a specified department.

Procedures and functions improve code reusability, maintainability, and consistency by centralising business logic. They can also reduce repeated application-side processing because operations execute on the database server. PL/SQL programs are created using `CREATE OR REPLACE PROCEDURE` or `CREATE OR REPLACE FUNCTION` and executed using appropriate PL/SQL statements.

## Algorithm

1. Connect to the Oracle database.
2. Identify the employee table and required columns.
3. Create the `IncreaseSalary` stored procedure.
4. Define department and percentage input parameters.
5. Implement the salary update operation.
6. Create the `GetAvgSalary` function.
7. Define the department identifier as its input parameter.
8. Calculate and return the department's average salary.
9. Execute the procedure for a selected department.
10. Call the function and display the average salary.
11. Verify the updated employee records.

## Conclusion

Successfully created and executed PL/SQL stored procedures and functions to update employee salaries and calculate departmental average salaries, demonstrating reusable database programming and centralised business logic.

## PL/SQL / Implementation Code

```sql
SET SERVEROUTPUT ON;

-- STEP 1: Drop existing objects if they exist

BEGIN
    EXECUTE IMMEDIATE 'DROP PROCEDURE IncreaseSalary';
EXCEPTION
    WHEN OTHERS THEN
        IF SQLCODE != -4043 THEN
            RAISE;
        END IF;
END;
/

BEGIN
    EXECUTE IMMEDIATE 'DROP FUNCTION GetAvgSalary';
EXCEPTION
    WHEN OTHERS THEN
        IF SQLCODE != -4043 THEN
            RAISE;
        END IF;
END;
/

BEGIN
    EXECUTE IMMEDIATE 'DROP TABLE employees CASCADE CONSTRAINTS';
EXCEPTION
    WHEN OTHERS THEN
        IF SQLCODE != -942 THEN
            RAISE;
        END IF;
END;
/

-- STEP 2: Create employee table

CREATE TABLE employees (
    emp_id NUMBER PRIMARY KEY,
    emp_name VARCHAR2(50),
    department_id NUMBER,
    salary NUMBER(10,2)
);

-- STEP 3: Insert sample employee records

INSERT INTO employees VALUES (1, 'Amit', 10, 30000);
INSERT INTO employees VALUES (2, 'Rahul', 10, 40000);
INSERT INTO employees VALUES (3, 'Priya', 10, 50000);
INSERT INTO employees VALUES (4, 'Sneha', 20, 35000);
INSERT INTO employees VALUES (5, 'Rohit', 20, 45000);

COMMIT;

-- STEP 4: Create stored procedure to increase salaries

CREATE OR REPLACE PROCEDURE IncreaseSalary (
    p_department_id IN NUMBER,
    p_percentage IN NUMBER
)
AS
BEGIN
    UPDATE employees
    SET salary = salary + (salary * p_percentage / 100)
    WHERE department_id = p_department_id;

    DBMS_OUTPUT.PUT_LINE(
        'Salary updated for department ' || p_department_id
    );

    DBMS_OUTPUT.PUT_LINE(
        'Percentage increase: ' || p_percentage || '%'
    );

    DBMS_OUTPUT.PUT_LINE(
        'Employees updated: ' || SQL%ROWCOUNT
    );
END;
/

-- STEP 5: Create function to calculate average salary

CREATE OR REPLACE FUNCTION GetAvgSalary (
    p_department_id IN NUMBER
)
RETURN NUMBER
AS
    v_avg_salary NUMBER;
BEGIN
    SELECT AVG(salary)
    INTO v_avg_salary
    FROM employees
    WHERE department_id = p_department_id;

    RETURN v_avg_salary;
END;
/

-- STEP 6: Execute procedure and function

DECLARE
    v_average_salary NUMBER;
BEGIN
    IncreaseSalary(10, 10);

    v_average_salary := GetAvgSalary(10);

    DBMS_OUTPUT.PUT_LINE(
        'Average salary of department 10: ' ||
        TO_CHAR(v_average_salary, 'FM999999990.00')
    );
END;
/

-- STEP 7: Display updated employee records

SELECT * FROM employees ORDER BY emp_id;

-- STEP 8: Display average salary of each department

SELECT department_id, AVG(salary) AS average_salary
FROM employees
GROUP BY department_id
ORDER BY department_id;
```

---

# Experiment No. 9

## Aim/Title

Write and execute suitable database triggers considering row-level and statement-level triggers.

## Theory

A database trigger is a stored program that automatically executes when a specified database event occurs. Common triggering events include INSERT, UPDATE, and DELETE operations. Triggers help maintain data integrity, enforce business rules, and record database activities for auditing.

A **row-level trigger** executes separately for every row affected by a SQL statement. It is useful when individual changes must be monitored, such as recording an employee's salary update. In Oracle PL/SQL, row-level triggers commonly use the `FOR EACH ROW` clause and can access old and new column values through `:OLD` and `:NEW`.

A **statement-level trigger** executes once for the entire SQL statement, regardless of how many rows it affects. It is useful for recording that an operation occurred on a table.

For example, an audit table can store information about database changes, including the affected employee, action performed, and timestamp. Triggers can automatically insert audit records whenever specified operations occur.

The behaviour and syntax of triggers vary between database systems. Testing triggers with sample data helps verify that they execute correctly and record the expected information.

## Algorithm

1. Connect to the database.
2. Create the employees table.
3. Create an audit_log table.
4. Insert sample employee records.
5. Create a row-level trigger for salary updates.
6. Configure the trigger to record individual row changes.
7. Create a statement-level trigger where supported.
8. Execute UPDATE statements on the employees table.
9. Query the audit_log table.
10. Verify the trigger-generated audit records.

## Conclusion

Successfully implemented and tested row-level and statement-level database triggers to monitor employee table operations and record audit information, demonstrating automatic event handling and database activity tracking.

## SQL / Implementation Code

```sql
-- Step 1: Create the Database
CREATE DATABASE company_db;
USE company_db;

-- Step 2: Create the Employees Table
CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    name VARCHAR(50),
    salary DECIMAL(10,2),
    dept VARCHAR(30)
);

-- Step 3: Create the Audit Log Table
CREATE TABLE audit_log (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    emp_id INT NULL,
    action VARCHAR(100),
    log_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Step 4: Insert Sample Data
INSERT INTO employees VALUES
(1, 'Alice', 50000, 'HR'),
(2, 'Bob', 60000, 'IT');

-- Step 5: Create a Row-Level Trigger for Salary Updates
DELIMITER //

CREATE TRIGGER trg_row_salary_update
AFTER UPDATE ON employees
FOR EACH ROW
BEGIN
    IF OLD.salary <> NEW.salary THEN
        INSERT INTO audit_log (emp_id, action)
        VALUES (NEW.emp_id, 'Salary updated');
    END IF;
END //

DELIMITER ;

-- Step 6: Create a Row-Level Trigger for General Updates
DELIMITER //

CREATE TRIGGER trg_row_statement_update
AFTER UPDATE ON employees
FOR EACH ROW
BEGIN
    INSERT INTO audit_log (emp_id, action)
    VALUES (NEW.emp_id, 'Employee record updated');
END //

DELIMITER ;

-- Step 7: Test the Triggers

-- Update Alice's salary
UPDATE employees
SET salary = salary + 1000
WHERE emp_id = 1;

-- Update Bob's department
UPDATE employees
SET dept = 'Finance'
WHERE emp_id = 2;

-- Update multiple employees
UPDATE employees
SET salary = salary + 500
WHERE dept IN ('HR', 'Finance');

-- Step 8: Display Employee Records
SELECT * FROM employees;

-- Step 9: Display Audit Logs
SELECT * FROM audit_log;
```

---

# Experiment No. 10

## Aim/Title

Create a MongoDB Document and Implement CRUD Operations on It.

## Theory

MongoDB is a NoSQL database that stores data in a document-oriented format called BSON (Binary JSON). Unlike relational databases, which organise data into tables and rows, MongoDB stores documents inside collections. Documents contain field-value pairs and can represent structured or nested data.

CRUD refers to the four fundamental database operations: Create, Read, Update, and Delete. **Create** inserts new documents into a collection using methods such as `insertOne()` and `insertMany()`. **Read** retrieves documents using methods such as `find()` and `findOne()`. **Update** modifies existing documents using methods such as `updateOne()` and `updateMany()`. **Delete** removes documents using `deleteOne()` and `deleteMany()`.

MongoDB Shell, accessed through the `mongosh` command, allows users to interact with databases using JavaScript-based commands. For example, `db.employees.insertOne({name: "Alice", salary: 50000})` inserts an employee document into the employees collection.

The `use company` command selects the company database, creating it when data is first stored. MongoDB also supports filtering, projections, and update operators such as `$set` and `$inc`, enabling flexible document management.

## Algorithm

1. Start the MongoDB service.
2. Connect using MongoDB Shell or Compass.
3. Select the database using `use company`.
4. Create the employees collection.
5. Insert sample employee documents.
6. Retrieve documents using `find()`.
7. Filter records using query conditions.
8. Update selected documents using `updateOne()` or `updateMany()`.
9. Delete documents using `deleteOne()` or `deleteMany()`.
10. Verify the results of all CRUD operations.

## Conclusion

Successfully created a MongoDB database and implemented CRUD operations on employee documents, demonstrating document storage, data retrieval, conditional updates, and deletion using MongoDB Shell commands.


mongosh experiment10.js

## MongoDB / Implementation Code

```javascript
db = db.getSiblingDB("company");

if (!db.getCollectionNames().includes("employees")) {
    db.createCollection("employees");
}

db.employees.deleteMany({});

db.employees.insertMany([
    {
        emp_id: 101,
        name: "Alice",
        department: "HR",
        salary: 50000
    },
    {
        emp_id: 102,
        name: "Bob",
        department: "IT",
        salary: 60000
    },
    {
        emp_id: 103,
        name: "Charlie",
        department: "Finance",
        salary: 55000
    }
]);

print("\n--- CREATE: All inserted employees ---");
db.employees.find().forEach(printjson);

print("\n--- READ: IT department employees ---");
db.employees.find({ department: "IT" }).forEach(printjson);

print("\n--- READ: Employee names and salaries ---");
db.employees.find(
    {},
    { _id: 0, name: 1, salary: 1 }
).forEach(printjson);

db.employees.updateOne(
    { emp_id: 103 },
    { $set: { salary: 58000 } }
);

db.employees.updateMany(
    { department: "IT" },
    { $inc: { salary: 2000 } }
);

print("\n--- UPDATE: Employees after salary changes ---");
db.employees.find().forEach(printjson);

db.employees.deleteOne({ emp_id: 101 });

db.employees.deleteMany({ department: "HR" });

print("\n--- DELETE: Remaining employees ---");
db.employees.find().forEach(printjson);

print("\nExperiment completed successfully.");

```
