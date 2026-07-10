class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        assert 1<= len(nums) <= 1000
        assert -10000000<= target <= 10000000
        # O(n^2) solution
        index_set=[0,0]
        for i in range(0, len(nums)-1):
            for j in range(i,len(nums)):
                if ((nums[i]+nums[j]) == target) and i!=j:
                    index_set[0]=i
                    index_set[1]=j
        return index_set
        
