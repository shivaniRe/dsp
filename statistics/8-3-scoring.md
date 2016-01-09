[Think Stats Chapter 8 Exercise 3](http://greenteapress.com/thinkstats2/html/thinkstats2009.html#toc77)

The standard error in this case is 1.71160743163. This way of making estimates seems to be biased since the mean error does not converge to 0 as m increases. And as lambda increases, the standard error increases.

Please find the code below:

import thinkstats2
import thinkplot
import math
import numpy as np
import random

def RMSE(estimates, actual):
    e2 = [(estimate-actual)**2 for estimate in estimates]
    mse = np.mean(e2)
    return math.sqrt(mse)

def MeanError(estimates, actual):
    e = [(estimate - actual) for estimate in estimates]
    return np.mean(e)

def Simulate(lam):
    goals = 0
    time = 0
    while time <= 1:
        timebetweengoals = random.expovariate(lam)
        time += timebetweengoals
        goals += 1
    return goals

def ComputeError(lam, m):
    
    L = []
    for i in range(m):
        L.append(Simulate(lam))
        
    stderr = RMSE(L, lam)
    print "Standard Error = ", stderr
    meanerr = MeanError(L, lam)
    print "Mean Error = ", meanerr
    
    pmf = thinkstats2.Pmf(L)
    cdf = thinkstats2.Cdf(L)
    ci = cdf.Percentile(5), cdf.Percentile(95)
    thinkplot.Hist(pmf)
    thinkplot.Show()

ComputeError(2, 10000)
for m in [1000, 10000, 100000, 1000000]:
    ComputeError(2,m)

---
