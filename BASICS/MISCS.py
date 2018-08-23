print (int(9.8))

name = input ("Ener your name")
print("Hello", name)

# input returns always a string.
hrs = input("Enter Hours:")
rate = input("Enter rate:")
print ("Pay:", (float(hrs)*float(rate)))

# intendation is important.
num = input ('Enter a number')
if int(num) > 5 :
    print ("greater than 5")
    print ("still 5")
    print ("third 5")
print ("Outside")

#if and else and elif blocks run only one block
#else doesnt get ever printed.
data = input ("enter something")
x = int(data)
if x < 2 :
    print ('Below 2')
elif x >= 2 :
    print ('2 or more')
else:
    print ('Something else')

###
hrs = input("Enter Hours:")
rate = input ("Enter rate")

h = float(hrs)
r = float (rate)

if (h > 40):
    r1 = 1.5 * r
    print ((h-40) * r1 + 40*r)
else:
    print (h*r)

################# max()
max ([1,2,3,4,99090909,'a', 'n', 'c', 53,-989])
