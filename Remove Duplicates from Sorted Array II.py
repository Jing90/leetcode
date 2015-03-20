# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

# Follow up for "Remove Duplicates":
# What if duplicates are allowed at most twice?
# For example,
# Given sorted array A = [1,1,1,2,2,3],
# Your function should return length = 5, and A is now [1,1,2,2,3].

class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
    	start = 0
    	end = 0
    	num = len(A)
    	for i in range(num - 1):
    		if i + 1 < num and A[i + 1] == A[i] and i + 2 < num and A[i + 2] == A[i]:
    			start = i + 2
    			end = start
    			while end + 1 < num and A[end + 1] == A[i]:
    				end = end + 1
    			if end >= start:
    				for j in range(end + 1, num):
    					A[j - (end - start + 1)] = A[j]
    				num = num - (end - start + 1)
    			i = start
    	return num
