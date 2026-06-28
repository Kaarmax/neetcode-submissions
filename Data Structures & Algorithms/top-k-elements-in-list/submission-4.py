class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = {}
        freq = [[] for i in range(len(nums) + 1)]

        for i in nums:
            my_dict[i] = 1 + my_dict.get(i, 0)
        for num, c in my_dict.items():
            freq[c].append(num)
        print(freq)
        ls = []
        for i in range(len(freq)-1, 0, -1):
            if freq[i] != []:
                for num in freq[i]:
                    ls.append(num)
                    k -= 1
            if k == 0:
                return ls

            