class InvalidMarkError(Exception):
    pass

class DuplicateStudentError(Exception):
    pass

class InvalidIDFormatError(Exception):
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
    print("overwrite:", overwrite)


    if not (
        student_id.startswith("S")
        and len(student_id) == 4
        and student_id[1:].isdigit()
    ):
        raise InvalidIDFormatError(
            "ID must be S + 3 digits (e.g. S007)"
        )


    if student_id in students and not overwrite:
        raise DuplicateStudentError("Student already exists")

   
    try:
        mark = int(mark)
    except ValueError as e:
        raise InvalidMarkError("Mark must be numeric") from e

   
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

    except InvalidIDFormatError as e:
        print("InvalidIDFormatError:", e)

    except Exception as e:
        print("Unexpected Error:", e)

    else:
        print(result)

    finally:
        print("Operation Completed\n")