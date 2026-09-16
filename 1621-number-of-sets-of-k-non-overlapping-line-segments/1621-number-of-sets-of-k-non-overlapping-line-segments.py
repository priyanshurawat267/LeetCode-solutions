class Solution(object):
    def numberOfSets(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        mod = (10**9 +7)
        # Calculation 
        N = n + k - 1 
        R = 2 * k
        ans = 1
        for i in range(1, R + 1):
            ans = ans * (N - R + i)% mod
            ans = ans * pow(i,mod - 2, mod )% mod
        return ans
    