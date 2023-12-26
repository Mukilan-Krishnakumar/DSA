def bubblesort(nums):
    swapping = True
    while swapping:
        swapping = False
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                nums[i - 1], nums[i] = nums[i], nums[i - 1]
                swapping = True
    return nums


print(bubblesort([15, 3, 52, 22, 1, 9, 0]))
