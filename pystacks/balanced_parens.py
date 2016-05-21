"""
written-by : John Mezzanotte
date: 5-19-2016
descr: this module uses a stack to implement a solution to the balanced parenthesis 
	   problem. 
"""

# Names for characters 
left_normal = '('
right_normal = ')'
left_curly = '{'
right_curly = '}'
left_square = '['
right_square = ']'

# try to implement a switch like structure in python using a dict
def is_balanced(exp):

	stack = []
	failed = False
	counter = 0

	while failed == False and counter < len(exp) and len(exp) > 0:

		x = exp[counter]

		if x == left_normal : 
			stack.append(x)
		elif x == left_curly:
			stack.append(x)
		elif x == left_square:
			stack.append(x)
		elif x == right_normal:
			if len(stack) == 0 or stack.pop() != left_normal:
				failed = True
		elif x == right_curly :
			if len(stack) == 0 or stack.pop() != left_curly:
				failed = True
		elif x == right_square :
			if len(stack) == 0 or stack.pop() != left_square:
				failed = True

		counter += 1
		
	
	return len(stack) == 0 and not failed
	
		

if __name__ == '__main__':
	print (is_balanced('{[()]}') )
	print (is_balanced('{[(])}'))
	print (is_balanced('[()}'))
	print (is_balanced('{{[[(())]]}}'))
	
