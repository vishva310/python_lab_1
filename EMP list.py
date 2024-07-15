EMPNAME = ["A", "B", "C", "D", "E"]

def add_employee(name):
    EMPNAME.append(name)
    print(f"Added {name} to EMPNAME list.")


def remove_employee(name):
    if name in EMPNAME:
        EMPNAME.remove(name)
        print(f"Removed {name} from EMPNAME list.")
    else:
        print(f"{name} is not in EMPNAME list.")


def append_employee(name):
    EMPNAME.append(name)
    print(f"Appended {name} to EMPNAME list.")


def main():
    print("Initial EMPNAME list:", EMPNAME)
    
   
    add_employee("F")
    print("After adding 'F':", EMPNAME)
    
   
    remove_employee("B")
    print("After removing 'B':", EMPNAME)
    
   
    append_employee("G")
    print("After appending 'G':", EMPNAME)

if __name__ == "__main__":
    main()