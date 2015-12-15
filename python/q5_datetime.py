# Hint:  use Google to find python function
from datetime import datetime

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'   
d_start = datetime.strptime(date_start, "%m-%d-%Y")
d_stop = datetime.strptime(date_stop, "%m-%d-%Y")
delta = d_stop - d_start
Print delta.days

####b)  
date_start = '12312013'  
date_stop = '05282015'  
d_start = datetime.fromtimestamp(float(date_start))
d_stop = datetime.fromtimestamp(float(date_stop))
diff = abs(d_stop - d_start)
print diff.days

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  
d_start = datetime.strptime(date_start, "%d-%b-%Y")
d_stop = datetime.strptime(date_stop, "%d-%b-%Y")
delta = d_stop - d_start
print delta.days
