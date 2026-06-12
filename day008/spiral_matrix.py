class Solution(object):
    @staticmethod
    def sprialOrder(matrix):
        top,bottom=0,len(matrix)-1
        left,right=0,len(matrix[0])-1
        result=[]
        while top<=bottom and left<=right:
            for i in range(left,right+1):
                result.append(matrix[top][i])
            top+=1
            for j in range(top,bottom+1):
                result.append(matrix[j][right])
            right-=1
            if top<=bottom:
                for k in range(right,left-1,-1):
                    result.append(matrix[bottom][k])
                bottom-=1
            if left<=right:
                for l in range(bottom,top-1,-1):
                    result.append(matrix[l][left])
                left+=1
        matrix[:]=result
        return matrix

print(Solution.sprialOrder([[5,1,9],[2,4,8],[13,3,6],[15,14,12]]))
