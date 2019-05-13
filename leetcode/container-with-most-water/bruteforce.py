class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_vol = -1
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                vol = (j - i) * min(height[i], height[j])
                
                if vol > max_vol:
                    max_vol = vol
        return max_vol
        