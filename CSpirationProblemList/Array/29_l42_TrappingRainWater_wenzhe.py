class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        res = 0
        
        while(left < right):
            left_val = height[left]
            right_val = height[right]
            if height[left] < height[right]:
                left_max = max(left_max, left_val)
                res += left_max - left_val
                left+=1
            else:
                right -= 1
                right_max = max(right_max, right_val)
                res += right_max - right_val
        return res