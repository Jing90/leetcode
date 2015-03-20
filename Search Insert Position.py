# Given a sorted array and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.

# You may assume no duplicates in the array.
# Here are few examples.
# [1,3,5,6], 5 → 2
# [1,3,5,6], 2 → 1
# [1,3,5,6], 7 → 4
# [1,3,5,6], 0 → 0

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        left = 0
    	right = len(A)
    	middle = (left + right) / 2
    	while middle >= 0:
            if target == A[middle]:
                return middle
            elif target < A[middle]:
                right = middle
                middle = (left + right) / 2
            else:
                left = middle
                middle = (left + right) / 2
            if left == middle:
                if target > A[middle]:
                    return right
                else:
                    return left
