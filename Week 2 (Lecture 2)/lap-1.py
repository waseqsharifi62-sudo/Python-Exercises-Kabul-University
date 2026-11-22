from typing import Dict, Set, Any

students: Dict[int, Dict[str, Any]] = {
    101: {"name": "Ahmad", "courses": {"CS201", "CS202"}},
    102: {"name": "Sara", "courses": {"CS202", "CS203"}}
}

def add_course(student_id: int, course: str) -> None:
    if student_id in students:
        students[student_id]["courses"].add(course)

def drop_course(student_id: int, course: str) -> None:
    if student_id in students:
        students[student_id]["courses"].discard(course)

common_courses: Set[str] = students[101]["courses"].intersection(students[102]["courses"])
all_unique_courses: Set[str] = students[101]["courses"].union(students[102]["courses"])