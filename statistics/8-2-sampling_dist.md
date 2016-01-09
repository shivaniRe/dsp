[Think Stats Chapter 8 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2009.html#toc77) (scoring)

In this experiment we observe the following:
1) The standard error and the 90% confidence interval for lambda=2, n=10 and m=1000 are 0.783878095312, (1.2641237353981147, 3.6180442952366194) respectively.
2) We also notice that as the sample size increases, i.e., as n increases, the standard error decreases.

Please find the code below:

import numpy as np
import thinkstats2
import thinkplot
import math

def RMSE(estimates, actual):
    e2 = [(estimate-actual)**2 for estimate in estimates]
    mse = np.mean(e2)
    return math.sqrt(mse)

def Estimate(n, m):
    lam = 2
    
    means = []
    for i in range(m):
        xs = np.random.exponential(1.0/lam, n)
        L = 1 / np.mean(xs)
        means.append(L)
        
    cdf = thinkstats2.Cdf(means)
    ci = cdf.Percentile(5), cdf.Percentile(95)
    stderr = RMSE(means, lam)
    print "Standard Error for n=10, m=1000 and l=2 is ", stderr
    print "90% Confidence Interval for n=10, m=1000 and l=2 is ", ci
    return stderr
    
Estimate(10, 1000)
se = []
n = [10,30,50,70,100,1000]
for j in n:
    se.append(Estimate(j, 1000))
thinkplot.Plot(se,n)
thinkplot.Show(xlabel = 'Standard Error', ylabel = 'Number of Samples')
    
