class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        i, j = 0, n - 1
        while i < j:
            mid = i + (j - i) // 2
            if n - mid == citations[mid]:
                return n - mid
            if n - mid > citations[mid]:
                i = mid + 1
            else:
                j = mid
        return n - i if (n-i) <= citations[i] else 0
