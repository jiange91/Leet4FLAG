# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = n
        def binarySearch(start, end):
            nonlocal res
            if start >= end:
                if isBadVersion(end):
                    res = min(res,end)
                return
            
            middle = (start + end) // 2
            
            if isBadVersion(middle):
                res = min(res, middle)
                binarySearch(start, middle-1)
            else:
                binarySearch(middle+1,end)
            
        binarySearch(1,n)
        return res