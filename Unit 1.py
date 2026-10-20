
# Hospital Appointment System

patients = [
    {"name": "Rahul", "start": 9, "end": 10},
    {"name": "Priya", "start": 10, "end": 11},
    {"name": "Amit", "start": 9, "end": 11},
    {"name": "Sneha", "start": 11, "end": 12},
    {"name": "Rohan", "start": 12, "end": 13},
    {"name": "Neha", "start": 10, "end": 12}
]

def merge_sort(records):
    if len(records) <= 1:
        return records

    mid = len(records) // 2
    left = merge_sort(records[:mid])
    right = merge_sort(records[mid:])

    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i]["end"] <= right[j]["end"]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    return result + left[i:] + right[j:]

def schedule_appointments(records):
    selected = []
    last_end = 9

    for patient in records:
        if patient["start"] >= last_end:
            selected.append(patient)
            last_end = patient["end"]

    return selected

print("HOSPITAL APPOINTMENT SYSTEM")

sorted_patients = merge_sort(patients)

print("\nAppointments Sorted by End Time:")
for p in sorted_patients:
    print(p["name"], "-", p["start"], "to", p["end"])

appointments = schedule_appointments(sorted_patients)

print("\nSelected Appointments:")
for p in appointments:
    print(p["name"], "-", p["start"], "to", p["end"])

print("\nTotal Appointments:", len(appointments))
