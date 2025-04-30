def is_valid_wage(e_wage):
    
            
    
    
    if e_wage < 0:
    
        print ("Error: Wage must be greater than 0.")
        return False
    elif e_wage > 45.50: 
        print ("Error: Wage may not be greater than $45.50.")
        return False
    return True