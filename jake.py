
matrix = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]

matrix = [[1,2,3],[4,5,6]]

matrix = [[1,2,3],[4,5,6],[7,8,9]]

transposed = [[0 for x in range(len(matrix))] for x in range(len(matrix[0]))]

for t in range(0, len(matrix)):
	for tt in range(0, len(matrix[t])):
		transposed[tt][t] = matrix[t][tt]
