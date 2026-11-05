class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        count = 0

        for i in arr1:
            found = False

            for j in arr2:
                if abs(i-j) <= d:
                    
                    found = True
                    break

            if found == False:
                count += 1

        return count



        