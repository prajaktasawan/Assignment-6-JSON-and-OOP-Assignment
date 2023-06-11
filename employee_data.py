import json


class Employee:
    def __init__(self, name, dob, height, city, state):
        self.name = name
        self.dob = dob
        self.height = height
        self.city = city
        self.state = state


# Read the JSON file
with open("employee.json", 'r', encoding='utf-8') as file:
    data = json.load(file)

employee_list = []

# Parse the JSON data and create Employee objects
for employee_data in data:
    employee = Employee(employee_data['Name'], employee_data['DOB'], employee_data['Height'], employee_data['City'],
                        employee_data['State'])
    employee_list.append(employee)

# Print the list of Employee objects
for employee in employee_list:
    print(f"Name: {employee.name}")
    print(f"DOB: {employee.dob}")
    print(f"Height: {employee.height}")
    print(f"City: {employee.city}")
    print(f"State: {employee.state}")
    print()  # Add a blank line for separation
