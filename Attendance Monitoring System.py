# Situation: Attendance Monitoring System
# Find the first repeating student ID

student_ids = list(map(int, input("Enter student IDs: ").split()))

seen = set()
repeating_id = None

for id in student_ids:
    if id in seen:
        repeating_id = id
        break
    seen.add(id)

if repeating_id is not None:
    print("First repeating student ID:", repeating_id)
else:
    print("No repeating student ID found")
