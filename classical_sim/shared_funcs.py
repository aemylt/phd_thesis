# -*- coding: utf-8 -*-
"""
Created on Thu May  9 12:15:25 2019

Common functions used in the graph code.

@author: aemylt
"""

from scipy.special import binom
import math

def worst_case(n, k, x=1, eta=1):
    '''
    Computes error bound from truncating the binomial distribution.
    '''
    return sum([binom(n,i)*(x*eta)**i*(1-x*eta)**(n-i) for i in range(k+1,n+1)])

def runtime(n,k,m=-1):
    '''
    Computes run time based on runtime of Clifford and Clifford.
    Assumes number of modes is n**2 if unspecified.
    '''
    if m==-1:
        m=n**2
    return 2*k*2**k + m*k*(k+1)/2 + (n-k)*m

def rencontres(n,i):
    '''
    Computes Rencontres number (number of permutations with n-i fixed points).
    '''
    return binom(n,i)*round(math.factorial(i)/math.e)

def c_i(n,m,i):
    '''
    Computes c_i/nCm.
    '''
    if i==1:
        return 0
    return sum([1/math.factorial(j) for j in range(m-i+1)])*binom(n-i,m-i)/(math.e*binom(n,m))

def jelmer_error(n, k, x=1, eta=1):
    '''
    Computes error bounds of point truncation as (approximately) geometric series.
    '''
    m = round(n*eta)
    m = int(m)
    return math.sqrt(sum([(x**2)**i*c_i(n,m,i) for i in range(k+1,m+1)]))

def jelmer_runtime(n,k,m=-1):
    '''
    Computes runtime for point truncation.
    If k<=1 assumes we're doing distinguishable photon sampling.
    '''
    if k <= 1:
        if m==-1:
            return n**2
        else:
            return n*m
    return 100*sum([binom(n,i)*rencontres(n,i)*i*2**(i)*max((n-i),1)**4*math.log(max(n-i,1),2) for i in range(k+1)])