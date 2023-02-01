arr = [5, 2, 4, 1, 3]

def MergeSort(arr):
    def sort(low, high):
        if high - low <2:
            return
        mid = (low+high)//2
        sort(low, mid)
        sort(mid, high)
        merge(low, mid, high)

    def merge(low, mid, high):
        temp = list()

        lidx = low
        ridx = mid

        while lidx<mid and ridx<high:
            if arr[lidx]<arr[ridx]:
                temp.append(arr[lidx])
                lidx+=1
            else:
                temp.append(arr[ridx])
                ridx+=1

        while lidx<mid:
            temp.append(arr[lidx])
            lidx+=1
        while ridx<high:
            temp.append(arr[ridx])
            ridx+=1

        for i in range(low, high):
            arr[i] = temp[i-low]

    return sort(0, len(arr))

MergeSort(arr)

print(arr)