class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        # we use dynamic programming
        # we have to make 2 different dp arrays
        # max_dp will hold the maximum subproduct upto ith element
        # min_dp will hold the minimum subproduct upto the ith element
        # the reason why we are including minimum product is because we never know when we get a -ve number and we multpily it with another -ve number and we end up getting max product of a subarray so far


        max_dp = [nums[0]] * len(nums)
        min_dp = [nums[0]] * len(nums)

        for i in range(1, len(nums)):

            # we first update the max_dp, we consider max of all these options
            # option 1: start fresh -> include just nums[i]
            # option 2: we consider min_dp[i-1]*nums[i]
            # option 3: we consider max_dp[i-1]*nums[i]

            max_dp[i] = max(nums[i], min_dp[i-1]*nums[i], max_dp[i-1]*nums[i])

            # we update the min_dp in the same way, we consider the same 3 options, but this time we choose the min one
            min_dp[i] = min(nums[i], min_dp[i-1]*nums[i], max_dp[i-1]*nums[i])


        # by the end of this, we have considered all the possibilities, and we can return max(max_dp)
        return max(max_dp)
