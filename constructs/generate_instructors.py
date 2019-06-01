import random
import names

departments = ["Biology", "Comp. Sci.", "Elec. Eng.", "Finance",\
    "History", "Music", "Physics"]

salaries = [65000, 40000, 45000, 72000, 90000]

for id in range(100000,110000):
    department = random.choice(departments)
    salary = random.choice(salaries)
    name = names.get_last_name()
    print(f"('{id}', '{name}', '{department}', {salary}),")