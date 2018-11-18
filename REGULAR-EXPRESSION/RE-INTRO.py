import re
import pandas as pd
companies_df = pd.read_csv("DATA-FILES/companies.txt", sep = '\t', encoding = 'ISO-8859-1')
companies_df.head()
list1 = list(companies_df['name'])
str1 = ''.join(str(list1))
str1 = "".join(str(list(companies_df['name'])))

#tell weather the serach was yes or no.
search_mach_object = re.search('s*m', str1)
type(search_df)
print (search_df)

#find the list of all the results.
result_list = re.findall('s*m', str1)
type(result_list)
print (result_list)

#EXAMPLE USING find()
hand = open ('DATA-FILES/mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if line.find('From:') >= 0 :
        print (line)

#SAME EXAMPLE USING REGULAR EXPRESSION
import re
hand = open ('DATA-FILES/mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('From:', line):
        print (line)

#EXAMPLE WITH STARTWITH
hand = open ('DATA-FILES/mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if line.startswith('From:'):
        print (line)

#SAME EXAMPLE USING REGULAR EXPRESSION
import re
hand = open ('DATA-FILES/mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:', line):
        print (line)
