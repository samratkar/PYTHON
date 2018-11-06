def thing() :
    print ('Hello')
    print ('Fun')
thing()
print ('Zip')
thing()

# 5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.

min = None
max = None
num_list = []
def find_max(data_list):
    max = data_list[0]
    for num in data_list:
        if (max < num) :
            max = num
    return max

def find_min(data_list):
    min = data_list[0]
    for num in data_list:
        if (min > num) :
            min = num
    return min

while True:
        data = input("Enter a number: ")
        if (data == 'done'):
             break
        try :
            num_list.append(int(data))
        except :
            print ("Invalid input")

print("Maximum is", find_max(num_list))
print("Minimum is", find_min(num_list))

# NOTE: BUILT IN FUNCTIONS -

#NOTE: VARIABLE ARGUMENTS  -
def total(a=5, *numbers, **phonebook):
    print('a', a)

    #iterate through all the items in tuple
    for single_item in numbers:
        print('single_item', single_item)

    #iterate through all the items in dictionary
    for first_part, second_part in phonebook.items():
        print(first_part,second_part)

total(10,1,2,3,Jack=1123,John=2231,Inge=1560)

# NOTE - Built-in Functions
abs()	divmod()	input()	open()	staticmethod()
all()	enumerate()	int()	ord()	str()
any()	eval()	isinstance()	pow()	sum()
basestring()	execfile()	issubclass()	print()	super()
bin()	file()	iter()	property()	tuple()
bool()	filter()	len()	range()	type()
bytearray()	float()	list()	raw_input()	unichr()
callable()	format()	locals()	reduce()	unicode()
chr()	frozenset()	long()	reload()	vars()
classmethod()	getattr()	map()	repr()	xrange()
cmp()	globals()	max()	reversed()	zip()
compile()	hasattr()	memoryview()	round()	__import__()
complex()	hash()	min()	set()
delattr()	help()	next()	setattr()
dict()	hex()	object()	slice()
dir()	id()	oct()	sorted()
