students = {
    "S001": 78, "S002": 55, "S003": None,
    "S004": 91, "S005": "63", "S006": 82
}


def class_report(data):
    marks = []
   
    skipped = {"missing mark": 0, "wrong type": 0, "out of range": 0}
    skipped_log = []  # (student_id, reason) for each individual skip

    for student_id, v in data.items():
        try:
            if v is None:
                skipped["missing mark"] += 1
                skipped_log.append((student_id, "missing mark"))
                continue

            mark = float(v)
            if mark < 0 or mark > 100:
                skipped["out of range"] += 1
                skipped_log.append((student_id, f"out of range ({mark})"))
                continue

            marks.append(mark)
        except TypeError:
            skipped["wrong type"] += 1
            skipped_log.append((student_id, f"wrong type ({type(v).__name__})"))
        except ValueError:
            skipped["wrong type"] += 1
            skipped_log.append((student_id, f"wrong type ({v!r})"))


    if marks:
        lowest = min(marks)
        print("Average:", sum(marks) / len(marks))
        print("Highest:", max(marks))
        print("Lowest:", lowest)
    else:
        print("No valid marks provided")

    print("Records skipped:")
    for reason, count in skipped.items():
        if count > 0:
            print(f"  {reason}: {count}")

    print("\nSkipped record details:")
    for student_id, reason in skipped_log:
        print(f"  {student_id}: {reason}")


if __name__ == "__main__":
    class_report(students)



    