import os

def create_file(filename):
    if not os.path.exists(filename):
        with open(filename, "w", encoding="utf-8") as f:
            f.write("1,Ahmad\n2,Sara\n3,Reza\n4,Nina\n5,Omid\n")

def add_student(filename, student_id, name):
    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"{student_id},{name}\n")

def list_students(filename):
    if not os.path.exists(filename):
        return
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            print(line.strip())

def search_student(filename, student_id):
    if not os.path.exists(filename):
        return None
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split(",")
            if parts[0] == str(student_id):
                return parts[1]
    return None

def count_records(filename):
    if not os.path.exists(filename):
        return 0
    with open(filename, "r", encoding="utf-8") as f:
        return len(f.readlines())

filename = "students.txt"
create_file(filename)
add_student(filename, 6, "Ali")
list_students(filename)
print(search_student(filename, 3))
print(count_records(filename))