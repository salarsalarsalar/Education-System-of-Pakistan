from people import Person
# --- Governing Body ---
""" 
These classes define the governing bodies that oversee the institutions.
"""
class GoverningBody:
    def __init__(self, name, body_type, jurisdiction):
        self.name = name
        self.type = body_type  # e.g., "Federal", "Religious"
        self.jurisdiction = jurisdiction

# --- Officer/Organogram Classes ---
class Officer(Person):
    def __init__(self, name, role):
        super().__init__(name, role=role)
        self.subordinates = []

    def add_subordinate(self, officer):
        self.subordinates.append(officer)

class OfficerNode:
    def __init__(self, title):
        self.title = title
        self.subordinates = []

    def add_subordinate(self, officer):
        self.subordinates.append(officer)

# --- Department/Administration Classes ---
class EducationDepartment:
    def __init__(self, name):
        self.name = name
        self.officers = []
        self.institutions = []
        self.islamic_institutions = []
        self.western_institutions = []
        self.governing_bodies = []

    def add_officer(self, officer):
        self.officers.append(officer)

    def add_institution(self, institution):
        self.institutions.append(institution)
        if institution.system_type == "Islamic":
            self.islamic_institutions.append(institution)
        else:
            self.western_institutions.append(institution)

    def add_governing_body(self, body):
        self.governing_bodies.append(body)