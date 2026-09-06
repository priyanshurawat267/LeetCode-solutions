class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        n = len(s)
        m = len(t)

        var = [[0]*(m+1) for _ in range(n+1)]

        for i in range(n+1): var[i][m] = 1
        for i in range(n-1,-1, -1,):
            for j in range(m-1, -1, -1):

                var[i][j] = var[i+1][j]

                if s[i] == t[j]: var[i][j] += var[i+1] [j+1]
                
        return var[0][0]