class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        a = 0
        for i in nums:
            if i != 0:
                product *= i
            else:
                a += 1
        L = []
        if a > 1:
            for i in range(len(nums)):
                L.append(0)
            return L
        for i in range(len(nums)):
            if a > 0 and nums[i] != 0:
                L.append(0)
            elif a > 0 and nums[i] == 0:
                L.append(product)
            else:
                L.append(product//nums[i])
        return L
