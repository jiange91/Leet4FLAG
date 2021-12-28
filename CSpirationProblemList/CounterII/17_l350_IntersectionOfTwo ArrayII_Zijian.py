class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s = {}
        ans = []
        for i in nums1:
            if i in s:
                s[i] = s[i] + 1
            else:
                s[i] = 1
        for i in nums2:
            if i in s and s[i] > 0:
                ans.append(i)
                s[i] = s[i] - 1
        return ans