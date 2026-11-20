class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:

        n = len(arr)
        if n == 1:
            return n
        if n == 2:
            if arr[0] != arr[1]:
                return n
            else:
                return 1
        max_length = 0
        # we start considering only if an array has 3 elements or more
        if arr[0] != arr[1]:
            current_length = 2
            max_length = current_length
        else: # this means that the first and second elements are equal
            current_length = 1
            max_length = current_length
        for i in range(2, n):

            # comparisons are alternate
            if arr[i-2] < arr[i-1] > arr[i] or arr[i-2] > arr[i-1] < arr[i]:
                current_length += 1
                max_length = max(current_length, max_length)
            # comparisons repeat
            elif arr[i-1] == arr[i]:
                current_length = 1
                max_length = max(current_length, max_length)

            else:
                current_length = 2
                max_length = max(current_length, max_length)
        return max_length

        