#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


page = requests.get('https://www.puredestinations.co.uk/top-10-famous-monuments-to-visit-in-india/')


# In[3]:


page


# In[4]:


soup = BeautifulSoup(page.content)


# In[10]:


name = []

for i in soup.find_all('strong',text='Taj Mahal'):
    print('Taj_Mahal, Agra'.next_sibling.strip())


# In[ ]:




