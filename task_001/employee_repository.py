from db import get_connection, create_tables
from validation import validation
def add_employee(employee):
    if validation(employee):
        conn=get_connection()
        cursor=conn.cursor()
        cursor.execute("""INSERT INTO EMPLOYEES (id,name,department,salary) VALUES(:1,:2,:3,:4)""",(employee["id"],employee["name"],employee["department"],employee["salary"]))
        conn.commit()
        cursor.close()
        conn.close()
        print("Employee added succesfully")
