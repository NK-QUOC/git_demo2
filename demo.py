
def check_matrix_symmetry(matrix):

	N = len(matrix)
	center = int(N/2)
	transpose_matrix = [[row[i] for row in matrix] for i in range(len(matrix[0]))]

	for i in range(center):
		# so sánh qua trục x
		same_list_x = all(x == y for x, y in zip(matrix[i], matrix[N-i-1]))
		# so sánh qua trục y
		same_list_y = all(x == y for x, y in zip(transpose_matrix[i], transpose_matrix[N-i-1]))
		if not (same_list_x and same_list_y):
			return False

	return True



if __name__ == "__main__":

	matrix = [[0,1,1,1,0],
			  [0,1,0,1,0],
			  [1,0,0,0,1],
			  [0,1,0,1,0],
			  [0,1,1,1,0]]
	matrix_symmetry = check_matrix_symmetry(matrix)
	if matrix_symmetry:
		print("Yes")
	else:
		print("No")