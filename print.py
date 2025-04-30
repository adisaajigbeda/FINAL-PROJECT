def print_employees():
    with open("employees.dat", "r") as file:
        print("GTC1305 Company".center(60))
        print("Employee Report".center(60))
        print(f"{'Employee Name':<18}{'Identification number':<25}{'Wage':<10}")
        print("-" * 60)
        for line in file:
            
            line = line.strip()
            if not line:
                continue
            
           
            last_name, first_name, e_id, wage = line.split(", ")
            wage = wage.strip("$")  
            
          
            print(f"{last_name} {first_name:<15} {e_id:<25} ${wage:>7}")


print_employees()