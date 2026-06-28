class Solution:
    def search(self, nums: List[int], target: int) -> int:
        offset = 0
        while len(nums) > 0:
            n = len(nums) // 2
            if nums[n] == target:
                return offset + n
            elif nums[n] > target:
                nums = nums[:n]
            else:
                offset += n + 1
                nums = nums[n+1:]
        return -1