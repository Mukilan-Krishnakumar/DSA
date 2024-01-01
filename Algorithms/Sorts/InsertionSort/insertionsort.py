def insertion_sort(nums_arr):
    for j in range(len(nums_arr)):
        while j > 0:
            if nums_arr[j] < nums_arr[j - 1]:
                nums_arr[j], nums_arr[j - 1] = nums_arr[j - 1], nums_arr[j]
            j -= 1

    return nums_arr


res = insertion_sort([231, 32, 112, 43, 69, 220, 1, 0])
print(res)
