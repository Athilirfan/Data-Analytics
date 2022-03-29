#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as body


# In[3]:


bodyfat=body.read_csv('C:/Users/atif2/Desktop/bodyfat.csv')


# In[4]:


bodyfat


# ### Mean

# In[5]:


bodyfat.mean()


# In[6]:


bodyfat.mean(axis=1)


# ### Median

# In[7]:


bodyfat.median()


# ### Difference between Maximum and Minimum values

# In[8]:


max(bodyfat['BodyFat'])-min(bodyfat['BodyFat'])


# ### Quantile

# In[9]:


body_quant=[bodyfat['BodyFat'].quantile(0),
            bodyfat['BodyFat'].quantile(0.25),
            bodyfat['BodyFat'].quantile(0.50),
            bodyfat['BodyFat'].quantile(0.75),
            bodyfat['BodyFat'].quantile(1)]


# In[10]:


body_quant


# ### Describing dataset

# In[11]:


bodyfat['BodyFat'].describe()


# ### IQR

# In[12]:


bodyfat['BodyFat'].quantile(0.75)-bodyfat['BodyFat'].quantile(0.25)


# ### Variance

# In[14]:


bodyfat['BodyFat'].var()


# ### Standard Deviation

# In[15]:


bodyfat['BodyFat'].std()


# ### Median absolute Deviation

# In[17]:


abs_median=abs(bodyfat['BodyFat']-bodyfat['BodyFat'].median())


# In[18]:


abs_median


# In[19]:


med=abs_median.median()*1.4628


# In[20]:


med


# ### Skewness

# In[21]:


bodyfat['BodyFat'].skew()


# ### Kurtosis

# In[22]:


bodyfat['BodyFat'].kurt()

