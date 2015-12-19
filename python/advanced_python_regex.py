import re
import csv

f = open('faculty.csv')
csv_f = csv.reader(f)
csv_f.next()

# Different degrees and their frequencies
degrees = []
degree_freq = {}
parsed_data = [re.findall('\S+', row[1]) for row in csv_f]

for x in parsed_data:
    degrees += x

unique = [w.replace('.', '') for w in degrees]
unique.remove('0')

for word in unique:
    degree_freq[word] = degree_freq.get(word, 0) + 1
    
print "The number different degrees are", len(degree_freq), "and the list of degrees and their frequencies is", degree_freq

# Different titles and their frquencies
titles = [row[2] for row in csv_f]

title_freq = {}
for title in titles:
    title_freq[title] = title_freq.get(title, 0) + 1
    
print "The number of unique titles are ", len(title_freq), "and the frequency of these tiles is ", title_freq

# List of email addresses
parsed_data = [re.findall('[a-z0-9]*@\S*', row[3]) for row in csv_f]

emails = []
for l in parsed_data:
    emails += l
print "The list of email addresses is ", emails

# List of unique email domains
email_domain = [re.findall('[a-z0-9]*@(\S*)', row[3]) for row in csv_f]

domains = []
for x in email_domain:
    domains += x
    
unique_domains = {}
for dom in domains:
    unique_domains[dom] = unique_domains.get(dom, 0) + 1
    
print "The number of unique email domains are ", len(unique_domains), "and the frequency of the domains is ", unique_domains 
