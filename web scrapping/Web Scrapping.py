#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install bs4


# In[2]:


pip install requests


# In[1]:


import requests 
from bs4 import BeautifulSoup
url='https://www.mysmartprice.com/appliance/pricelist/fully-automatic-washing-machines-price-list-in-india.html'


# In[2]:


response=requests.get(url)


# In[3]:


response


# In[4]:


won=BeautifulSoup(response.text)


# In[5]:


won


# In[8]:


wm=won.select('.prdct-item__name')


# In[9]:


wm


# In[10]:


wm_name= []
for item in wm:
    wm_name.append(item.text)
    link="https://www.mysmartprice.com/"+item["href"]


# In[11]:


wm_name


# In[13]:


price=won.select('.prdct-item__prc-val')


# In[14]:


price


# In[15]:


wm_price=[]
for item in price:
    wm_price.append(item.text)


# In[16]:


wm_price


# In[17]:


cc=won.select('.prdct-item__spcftn:nth-child(2)')


# In[18]:


cc


# In[19]:


wm_cc=[]
for item in cc:
    wm_cc.append(item.text)


# In[20]:


wm_cc


# In[21]:


ml=won.select('.prdct-item__spcftn:nth-child(1)')


# In[22]:


ml


# In[23]:


wm_ml=[]
for item in ml:
    wm_ml.append(item.text)
    wm_ml
    


# In[24]:


wm_ml


# In[29]:


import pandas as pd


# In[32]:


WashingMachine=pd.DataFrame(wm_name,columns=['Washing Machine Name'])


# In[33]:


WashingMachine


# In[34]:


WashingMachine['Price']=wm_price


# In[35]:


WashingMachine


# In[36]:


WashingMachine ['capacity']=wm_cc


# In[39]:


WashingMachine


# In[41]:


WashingMachine['Model']=wm_ml
WashingMachine

