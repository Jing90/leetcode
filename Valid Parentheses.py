# https://leetcode.com/problems/valid-parentheses/

# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

class Solution:
	#@return a boolean
	def isValid(self, s):
		tmp = []
		for i in range(len(s)):
			if s[i] == '(' or s[i] == '[' or s[i] == '{':
				tmp.append(s[i])
			elif s[i] == ')':
				if len(tmp) > 0 and tmp[len(tmp) - 1] == '(':
					tmp.pop()
				else:
					return False
			elif s[i] == ']':
				if len(tmp) > 0 and tmp[len(tmp) - 1] == '[':
					tmp.pop()
				else:
					return False
			elif s[i] == '}':
				if len(tmp) > 0 and tmp[len(tmp) - 1] == '{':
					tmp.pop()
				else:
					return False
		if len(tmp) == 0:
			return True
		else:
			return False
