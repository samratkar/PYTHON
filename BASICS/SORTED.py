def key_fn(object):
    if object == 'S':
        return 100
    if object == 'a':
        return 99
    if object == 'm':
        return 98
    if object == 'r':
        return 97
#    if object == 'a':
#        return 96
    if object == 't':
        return 95
    if object == ' ':
        return 94
    if object == 'K':
        return 93
#    if object == 'a':
#        return 92
#    if object == 'r':
#        return 91

a = 'Samrat Kar'
list_a = list(a)
print (list_a)
list_b = [9,8,7,6,5,4,3,2,1,0]
list_b.sort()
print (list_b)
list_b = [9,8,7,6,5,4,3,2,1,0]
sorted(list_b)

#print (a)
#print (list_a)
#print (sorted(list_a, key=key_fn))
#print (sorted(list_a))
print (sorted([7,10,98,-4,0,5]))
print (sorted(list_a))

# NOTE: key is a function that takes one argument. This one argument is the element from the list of the first argument of the method sorted(). return value can be an transofrmation on the element.
