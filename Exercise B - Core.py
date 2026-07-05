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

    print("student_id:", student_id)
    print("mark:", mark)

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



records = [
    ("S007", 75, False),
    ("S001", 88, False),
    ("S008", 120, False),
    ("S009", "eighty", False),
    ("S001", 90, True)
]


for sid, mark, overwrite in records:
    try:
        result = set_mark(sid, mark, overwrite)

    except InvalidMarkError as e:
        print("InvalidMarkError:", e)

    except DuplicateStudentError as e:
        print("DuplicateStudentError:", e)

    except ValueError as e:
        print("ValueError:", e)

    except Exception as e:
        print("Unexpected Error:", e)

    else:
        print(result)

    finally:
        print("Operation Completed\n")