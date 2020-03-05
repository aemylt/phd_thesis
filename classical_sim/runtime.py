# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 14:04:52 2019

Comparison of the two truncation methods considering their runtime.

@author: aemylt
"""

import matplotlib.pyplot as plt

from shared_funcs import worst_case, runtime, jelmer_error, jelmer_runtime

xs = [0.982,0.5]
etas = [0.755,0.5]
runtimes = []
jelmers = []
n_max = 400
ns = range(2,n_max)
epsilon = 0.1
colours = ['r','g','b']
for eta, x, c in zip(etas,xs,colours):
    k=0
    k_j=0
    runtimes = []
    jelmers = []
    for n in ns:
        # Find smallest k that can simulate x
        # k always has to increase with n
        for k in range(k,n):
            if worst_case(n,k,eta=eta,x=x) <= epsilon:
                break
        runtimes.append(runtime(n,k))
        # Find smallest k that can simulate x via point truncation
        # k always has to increase with n
        for k_j in range(k_j,n):
            if jelmer_error(n,k_j,eta=eta,x=x) <= epsilon:
                break
        jelmers.append(jelmer_runtime(n,k_j))
        print(n,k,k_j,runtimes[-1],jelmers[-1])
    
    plt.plot(ns, runtimes,c+"-", label=r'State Truncation, $\eta=$'+str(eta)+r', x='+str(x))
    plt.plot(ns, jelmers,c+"--", label=r'Point Truncation, $\eta=$'+str(eta)+r', x='+str(x))
plt.ylim(float(10**1),float(10**100))
plt.yscale('log')
plt.xlabel(r'$n$')
plt.ylabel("Runtime")
plt.legend()
plt.savefig("runtime.pdf", bbox_inches="tight")