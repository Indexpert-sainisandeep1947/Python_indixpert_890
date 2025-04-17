listdata=[]
def view_all_students():
    if not listdata:
        print("No student records found.\n")
        return

    for student in listdata:
        print(f"ID: {student['id']}")
        print(f"Name: {student['name']}")
        print(f"Contact: {student['contact']}")
        print(f"Email: {student['email']}")
        print("Qualifications:")
        for q in student["qualification"]:
            print(f" {q['qualificationname']} (Year: {q['passingyear']})")
        