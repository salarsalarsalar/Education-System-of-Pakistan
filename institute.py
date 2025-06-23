from people import Person, Teacher, Student, Principal

# --- Institution Classes ---
""" 
These are the classes which define the institutions
in which our people will work or study.
"""
class Institution:
    def __init__(self, name, institution_type, principal, system_type="Western"):
        self.name = name
        self.type = institution_type
        self.system_type = system_type
        self.principal = principal
        self.teachers = []
        self.students = []

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def add_student(self, student):
        self.students.append(student)

# Western Institutions
class School(Institution):
    def __init__(self, name, principal):
        super().__init__(name, "School", principal, system_type="Western")

class College(Institution):
    def __init__(self, name, principal):
        super().__init__(name, "College", principal, system_type="Western")

class University(Institution):
    def __init__(self, name, principal):
        super().__init__(name, "University", principal, system_type="Western")

# Islamic Institutions
class Maktab(Institution):
    def __init__(self, name, principal):
        super().__init__(name, "Maktab", principal, system_type="Islamic")

class Madrasa(Institution):
    def __init__(self, name, principal):
        super().__init__(name, "Madrasa", principal, system_type="Islamic")

class Jamia(Institution):
    def __init__(self, name, principal):
        super().__init__(name, "Jamia", principal, system_type="Islamic")