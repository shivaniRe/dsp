import re
import csv

f = open('faculty.csv')
csv_f = csv.reader(f)
csv_f.next()

parsed_data = [row for row in csv_f]

for row in parsed_data:
    r = re.findall('\S*$', row[0])
    row[0] = r[0]

# DIctionary of professors with unique last names
faculty = {}
for r in parsed_data:
    faculty.setdefault(r[0], []).append(r[1:])

#Print first 3 key value pairs of the dictionary
for key in faculty.keys()[:3]:
    print "%s: %s" % (key, faculty[key])
