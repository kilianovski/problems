from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)

        while l < r:
            i = int((r + l) / 2)

            el = nums[i]

            if el < target:
                i+=1
                l = i
            
            elif el > target:
                r = i
            else:
                return i

        return i

s = Solution()
# print(s.searchInsert([1, 3], 2))
# print(s.searchInsert([1, 3], 0))
print(s.searchInsert([1,3, 4], 7))
