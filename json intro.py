#import json 
#emp = '{ "id":1, "name":"name", "city":"bbsr" }'
#print(emp)
#print(type(emp)
#      )
#data = json.loads(emp)
#print(data)
#print(type(data))
#print(data['name'])
#print(data['id'])
#print(data['city'])

import json


file_path = 'employee_data.json'  
with open(file_path, 'r') as file:
    emp_data = json.load(file)


print(emp_data)
print(type(emp_data))
print(emp_data['name'])
print(emp_data['id'])
print(emp_data['city'])
