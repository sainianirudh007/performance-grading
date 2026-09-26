from student import Student


FILE_NAME = "students.txt"


def find_student(students, roll_no):
    for student in students:
        if student.roll_no == roll_no:
            return student

    return None


def save_students(students):
    with open(FILE_NAME, "w") as file:

        for student in students:

            marks = ",".join(map(str, student.marks))

            file.write(
                f"{student.name}|{student.roll_no}|{marks}\n"
            )


def load_students():
    students = []

    try:
        with open(FILE_NAME, "r") as file:

            for line in file:

                line = line.strip()

                if line == "":
                    continue

                data = line.split("|")

                name = data[0]
                roll_no = int(data[1])

                marks = list(map(int, data[2].split(",")))

                student = Student(name, roll_no, marks)

                students.append(student)

    except FileNotFoundError:
        # File will be created when data is saved
        pass

    return students


def show_topper(students):

    if not students:
        print("No students available.")
        return

    topper = students[0]

    for student in students:

        if student.total() > topper.total():
            topper = student

    print("\n========== TOPPER ==========")

    topper.display()


def show_all(students):

    if not students:
        print("No student records found.")
        return

    for student in students:
        student.display()