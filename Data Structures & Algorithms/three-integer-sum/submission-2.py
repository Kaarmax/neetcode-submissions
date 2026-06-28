class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        a = 0
        L = []

        nums.sort()
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if a == - nums[left] - nums[right]:
                    L.append([a, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                elif a > - nums[left] - nums[right]:
                    right -= 1
                else:
                    left += 1
        return L

        
        
        