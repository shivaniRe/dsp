[Think Stats Chapter 7 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2008.html#toc70) (weight vs. age)

We observe that the Pearson's correlation and Spearman's correlation between mother's pregnancy age and total birth weight is 0.0688339703541, 0.0946100410966 respectively. The difference between them could be because of some outliers or the relationship between the variables is non-linear.

Please find the code below:

import thinkplot
import thinkstats2
import numpy as np
import pandas
import nsfg
import math

#Plot of percentiles of birth weight vs mother's age
def percentilePlot(df):
    bins = np.arange(10, 45, 2)
    indices = np.digitize(live.agepreg, bins)
    groups = df.groupby(indices)
    age = [group.agepreg.mean() for i, group in groups]
    cdfs = [thinkstats2.Cdf(group.totalwgt_lb) for i, group in groups]
    
    thinkplot.PrePlot(3)
    for percent in [75, 50, 25]:
        weights = [cdf.Percentile(percent) for cdf in cdfs]
        label = '%dth' %percent
        thinkplot.Plot(age, weights, label=label)

    thinkplot.Save(root='ch7sol',
                   formats=['jpg'],
                   xlabel="mother's age (years)",
                   ylabel='birth weight (lbs)')
    
def Cov(xs, ys, meanx = None, meany = None):
    xs = np.asarray(xs)
    ys = np.asarray(ys)
    
    if meanx is None:
        meanx = np.mean(xs)
    if meany is None:
        meany = np.mean(ys)
        
    cov = np.dot(xs-meanx, ys-meany) / len(xs)
    return cov

def MeanVar(s):
    return np.mean(s), np.var(s)
    
def pearsonsCorr(xs, ys):
    xs = np.asarray(xs)
    ys = np.asarray(ys)
    
    meanx, varx = MeanVar(xs)
    meany, vary = MeanVar(ys)
    
    corr = Cov(xs, ys, meanx, meany) / math.sqrt(varx* vary)
    return corr

def SpearmanCorr(xs, ys):
    xranks = pandas.Series(xs)
    yranks = pandas.Series(ys)
    return xs.corr(ys, method='spearman')

preg = nsfg.ReadFemPreg()
live = preg[preg.outcome == 1]
live = live.dropna(subset = ['agepreg', 'totalwgt_lb'])
percentilePlot(live)
pcorr = pearsonsCorr(live.agepreg, live.totalwgt_lb)
print "Pearsons Correlation is", pcorr
scorr = SpearmanCorr(live.agepreg, live.totalwgt_lb)
print "Spearmans Correlation is", scorr

# Scatter plot of birth weight vs mother's age
thinkplot.scatter(live.agepreg, live.totalwgt_lb)
thinkplot.Show(xlabel = 'Age', ylabel = 'Weight')


