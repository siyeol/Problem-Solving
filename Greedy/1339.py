N = int(input())

str_list = []
total_str = ""

decode = dict()

for i in range(N):
    temp = input()    
    str_list.append(temp)    
    for idx, char in enumerate(temp[::-1]):
        if char not in decode:
            decode[char]=10**idx
        else:
            decode[char]+=10**idx
    total_str+=temp


convert = dict()

maxint=9
for cv in sorted(decode.items(), key=lambda x:x[1], reverse=True):
    convert[cv[0]] = maxint
    maxint-=1


result = 0
for sl in str_list:
    temp_str = ""
    for char in sl:
        temp_str+=str(convert[char])
    result+=int(temp_str)

print(result)
