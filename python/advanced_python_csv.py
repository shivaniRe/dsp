import re
import csv

f = open('faculty.csv')
csv_f = csv.reader(f)
csv_f.next()

# List of email addresses
parsed_data = [re.findall('[a-z0-9]*@\S*', row[3]) for row in csv_f]

with open("emails.csv", "wb") as file:
    writer = csv.writer(file)
    writer.writerows(parsed_data)

