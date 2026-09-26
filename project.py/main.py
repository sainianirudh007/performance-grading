from student import Student

from result_utils import (
    find_student,
    show_topper,
    show_all,
    save_students,
    load_students
)


# Load existing students from text file
students = load_students()


while True:

    print("\n==============================================")
    print("       STUDENT RESULT MANAGEMENT SYSTEM")
    print("==============================================")

    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Show Topper")
    print("7. Exit")

    print("==============================================")

    choice = input("Enter your choice: ")


    # -----------------------------------------
    # 1. ADD STUDENT
    # -----------------------------------------

    if choice == "1":

        name = input("Enter student name: ")

        roll_no = int(input("Enter roll number: "))


        # Check duplicate roll number
        if find_student(students, roll_no):

            print("Roll number already exists!")

            continue


        marks = []


        for i in range(5):

            mark = int(
                input(f"Enter marks for subject {i + 1}: ")
            )

            marks.append(mark)


        student = Student(name, roll_no, marks)

        students.append(student)


        # Save data to text file
        save_students(students)


        print("\nStudent added successfully!")
        print("Data saved to students.txt")


    # -----------------------------------------
    # 2. DISPLAY ALL STUDENTS
    # -----------------------------------------

    elif choice == "2":

        show_all(students)


    # -----------------------------------------
    # 3. SEARCH STUDENT
    # -----------------------------------------

    elif choice == "3":

        roll_no = int(
            input("Enter roll number: ")
        )


        student = find_student(students, roll_no)


        if student:

            student.display()

        else:

            print("Student not found.")


    # -----------------------------------------
    # 4. UPDATE MARKS
    # -----------------------------------------

    elif choice == "4":

        roll_no = int(
            input("Enter roll number: ")
        )


        student = find_student(students, roll_no)


        if student:

            print("\nEnter new marks:")


            for i in range(5):

                student.marks[i] = int(
                    input(
                        f"Enter marks for subject {i + 1}: "
                    )
                )


            # Save updated data
            save_students(students)


            print("\nMarks updated successfully!")
            print("Data saved to students.txt")


        else:

            print("Student not found.")


    # -----------------------------------------
    # 5. DELETE STUDENT
    # -----------------------------------------

    elif choice == "5":

        roll_no = int(
            input("Enter roll number: ")
        )


        student = find_student(students, roll_no)


        if student:

            students.remove(student)


            # Save updated list
            save_students(students)


            print("\nStudent deleted successfully!")
            print("Data updated in students.txt")


        else:

            print("Student not found.")


    # -----------------------------------------
    # 6. SHOW TOPPER
    # -----------------------------------------

    elif choice == "6":

        show_topper(students)


    # -----------------------------------------
    # 7. EXIT
    # -----------------------------------------

    elif choice == "7":

        # Save before exiting
        save_students(students)

        print("\nData saved successfully.")
        print("Thank you for using the system!")

        break


    # -----------------------------------------
    # INVALID CHOICE
    # -----------------------------------------

    else:

        print("Invalid choice!")
        print("Please enter a number from 1 to 7.")