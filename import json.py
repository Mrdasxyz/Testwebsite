import json

file_path = r'C:\fastapi\employee_data.json'  
with open(file_path, 'r') as file:
    emp_data = json.load(file)

print(emp_data)
print(type(emp_data))

print(emp_data['name'])
print(emp_data['id'])
print(emp_data['city'])
