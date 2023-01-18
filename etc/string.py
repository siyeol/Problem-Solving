in_str = input()

temp_str = ""
for i in range(len(in_str)):
    if i%10 == 0 and i != 0:
        print(temp_str)
        temp_str = ""
    temp_str+=in_str[i]
print(temp_str)
