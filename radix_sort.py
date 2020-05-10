#!python3
from counting_sort_whole_nums import shift_right_key_arr, cumulative_key_arr


def counting_sort_for_digits(arr, sorted_arr, digit):
    key_arr = [0]*10
    for element in arr:
        str_element = str(element)
        len_element = len(str_element)
        if len_element < digit:
            key_arr[0] += 1
        else:
            key_arr[int(str_element[len_element-digit])] += 1
    key_arr = shift_right_key_arr(cumulative_key_arr(key_arr))
    for element in arr:
        str_element = str(element)
        len_element = len(str_element)
        if len_element < digit:
            index = 0
        else:
            index = int(str_element[len_element-digit])
        sorted_arr[key_arr[index]] = element
        key_arr[index] += 1

    arr = sorted_arr.copy()
    return arr, sorted_arr


def radix_sort(arr):
    digits_max = len(str(max(arr)))
    digit = 1
    sorted_arr = [0]*len(arr)
    while digits_max >= digit:
        arr, sorted_arr = counting_sort_for_digits(arr, sorted_arr, digit)
        digit += 1

    return sorted_arr


if __name__ == "__main__":
    arr = [170, 45, 75, 90, 802, 24, 2, 66]
    print(radix_sort(arr))
