class Solution:
    def trap(self, height: List[int]) -> int:
        left = [0]
        right = [0]
        height_reverse = height.copy()
        height_reverse.reverse()
        for i in height:
            if i > left[-1]:
                left.append(i)
            else:
                left.append(left[-1])
        for i in height_reverse:
            if i > right[-1]:
                right.append(i)
            else:
                right.append(right[-1])
        right.reverse()
        a = 0
        for i, num in enumerate(height):
            if num < min(left[i], right[i]):
                a += min(left[i], right[i]) - num
        return a
            

