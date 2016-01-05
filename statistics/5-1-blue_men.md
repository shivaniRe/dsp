[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

import thinkstats2
import scipy.stats

mu = 178
sigma = 7.7
# CDF at 5'10" i.e., 177.8 cm
cdf1 = scipy.stats.norm.cdf(177.8, loc = mu, scale = sigma)
# CDF at 6'1" i.e., 185.4cm
cdf2 = scipy.stats.norm.cdf(185.4, loc = mu, scale = sigma)
# Percentage of men between 5'10" and 6'1" 
print "Percentage of U.S men that are in the 5'10 and 6'1 range are", cdf2-cdf1 


Null Hypothesis: Percentage of U.S men that are in the 5'10" and 6'1" range is 0.342094682946
Alternate Hypothesis: Percentage of U.S men that are in the 5'10" and 6'1" range is not 0.342094682946
Critical value for testing: 0.05
The associated p-value is: 1 - cdf = 1-0.342094682946 = 0.657905317054
