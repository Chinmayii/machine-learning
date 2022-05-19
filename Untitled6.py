#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
data=pd.read_csv("play.csv")
data


# In[10]:


import numpy as np
np.array(data)[0:3,0:1]
conc=np.array(data)[:,:-1]
tar=np.array(data)[0:5,-1]


# In[11]:


data[0:3]


# In[22]:


data[:3:3]


# In[92]:


import numpy as np


# In[93]:


np.array(data)[0:3,:3]


# In[94]:


conc=np.array(data)[:,:-1]
conc


# In[95]:


tar=np.array(data)[0:5,-1:]
tar


# In[96]:


for x in tar:
    print(x)


# In[97]:


def finds(tar,conc):
    for i,val in enumerate(tar):
        if val=='yes':
            spec=conc[i].copy()
            break
    for i,val in enumerate(conc):
        if tar[i]=='yes':
            for x in range(len(spec)):
                if val[x] !=spec[x]:
                    spec[x]="?"
                else:
                    pass
            print("the mainly specific hypothesis is",i)
            print(spec)

                


# In[98]:


print(finds(tar,conc))


# In[ ]:





# In[ ]:





# In[ ]:




