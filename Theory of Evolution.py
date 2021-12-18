#!/usr/bin/env python
# coding: utf-8

# In[9]:


with open("file1.txt","r+") as myfile:
    print (myfile.read())
    myfile.write(" I am fine ")
myfile.close()


# In[6]:


open("file1.txt","r")


# In[10]:


random.randint(1,5)


# In[14]:


import random
def evolve(x):
    ind = random.randint(0,len(x)-1)
    p = random.randint(1,100)
    print(p)
    if (p==1):
        if(x[ind]=='0'):
            x[ind]=='1'
        else:
            x[ind]=='0'
     










with open("DNA DATA.txt") as myfile:
    x=myfile.read()
    x=list(x)
for i in range(0,1000):
    evolve(x)
print(x)


# In[ ]:




