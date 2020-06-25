import re
#extract all the numbers from this string
x = 'My 2    favorite numbers are 19 and 41 when i was 14yrs in 2018 during my 1st year at school'
#Here I am repeating (+ and * repeats) the character [0-9]. So, now any repeatation of only numbers 0-9 to any numbre of times will be correctly listed.
find_list = re.findall('[0-9]+',x)
print (find_list)
find_list = re.findall('[0-9]+\s',x)
print (find_list)
find_list = re.findall('([0-9]+)\s',x)
print (find_list)
#Here i am hardcoding the fact that there can be one an donly one character after 0-9. And mind it that this character can be any character. So, you can see a 1s also listed in the print.
find_list = re.findall('[0-9].',x)
print (find_list)

#GREEDING OPTION - BY DEFAULT. * AND + ALWAYS PUSHES OUTWARDS AS MUCH AS POSSIBLE
import re
x = 'From: using the : character'
y = re.findall('^F.+:', x)
#SINCE BY DEFAULT DOT AND STAR ARE GREEDY, THEY ARE GIVING THE FOLLWOIN OUTPUT AND NOT SHOWING US THE SHORTER ANSWER "From:"
print (y)

#What? DONT BE GREEDY!! This is given by the what symbol ?. So, the following shows From:
y = re.findall('^F.+?:', x)
print (y)

##################

#EXTRACT THE EMAIL ADDRESSES! NOTE THAT HERE WE WANTED THE GREEDY NATURE.
x= 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16  2008'
y = re.findall('\S+@\S+', x)
print (y)

###################
#USING BRACES TO SELECT EXTRACTION TO START FROM WHERE
x= 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16  2008'
y= re.findall('^From (\S+@\S+)',x)

###################Note that by default + is greedy
x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print(y)
###NOTE THAT SINCE THERE IS NO REPITITION OF @ SYMBOL, NON GREEDY SYMBOL ? DOES NOT SOLVE ANY PURPOSE.
x = From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
y = re.findall('\S+?@\S+', x)
print(y)

#############finding the sum of all numbers from the sample_data.txt
import re
#file_handle = open ('DATA-FILES/sample-data.txt')
file_handle = open ('DATA-FILES/actual-data.txt')
l2_null = [re.findall('[0-9]+',line.rstrip()) for line in file_handle]
l2 = [value for value in l2_null if value]
sum_num = sum([ int(s1) for l1 in l2 for s1 in l1 ])
print(sum_num)
