[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

Here we notice that the CDF is approximately a straight line which means that the distribution of the sample of random numbers generated is uniform.

Code:

import random
import thinkstats2
import thinkplot

rand = [random.random() for i in range(1000)]
pmf = thinkstats2.Pmf(rand)
thinkplot.Pmf(pmf, label = 'rand_pmf')
thinkplot.Show()

cdf = thinkstats2.Cdf(rand)
thinkplot.Cdf(cdf, label = 'rand_cdf')
thinkplot.Show()
