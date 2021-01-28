employees = ['Kelly', 'Emma', 'John']

defaults = {"designation": 'Application Developer', "salary": 8000}

employees_dict = dict.fromkeys(employees, defaults)

print(employees_dict)
