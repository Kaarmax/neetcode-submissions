class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        L = []
        res = [0] * len(temperatures)
        for i, num in enumerate(temperatures):
            while L and num > L[-1][0]:
                stackt, stacki = L.pop()
                res[stacki] = i - stacki
            L.append([num, i])
        return res