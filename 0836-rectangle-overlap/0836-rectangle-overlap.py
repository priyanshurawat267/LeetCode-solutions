class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """

        x1, y1, x2, y2 = rec1
        a1, b1, a2, b2 = rec2

        x_overlap = x1 < a2 and a1 < x2
        y_overlap = y1 < b2 and b1 < y2

        return x_overlap and y_overlap