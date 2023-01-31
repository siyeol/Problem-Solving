student_course_pairs_1 = [
  ["58", "Software Design"],
  ["58", "Linear Algebra"],
  ["94", "Art History"],
  ["94", "Operating Systems"],
  ["17", "Software Design"],
  ["58", "Mechanics"],
  ["58", "Economics"],
  ["17", "Linear Algebra"],
  ["17", "Political Science"],
  ["94", "Economics"],
  ["25", "Economics"],
]

student = dict()

for id, course in student_course_pairs_1:
    if id not in student:
        student[id] = [course]
    else:
        student[id].append(course)

from itertools import combinations

result = dict()

for s1, s2 in combinations(student.keys(), 2):
    key = "["+s1+", "+s2+"]"
    result[key] = []
    for course in student[s1]:
        if course in student[s2]:
            result[key].append(course)

print(str(result.items()))