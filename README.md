# python_data_structures
Contains solutions to common data structure and algorithm problems implemented in Python

#AUTHOR
John Mezzanotte

#DATE-CREATED 
5-20-2016

#PACKAGE CONTENTS

#pystacks
  - pystacks is a package of python scripts containing solutions to programming problems that can be solved by using stacks. The 
  package contains the following scripts
#balanced_parens.py 
      Contains a function that can be used to solve the balanced parenthesis problem. This is a very 
      common programming problem where a stack is used to determine whether or not an expression containing parenthesis is 
      balanced or not. For example, '()' would be balanced, as well as '{[]}'. However, '[([})]' would not be balanced. 
      The algorithm scans the characters of the string from left to right. Every time a left parenthesis occurs, it 
      is pushed onto the stack. Every time a right parenthesis occurs a matching left parenthesis is popped off the stack. 
      If the correct type of left parenthesis is not on the top of the stack, then the string is unbalanced. 
#Usage of balanced_parens.py 
        from balanced_parens use the function is_balanced():
	-This function takes a single string which is the parenthesis in question. 
        -the function will return a boolean value, true if balanced, false otherwise. 
      ```
      from pystacks import balanced_parens as bp 

      test_cases = ['{[]}', '[{(([]))}]', '{(])}', '[{([}])}]', '(}']

      for case in test_cases:
	       print(bp.is_balanced(case))
      
      ```
      
      From the above example, you would recieve the following output: 
        True True False False False
      
    
