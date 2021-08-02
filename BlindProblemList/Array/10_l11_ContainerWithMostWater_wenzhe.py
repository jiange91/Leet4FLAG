class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height)-1
        
        result = 0
        while i < j:
            if height[i] < height[j]:
                result = max(result, height[i] * (j-i))                
                i += 1
            elif height[i] > height[j]:
                result = max(result, height[j] * (j-i))
                j -= 1
            else:
                result = max(result, height[j] * (j-i))
                i += 1
                j -=1
        return result