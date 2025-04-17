import viewallstudent

def search_by_contact():
    contact_no = input("Enter contact number to search: ")

    found = False
    for student in viewallstudent.students:
        if student.get("contact") == contact_no:
            print("\n--- Student Found ---")
            for key, value in student.items():
                print(f"{key.capitalize()}: {value}")
            found = True
            break

    if not found:
        print("No student found with this contact number.")

















