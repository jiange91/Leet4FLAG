class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = len(nums1), len(nums2)
        if n1 > n2:
            return self.findMedianSortedArrays(nums2, nums1)
        elif not n1:
            return self.normalWay(nums2)
        elif not n2:
            return self.normalWay(nums1)
        i, j, tl = 0, n1, n1 + n2
        while i <= j:
            s1 = (i + j) // 2
            s2 = (tl + 1) // 2 - s1
            lmax1 = float('-inf') if s1 <= 0 else nums1[s1-1]
            rmin1 = float('inf') if s1 >= n1 else nums1[s1]
            lmax2 = float('-inf') if s2 <= 0 else nums2[s2 - 1]
            rmin2 = float('inf') if s2 >= n2 else nums2[s2]
            if lmax1 <= rmin2 and lmax2 <= rmin1:
                if not tl & 1:
                    return (max(lmax1, lmax2) + min(rmin1, rmin2)) / 2
                else:
                    return (max(lmax1, lmax2))
            elif lmax1 > rmin2:
                j = s1 - 1
            else:
                i = s1 + 1
    
    def normalWay(self, nums):
        n = len(nums)
        if not n & 1:
            return (nums[n//2 - 1] + nums[n//2]) / 2
        else:
            return nums[n//2]
