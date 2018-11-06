# Dictionary is like Map.
food  = {'wine': 123, 'beer':154, 'pizza':258, 'burger':354, 'fries':365, 'cola':150, 'apple':95, 'donut':195}
print (food)
print (list(food))

print (food['wine'],food['beer'], food['pizza'])

for index in food:
    print(food[index])

# note that when you use values() method the object returned is not a dict type. it is rather a normal value. So, indexing will not work here.
for calories in food.values():
    print(calories)

# items() is used to get the index:value pair from dictionary.
# This is known as UNPACKING
for name, cal in food.items():
    print (name)
    print (cal)

food  = {'wine': 123, 'beer':154, 'pizza':258, 'burger':354, 'fries':365, 'cola':150, 'apple':95}
for a in food:
    print (a)
print (food)


#9.4 Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
import os
os.chdir ("/home/samrat/Dropbox/Jrnl/LifeChronology/PROFESSIONAL/PJ8-PYTHON/BASICS")
name_dict = dict()
file_handle = open("mbox-short.txt")
for line in file_handle:
    if line.startswith("From "):
        name = line.split()[1]
        name_dict[name] = name_dict.get(name,0) + 1
values = name_dict.values()
bigval = None
for k, v in name_dict.items():
    if ((bigval is None) or (v > bigval)):
        bigval = v
        bigkey = k
print (bigkey, bigval)

#using sorted() to sort dictionaries, althhough they are not sorted. the trick is that it returns items which are tuples which can be sorted

import os
os.chdir ("/home/samrat/Dropbox/Jrnl/LifeChronology/PROFESSIONAL/PJ8-PYTHON/BASICS")
name_dict = dict()
file_handle = open("mbox-short.txt")
for line in file_handle:
    if line.startswith("From "):
        name = line.split()[1]
        name_dict[name] = name_dict.get(name,0) + 1
print(name_dict)
#sorting using keys.
print(sorted(name_dict.items()))
#sorting using value
temp = []
for k, v in name_dict.items():
    temp.append((v,k))
print (temp)
temp.sort(reverse=True)
print (temp)

#using list comprehension to replace line 59-62
import os
os.chdir ("/home/samrat/Dropbox/Jrnl/LifeChronology/PROFESSIONAL/PJ8-PYTHON/BASICS")
name_dict = dict()
file_handle = open("mbox-short.txt")
for line in file_handle:
    if line.startswith("From "):
        name = line.split()[1]
        name_dict[name] = name_dict.get(name,0) + 1
#print(name_dict)
#sorting using keys.
#print(sorted(name_dict.items()))
#sorting using value
print (sorted([(v,k) for k,v in name_dict.items()], reverse=True))

#zip
merge_list = zip([1,2,4,5],['a','b','c','d','e'],['!','@','#','$','^'])
for i in merge_list:
    print (i)
#the output of zip can be directly converted to a dictionary as follows. But then it would need to have only two zipped lists.  
merge_dict = dict (zip([1,2,4,5],['a','b','c','d','e']))
print (merge_dict)

dict = {0:'Fish', 1:'Bird', 2:'Mammal'}
#Printing dict elements directly results in printing of the values
print (dict[0], dict[1], dict[2])
#Printing dict elements as list prints the indices
print (list(dict))
#as expected the iterator in the for would contain the index and not the value
for i in dict:
    print (i)

d = {0, 1, 2}
for x in d:
    print(d.add(x))


    