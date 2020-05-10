#!python3


def make_key_arr(arr):
    max_element = max(arr)
    key_arr = [0]*(max_element+1)
    for element in arr:
        key_arr[element] += 1
    return key_arr


def cumulative_key_arr(key_arr):
    for key in range(1, len(key_arr)):
        key_arr[key] += key_arr[key-1]
    return key_arr


def shift_right_key_arr(key_arr):
    for key in range(len(key_arr)-1, 0, -1):
        key_arr[key] = key_arr[key-1]
    key_arr[0] = 0
    return key_arr


def counting_sort(arr):
    key_arr = shift_right_key_arr(cumulative_key_arr(make_key_arr(arr)))
    sorted_arr = [0]*len(arr)
    for element in arr:
        sorted_arr[key_arr[element]] = element
        key_arr[element] += 1
    return sorted_arr


if __name__ == "__main__":
    arr = [1, 0, 3, 1, 3, 1]
    # takes only whole numbers. works for duplicate numbers. stable
    print(counting_sort(arr))
