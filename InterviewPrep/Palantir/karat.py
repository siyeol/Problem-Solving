ab_list = list()
while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    ab_list.append([a, b])

for a, b in ab_list:
    result_list = list()

    while True:
        print(a, b)
        if b%a != 0:
            quot = b//a + 1
            result_list.append(quot)
        else:
            result_list.append(b//a)
            break

        #incoming
        a = a*quot - b
        b = b*quot

    print(result_list)