# Reading all 3 CSV files.
f1 = open('2by3.csv', 'r')
f2 = open('3by3.csv', 'r')
f3 = open('3by4.csv', 'r')

# Declare the 3 matrices.
m1,m2,m3 = [],[],[]

# Assign values from the files to matrices.
# Print to check the values.
for line in f1:
	m1.append(line.split(','))
print(m1)

for line in f2:
	m2.append(line.split(','))
print(m2)

for line in f3:
	m3.append(line.split(','))
print(m3)

# Function to check whether the matrix is valid.
def checkMat(m):

	l = []
    
  # Get the lengths of all rows.
	for x in range(0, len(m)):
		l.append(len(m[x]))

  # Compare all lengths.
	for x in range(1, len(l)):
		if l[x-1] == l[x]:
			mat = True  # Valid matrix.
		else:
			mat = False # Invalid matrix.

	return mat

print(checkMat(m1))
print(checkMat(m2))
print(checkMat(m3))
