N = int(input())
students = []

for _ in range(N):
    name, korean, english, math = input().split()
    students.append([name, int(korean), int(english), int(math)])

def sort(student):
    return -student[1], student[2], -student[3], student[0]

students.sort(key=sort)

for student in students:
    print(student[0])
