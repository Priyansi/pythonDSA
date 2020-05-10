#!python3


def find_max_min(arr):
    max_element = min_element = arr[0]
    for element in arr:
        if element > max_element:
            max_element = element
        elif element < min_element:
            min_element = element
    return max_element, min_element


def make_key_arr(arr):
    max_element, min_element = find_max_min(arr)
    key_arr = [0]*(max_element-min_element+1)
    for element in arr:
        key_arr[element-min_element] = 1

    return min_element, key_arr


def traverse_replace(arr):
    min_element, key_arr = make_key_arr(arr)
    i = 0
    for key, value in enumerate(key_arr):
        if value:
            arr[i] = key+min_element
            i += 1
    return arr


if __name__ == "__main__":
    arr = [2, 3, 0, -3]
    # takes only unique elements. works for both positive and negative numbers
    print(traverse_replace(arr))
