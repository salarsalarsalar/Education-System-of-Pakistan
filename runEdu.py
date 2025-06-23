
from people import Person,Teacher, Student, Principal
from institute import Institution ,School ,College ,University ,Maktab ,Madrasa ,Jamia
from governingBody import GoverningBody ,Officer ,OfficerNode ,EducationDepartment

# --- Example Setup Using Classes and Dictionary (Hybrid) ---

# Governing Bodies
hec = GoverningBody("HEC", "Federal", "Higher Education")
wifaq = GoverningBody("Wifaq-ul-Madaris", "Religious", "Madaris across Pakistan")

# Principals
principal_qasim = Principal("Dr. Qasim", 55, "Male", "Western", 20)
principal_imran = Principal("Mufti Imran", 60, "Male", "Islamic", 25)

# Institutions
forman_college = College("Forman College", principal_qasim)
jamia_binoria = Jamia("Jamia Binoria", principal_imran)

# Teachers
teacher_ahsan = Teacher("Prof. Ahsan", 40, "Male", "Physics", "Western")
teacher_tariq = Teacher("Molana Tariq", 50, "Male", "Fiqh", "Islamic")

# Students
student_sana = Student("Sana", 18, "Female", "12", "Western")
student_ahmed = Student("Ahmed", 22, "Male", "Dars-e-Nizami Final", "Islamic")

# Add teachers and students to institutions
forman_college.add_teacher(teacher_ahsan)
forman_college.add_student(student_sana)
jamia_binoria.add_teacher(teacher_tariq)
jamia_binoria.add_student(student_ahmed)

# Departments
fed_dept = EducationDepartment("Federal Education Department")
fed_dept.add_officer(Officer("Federal Minister", "Federal Minister"))
fed_dept.add_institution(forman_college)
fed_dept.add_governing_body(hec)

punjab_dept = EducationDepartment("Punjab Religious Affairs Department")
punjab_dept.add_officer(Officer("Punjab Minister", "Provincial Minister"))
punjab_dept.add_institution(jamia_binoria)
punjab_dept.add_governing_body(wifaq)

# Convert to dictionary for JSON-friendly output
def institution_to_dict(inst):
    return {
        "name": inst.name,
        "type": inst.type,
        "principal": inst.principal.name,
        "teachers": [
            {"name": t.name, "age": t.age, "gender": t.gender, "subject": t.subject, "system_type": t.system_type}
            for t in inst.teachers
        ],
        "students": [
            {"name": s.name, "age": s.age, "gender": s.gender, "level": s.level, "system_type": s.system_type}
            for s in inst.students
        ]
    }

def officer_to_dict(officer):
    return {"name": officer.name, "role": officer.role}

def governing_body_to_dict(body):
    return {"name": body.name, "type": body.type, "jurisdiction": body.jurisdiction}

def department_to_dict(dept):
    return {
        "name": dept.name,
        "officers": [officer_to_dict(o) for o in dept.officers],
        "institutions": [inst.name for inst in dept.institutions],
        "governing_bodies": [body.name for body in dept.governing_bodies]
    }

example_data = {
    "governing_bodies": [governing_body_to_dict(hec), governing_body_to_dict(wifaq)],
    "principals": [
        {"name": principal_qasim.name, "age": principal_qasim.age, "gender": principal_qasim.gender,
         "system_type": principal_qasim.system_type, "experience_years": principal_qasim.experience_years},
        {"name": principal_imran.name, "age": principal_imran.age, "gender": principal_imran.gender,
         "system_type": principal_imran.system_type, "experience_years": principal_imran.experience_years}
    ],
    "institutions": [institution_to_dict(forman_college), institution_to_dict(jamia_binoria)],
    "departments": [department_to_dict(fed_dept), department_to_dict(punjab_dept)]
}

# --- Print Example (Dictionary Version) ---
def print_department_dict(dept_dict):
    print(f"\nDepartment: {dept_dict['name']}")
    print(" Governing Bodies:")
    for body in dept_dict["governing_bodies"]:
        print(f"  - {body}")
    print(" Officers:")
    for officer in dept_dict["officers"]:
        print(f"  - {officer['name']} ({officer['role']})")
    print(" Institutions:")
    for inst in dept_dict["institutions"]:
        print(f"  - {inst}")

if __name__ == "__main__":
    for dept in example_data["departments"]:
        print_department_dict(dept)
    # To print the whole structure as JSON:
    # print(json.dumps(example_data, indent=2))
