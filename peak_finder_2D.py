def global_maximum(row):
    maximum = row[0]
    pos = 0
    for i, j in enumerate(row[1:]):
        if j > maximum:
            maximum = j
            pos = i+1
    return maximum, pos


def findPeak(arr, mid):
    maximum, pos = global_maximum(arr[mid])
    if len(arr) == 1:
        return maximum
    if len(arr) == 2:
        return arr[mid-1][pos] if maximum < arr[mid-1][pos] else maximum
    if maximum < arr[mid-1][pos]:
        return findPeak(arr[:mid], len(arr[:mid])//2)
    elif maximum < arr[mid+1][pos]:
        return findPeak(arr[mid+1:], len(arr[mid+1:])//2)
    else:
        return maximum


arr = [[1, 2, 3], [4, 5, 6]]
print(findPeak(arr, len(arr)//2))
