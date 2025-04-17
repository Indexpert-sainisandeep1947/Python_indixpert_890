# import registrationstudent
# import viewallstudent
# import searchbyqualification
# import searchbycontact_no
# def main_menu():
#     while True:
#         print("\n--- Student Management System ---")
#         print("Press 1 to Registration Student")
#         print("Press 2 to View All Student Details")
#         print("Press 3 to Search Student by Qualification")
#         print("press 4 to search student by contact no")
#         print("Press 0 to Exit")

#         choice = input("Enter your choice: ")

#         if choice == "1":
#             registrationstudent.register_multiple_students()
#         elif choice == "2":
#             viewallstudent.view_all_students()
#         elif choice == "3":
#             searchbyqualification.search_by_qualification()
#         elif choice == "4":
#             searchbycontact.sesearch_by_contact()    
#         elif choice == "0":
#             print("Exiting program. Goodbye!")
#             break
#         else:
#             print("Invalid choice. Please enter 1, 2, 3 or 4.")

# # Main execution
# main_menu()

import registrationstudent
import viewallstudent
import searchbyqualification
import searchbycontact_no

def main_menu():
    while True:
        print("\n--- Student Management System ---")
        print("Press 1 to Register Student")
        print("Press 2 to View All Student Details")
        print("Press 3 to Search Student by Qualification")
        print("Press 4 to Search Student by Contact No")
        print("Press 0 to Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            registrationstudent.register_multiple_students()
        elif choice == "2":
            viewallstudent.view_all_students()
        elif choice == "3":
            searchbyqualification.search_by_qualification()
        elif choice == "4":
            searchbycontact_no.search_by_contact()  # Function name correct kiya
        elif choice == "0":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3 or 4.")

# Main execution
main_menu()




























