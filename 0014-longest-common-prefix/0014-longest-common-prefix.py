class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        str = strs[0]

        for i in range(1, len(strs)):
            while not strs[i].startswith(str):

                str = str[:-1]
        return str



        