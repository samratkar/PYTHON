l1 = [1,2,3,4,2,1,2,3,4,32,4,5,2,3,1]
print (l1)
print (set(l1))

# Read the three input lists, i.e. 'C', 'F', and 'H'.
'''
Description
In a school, there are total 20 students numbered from 1 to 20. You’re given three lists named ‘C’, ‘F’, and ‘H’, representing students who play cricket, football, and hockey, respectively. Based on this information, find out and print the following: 
Students who play all the three sports
Students who play both cricket and football but don’t play hockey
Students who play exactly two of the sports
Students who don’t play any of the three sports
'''

import ast,sys
input_str = sys.stdin.read()
input_list = ast.literal_eval(input_str)
C = input_list[0]
F = input_list[1]
H = input_list[2]

# Write your code here
c_set = set(C)
f_set = set (F)
h_set = set (H)
universal_set = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
print (sorted(list ((c_set & f_set & h_set))))
print (sorted(list (((c_set & f_set ) - h_set))))
print (sorted(list (((c_set & f_set) | (c_set & h_set) | (h_set & f_set)) - (c_set & f_set & h_set))))
print (sorted (list (universal_set - (c_set | f_set | h_set ))))
# (Make sure your lists are sorted in ascending order before you print them out)
