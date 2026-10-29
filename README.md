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

```
