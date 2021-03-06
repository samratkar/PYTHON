#lists are mutable. But this is wrong, as fruit is a string instead of a list.

fruit = 'Banana'
fruit[0] = 'b'
print(fruit)


my_list = [123, 'samrat', 1.23]
print (my_list)
my_list.pop()
print (my_list)
#NESTING
L = [1,2,3,4,5,6,7,8,9,10]
M = [[1,2,3], [4,5,6], [7,8,9]]
L1 = 1,2,3,4,5,6,7,8,9,10
L2 = (1,2,3,4,5,6,7,8,9,10)
print (L1)
print (L)
print (L2)
print (M)
print (M[0])
print (M[2][2])

#LIST COMPREHENSION EX 1
#I want a list for n for each n in the list
#The first letter is one instance of the collection of the list. Simiar values are stacked together to design the list
my_list = [x for x in L]
print (my_list)

#LIST COMPREHENSION EX 2
#I want a list for n*n for each n in the list
my_list = [x*x for x in L]
print (my_list)

#LIST COMPREHENSION EX 3
#I want a list for even values for each n in the list
my_list = [n for n in L if (n%2 == 0)]
print (my_list)

#LIST COMPREHENSION EX 4
#I want a letter, number pair
my_list = [(letter,num) for letter in 'abcd' for num in range(4)]
print (my_list)

#LIST COMPREHENSION EX 5
# print the columns of a matrix M
# keep collecting the row[1] from the for loop and keep appending in the list.
my_list = [ row[1] for row in M]
print (my_list)


t = ['a', 'b', 'c', 'd']
t.append('e')
print (t)
t2 = ['a', 'b']

#we do not need to use for loops to search a value in a list. Nor we need to use find(). Just use 'in'. find() is handy when you wannna know the the index.
if ('a' not in t) : print ('samrat')
if ('a' in t) : print ('samrat')

#8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in alphabetical order.
#You can download the sample data at http://www.py4e.com/code3/romeo.txt
import os
os.chdir ("/home/samrat/Dropbox/Jrnl/LifeChronology/PROFESSIONAL/PJ8-PYTHON/BASICS")
word_list = []
file_words_list = []
file_handle = open ("romeo.txt", "r")
for file_line in file_handle:
    file_words_list = file_line.split()
    for word in file_words_list:
        if (word not in word_list):
            word_list.append(word)
word_list.sort()
print(word_list)

#8.5 Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out a count at the end.
#Hint: make sure not to include the lines that start with 'From:'.
#You can download the sample data at http://www.py4e.com/code3/mbox-short.txt

import os
os.chdir ("/home/samrat/Dropbox/Jrnl/LifeChronology/PROFESSIONAL/PJ8-PYTHON/BASICS")
counter = 0
file_words_list = []
file_handle = open ("mbox-short.txt", "r")
for file_line in file_handle:
    if file_line.startswith("From "):
        counter += 1
        file_words_list = file_line.split()
        print (file_words_list[1])
print ("There were", counter, "lines in the file with From as the first word")

'''
SLICING
'''
a[start:end:STEP] # items start through end-1
a[start:]    # items start through the rest of the array
a[:end]      # items from the beginning through end-1
a[:]         # a copy of the whole array
a[start:end:step] # start through not past end, by step

#The other feature is that start or end may be a negative number, which means it counts from the end of the array instead of the beginning. So:
a[-1]    # last item in the array
a[-2:]   # last two items in the array
a[:-2]   # everything except the last two items


#Similarly, step may be a negative number:
#NOTE THAT THESE ARE FOR ONLY ONE DIMENSION.
a[::-1]    # all items in the array, reversed
a[1::-1]   # the first two items, reversed
a[:-3:-1]  # the last two items, reversed
a[-3::-1]  # everything except the last two items, reversed

my_list = ['1','2','3','4']
print (my_list[:3])
print (my_list)
my_list[:] = []
print (my_list)

#NOTE : multiplying by number to a list does not multiply the elements. Rather it just repeats
my_list = ['1','2','3','4']
my_list * 2

my_list = [1,2,3,4]
my_list * 2

#NOTE : square the elements of a list. Since the above didnt work, we use numpy arrays as they work easily as matrices.
my_list = [1,2,3,4,5,6]
print (list(map(lambda x:x**2, my_list)))
sum(my_list)

#NOTE : ELEMENT WISE PRODUCT OF LIST
list_1 = [3,6,7,5]
list_2 = [4,5,1,7]
print (list(map(lambda x,y: x*y, list_1, list_2)))
