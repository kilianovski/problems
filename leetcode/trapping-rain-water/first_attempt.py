class Solution:
    def trap(self, height) -> int:
        covered_points = set()
        volume = 0
        
        pot_covered_points = []
        pot_volume = 0
        current_highest = 0
        
        i = 0
        while i < len(height):
            
            block = height[i]
            max_height_left = block
            max_height_right = block
            j, k = i, i

            while j >= 0:
                max_height_left = max(height[j], max_height_left)
                j -= 1

            while k < len(height):
                max_height_right = max(height[k], max_height_right)
                k += 1

            volume += min(max_height_left, max_height_right) - block
            
            i += 1


        return volume


print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(Solution().trap([4,2,3]))
