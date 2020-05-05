import max_heapify


def heap_sort(arr):
    sorted_arr = []
    arr = max_heapify.build_max_heap(arr)
    heap_size = len(arr)
    for i in range(len(arr)):
        sorted_arr.append(arr[0])
        arr[0] = arr[heap_size-1]
        heap_size -= 1
        arr = max_heapify.build_max_heap(arr[:heap_size])
    return sorted_arr


if __name__ == "__main__":
    arr = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
    print(heap_sort(arr))
