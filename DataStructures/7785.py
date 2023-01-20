n = int(input())

office = set()

for _ in range(n):
    name, command = input().split()
    if command == 'enter':
        office.add(name)
    elif command == 'leave':
        office.remove(name)

for item in sorted(office, reverse=True):
    print(item)