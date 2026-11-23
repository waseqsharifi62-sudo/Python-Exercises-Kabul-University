import csv
import shutil
from pathlib import Path

def validate(student_id, name, department, semester):
    if not student_id or not name or not department or not semester:
        return False
    return True

def read_all(filepath):
    if not filepath.exists():
        return []
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return list(csv.DictReader(f))
    except Exception:
        return []

def write_all(filepath, data):
    with open(filepath, "w", newline="", encoding="utf-8") as f:
        fields = ["student_id", "name", "department", "semester"]
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(data)

def add_student(filepath, student_id, name, department, semester):
    if not validate(student_id, name, department, semester):
        return
    with open(filepath, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([student_id, name, department, semester])

def list_students(filepath):
    for student in read_all(filepath):
        print(student)

def search_student(filepath, student_id):
    for student in read_all(filepath):
        if student["student_id"] == str(student_id):
            return student
    return None

def update_student(filepath, student_id, name, department, semester):
    if not validate(student_id, name, department, semester):
        return
    data = read_all(filepath)
    for student in data:
        if student["student_id"] == str(student_id):
            student["name"] = name
            student["department"] = department
            student["semester"] = semester
    if filepath.exists():
        shutil.copy(filepath, filepath.with_suffix(".bak"))
    write_all(filepath, data)

def delete_student(filepath, student_id):
    data = read_all(filepath)
    filtered = [s for s in data if s["student_id"] != str(student_id)]
    if len(filtered) < len(data):
        if filepath.exists():
            shutil.copy(filepath, filepath.with_suffix(".bak"))
        write_all(filepath, filtered)

path = Path("students.csv")
if not path.exists():
    write_all(path, [])

add_student(path, "1", "Ali", "CS", "3")
add_student(path, "2", "Sara", "Math", "2")
list_students(path)
search_student(path, "1")
update_student(path, "1", "Ali Reza", "CS", "4")
delete_student(path, "2")