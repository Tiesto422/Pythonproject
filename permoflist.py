def helper(index, nums):
    if index == len(nums):
        results.append(nums.copy())
    for i in range(index, len(nums)):
        nums[index], nums[i] = nums[i], nums[index]
        helper(index + 1, nums)
        nums[index], nums[i] = nums[i], nums[index]


results = []
nums2 = [1, 2, 3]
helper(0, nums2)
print(results)
