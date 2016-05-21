# python_data_structures
Contains solutions to common data structure and algorithm problems implemented in Python

#Author
John Mezzanotte

#Date-Created 
5-20-2016

#Packages
-pystacks
  - pystacks is a packages of python scripts containing solutions to programming problems that can be solved by using stacks. The 
  package contains the following scripts
  - balanced_parens.py 
      balanced_parens.py contains a function that can be used to solve the balanced parenthesis problem. This is a very 
      common programming problem where a stack is used to determine whether or not an expression containing parenthesis is 
      balanced or not. For example, '()' would be balanced, as well as '{[]}'. However, '[([})]' would not be balanced. 
      The algorithm scans the characters of the string from left to right. Every time a left parenthesis occurs, it 
      is pushed onto the stack. Every time a right parenthesis occurs a matching left parenthesis is popped off the stack. 
      If the correct type of left parenthesis is not on the top of the stack, then the string is unbalanced. 
      
    
