class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic = collections.defaultdict(int)
        for i in range(len(numbers)):
            dic[numbers[i]] = i + 1
        print(dic)
        for i in range(len(numbers)):
            if target - numbers[i] in dic:
                return[i + 1, dic[target - numbers[i]]]