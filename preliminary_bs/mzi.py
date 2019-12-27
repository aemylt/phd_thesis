# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 08:34:29 2019

@author: dm1905
"""

import cmath
import matplotlib.pyplot as plt

xs = []
ys = []

n=100

for i in range(n):
    theta = 2*cmath.pi*i/n
    xs.append(theta)
    ys.append(abs(cmath.exp(1j*theta)-1)**2/4)

plt.plot(xs, ys, label=r'$|1,0\rangle$')
plt.plot(xs, [1-y for y in ys], label=r'$|0,1\rangle$')
plt.legend()
plt.xlabel(r'$\theta$')
plt.ylabel("Probability")
plt.savefig("mzi_plot.pdf", bbox_inches="tight")