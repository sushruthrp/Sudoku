#!/usr/bin/env python
# coding: utf-8

# In[281]:


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


# In[282]:


board = [
    [0,0,6,0,0,9,2,4,0],
    [0,0,0,0,0,0,0,0,0],
    [0,5,0,1,2,0,0,7,0],
    [0,0,4,0,3,2,0,6,0],
    [0,0,5,0,0,0,3,0,0],
    [0,7,0,4,5,0,9,0,0],
    [0,9,0,0,6,8,0,1,0],
    [0,0,0,0,0,0,0,0,0],
    [0,6,7,2,0,0,8,0,0]
]
hard = [
    [8,0,0,0,0,0,0,0,0],
    [0,0,3,6,0,0,0,0,0],
    [0,7,0,0,9,0,2,0,0],
    [0,5,0,0,0,7,0,0,0],
    [0,0,0,0,4,5,7,0,0],
    [0,0,0,1,0,0,0,3,0],
    [0,0,1,0,0,0,0,6,8],
    [0,0,8,5,0,0,0,1,0],
    [0,9,0,0,0,0,4,0,0]
]
def print_board(b):
    
    for i in range(len(b)):
        if i%3 ==0 and i!=0:
            print('- - - - - - - - - - - - - -')
        for j in range(len(b[0])):
            if j%3==0 and j!=0:
                print('  |  ', end = '')
            if j==8:
                print(str(b[i][j]))
            else:
                print(str(b[i][j])+ ' ', end='')
#print_board(hard)
                    


# In[283]:


def find_empty(b):
    for i in range(len(b)):
        for j in range(len(b[0])):
            if b[i][j] == 0:
                return (i, j)
    return False

            
def is_valid(b, n, pos):
    # Check row
    for i in range(len(b[0])):
        if b[pos[0]][i]==n and i!= pos[1]:
            return False
        
    #check column    
    for i in range(len(b)):
        if b[i][pos[1]] == n and i!=pos[0]:
            return False
        
        
    # Check square
    row = pos[0]//3
    col = pos[1]//3
    for i in range(row*3, row*3 +3):
        for j in range(col*3, col*3+3):
            if b[i][j] == n and i!=pos[0] and j!= pos[1]:
                return False
    return True




def solve(b):

    slot = find_empty(b)
    if not slot:
        return True
    else:
        row , col = slot
    for i in range(1,10):
        if is_valid(b, i, (row,col)):
            b[row][col]=i

            if solve(b):
                return True
            b[row][col] = 0
    return False



print(solve(hard))

