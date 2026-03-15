from db import get_connection

def highest_salary():
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("""SELECT id,name,department,salary FROM EMPLOYEES WHERE salary = (SELECT MAX(salary) FROM EMPLOYEES)""")
    employees = cursor.fetchall()
    cursor.close()
    conn.close()
    return employees
def lowest_salary():
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("""SELECT id,name,department,salary FROM EMPLOYEES WHERE salary = (SELECT MIN(salary) FROM EMPLOYEES)""")
    employees=cursor.fetchall()
    cursor.close()
    conn.close()
    return employees
