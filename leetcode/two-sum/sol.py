class Solution:
    def twoSum(self, nums, target: int):
        i_want_you = {}
        
        for i in range(len(nums)):
            
            item = nums[i]
            
            if item in i_want_you:
                return i_want_you[item], i
            i_want_you[target-item] = i