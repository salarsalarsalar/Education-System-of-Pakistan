# --- Core People Classes ---
""" 
These classes will be same for both islamic and western education systems.
"""
class Person:
    def __init__(self, name, age=None, gender=None, role=None):
        self.name = name
        self.age = age
        self.gender = gender
        self.role = role

class Teacher(Person):
    def __init__(self, name, age, gender, subject, system_type):
        super().__init__(name, age, gender, role="Teacher")
        self.subject = subject
        self.system_type = system_type

class Student(Person):
    def __init__(self, name, age, gender, level, system_type):
        super().__init__(name, age, gender, role="Student")
        self.level = level
        self.system_type = system_type

class Principal(Person):
    def __init__(self, name, age, gender, system_type, experience_years):
        super().__init__(name, age, gender, role="Principal")
        self.system_type = system_type
        self.experience_years = experience_years