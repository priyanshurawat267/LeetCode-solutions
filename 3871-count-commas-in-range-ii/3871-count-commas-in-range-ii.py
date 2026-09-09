class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        Sol = 0        # store int value
        start = 1000   # starting value,s
        commas = 1     # 1000 to first commas....1001 __2, 1002__3

        while start  <= n:                  # 1000 < n value  
            end = min(n, start * 1000 - 1)  # return minimun  value
            Sol += (end - start + 1) * commas # 

            start *= 1000
            commas += 1      # commas = commas + 1

        return Sol           # Ans