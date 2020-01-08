students = []


class Student:
    school_name = "St James Hatcham School Nursery"

    def __init__(self, name, age, town):
        self.name = name
        self.age = age
        self.town = town
        students.append(self)

    def __str__(self):
        return "Student " + self.name

    def get_name_capitalize(self):
        return self.name.capitalize()

    def get_school_name(self):
        return self.school_name
