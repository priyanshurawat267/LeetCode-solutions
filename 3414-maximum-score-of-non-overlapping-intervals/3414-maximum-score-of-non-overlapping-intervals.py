class Solution(object):
    def maximumWeight(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        import bisect
        n = len(intervals)
        arr = []

        for i in range(n):
            l, r, w = intervals[i]
            arr.append([l, r, w, i])
        arr.sort()

        starts = [x[0] for x in arr]
        nxt = [0] * n

        for i in range(n):
            nxt[i] = bisect.bisect_right(starts, arr[i][1])
        dp = [[(0, ()) for _ in range(5)] for _ in range(n + 1)]

        def better(a, b):
            if a[0] > b[0]:
                return a
            if a[0] < b[0]:
                return b
            return a if a[1] < b[1] else b

        for i in range(n - 1, -1, -1):
            for k in range(1, 5):
                skip = dp[i + 1][k]
                score, indices = dp[nxt[i]][k - 1]

                take = (
                    score + arr[i][2],
                    tuple(sorted(indices + (arr[i][3],)))
                )
                dp[i][k] = better(skip, take)
        return list(dp[0][4][1])
        