# https://leetcode.com/problems/spiral-matrix/

# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
# For example,
# Given the following matrix:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# You should return [1,2,3,6,9,8,7,4,5].

class Solution:
  # @param matrix, a list of lists of integers
  # @return a list of integers
	def spiralOrder(self, matrix):
		array = []
		
		if len(matrix) == 0:
		    return array
		    
		m = len(matrix)
		n = len(matrix[0])
		i = 0
		j = 0
		curr_m = 0
		curr_n = 0
		while len(array) < m * n:
			while j < n - curr_n/2:
				array.append(matrix[i][j])
				j = j + 1
			if len(array) == m * n:
				break
			else:
				curr_m = curr_m + 1


			j = j - 1
			i = i + 1
			while i < m - curr_m/2:
				array.append(matrix[i][j])
				i = i + 1
			if len(array) == m * n:
				break
			else:
				curr_n = curr_n + 1


			i = i - 1
			j = j - 1
			while j > -1 + curr_n/2:
				array.append(matrix[i][j])
				j = j - 1
			if len(array) == m * n:
				break
			else:
				curr_m = curr_m + 1


			j = j + 1
			i = i - 1
			while i > -1 + curr_m/2:	
				array.append(matrix[i][j])
				i = i - 1
			curr_n = curr_n + 1


			i = curr_m/2
			j = j + 1

		return array
