from re import sub


S = input()

flag = False
substr = ""

temp_list = []
for char in S:
    if char == '<':
        flag = True
        temp_list.append(substr)
        substr=""

    substr+=char

    if char == '>':
        flag = False
        temp_list.append(substr)
        substr=""

temp_list.append(substr)

output = ""
for temp in temp_list:
    if '<' in temp:
        output+=temp
    else:
        for t in temp.split():
            output+=t[::-1]
            output+=" "
    output = output.rstrip()

print(output)