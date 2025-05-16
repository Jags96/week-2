import numpy as np


# update/add code below ...
def ways(n):
    max_5 = n//5
    n_ways = 0
    for i in len(max_5):
        if n>(i*5):
            n_ways+=1
    
    return n_ways


def ways_np(n):
    
    return None
