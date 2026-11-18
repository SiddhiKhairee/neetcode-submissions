class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # start from last index
        n = len(nums) 
        final_destination = n-1
        # we gotta ensure that this final destination reaches 0
        for i in range(n-2, -1, -1):
            # we check nums[i] + i for every single element
            val = nums[i] + i 
            # if this value is greater that the final_destination index, that means from ith position we can reach the last index
            if val >= final_destination:
                # thus we then change the value of the final_destination, and make it to the ith index
                final_destination = i

        # ideally, we must be able to get our final_desitination to 0th index for the program to return true, if due to any reason that does not happen then we can say that our final_destination is not reachable from 0th index
        return (final_destination == 0)
             