class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        # we have to use kadane's algorithm but with a few tweaks
        # circular subarray means we have to exclude the min_subarray_sum continugous array from the total_sum

        # step 1: calculate the max_sum_subarray
        current_max_sum = nums[0]
        max_sum_subarray = nums[0]

        for i in range(1, len(nums)):

            # at each i we use Kadane's to check if we gotta extend or we gotta start fres
            current_max_sum = max(nums[i], current_max_sum + nums[i])
            max_sum_subarray = max(max_sum_subarray, current_max_sum)

        # step 2: calculate the min_subarray_sum

        current_min_sum = nums[0]
        min_sum_subarray = nums[0]

        for i in range(1, len(nums)):

            # at each i, we use a tweaked kadane to check if we need to extend or start fresh
            current_min_sum = min(nums[i], current_min_sum + nums[i])
            min_sum_subarray = min(min_sum_subarray, current_min_sum)

        # check for the edge case in case all elements are negetive
        if max_sum_subarray < 0:
            return max_sum_subarray

        # if that is not the case, we need to find the total sum of all the elements present in nums
        return max(max_sum_subarray, sum(nums) - min_sum_subarray) 