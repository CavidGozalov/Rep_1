import oracledb
def get_connection():
    return oracledb.connect(
        user="cavid19",
        password="12345",
        dsn="localhost/orcl21c222"
    )
def create_tables():
    try:
        conn=get_connection()
        cursor=conn.cursor()
        cursor.execute("""CREATE TABLE EMPLOYEES(
                       ID NUMBER PRIMARY KEY,
                       NAME VARCHAR2(50),
                       DEPARTMENT VARCHAR2(50),
                       SALARY NUMBER)""")
        conn.commit()
    except:
        print("Table 'employees' already exists, skipping.")
    conn.commit()
    cursor.close()
    conn.close()
