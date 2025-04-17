listdata=[]
def search_by_qualification():
    input_qualification = input("Please enter qualification to check student details: ").lower()
    found = False

    for student in listdata:
        for q in student["qualification"]:
            if q["qualificationname"].lower() == input_qualification:
                print("Student found:")
                print(student)
                found = True
                break

    if not found:
        print("No student found with the given qualification.")