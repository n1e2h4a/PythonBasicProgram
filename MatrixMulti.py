P = int(input("Enter the row number for matrix1:-"))
Q = int(input("Enter the column number for matrix2:-"))
N = int(input("Enter the column number for matrix1/row number of matrix2:-"))
print("Enter the Elements for matrix1:-")
Matrix1 = [[int(input())for i in range(N)]for j in range(P)]
print('Matrix1:')
for i in range(P):
    for j in range(N):
        print(format(Matrix1[i][j], "<5"), end=" ")
    print()
print("Enter the Elements for matrix2:-")
Matrix2 = [[int(input())for i in range(Q)]for j in range(N)]
print('Matrix2:-')
for i in range(N):
    for j in range(Q):
        print(format(Matrix2[i][j], "<5"), end=" ")
    print()
Result = [[0 for i in range(Q)]for j in range(P)]
for i in range(P):
    for j in range(Q):
        for k in range(N):
            Result[i][j] = Result[i][j] + Matrix1[i][k] * Matrix2[k][j]
print("Result Is")
for i in range(P):
    for j in range(Q):
        print(format(Result[i][j], "<5"),end=" ")
    print()




