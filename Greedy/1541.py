from collections import deque

input = input()
iq = deque(input)

input_split = input.replace("+", "-").split(sep="-")

first = input_split.pop(0)
result = int(first)
for _ in range(len(first)):
    iq.popleft()

for idx, splitted in enumerate(input_split):
    sign = iq.popleft()
    for _ in range(len(splitted)):
        iq.popleft()

    if sign == '+':
        result += int(splitted)
    else:
        result -= sum(map(int, input_split[idx:]))
        print(result)
        exit()
    
print(result)