def init_database():
    names = ["Deanna Troi", "Wesley Crusher", "William Riker", "Liam Shaw", "T'Veen"]
    ranks = ["Lieutenant Commander", "Lieutenant", "Commander", "Captain", "Ensign"]
    divs = ["Command", "Operations", "Command", "Command", "Sciences",]
    ids = [101, 102, 103, 104, 105]

    return names, ranks, divs, ids

def display_menu():
    full_name = input("FULL NAME:")
    print("HELLO ", full_name)

    print("MENU:")
    print("1. Add Member")
    print("2. Remove Member")
    print("3. Update Rank")
    print("4. Display Roster")
    print("5. Search Crew")
    print("6. Filter By Divisions")
    print("7. Calculate Payroll")
    print("8. Count Officers")
    print("9. Exit")

    option = input("Select an Option:")

    return option

def add_member(names, ranks, divs, ids):
    new_name = input("NAME:")
    new_rank = input("RANK:")
    new_div = input("DIVISION:")
    new_id = int(input("ID:"))

    valid_ranks = ["Lieutenant Commander", "Lieutenant", "Commander", "Captain", "Ensign"]

    if new_rank not in valid_ranks:
        print("INVALID RANK")
        return 
    if new_id in ids:
        print("ID IS INVALID")
        return 
    
    names.append(new_name)
    ranks.append(new_rank)
    divs.append(new_div)
    ids.append(new_id) 

    print("NEW MEMBER ADDED SUCCESSFULLY")
    print("NAME:", new_name)
    print("RANK:", new_rank)
    print("DIVISION:", new_div)
    print("ID:", new_id)

def remove_member(names, ranks, divs, ids):
    rem = int(input("ID TO REMOVE: "))
    if rem in ids:
        idx = ids.index(rem)
        names.pop(idx)
        ranks.pop(idx)
        divs.pop(idx)
        ids.pop(idx)
    else: 
        print("ID NOT FOUND")

def update_rank(names, ranks, ids):
    update_id = int(input("ID TO UPDATE: "))
    if update_id not in ids: 
        print("ID NOT FOUND")
        return
    
    idx = ids.index(update_id)
    new_rank = input("INPUT NEW RANK: ")
    
    valid_ranks = ["Lieutenant Commander", "Lieutenant", "Commander", "Captain", "Ensign"]
     
    if new_rank not in valid_ranks:
        print("INVALID RANK")
        return
    ranks[idx] = new_rank
    print("RANK UPDATED SUCCESSFULLY")

def display_roster(names, ranks, divs, ids):
    print("ROSTER:")
    print("NAME - RANK - DIVISION - ID")

    for i in range(len(names)):
        print(names[i] + " - " + ranks[i] + " - " + divs[i] + " - " + str(ids[i]))
    