INDEX -
> BROADCASTING
> Bytearray
> find
> replace
> SPLIT (splits a string based on a given character and creates separate strings)
> STRIP (strips letters from right and left. lstrip and rstrip does from one direction only)
> String formatting
> Indexing a string
> concatenating using + symbol. There is no method known as concat
> Slicing.
> join


NOTE: BROADCASTING -
Borad casting
[ m*n ] arithmetic with [1*n] will broadcast to all columns and with [n*1] will broadcast to all rowsself.
# *****************************************Date - 05/05/2018 - Learning about Strings and lists.
# strings are non mutable. If you wanna make it mutable you need to make them list or bytearrays.
s = 'samrat'
print (s)
l = list(s) #expand the string to a list.
print (l)
l[0] = 'V'
print (l)
l1 = ''.join(l) #join has this special characteristics to convert a list to string.
#str.join(iterable)
#Return a string which is the concatenation of the strings in iterable. A TypeError will be raised if there #are any non-string values in iterable, including bytes objects. "
#THE SEPARATOR BETWEEN ELEMENTS IS THE STRING PROVIDING THIS METHOD.
print (l1)
l2 = "_".join(l)
print (l2)

#***********************************************Date 05/06/2018 - Bytearray - string manupulation
#bytearray is a mutable string. But then it can house only 1 Byte long data.
B = bytearray(b'SAMRATKAR')
print (B.decode())
#The sequencing followed in strings are the same as that of the other structures like list, tuples, etcself.
# STRING METHODS
#find()
print ("----find function demo-----")
print (s)
print (s.find('rat'))
#replace()
print (s.replace('rat','mouse'))
#split() - THe list() method expands the string into a list of all the characters separately. But split method helps us to expand the strings with respect to the delimitersself.
print(s.split('a'))
whiteSpacedString = 'aaaaaGeema and Daddy \n Studies\n \naaaaaaa     '
print(whiteSpacedString)
print(whiteSpacedString.rstrip()) #just strips the new line character 'return' and white spaces from right
print (whiteSpacedString.strip('a'))

#Format methods for Strings
# 'format characters' % (list of actual string data enclosed in quotes)
# note that with '%' you should not use curly braces. Curly braces are rather place holders, where you can directly place the format characters. Curly braces are dictionaries, to which you apply formating using the format method.
print ('%s' % ('Samrat Kar'))
print('%s, eggs, and %s' %('spam', 'SPAM!'))
print('%s' % ('spam'))
print ('%.2f' % 223.2567)
print ('%s, %s, %d, %.2f' % ('first string', 'second string', 1111, 2222.345))
# '{format characters}'.format(list of data to be printed separated by comma). THis is away to format the content of a dictionary. PAGE 103 PYTHON OREILLY BOOK
print ('{:.2f}'.format(296999.2567))
print ('{:,.2f}'.format(296999.2567))
print('{%.2f}'.format(296999.2567)) # incorrect. % cannot be used as a place holder in dicts. It is primarily for string types.

# dir() method is used to get all the methods for a given object that the variable is a type of.
test_str = 'Samrat Kar'
dir('test_str')
dir('Samrat Kar')

# SLICING
x = "This is a string"
x[0] #T
x[0:2] #Th. 0 is optional. The second argument '2' if not present all the letters are printed. Second argument says how many characters are to be printed.
x[:2] #Th. 0 not mentioned as it is optional
x[:] #This is a string. 0 is not mentioned for both the first index and second as number of letters.
x[3:] #s is a string. index starts from zero.

# LIST OPERATIONS ARE ALL VALID IN STRINGS
S = "samrat"
print (S*3)
print (S + "kar")

# SPLIT STRING BASED ON A GIVEN CHARACTER
s= "Samrat Samares Chandra Kar"
print (s.split()) #without any character it takes the split basis as blank

# TYPE CONVERSION ISSUES. string operations are not dynamically type safe.
print ('Chris' + 2)
print ('Chris' + str(2))

# to circumvent this we use the format methods.
# format() is used to push the actual data values to the object on which the format() is called. The object typically becomes a string. You can have special formatting specifiers in the object on which you are calling format as shown above.
sales_record = {'price': 3.24,
                'num_items': 4,
                'person': 'Samrat'}
sales_statement = '{} bought {} items at a price of {} each with a total expenditure of {}'
print (sales_statement.format(sales_record['person'], sales_record['num_items'], sales_record['price'], sales_record['num_items']*sales_record['price']) )

sales_statement = '{3} bought {1} items at a price of {2} each with a total expenditure of {0}'
print (sales_statement.format(sales_record['person'], sales_record['num_items'], sales_record['price'], sales_record['num_items']*sales_record['price']) )

#SLICING
#You can go past the new line in a string.
#note that the indexing is done wrt characters.
name = 'samrat'
print (name)
name[:2]
print (name[2:4])
print (name[:3]) #sam
print (name[4:]) #at


# second parameter for slicing is the destination position  not including the same.
data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
pos = data.find('.')
print (pos)
print(data[pos:pos+3])

#6.5 Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. Convert the extracted value to a floating point number and print it out.

text = "X-DSPAM-Confidence:    0.8475";
num_pos = text.find('0')
num_data = text[num_pos:]
print (float(num_data))
