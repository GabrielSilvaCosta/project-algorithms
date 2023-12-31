def find_duplicate(nums):
    if not nums or not isinstance(nums, list) or len(nums) < 2:
        return False

    if any(not isinstance(num, (int, float)) or num < 0 for num in nums):
        return False

    nums.sort()

    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return nums[i]

    return False
