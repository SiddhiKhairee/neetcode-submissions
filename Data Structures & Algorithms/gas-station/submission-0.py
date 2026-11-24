class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        # step 1: calculate the changes array as gas[i] - cost[i]
        # changes[i] represents how much net fuel would be gone when we enter and leave i
        # if changes[i] is negetive then the cost to move from i is more than the refueled amount, so we cannot move from there

        if sum(gas) < sum(cost):
            return -1

        start = 0
        tank = 0
# at every i, calculate the change[i] value
# if at any point if tank < 0 then consider i+1
        for i in range(len(gas)):
            tank += (gas[i] - cost[i])

            if tank < 0:
                tank = 0
                start = i+1

        return start