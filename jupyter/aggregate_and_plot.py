#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


path_to_csv = '../data/organized_data.csv'


# In[3]:


df = pd.read_csv ( path_to_csv, sep=',' )


# In[4]:


dfs = df.loc[df['tipo'] == 'sequential']
dfp = df.loc[df['tipo'] == 'parallel']

dfs = dfs.drop(columns=[ 'tipo', 'index', 'threads', 'tentativa' ])
dfp = dfp.drop(columns=[ 'tipo' ])

dfp2 = dfp.loc[df['threads'] == 2]
dfp4 = dfp.loc[df['threads'] == 4]
dfp8 = dfp.loc[df['threads'] == 8]

dfp2 = dfp2.drop(columns=[ 'index', 'threads', 'tentativa' ])
dfp4 = dfp4.drop(columns=[ 'index', 'threads', 'tentativa' ])
dfp8 = dfp8.drop(columns=[ 'index', 'threads', 'tentativa' ])


# In[5]:


dfs = dfs.sort_values('tempo')
dfs = dfs.groupby('tempo').mean().reset_index()

dfp2 = dfp2.sort_values('tempo')
dfp2 = dfp2.groupby('tempo').mean().reset_index()

dfp4 = dfp4.sort_values('tempo')
dfp4 = dfp4.groupby('tempo').mean().reset_index()

dfp8 = dfp8.sort_values('tempo')
dfp8 = dfp8.groupby('tempo').mean().reset_index()


# In[11]:


fig = plt.figure(figsize=(20,15))
frames = [ dfs, dfp2, dfp4, dfp8 ]
for frame in frames :
    plt.plot ( frame['tempo'], frame['num_primes'] )
plt.grid()
plt.title('Número de primos gerados por tempo')
plt.xlabel('Tempo (s)')
plt.ylabel('Número médio de primos gerados')
plt.legend([ 'sequencial', '2-threads', '4-threads', '8-threads' ])
# plt.savefig('resultado.pdf', dpi=150)
plt.show()


# In[67]:


def is_prime_n ( n ) :
    if n < 2 :
        return False
    aux = n - 1
    while aux > 2 :
        if n % aux == 0 :
            return False
        aux -= 1
    return True    


# In[68]:


from math import sqrt


# In[73]:


def is_prime_sqrt ( n ) :
    if n < 2 :
        return False
    aux = int(sqrt(n))
    while aux > 2 :
        if n % aux == 0 :
            return False
        aux -= 1
    return True    


# In[81]:


get_ipython().run_line_magic('timeit', '-r 10 is_prime_n(99_999_999)')


# In[82]:


get_ipython().run_line_magic('timeit', '-r 10 is_prime_sqrt(99_999_999)')


# In[ ]:




