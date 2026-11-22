from typing import Dict, Set, List, Any, TypeVar

T = TypeVar("T")

def make_set(items: List[T]) -> Set[T]:
    return set(items)

class CourseRegistrationManager:
    def __init__(self) -> None:
        self.students: Dict[int, Dict[str, Any]] = {}

    def add_student(self, student_id: int, name: str) -> None:
        if student_id not in self.students:
            self.students[student_id] = {"name": name, "courses": set()}

    def register_course(self, student_id: int, course: str) -> None:
        if student_id in self.students:
            self.students[student_id]["courses"].add(course)

    def drop_course(self, student_id: int, course: str) -> None:
        if student_id in self.students:
            self.students[student_id]["courses"].discard(course)

    def search_student(self, student_id: int) -> Dict[str, Any]:
        return self.students.get(student_id, {})

    def get_all_unique_courses(self) -> Set[str]:
        all_courses: Set[str] = set()
        for data in self.students.values():
            all_courses.update(data["courses"])
        return all_courses

    def find_students_in_course(self, course: str) -> List[str]:
        return [data["name"] for data in self.students.values() if course in data["courses"]]

    def sort_students_by_name(self) -> List[Dict[str, Any]]:
        return sorted(self.students.values(), key=lambda x: x["name"])

manager = CourseRegistrationManager()
manager.add_student(1, "Ali")
manager.add_student(2, "Sara")
manager.register_course(1, "CS101")
manager.register_course(2, "CS101")