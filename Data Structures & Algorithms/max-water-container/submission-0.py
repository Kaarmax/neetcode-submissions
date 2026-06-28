class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_wid = len(heights)
        left, right = 0, len(heights)-1
        max_con = 0
        while left < right:
            size = (right - left) * min(heights[left], heights[right])
            if size > max_con:
                max_con = size
                print(max_con)
            if min(heights[left], heights[right]) == heights[left]:
                left += 1
            else:
                right -= 1
        return max_con