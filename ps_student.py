from student import Student


class PrimarySchoolStudent(Student):
    school_name = "St James Hatcham School Nursery"

    def get_school_name(self):
        return "This is a Primary School Student"

    def get_name_capitalize(self):
        original_value = super(PrimarySchoolStudent, self).get_name_capitalize()
        return original_value + "-PS"
