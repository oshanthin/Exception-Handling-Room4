students = {"S001": 78, "S002": 55, "S003": None,
"S004": 91, "S005": 63, "S006": 82}
def add_student(student_id, mark):
    try:
        students[student_id] = int(mark)
    except ValueError:
        print("Invalid mark. Please enter a number.")
def get_average():
    try:
        valid_marks = [m for m in students.values() if isinstance(m, int)]
        return sum(valid_marks) / len(valid_marks)
    except ZeroDivisionError:
        print("No valid marks to average.")
def find_student(student_id):
    try:
        return students[student_id]
    except KeyError:
        print("Student ID not found.")
def remove_student(student_id):
    try:
        del students[student_id]
    except KeyError:
        print("Cannot remove: ID not found.")
