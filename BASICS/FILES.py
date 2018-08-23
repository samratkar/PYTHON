import os
os.chdir ("/home/samrat/Dropbox/Jrnl/LifeChronology/PROFESSIONAL/PJ8-PYTHON/BASICS")

#new lines are printed as is when print is not used to display data.
stuff = 'Hello \n World'
stuff
print (stuff)

#7.1 Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case. Use the file words.txt to produce the output below.
#You can download the sample data at http://www.py4e.com/code3/words.txt

file_name = input ("Enter file name")
file_handle = open (file_name)
data = file_handle.read()
print ((data.upper()).strip())


#7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
#X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
#You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.

import os
os.chdir ("/home/samrat/Dropbox/Jrnl/LifeChronology/PROFESSIONAL/PJ8-PYTHON/BASICS")
total = 0
avg = 0
counter = 0
file_name = input ("Enter file name")
file_handle = open(file_name)
#data = file_handle.read()
for line in file_handle:
    if line.startswith('X-DSPAM-Confidence:'):
        pos = line.find('0')
        char_num = line [pos:]
        total = total + float(char_num)
        counter = counter + 1
avg = total / counter
print ("Average spam confidence: ", avg)
