class Solution(object):
    def setZeroes(matrix):
        rows_to_zero=set()
        cols_to_zero=set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    rows_to_zero.add(i)
                    cols_to_zero.add(j)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in rows_to_zero:
                    matrix[i][j]=0
                if j in cols_to_zero:
                    matrix[i][j]=0
        
        return matrix
            
print(Solution.setZeroes([[1,1,1],[1,0,1],[1,1,1]]))
print(Solution.setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))
        