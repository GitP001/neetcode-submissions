class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices={}
        for i,num in enumerate(nums):
            indices[num]=i
        
        for i in range(0,len(nums)):
            difference=target-nums[i]
            if difference in indices and i!= indices[difference]:
                return [i,indices[difference]]

