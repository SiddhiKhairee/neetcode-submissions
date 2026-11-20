class Solution:
    def jump(self, nums: List[int]) -> int:

        # # will keep a count of the number of jumps 
        jumps = 0

        # keep two pointers to keep a track of the jumpable window

        left = right = 0

        while right < len(nums) -1:
            farthest_jump = 0
            for i in range(left, right+1):
                farthest_jump = max(farthest_jump, nums[i]+i)
            left = right+1
            right = farthest_jump
            jumps += 1

        return jumps
    