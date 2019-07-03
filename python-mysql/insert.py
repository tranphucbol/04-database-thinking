import mysql.connector

cnx = mysql.connector.connect(user='root', password='password', host='127.0.0.1', database='company')
cursor = cnx.cursor()

add_employee = ("INSERT INTO employees (name) VALUES (%(name)s)")

data_employee = {'name': 'Phuc dep trai'}

cursor.execute(add_employee, data_employee)
emp_no = cursor.lastrowid

cnx.commit()

cursor.close()
cnx.close()