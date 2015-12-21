import re
import csv

f = open('faculty.csv')
csv_f = csv.reader(f)
csv_f.next()

parsed_data = [row for row in csv_f]

# DIctionary of professors with unique last names
faculty_dict = {}
for r in parsed_data:
    r1 = re.findall('\S*$', r[0])
    faculty_dict.setdefault(r1[0], []).append(r[1:])

for key in faculty_dict.keys()[:3]:
    print "Faculty_dict = %s: %s" % (key, faculty_dict[key])

# Question 7, 8. create professor_dict and print 3 key value pairs sorted by last name
professor_dict = {}
for row in parsed_data:
    row1 = re.findall('^\S*', row[0])
    if len(row1[0]) <= 2:
        row1 = re.findall('^\S*\s(\S+)', row[0])
    row2 = re.findall('\S*$', row[0])
    k = row1[0], row2[0]
    professor_dict.setdefault(k, []).append(row[1:])
    
d = sorted(professor_dict, key = lambda k:(k[1]))
for i in d[0:3]:
    print "professor_dict = ", i, ':', professor_dict[i]
