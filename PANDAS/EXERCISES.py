import pandas as pd
ipl18 = pd.DataFrame({'Team': ['SRH', 'CSK', 'KKR', 'RR', 'MI', 'RCB', 'KXIP', 'DD'],
                         'Matches': [14, 14, 14, 14, 14, 14, 14, 14],
                         'Won': [9, 9, 8, 7, 6, 6, 6, 5],
                         'Lost': [5, 5, 6, 7, 8, 8, 8, 9],
                         'Tied': [0, 0, 0, 0, 0, 0, 0, 0],
                         'N/R': [0, 0, 0, 0, 0, 0, 0, 0],
                         'Points': [18, 18, 16, 14, 12, 12, 12, 10],
                         'NRR': [0.284, 0.253, -0.070, -0.250, 0.317, 0.129, -0.502, -0.222],
                         'For': [2230, 2488, 2363, 2130, 2380, 2322, 2210, 2297],
                         'Against': [2193, 2433, 2425, 2141, 2282, 2383, 2259, 2304]},
                         index = range(1,9)
                    )
ipl17 = pd.DataFrame({'Team': ['MI', 'RPS', 'SRH', 'KKR', 'KXIP', 'DD', 'GL', 'RCB'],
                         'Matches': [14, 14, 14, 14, 14, 14, 14, 14],
                         'Won': [10, 9, 8, 8, 7, 6, 4, 3],
                         'Lost': [4, 5, 5, 6, 7, 8, 10, 10],
                         'Tied': [0, 0, 0, 0, 0, 0, 0, 0],
                         'N/R': [0, 0, 1, 0, 0, 0, 0, 1],
                         'Points': [20, 18, 17, 16, 14, 12, 8, 7],
                         'NRR': [0.784, 0.176, 0.469, 0.641, 0.123, -0.512, -0.412, -1.299],
                         'For': [2407, 2180, 2221, 2329, 2207, 2219, 2406, 1845],
                         'Against': [2242, 2165, 2118, 2300, 2229, 2255, 2472, 2033]},
                         index = range(1,9)
                    )


#QUESTION 1
#Extract top 4 teams with only the columns Teams and Points.
#way 1 (using the index, you need to use iloc!)
ipl18.iloc[0:4,[0,6]]
#way 2 (using the labels, you need to just use loc)
ipl18.loc[1:4,['Team', 'Points']]

#QUESTION 2
#Suppose in ‘ipl18’, you want to filter out the teams that have an NRR greater than zero, and for which the ‘For’ score exceeds the ‘Against’ score, i.e. both the conditions should be satisfied. Which teams will be left after you perform the above filtration? (Run the commands on the Python Notebook provided, rather than performing a manual calculation)
ipl18[(ipl18['NRR'] > 0) & (ipl18['For'] > ipl18['Against'])]

#QUESTION 3
#Operations on multiple dataframes
#If all the stats are taken for both ‘ipl17’ and ‘ipl18’, which team with its total points greater than 25 will have the highest win percentage?
df = pd.merge(ipl17, ipl18, how = 'outer', on = 'Team')
df['Total_points'] =  df['Points_x'] + df['Points_y']
df['Total_won'] =  df['Won_x'] + df['Won_y']
df['Total_matches'] = df ['Matches_x'] + df ['Matches_y']
df['Win_percent'] = df ['Total_won'] / df ['Total_matches'] * 100
df1 = df [df['Total_points'] > 25]
print (df1)
