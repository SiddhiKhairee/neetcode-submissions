class Solution:
    def maxSubArray(self, nums: list[int]) -> int:

        # we initialize both of them with the first element
        current_sum = nums[0]
        max_sum = nums[0]

        # we traverse thru rest of the array
        for i in range(1, len(nums)):
            current_sum = max(current_sum+nums[i], nums[i])
            max_sum = max(current_sum, max_sum)

        return max_sum