class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        eCount = [0] * (max(nums) + 1)
        
        for n in nums:
            eCount[n] += 1
            
        prevDel, nprevDel = 0,0
        
        for i in range(len(eCount)):
            newNPrevDel = max(nprevDel, prevDel)
            newPrevDel = max(nprevDel + eCount[i] * i, prevDel)
            prevDel, nprevDel = newPrevDel, newNPrevDel
        return max(prevDel, nprevDel)