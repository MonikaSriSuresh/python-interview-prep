"""
Topic 13 - File Handling Examples
"""

import csv
import json
import pickle

# JSON
student = {"name": "Monika", "skills": ["Python", "SQL"], "experience": 10}

json_str = json.dumps(student, indent=4)
print(json_str)

with open("student.json", "w", encoding="utf-8") as f:
    json.dump(student, f, indent=4)

with open("student.json", encoding="utf-8") as f:
    print(json.load(f))

# CSV
with open("employees.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["id", "name", "salary"])
    writer.writerow([101, "Monika", 100000])

with open("employees.csv", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        print(row["name"], row["salary"])

# Pickle
employee = {"id": 101, "name": "Monika"}

with open("employee.pkl", "wb") as f:
    pickle.dump(employee, f)

with open("employee.pkl", "rb") as f:
    print(pickle.load(f))

# Production API pattern (reference)
# response = requests.get(url, timeout=10)
# response.raise_for_status()
# data = response.json()
# employee_id = data.get("employeeId")
