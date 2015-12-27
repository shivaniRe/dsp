[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

import numpy as np
import thinkstats2
import sys
import math
import thinkplot

def ReadFemPreg(dct_file='2002FemPreg.dct',
                dat_file='2002FemPreg.dat.gz'):
    """Reads the NSFG pregnancy data.

    dct_file: string file name
    dat_file: string file name

    returns: DataFrame
    """
    dct = thinkstats2.ReadStataDct(dct_file)
    df = dct.ReadFixedWidth(dat_file, compression='gzip')
    CleanFemPreg(df)
    return df

def CleanFemPreg(df):
    # birthwgt_lb contains at least one bogus value (51 lbs)
    # replace with NaN
    df.loc[df.birthwgt_lb > 20, 'birthwgt_lb'] = np.nan
    
    # replace 'not ascertained', 'refused', 'don't know' with NaN
    na_vals = [97, 98, 99]
    df.birthwgt_lb.replace(na_vals, np.nan, inplace=True)
    df.birthwgt_oz.replace(na_vals, np.nan, inplace=True)
    
    # birthweight is stored in two columns, lbs and oz.
    # convert to a single column in lb
    df['totalwgt_lb'] = df.birthwgt_lb + df.birthwgt_oz / 16.0
    
def CohenEffectSize(group1, group2):
    diff = group1.mean() - group2.mean()
    
    var1 = group1.var()
    var2 = group2.var()
    n1,n2 = len(group1), len(group2)
     
    pooled_var = (n1*var1 + n2*var2) / (n1 + n2)
    d = diff / math.sqrt(pooled_var)
    return d

preg = ReadFemPreg()
live = preg[preg.outcome == 1]

firsts = live[live.pregordr == 1]
others = live[live.pregordr != 1]

first_hist = thinkstats2.Hist(firsts.totalwgt_lb)
other_hist = thinkstats2.Hist(others.totalwgt_lb)

# Plot histograms on the same axis
thinkplot.PrePlot(2)
thinkplot.Hist(first_hist, align = 'right', width = 0.45)
thinkplot.Hist(other_hist, align = 'left', width = 0.45)
thinkplot.show(xlabel = "totalwgt_lb", ylabel = "frequency")

cohens_d = CohenEffectSize(firsts.totalwgt_lb, others.totalwgt_lb)
print "Cohen's Effect Size = ", cohens_d
