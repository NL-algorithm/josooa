import sys

n = int(sys.stdin.readline())
students = []
for _ in range(n):
    students.append((sys.stdin.readline().strip()))
min_length = 1

liststu = set()

while(len(liststu)!=n):
    liststu = set()
    for i in range(n):
        liststu.add(students[i][-min_length:])
    min_length += 1

print(min_length-1)