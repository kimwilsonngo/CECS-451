import numpy as np
import matplotlib.pyplot as plt
from random import randint
from operator import mul   
from fractions import Fraction
import functools as f

def q1(N):
    d1 = 0
    d2 = 0
    d3 = 0
    x = []
    totalsucc = 0
    for k in range(0, N):
        success = 0
        for k in range(0,1000):
            d1 = randint(1,7)
            d2 = randint(1,7)
            d3 = randint(1,7)
            if d1 == 6 and d2 == 6 and d3 == 6:
                success = success + 1
                totalsucc = totalsucc + 1
        x.append(success)
    print(x)
    b = range(1,17)
    h1, bin_edges = np.histogram(x, bins = b)
    b1 = bin_edges[0:15]
    #
    p1=h1/N
    
    fig1 = plt.figure(1)
    plt.bar(b1,p1)
    plt.title('Experimental Results')
    plt.xlabel('# of Successes')
    plt.ylabel('Probability of Success')

q1(1000)