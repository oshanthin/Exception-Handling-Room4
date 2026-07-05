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
    
    if not (
        student_id.startswith("S")
        and len(student_id) == 4
        and student_id[1:].isdigit()
    ):
        raise InvalidIDFormatError("Invalid ID format (e.g. S007)")

    
    if student_id in students and not overwrite:
        raise DuplicateStudentError("Student already exists")

    # Convert mark with exception chaining
    try:
        mark = int(mark)
    except ValueError as e:
        raise InvalidMarkError("Mark must be numeric") from e

   
    if mark < 0 or mark > 100:
        raise InvalidMarkError("Mark must be between 0 and 100")

    students[student_id] = mark
    return "Record Saved"


def batch_register(records, overwrite=False):

    summary = {
        "success": [],
        "failed": []
    }

    for student_id, mark in records:
        try:
            result = set_mark(student_id, mark, overwrite)
            summary["success"].append((student_id, result))

        except Exception as e:
            summary["failed"].append((student_id, str(e)))

    return summary



records = [
    ("S007", 75),
    ("S001", 88),
    ("S008", 120),
    ("S009", "eighty"),
    ("S001", 90),
    ("S010", 85)
]



result = batch_register(records)


print("SUCCESS RECORDS:")
for item in result["success"]:
    print(item)

print("\nFAILED RECORDS:")
for item in result["failed"]:
    print(item)