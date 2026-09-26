from array import array


class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = array('i', marks)

    def total(self):
        return sum(self.marks)

    def percentage(self):
        return self.total() / len(self.marks)

    def grade(self):
        percentage = self.percentage()

        if percentage >= 90:
            return "A+"
        elif percentage >= 80:
            return "A"
        elif percentage >= 70:
            return "B"
        elif percentage >= 60:
            return "C"
        elif percentage >= 50:
            return "D"
        else:
            return "F"

    def display(self):
        print("\nName       :", self.name)
        print("Roll No.   :", self.roll_no)
        print("Marks      :", list(self.marks))
        print("Total      :", self.total())
        print("Percentage :", round(self.percentage(), 2), "%")
        print("Grade      :", self.grade())

    