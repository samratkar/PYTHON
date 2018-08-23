d = (1,'a', 2, 'b', 3, 'c', 4, 'd')
print (d)
print (d(0))

#10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

import os
os.chdir ("/home/samrat/Dropbox/Jrnl/LifeChronology/PROFESSIONAL/PJ8-PYTHON/BASICS")
name_dict = dict()
file_handle = open("mbox-short.txt")
words_list = [line.split() for line in file_handle if line.startswith("From ")]
time_list = [ words[5] for words in words_list]
#print (words_list)
#print (time)
hour_list = [ time.split(':')[0] for time in time_list]
#print (hour_list)
from collections import Counter
[print (hour, freq) for  hour, freq in sorted(Counter(hour_list).items())]
