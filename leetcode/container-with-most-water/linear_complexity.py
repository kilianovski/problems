# Idea:
# 1. Start with the widest container
# 2. Try to maximize the capacity 
#   - the only way to do so is to have higher line in a pair
#   - so move the shortest bulk with hope that it will increase capacity

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_vol = -1 # max volume
        i, j = 0, len(height)

        while i < j:
            vol = (j - i) * min(height[i], height[j])
            if vol > max_vol:
                max_vol = vol
            
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
            

        return max_vol