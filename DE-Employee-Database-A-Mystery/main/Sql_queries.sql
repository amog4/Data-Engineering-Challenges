/* List the following details of each employee: employee number, last name, first name, gender, and salary. */


set search_path = employees_info;

select 
	e.emp_no  as "employee number",
	first_name as "first name",
	last_name  as "last name",
	gender,
	s.salary
from employees e 
	join salaries s on 
		e.emp_no = s.emp_no 


/* List employees who were hired in 1986. */
		
		
select * from employees where date_part('year',hire_date) = '1986'


/* List the manager of each department with the following information: 
 * 	department number, 
 * department name, the manager's employee number, last name, first name, and start and end employment dates. */


select  dm.dept_no,
		d.dept_name ,
		dm.emp_no,
		e.first_name ,
		e.last_name ,
		dm.from_date ,
		dm.to_date 
from department_managers dm left join
	department d on 
	dm.dept_no = d.dept_no
	join employees e on 
	dm.emp_no = e.emp_no 

/*4.List the department of each employee with the following information: employee number, last name, first name, and department name. */ 
	

select 
	de.dept_no,
	e.first_name ,
	e.last_name ,
	d.dept_name
from dep_employees de 
	left join 
	department d on de.dept_no = d.dept_no 
	join employees e on 
	e.emp_no = de.emp_no 

/* List all employees whose first name is "Hercules" and last names begin with "B." */
	
	
select * from employees e  where first_name 
		like 'Hercules%' and last_name like 'B%'

/* List all employees in the Sales department, including their employee number, last name, first name, and department name. */
		
select 
	e.emp_no,
	e.first_name ,
	e.last_name ,
	d.dept_name
from dep_employees de 
	left join 
	department d on de.dept_no = d.dept_no 
	join employees e on 
	e.emp_no = de.emp_no 
	where d.dept_name = 'Sales'
	
/* List all employees in the Sales and Development departments, including their employee number, last name, first name, and department name. */
select  
	e.emp_no,
	e.first_name ,
	e.last_name ,
	d.dept_name
from dep_employees de 
	left join 
	department d on de.dept_no = d.dept_no 
	join employees e on 
	e.emp_no = de.emp_no 
	where d.dept_name in ('Sales','Development');
	
	

/*In descending order, list the frequency count of employee last names, i.e., how many employees share each last name.	*/
	
select last_name,count(last_name) as freq from employees e 
group by last_name

	


	

