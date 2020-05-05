def max_heapify(arr, node):
    def swap(arr, node):
        temp = arr[node-1]
        arr[node-1] = arr[2*node-1]
        arr[2*node-1] = temp
        return arr
    if arr[node-1] < arr[2*node-1]:
        arr = swap(arr, node)
    if 2*node + 1 < len(arr):
        if arr[node-1] < arr[2*node]:
            arr = swap(arr, node)
    return arr


def build_max_heap(arr):
    for node in range(len(arr)//2, 0, -1):
        arr = max_heapify(arr, node)
    return arr


if __name__ == "__main__":
    arr = [2, 4]
    print(build_max_heap(arr))
