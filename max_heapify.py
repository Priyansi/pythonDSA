def max_heapify(arr, node):
    if arr[node-1] < arr[2*node-1]:
        temp = arr[node-1]
        arr[node-1] = arr[2*node-1]
        arr[2*node-1] = temp
    if 2*node < len(arr):
        if arr[node-1] < arr[2*node]:
            temp = arr[node-1]
            arr[node-1] = arr[2*node]
            arr[2*node] = temp
    return arr


def build_max_heap(arr):
    for node in range(len(arr)//2, 0, -1):
        arr = max_heapify(arr, node)
    return arr


if __name__ == "__main__":
    arr = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
    print(build_max_heap(arr))
