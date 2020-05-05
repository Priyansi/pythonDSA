def findPeak(arr, mid):
    if mid <= 1:
        return max(arr)
    if arr[mid+1] >= arr[mid]:
        return findPeak(arr[mid+1:], len(arr[mid+1:])//2)
    elif arr[mid-1] >= arr[mid]:
        return findPeak(arr[:mid], len(arr[:mid])//2)
    else:
        return arr[mid]


if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(findPeak(arr, len(arr)//2))
