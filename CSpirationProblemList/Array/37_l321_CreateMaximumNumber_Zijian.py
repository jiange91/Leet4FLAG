class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def maxSub(nums, k):
            if not k: 
                return []
            ans = [float('-inf')] * k
            cur = 0
            n = len(nums)
            for i in range(n):
                while cur > 0 and k - cur + i < n and nums[i] > ans[cur-1]:
                    cur -= 1
                if cur < k:
                    ans[cur] = nums[i]
                    cur += 1
            return ans
        
        def merge(nums1, nums2, k):
            def gt(nums1, nums2, i, j):
                while i < len(nums1) and j < len(nums2) and nums1[i] == nums2[j]:
                    i += 1
                    j += 1
                return j == len(nums2) or (i < len(nums1) and nums1[i] > nums2[j])
            ans = []
            i, j = 0, 0
            for _ in range(k):
                if gt(nums1, nums2, i, j):
                    ans.append(nums1[i])
                    i += 1
                else:
                    ans.append(nums2[j])
                    j += 1
            return ans
        
        def dmax(nums1, nums2):
            for i in range(len(nums1)):
                if nums1[i] > nums2[i]:
                    return nums1
                elif nums2[i] > nums1[i]:
                    return nums2
            return nums1
        
        n1, n2 = len(nums1), len(nums2)
        if n1 > n2:
            return self.maxNumber(nums2, nums1, k)
        ans = [float('-inf')] * k
        for i in range(max(0, k-n2), n1+1):
            m1, m2 = maxSub(nums1, i), maxSub(nums2, k-i)
            m = merge(m1, m2, k)
            ans = dmax(ans, m)
        return ans
    
