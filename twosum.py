class Solution:
    def twoSum(self, nums ,target):
        flag= True
        while flag == True:
            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i!=j:
                        if nums[i]+nums[j] == target:
                            return[i,j]
                            flag = False


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {} 
        
        for i, num in enumerate(nums):
            complement = target - num
            
            if complement in seen:
                return [seen[complement], i]
        
            seen[num] = i
