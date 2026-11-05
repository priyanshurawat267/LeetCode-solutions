class Solution(object):
    def minSumOfLengths(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        n = len(arr)
        dp = [float('inf')] * (n + 1)

        left = 0
        total = 0
        ans = float('inf')

        for right in range(n):

            total += arr[right]

            while total > target:
                total -= arr[left]
                left += 1

            dp[right + 1] = dp[right]

            if total == target:
                length = right - left + 1

                if dp[left] != float('inf'):
                    ans = min(ans, length + dp[left])

                dp[right + 1] = min(dp[right + 1], length)

        return ans if ans != float('inf') else -1
