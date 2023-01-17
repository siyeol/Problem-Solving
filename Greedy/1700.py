from collections import deque

N, K = map(int, input().split())
elec_list = list(map(int, input().split()))

count=0

multitap = deque()

for idx, elec in enumerate(elec_list):
    if elec in multitap:
        continue

    if len(multitap) < N:
        multitap.append(elec)
        continue

    flag = False
    temp_idx_max = 0
    temp_tap = None

    sublist = elec_list[idx:]
    for tap_idx, tap in enumerate(multitap):
        if tap not in sublist:
            multitap[tap_idx] = elec
            count+=1
            flag = True
            break
        elif temp_idx_max < sublist.index(tap):
            temp_idx_max = sublist.index(tap)
            temp_tap = tap_idx
    if flag is False:
        multitap[temp_tap] = elec
        count += 1

print(count)