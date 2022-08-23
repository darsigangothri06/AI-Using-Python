mat1 = [[1,2],[1,2],[1,2]]
mat2 = [[1,2],[1,2],[1,2]]
res = []
for i in range(len(mat1)):
    temp = []
    for j in range(len(mat1[0])):
        temp.append(mat1[i][j] + mat2[i][j])
    res.append(temp)
print(res)