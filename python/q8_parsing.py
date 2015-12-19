#The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

# The below skeleton is optional.  You can use it or you can write the script with an approach of your choice.


import csv

f= open('football.csv')
csv_f = csv.reader(f)
csv_f.next()
parsed_data = [row for row in csv_f]

diff = [int(row[5]) - int(row[6]) for row in parsed_data]
index_value = diff.index(min(diff)) # index value of the smallest difference in 'for' and 'against' goals
    
teams = [row[0] for row in parsed_data]
print "The team with the smallest differnece in 'for' and 'against' goals is ", teams[index_value]
