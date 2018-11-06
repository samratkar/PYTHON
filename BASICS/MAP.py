store1 = [10.00, 11.00, 12.00, 2.34]
store2 = [1.11, 9.22, 10.99, 13]
min_val = map(min, store1, store2)
print (min_val)


# SPLITTING NAMES USING MAP
people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

def split_title_and_name(person):
    split_name = person.split()
    return split_name[0]+split_name[-1]

list(map(split_title_and_name, people))

#NOTE : square the elements of a list
my_list = [1,2,3,4,5,6]
print (list(map(lambda x:x**2, my_list)))

#NOTE : count all the entries which start with S
import ast,sys
input_str = sys.stdin.read()
input_list = ast.literal_eval(input_str)
s_list = list()
count = 0
my_list = list(map(lambda x: 1 if (x[0] == 'S') else 0, input_list))
count = sum(my_list)
print(count)
