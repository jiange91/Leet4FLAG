class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # heap: O(nlogn)
        # bucket: O(n)
        
        d = collections.Counter()
        fb = [[] for _ in range(len(nums)+1)]
        for n in nums:
            d[n] += 1
        for n in d:
            fb[d[n]].append(n)
        ans = [i for row in fb for i in row][-1*k::]
        return ans
