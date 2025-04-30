from is_valid_id import is_valid_id
from is_valid_wage import is_valid_wage

FILENAME = "employees.dat"  

def main():
    file = open(FILENAME, "w")
    while True:
        e_id =  input("Enter employe Id (type 'done' when finished): ")
        if e_id == "done":
            break
        if not is_valid_id(e_id):
            continue
        first_name = input("Enter employee FIRST name: ")
        last_name = input("Enter employee LAST name: ")
        while True:
            e_wage = float(input("Enter employee hourly wage: "))
            if is_valid_wage(e_wage):
                    break
            
        record = (f"\n{first_name}, {last_name}, {e_id}, ${e_wage:.2f}")
        file.write(record)
        print("Employee data recorded. ")
    file.close()
    print("Data entry complete. File saved as 'employees.dat'.")
    
main()