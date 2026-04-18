class Solution:
    def searchMatrix(self, matrix, target):
        for row in matrix:
            for num in row:
                if num == target:
                    return True
        return False