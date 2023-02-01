from curses.panel import bottom_panel
from itertools import count


employees = [
  "1, Bill, Engineer",
  "2, Joe, HR",
  "3, Sally, Engineer",
  "4, Richard, Business",
  "6, Tom, Engineer"
]

friendships = [
  "1, 2",
  "1, 3",
  "3, 4",
  "6, 1"
]

def find_adj (employees, friendships):
    relation = dict()

    for emp in employees:
        num, _, _ = emp.split(sep=", ")
        relation[num] = list()
    
    for frnd in friendships:
        start, end = frnd.split(sep=", ")
        relation[start].append(end)
        relation[end].append(start)

    for key, value in relation.items():
        print(key, end=": ")
        if len(value) == 0:
            print("None")
        else:
            for idx in range(len(value)):
                if idx != len(value)-1:
                    print(value[idx], end=", ")
                else:
                    print(value[idx])

    return relation


relation = find_adj(employees, friendships)

print("#################SEP###################")

def dep_count (employees, friendships, relation):
    role_dict = dict()

    for emp in employees:
        num, name, role = emp.split(sep=", ")
        role_dict[role] = list()

    for emp in employees:
        num, name, role = emp.split(sep=", ")
        if len(relation[num])!=0:
            role_dict[role].append(1)
        else:
            role_dict[role].append(0)

    for key, value in role_dict.items():
        print(key, end=": ")
        top = sum(value)
        bottom = len(value)
        print(top, "of", bottom)

dep_count(employees, friendships, relation)