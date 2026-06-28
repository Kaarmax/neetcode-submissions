class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        L = [1] * len(nums)
        
        prefix = 1
        for i in range(len(nums)):
            L[i] = prefix
            prefix *= nums[i]
        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            L[i] *= suffix
            suffix *= nums[i]
        return L