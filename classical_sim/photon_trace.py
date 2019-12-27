# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 11:30:06 2019

@author: dm1905
"""

import matplotlib.pyplot as plt

n = 7
xs = [i/50 for i in range(51)]
ys = []

with open("%d_photon_trace.csv" % (n)) as data_file:
    for line in data_file:
        ys.append([float(x.split("+")[0]) for x in line.split(",")[:51]])
        
for i, y_line in enumerate(ys):
    plt.plot(xs, y_line, label=r'$k=%d$'%(i+1))

plt.xlabel(r'$x$')
plt.ylabel(r'$\delta_{\rm{Tr}}(\rho_{n,x}, \rho_{\leq k, x})$')
plt.ylim(0,1)
plt.legend()
plt.savefig("%d_photon_trace.pdf" % (n), bbox_inches="tight")