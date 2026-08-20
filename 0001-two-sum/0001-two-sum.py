class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for i, num in enumerate(nums):
            needed = target - num
            if needed in seen:
                return [seen[needed], i]
            seen[num] = i
