class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        start = collections.defaultdict(int)
        if nums == []:
            return 0
        for i in nums:
            if i - 1 not in nums:
                start[i] = i
        max_c = 0
        for key in start:
            counter = 1
            n = key
            
            for i in range(len(nums)):
                if n + 1 in nums:
                    counter += 1
                    n += 1
            if counter > max_c:
                max_c = counter
        return max_c
