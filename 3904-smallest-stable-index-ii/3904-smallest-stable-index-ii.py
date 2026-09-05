class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)

        rightMin = [0] * n
        rightMin[n - 1]  = nums[n -1]

        for i in range(n-2, -1, -1):
            rightMin[i] = min(rightMin[i+1], nums[i])
        leftMax = float('-inf')

        for i in range(n):
            leftMax = max(leftMax, nums[i])

            if leftMax - rightMin[i] <= k:
                return i 
        return -1