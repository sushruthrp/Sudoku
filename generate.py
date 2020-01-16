#!/usr/bin/env python
# coding: utf-8

# In[2]:


# %load imports_default.py
#!/usr/bin/env python

# In[ ]:


import numpy as np
import math
import random as rn
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import json
get_ipython().run_line_magic('matplotlib', 'inline')
get_ipython().run_line_magic('pylab', 'inline')
get_ipython().run_line_magic('config', "InlineBackend.figure_format = 'svg'")


# In[3]:


start = [
    [1,2,3,4,5,6,7,8,9],
    [4,5,6,7,8,9,1,2,3],
    [7,8,9,1,2,3,4,5,6],
    [2,3,1,5,6,4,8,9,7],
    [5,6,4,8,9,7,2,3,1],
    [8,9,7,2,3,1,5,6,4],
    [3,1,2,6,4,5,9,7,8],
    [6,4,5,9,7,8,3,1,2],
    [9,7,8,3,1,2,6,4,5]
]
def col_change(b, col1, col2):
    for i in range(len(b)):
        buff = b[i][col1]
        b[i][col1] = b[i][col2]
        b[i][col2] = buff
    return b



import copy
def shuffle_board(seed):
    random.seed()
    row_shuffle = randint(1,100)
    col_shuffle = randint(1,100)
    for i in range(row_shuffle):
        roll= randint(0,3)
        changes = rn.sample(range(3), 2)
        buff = seed[roll*3 + changes[0]]
        seed[roll*3 + changes[0]] = seed[roll*3 + changes[1]]
        seed[roll*3 + changes[1]] = buff
    for i in range(col_shuffle):
        roll = randint(0,3)
        changes = rn.sample(range(3), 2)
        seed = col_change(seed, roll*3+ changes[0], roll*3+changes[1])
    return seed
def slots(s):
    if s=='easy':
        return (81-28)
    elif s =='medium':
        return (81-26)
    elif s =='hard':
        return (81-23)
    elif s=='v_hard':
        return (81-20)
def generate(seed,lvl):
    """ With levels 'easy' 'medium', 'hard', 'v_hard' levels."""
    seed = shuffle_board(seed)
    num = slots(lvl)
    a = rn.sample(range(0,9),9)
    b = rn.sample(range(0,9),9)
    removals = rn.sample([(x,y) for x in a for y in b],num)
    seed1 = copy.deepcopy(seed)
    for i in range(num):
#        print(removals[i])
        seed1[removals[i][0]][removals[i][1]] = 0
    return seed1, seed
        

