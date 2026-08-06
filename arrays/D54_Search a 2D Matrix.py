class Solution:
    def searchMatrix(self, matrix, target):
        rows = len(matrix)
        cols = len(matrix[0])

        lo = 0
        hi = rows * cols - 1

        while lo <= hi:
            mid = lo + (hi - lo) // 2

            row = mid // cols
            col = mid % cols

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                lo = mid + 1
            else:
                hi = mid - 1

        return False