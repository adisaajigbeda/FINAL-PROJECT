VALID_IDS = ["RE49762358", "PR156125", "OF45461", "RE68566547", "PR156984" ]

def is_valid_id(e_id):
    if len(e_id) > 10:
        print("Error: Employee ID may not be more than 10 characters long.")
        return False
    elif e_id not in VALID_IDS:
        print("Error: Invalid employee ID. Not found in system. ")
        return False
    return True