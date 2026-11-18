class Solution:
    def maxProduct(self, nums: list[int]) -> int:

        current_max_prod = nums[0]
        current_min_prod = nums[0]

        global_max = nums[0]

        for i in range(1, len(nums)):
            new_max = max(nums[i], current_max_prod*nums[i], current_min_prod*nums[i])
            new_min = min(nums[i], current_max_prod*nums[i], current_min_prod*nums[i])
            current_max_prod, current_min_prod = new_max , new_min
            global_max = max(global_max, current_max_prod)

        return global_max
        