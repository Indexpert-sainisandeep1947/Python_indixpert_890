import json
import os

# List to store all student data temporarily
listdata = []

# Function to register a single student
def register_student():
    student_data = {}
    student_data["id"] = int(input("Please enter student ID: "))
    student_data["name"] = input("Please enter student name: ")
    student_data["contact"] = int(input("Please enter student contact number: "))
    student_data["email"] = input("Please enter the email: ")

    # Input qualifications
    qualification_list = []
    while True:
        qualification_data = {}
        qualification_data["qualificationname"] = input("Qualification of student: ")
        qualification_data["passingyear"] = input("Please enter the passing year: ")
        qualification_list.append(qualification_data)

        ask_qualification = input("Add more qualification? (yes/no): ").lower()
        if ask_qualification != "yes":
            break

    student_data["qualification"] = qualification_list

    # Load existing data from file if it exists
    if os.path.exists("students.json"):
        with open("students.json", "r") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = []
    else:
        data = []

    # Append new student and save back to file
    data.append(student_data)
    with open("students.json", "w") as file:
        json.dump(data, file, indent=4)

    # Optional: store in listdata too
    listdata.append(student_data)

    print("Student registered successfully.\n")

# Function to register multiple students
def register_multiple_students():
    while True:
        register_student()
        inputdata = input("Add more registrations? (yes/no): ").lower()
        if inputdata != "yes":
            break

# To run:
# register_multiple_students()
