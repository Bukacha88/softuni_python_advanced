def fix_calendar(nums):
    swaps = 0
    for number in range(len(nums)):
        if number < len(nums) - 1:
            if nums[number] > nums[number + 1]:
                nums[number], nums[number + 1] = nums[number + 1], nums[number]
                swaps += 1
            if swaps > 0:
                fix_calendar(nums)

    return nums



numbers = [7, 20, 25, 25, 10, 2, 3, 19, 34]
fixed = fix_calendar(numbers)
print(fixed)
