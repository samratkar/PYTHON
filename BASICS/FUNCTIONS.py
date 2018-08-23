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
