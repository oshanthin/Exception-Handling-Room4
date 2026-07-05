class InvalidMarkError(Exception):
    pass

class DuplicateStudentError(Exception):
    pass


students = {
    "S001": 78,
    "S002": 55,
    "S003": None,
    "S004": 91,
    "S005": 63,
    "S006": 82
}


def set_mark(student_id, mark, overwrite=False):

    if student_id in students and not overwrite:
        raise DuplicateStudentError("Student already exists")

    try:
        mark = int(mark)
    except ValueError as e:
        raise ValueError("Mark must be numeric") from e

    if mark < 0 or mark > 100:
        raise InvalidMarkError("Mark must be between 0 and 100")

    students[student_id] = mark
    return "Record Saved"


print("1. Adding a new student with valid mark")
try:
    print(set_mark("S007", 75, False))
except Exception as e:
    print(type(e).__name__, e)
finally:
    print("Operation Completed\n")


print("2. Trying to add a duplicate student")
try:
    print(set_mark("S001", 88, False))
except Exception as e:
    print(type(e).__name__, e)
finally:
    print("Operation Completed\n")

print("3. Trying to add a student with an invalid mark")
try:
    print(set_mark("S008", 120, False))
except Exception as e:
    print(type(e).__name__, e)
finally:
    print("Operation Completed\n")

print("4. Trying to add a student with a non-numeric mark")
try:
    print(set_mark("S009", "eighty", False))
except Exception as e:
    print(type(e).__name__, e)
finally:
    print("Operation Completed\n")

print("5. Trying to update an existing student's mark")
try:
    print(set_mark("S001", 90, True))
except Exception as e:
    print(type(e).__name__, e)
finally:
    print("Operation Completed\n")