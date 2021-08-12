class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        def getBucketId(i):
            return i//(t+1)
        buckets = dict()
        for i,n in enumerate(nums):
            bucketId = getBucketId(n)
            if bucketId in buckets:
                return True
            prevBucket = buckets.get(bucketId-1, float('inf'))
            nextBucket = buckets.get(bucketId+1, float('inf'))
            if prevBucket != float('inf') and n - prevBucket <= t:
                return True
            if nextBucket != float('inf') and nextBucket - n <= t:
                return True
            buckets[bucketId] = n
            if i>= k:
                buckets.pop(getBucketId(nums[i - k]))
                
        return False