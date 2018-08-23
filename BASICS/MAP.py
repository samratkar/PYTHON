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
