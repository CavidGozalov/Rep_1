from employee_repository import add_employee
from department_statistics import lowest_salary,highest_salary
from db import get_connection,create_tables
from validation import validation

def main():
    create_tables()
    while True:
        print("\nChoose an option:")
        print("1. Add employee")
        print("2. Show highest salary")
        print("3. Show lowest salary")
        print("4. Exit")

        choice=input("Input choice: ")

        if choice == "1":
            employee_id=int(input("Enter ID: "))
            employee_name=input("Enter name: ")
            employee_department=input("Enter department: ")
            employee_salary=int(input("Enter salary: "))

            employee={
                "id":employee_id,"name":employee_name,"department":employee_department,"salary":employee_salary
            }
            add_employee(employee)

        elif choice == "2":
            result=highest_salary()
            if result:
                print("The highest salary employee: ",result)
            else:
                print("No employees found.")
        elif choice == "3":
            result=lowest_salary()
            if result:
                print("The lowest salary employee: ",result)
            else:
                print("No employees found.")
        
        elif choice == "4":
            print("Exiting program...")
            break
        else:print('Invalid choice')
if __name__=="__main__":
    main()