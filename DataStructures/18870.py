N = int(input())

input_list = list(map(int, input().split()))

sorted_list = sorted(list(set(input_list)))

mydict = dict()

for idx, elem in enumerate(sorted_list):
    mydict[elem]=idx

for x in input_list:
    print(mydict[x], end=" ")