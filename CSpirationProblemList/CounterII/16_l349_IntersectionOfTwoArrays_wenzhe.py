class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict1 = dict()
        
        for n in nums1:
            dict1[n] = True
        
        res = []
        for n in nums2:
            if dict1.get(n,False):
                dict1[n] = False
                res.append(n)
        return res