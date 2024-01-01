def merge_sort(nums_arr):
    if len(nums_arr) < 2:
        return nums_arr
    left_arr = merge_sort(nums_arr[: len(nums_arr) // 2])
    right_arr = merge_sort(nums_arr[len(nums_arr) // 2 :])
    return merge(left_arr, right_arr)


def merge(left_arr, right_arr):
    sorted_arr = []
    i, j = 0, 0
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            sorted_arr.append(left_arr[i])
            i += 1
        else:
            sorted_arr.append(right_arr[j])
            j += 1
    while i < len(left_arr):
        sorted_arr.append(left_arr[i])
        i += 1
    while j < len(right_arr):
        sorted_arr.append(right_arr[j])
        j += 1
    return sorted_arr


res = merge_sort([69, 120, 4, 22, 0, 1, 221, 20, 13, 7, 2])
print(res)
