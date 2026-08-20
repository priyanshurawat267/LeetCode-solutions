class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        cycle = 2 * numRows - 2
        result = ""
        for row in range(numRows):
            for i in range(row, len(s), cycle):
                result += s[i]
                if row != 0 and row != numRows - 1:
                    diagonal = i + cycle - 2 * row
                    if diagonal < len(s):
                        result += s[diagonal]
        return result




        