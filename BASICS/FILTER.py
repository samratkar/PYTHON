#NOTE : IT IS SAME MAP. ONLY THAT IT EXPECTS THE LAMBDA FUNCTION TO BE RETURNING TRUE OR FALSE. IF THE RETURN IS TRUE, THAT ELEMENT IS RETURNED BY THE LAMBDA FUNCTION-
#QUESTION 1 - DESIGN A FLITER TO SELECT ONLY THE NUMBERS WHICH ARE DIVISIBLE BY 5
import ast,sys
input_str = sys.stdin.read()
input_list = ast.literal_eval(input_str)
div_by_five = lambda x : x%5 == 0
list_answer = list(filter (div_by_five, input_list))

print(list_answer)


# QUESTION 2 - You are given a list of strings such as input_list =  ['hdjk', 'salsap', 'sherpa']. Extract a list of names that start with an ‘s’ and end with a ‘p’ (both 's' and 'p' are lowercase) in input_list.

import ast,sys
input_str = sys.stdin.read()
input_list = ast.literal_eval(input_str)
func = lambda x: True if (x[0] == 's' and x[-1] == 'p') else False
sp = list (filter(func, input_list))

print(sp)