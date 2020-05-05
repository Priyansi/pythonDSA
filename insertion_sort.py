def traverse(arr):
    for key in range(1, len(arr)):
        while arr[key-1] > arr[key] and key-1 >= 0:
            temp = arr[key-1]
            arr[key-1] = arr[key]
            arr[key] = temp
            key -= 1
    return arr


if __name__ == "__main__":
    arr = [5, 2, 4, 6, 1, 3]
    print(traverse(arr))
