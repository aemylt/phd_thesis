# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 08:52:33 2019

@author: dm1905
"""

import cmath
import matplotlib.pyplot as plt

xs = []
ys = []
n = 100

for i in range(n):
    tau = (i-n/2)/5
    xs.append(tau)
    ys.append(abs(1-cmath.exp(-abs(tau)))**2/2)

plt.plot(xs, ys)
plt.xlabel(r'$\Delta\tau$ (arbitrary units)')
plt.ylabel(r'Pr$[|1,1\rangle]$')
plt.savefig("hom_plot.pdf", bbox_inches="tight")