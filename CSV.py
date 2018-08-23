import os
os.chdir("C:\DATA_BKP\ONE-DRIVE\OneDrive - Honeywell\IDP\IDP\PYTHON")
#csv_file = open ("MPG.csv", "r")
#for line in csv_file:
#   print(line)
import csv
csv_file = open ("MPG.csv")
file_list = list(csv.DictReader(csv_file))
#print (file_list)
sum([float(d['hwy']) for d in file_list]) / len (file_list)
sum([float(d['cty']) for d in file_list]) / len (file_list)

#WHAT IS THE AVERAGE CITY MPG GROUPED BY NUMBER OF CYLINDER A CAR HAS
cyl_list = [float (d['cyl']) for d in file_list]
cyl_set = list(set(cyl_list))
CtyMpgByCyl = []
avg = 0
for cyl in cyl_set:
    mpg_list = [int(d['cty']) for d in file_list if (int(d['cyl']) == int(cyl))]
    avg = sum(mpg_list)/len(mpg_list)
    CtyMpgByCyl.append((cyl, avg))
CtyMpgByCyl.sort()
print (CtyMpgByCyl)

#AVEREAGE CITY VEHILE MPG WITH RESEPCT TO CLASSES
class_list = [d['class'] for d in file_list]
class_set = list(set(class_list))
CtyMpgByClass = []
avg = 0.0
for car_class in class_set:
    mpg_list = [int(d['cty']) for d in file_list if (d['class'] == car_class)]
    avg = sum(mpg_list)/len(mpg_list)
    CtyMpgByClass.append((car_class, avg))
CtyMpgByClass.sort()
print (CtyMpgByClass)
