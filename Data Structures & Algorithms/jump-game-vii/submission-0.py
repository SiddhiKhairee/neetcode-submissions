class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:

        # we have to do a breadth first search
        # we will make a queue
        # at index i, we can jump within a range say [a, b]
        # all the indices within a to b will be pushed into the queue
        # when we pop an index out of the queue, we will explore its reachable jump length or indices
        # Note: we also maintain another variable called farthest
        # this variable will be initialized to 0
        # everytime we pop out of the queue, we will update the farthest with the max_reachable_index by the popped index

        farthest_visited = 0 # we start at the 0th index
        queue = deque([0]) # we have a single first index into the queue

        # apply breadth first search
        while queue:

            # we pop the index out of the queue
            popped_index = queue.popleft()
            # for this popped index, we have to get the reachable index range by this popped index
            start = max(popped_index+minJump , farthest_visited+1) 
            # we do this because if a range is already visited by farthest, we do not consider it again, essential in maintaining O(n) time complexity
            end = min(popped_index+maxJump, len(s)-1)

            # now for this newly acquired range, we need to add it to the queue
            for i in range(start, end+1):
                # we check if s[i] == 0
                if s[i] == '0':
                    # append it to the queue
                    queue.append(i)
                    # say if we append the last index to the queue, it means one of the elements in our range ended up being the last element, so we return true
                    if i == len(s)-1:
                        return True

            # everytime we pop out of the queue, we have to update the farthest as per the newly calculated range
            farthest_visited = popped_index + maxJump

        return False


                
            

        
        