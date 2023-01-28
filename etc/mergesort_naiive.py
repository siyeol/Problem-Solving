arr = [5, 3, 2, 4, 1]

def MergeSort(arr):
    #basecase
    if len(arr) < 2:
        return arr

    mid = len(arr)//2

    left = MergeSort(arr[:mid])
    right = MergeSort(arr[mid:])

    merged = list()
    l_idx = r_idx = 0

    while l_idx < len(left) and r_idx < len(right):
        if left[l_idx] < right[r_idx]:
            merged.append(left[l_idx])
            l_idx+=1
        else:
            merged.append(right[r_idx])
            r_idx+=1

    print(merged)
    merged += left[l_idx:]
    merged += right[r_idx:]

    return merged

print(MergeSort(arr))

