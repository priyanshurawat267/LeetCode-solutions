class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # Always use nums1 as the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)
        low = 0
        high = m

        while low <= high:

            partition1 = (low + high) // 2
            partition2 = (m + n + 1) // 2 - partition1

            # Left side
            if partition1 == 0:
                left1 = float("-inf")
            else:
                left1 = nums1[partition1 - 1]

            if partition2 == 0:
                left2 = float("-inf")
            else:
                left2 = nums2[partition2 - 1]

            # Right side
            if partition1 == m:
                right1 = float("inf")
            else:
                right1 = nums1[partition1]

            if partition2 == n:
                right2 = float("inf")
            else:
                right2 = nums2[partition2]

            # Correct partition
            if left1 <= right2 and left2 <= right1:

                # Odd number of elements
                if (m + n) % 2 == 1:
                    return max(left1, left2)

                # Even number of elements
                return (max(left1, left2) +
                        min(right1, right2)) / 2.0

            # Move partition1 to left
            elif left1 > right2:
                high = partition1 - 1

            # Move partition1 to right
            else:
                low = partition1 + 1