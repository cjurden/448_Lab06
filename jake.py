############################################################################################
#Transposition

def TransposeMatrix(matrix):
	transposed = [[0 for x in range(len(matrix))] for x in range(len(matrix[0]))]
	for i in range(0, len(matrix)):
		for j in range(0, len(matrix[i])):
			transposed[j][i] = matrix[i][j]
	print 'Transposed Matrix:'
	printMatrix(transposed)

############################################################################################
#Multiplication

def MultiplyMatrices(matrix1,matrix2):
	if len(matrix1[0]) == len(matrix2):
		multiplied = [[0 for x in range(len(matrix2[0]))] for x in range(len(matrix1))]
		for i in range(0, len(multiplied)):
			for j in range(0, len(multiplied[i])):
				temp = 0
				for k in range(0, len(matrix1[0])):
					temp = temp + (matrix1[i][k] * matrix2[k][j])
				multiplied[i][j] = temp
		print 'Multiplied Matrix:'
		printMatrix(multiplied)
	else:
		print 'Cannot multiply matrices'

############################################################################################
#Addition

def AddMatrices(matrix1,matrix2):
	if len(matrix1)==len(matrix2) and len(matrix1[0])==len(matrix2[0]):
		added = [[0 for x in range(len(matrix1[0]))] for x in range(len(matrix1))]
		for i in range(0, len(added)):
			for j in range(0, len(added[0])):
				added[i][j] = matrix1[i][j] + matrix2[i][j]
		print 'Added Matrix:'
		printMatrix(added)
	else:
		print 'Cannot add matrices'
	

############################################################################################
#Print Matrix

def printMatrix(matrix):
	for i in range(0, len(matrix)):
		string = ''
		for j in range(0, len(matrix[0])):
			string = string + '\t' + str(matrix[i][j])
		print string

############################################################################################
############################################################################################
#PROGRAM STARTS HERE

#x = int(raw_input("input your stuff: ")) #Input from user

matrix = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
TransposeMatrix(matrix)

matrix = [[1,2,3],[4,5,6]]
TransposeMatrix(matrix)

matrix = [[1,2,3],[4,5,6],[7,8,9]]
TransposeMatrix(matrix)

matrix1 = [[1],[2],[3]]
matrix2 = [[1,2,3]]
MultiplyMatrices(matrix1,matrix2)

matrix1 = [[1,4,1],[5,2,2]]
matrix2 = [[1],[2],[3]]
MultiplyMatrices(matrix1,matrix2)

matrix1 = [[1,4,1],[5,2,2]]
matrix2 = [[1,2],[2,1],[3,6]]
MultiplyMatrices(matrix1,matrix2)

matrix1 = [[1],[2],[3]]
matrix2 = [[2],[3],[4],[5]]
AddMatrices(matrix1,matrix2)

matrix1 = [[1],[2],[3]]
matrix2 = [[2],[3],[4]]
AddMatrices(matrix1,matrix2)
