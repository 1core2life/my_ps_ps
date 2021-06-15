class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        col = len(mat)
        row = len(mat[0])
        
        result = 0
        x = 0
        for i in range(0, col):
            if row % 2 == 1 and x == ceil(col/2):
                result += mat[i][x]
            else:
                result += mat[i][x]
                result += mat[i][row -1 - x]
                
            x += 1
        
        return result
