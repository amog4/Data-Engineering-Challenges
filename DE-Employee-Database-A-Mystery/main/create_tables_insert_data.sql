
create schema if not exists  employees_info;
set search_path = employees_info;

drop table employees;
drop table department;
drop table salaries;

-------------------------------------------------------------------------
create TABLE IF NOT EXISTS employees (

emp_no int PRIMARY KEY,
birth_day date,
first_name char(100),
last_name char(100),
gender char(100),
hire_date date
);


\copy employees_info.employees(emp_no,birth_day,first_name,last_name,gender,hire_date) FROM 
'/home/amogh/Documents/A-Mystery-in-Two-Parts-master/data/employees.csv'
DELIMITER ','
CSV HEADER;


-------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS department (

dept_no varchar(100) PRIMARY KEY,
dept_name varchar(100)
);

\copy employees_info.department(dept_no,dept_name) FROM '/home/amogh/Documents/A-Mystery-in-Two-Parts-master/data/departments.csv' DELIMITER ',' CSV HEADER;

-------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS titles(

emp_no int  REFERENCES employees(emp_no),
titles varchar(100),
from_date date,
to_date date
);

\copy employees_info.titles(emp_no,titles,from_date ,to_date) FROM '/home/amogh/Documents/A-Mystery-in-Two-Parts-master/data/titles.csv' DELIMITER ',' CSV HEADER;

-------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS dep_employees(

emp_no int REFERENCES employees(emp_no) ,
dept_no varchar(100) REFERENCES department(dept_no),
from_date date,
to_date date
);

\copy employees_info.dep_employees(emp_no,dept_no,from_date,to_date) FROM  '/home/amogh/Documents/A-Mystery-in-Two-Parts-master/data/dept_emp.csv' DELIMITER ',' CSV HEADER;

-------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS salaries(

emp_no int REFERENCES employees(emp_no),
salary varchar(100),
from_date date,
to_date date
);

\copy employees_info.salaries(emp_no ,salary  ,from_date,to_date) FROM  '/home/amogh/Documents/A-Mystery-in-Two-Parts-master/data/salaries.csv' DELIMITER ',' CSV HEADER;

-------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS department_managers(
dept_no varchar(100)  REFERENCES department(dept_no),
emp_no int REFERENCES employees(emp_no) ,
from_date date,
to_date date
);


\copy employees_info.department_managers(dept_no,emp_no,from_date,to_date ) FROM  '/home/amogh/Documents/A-Mystery-in-Two-Parts-master/data/dept_manager.csv' DELIMITER ',' CSV HEADER;








