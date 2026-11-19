class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # we use Kadane's algorithm
        # we have 2 variables max_sum and current_sum, both of them initialized to the first element of the array

        max_sum = nums[0]
        current_sum = nums[0]

        # then we iterate from the second eleement to the last element of the array
        for i in range(1, len(nums)):

            # at each element we update both current sum and max_sum
            # for current sum we have 2 options, either we pick, the sum seen upto the current index + new element OR we simply just pick the new element, we choose whichever is the maximum
            current_sum = max(current_sum + nums[i], nums[i])

            # we update max_sum in a way such that max_sum will hold the largest subarray sum seen so far
            max_sum = max(max_sum, current_sum)

        return max_sum
        