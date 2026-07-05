students = {
    "S001": 78, "S002": 55, "S003": None,
    "S004": 91, "S005": "63", "S006": 82
}


def class_report(data):
    marks = []
    for v in data.values():
        try:
            if v is None:
                continue
            # allow numeric strings
            mark = float(v)
            marks.append(mark)
        except (ValueError, TypeError):
            continue

    if not marks:
        print("No valid marks provided")
        return

    total = sum(marks)
    average = total / len(marks)
    highest = max(marks)
    lowest = min(marks)
    print("Average:", average)
    print("Highest:", highest)
    print("Lowest:", lowest)


if __name__ == "__main__":
    class_report(students)
