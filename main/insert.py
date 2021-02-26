import psycopg2

conn = psycopg2.connect(host="localhost",
    database="postgres",
    user="postgres",
    port = 5433,
    password="amogh")


cur = conn.cursor()

cur.execute(r"""copy employees_info.employees(emp_no,birth_day,first_name,last_name,gender,hire_date) FROM 
'/home/amogh/Documents/A-Mystery-in-Two-Parts-master/data/employees.csv'
DELIMITER ','
CSV HEADER;""")
