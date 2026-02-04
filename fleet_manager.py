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

    option = input("Select an Option:")

    return option
    

