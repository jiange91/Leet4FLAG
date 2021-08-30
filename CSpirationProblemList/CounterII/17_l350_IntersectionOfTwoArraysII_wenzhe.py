class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict1 = dict()
        
        for n in nums1:
            dict1[n] = dict1.get(n, 0) + 1
        
        res = []
        for n in nums2:
            if dict1.get(n,0) > 0:
                dict1[n] -= 1
                res.append(n)
        return res