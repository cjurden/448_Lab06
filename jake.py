
#Transposition

matrix = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]

matrix = [[1,2,3],[4,5,6]]

matrix = [[1,2,3],[4,5,6],[7,8,9]]

transposed = [[0 for x in range(len(matrix))] for x in range(len(matrix[0]))]

for t in range(0, len(matrix)):
	for tt in range(0, len(matrix[t])):
		transposed[tt][t] = matrix[t][tt]

##################################################################################
#Multiplication

matrix1 = [[1],[2],[3]]
matrix2 = [[1,2,3]]

matrix1 = [[1,4,1],[5,2,2]]
matrix2 = [[1],[2],[3]]

matrix1 = [[1,4,1],[5,2,2]]
matrix2 = [[1,2],[2,1],[3,6]]

if len(matrix1[0]) == len(matrix2):
	multiplied = [[0 for x in range(len(matrix2[0]))] for x in range(len(matrix1))]
	for i in range(0, len(multiplied)):
		for j in range(0, len(multiplied[i])):
			temp = 0
			for k in range(0, len(matrix1[0])):
				temp = temp + (matrix1[i][k] * matrix2[k][j])
			multiplied[i][j] = temp
else:
	print 'Cannot multiply matrices'
