class InvalidGradeError(Exception):
    pass

def validate_grade(value):
    try:
        grade = float(value)
    except ValueError:
        raise InvalidGradeError("Grade must be numeric.")
    
    if grade < 0 or grade > 100:
        raise InvalidGradeError("Grade must be between 0 and 100.")
    return grade

def main():
    test_cases = ["85", "abc", "-10", "105", "50"]
    for val in test_cases:
        try:
            valid_grade = validate_grade(val)
            print(f"Valid grade: {valid_grade}")
        except InvalidGradeError as e:
            print(f"Error: {e}")

main()