INDEX -
1. IMPORTING DATA USING STRING
2. IMPORTNT DATA AS A dictionary
3. USING TUPLE AND LIST COMPREHENSION TO MANIPULATE DATA FROM THE DISCTIONARY

# import os
# path = "/home/samrat/Dropbox/Jrnl/LifeChronology/PROFESSIONAL/PJ7-DATA-SCIENCE/PJ7.1-APPLIED-DATA-SC-WITH-PYTHON-COURSERA/PJ7.1.1-INTRODUCT-TO-DATA-SC-IN-PYTHON/WEEK1-PYTHON-FUNDAMENTALS/DATA-FILES"
# os.chdir(path)
# #opening the file as a normal text file. No data structure is imposed on the file. each line is a string
# csvfile = open ("mpg.csv")
# for line in csvfile:
#     print (line)
# print (type(line))
#
import os
path="/home/samrat/Dropbox/Jrnl/LifeChronology/PROFESSIONAL/PJ8-PYTHON/BASICS"
os.chdir(path)
#importing the data file as a dictionary.
import csv
#%precision 2
csvfile = open ("MPG.csv")
mpg = list(csv.DictReader(csvfile))
# print (mpg)
# mpg[:3]
# len(mpg)
# mpg[4].keys()
# mpg[4].items()

# see the comprehension of list also works seamlessly, Like the comprehension of tuples below. It is advisable to create tuples because of their immuntability.
# sum([float(dict['hwy']) for dict in mpg])/len(mpg)
# # sum([float(dict['cty']) for dict in mpg])/len(mpg)
#
# #Tuple Comprehension. Average city mpg
# avg_city =  sum((float(d['cty']) for d in mpg))/len(mpg)
# print (avg_city)
# #Tuple Comprehension. Average HWY mpg
# avg_hwy =  sum((float(d['hwy']) for d in mpg))/len(mpg)
# print (avg_hwy)

#Finding the unique number of cylinders that all the cars have -
cyl = set((d['cyl'] for d in mpg))
print (cyl)

#WHAT IS THE AVERAGE CITY MPG GROUPED BY NUMBER OF CYLINDER A CAR HAS
cyl_list = [float (d['cyl']) for d in mpg]
cyl_set = set(cyl_list)
CtyMpgByCyl = []
avg = 0
for cyl in cyl_set:
    mpg_list = [int(d['cty']) for d in mpg if (int(d['cyl']) == int(cyl))]
    avg = sum(mpg_list)/len(mpg_list)
    CtyMpgByCyl.append((cyl, avg))
CtyMpgByCyl.sort()
print (CtyMpgByCyl)

#AVEREAGE CITY VEHILE MPG WITH RESEPCT TO CLASSES
class_list = [d['class'] for d in mpg]
class_set = set(class_list)
CtyMpgByClass = []
avg = 0
for car_class in class_set:
    mpg_list = [int(d['cty']) for d in mpg if (d['class'] == car_class)]
    avg = sum(mpg_list)/len(mpg_list)
    CtyMpgByClass.append((car_class, avg))
CtyMpgByClass.sort()
print (CtyMpgByClass)
