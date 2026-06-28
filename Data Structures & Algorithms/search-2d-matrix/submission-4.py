class Solution: 
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 1:
            return target in matrix[0]
        else:
            m = len(matrix)
            mid = m // 2
            if target < matrix[mid][0]:
                return self.searchMatrix(matrix[:mid], target)
            else:
                if target in matrix[mid]:
                    return True
                return self.searchMatrix(matrix[mid:], target)