class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = {}
        for num in nums:
            if num not in my_dict:
                my_dict[num] = 1
            else:
                my_dict[num] += 1
        L = []
        while k > 0:
            for key in my_dict:
                if my_dict[key] == max(my_dict.values()):
                    L.append(key)
                    break
            del my_dict[L[-1]]
            k -= 1
        return L
            