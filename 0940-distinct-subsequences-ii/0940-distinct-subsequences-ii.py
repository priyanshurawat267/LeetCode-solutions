class Solution(object):
    def distinctSubseqII(self, s):
        """
        :type s: str
        :rtype: int
        """
        MOD = 10**9 + 7

        dp = [0] * (len(s) + 1)
        dp[0] = 1
        last = [-1] * 26

        for i, ch in enumerate(s, 1):
            x = ord(ch) - ord('a')
            dp[i] = 2 * dp[i - 1]

            if last[x] != -1:
                dp[i] -= dp[last[x] - 1]

            dp[i] %= MOD
            last[x] = i
        # Remove the empty subsequence
        return (dp[len(s)] - 1) % MOD