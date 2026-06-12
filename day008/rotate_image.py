class solution(object):
    def rotate(matrix):
        n=len(matrix)
        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for i in range(n):
            matrix[i].reverse()
        print("\n")
        print(f"Matrix has {len(matrix)} rows and {len(matrix[0])} columns.")
        return matrix

print(solution.rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(solution.rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))
print(solution.rotate([[5,1,9],[2,4,8],[13,3,6]]))

