#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

import seaborn as sns

import matplotlib.pyplot as plt


# In[5]:


df = pd.read_csv(r"C:\Users\maggi\OneDrive\Documents\Python Pandas\world_population2.csv")

df


# In[4]:


pd.set_option('display.float_format', lambda x: '%.2f' % x)


# In[6]:


df.info()


# In[7]:


df.describe()


# In[9]:


df.isnull().sum()

# gives us all the columns and how many are missing values


# In[10]:


df.nunique()

# displays how many unique values there are


# In[11]:


df.sort_values(by="2022 Population", ascending=False).head()

# shows top 5 by default


# In[12]:


df.sort_values(by="2022 Population", ascending=False).head(10)

# shows top 10 population


# In[16]:


df.corr(numeric_only = True) 


# In[24]:


sns.heatmap(df.corr(numeric_only = True), annot = True)

plt.rcParams['figure.figsize'] = (5,7)

plt.show()


# In[27]:


df.groupby('Continent').mean(numeric_only=True)


# In[29]:


df[df['Continent'].str.contains('Oceania')]


# In[30]:


df.groupby('Continent').mean(numeric_only=True).sort_values(by="2022 Population", ascending=False)


# In[33]:


df2 = df.groupby('Continent').mean(numeric_only=True).sort_values(by="2022 Population", ascending=False)

df2


# In[38]:


df.columns


# In[45]:


df2 = df.groupby('Continent')[['1970 Population',
       '1980 Population', '1990 Population', '2000 Population',
       '2010 Population', '2015 Population', '2020 Population',
       '2022 Population']].mean(numeric_only=True).sort_values(by="2022 Population", ascending=False)

df2


# In[46]:


df3 = df2.transpose()

df3


# In[47]:


df3.plot()


# In[49]:


df.boxplot(figsize=(20,10))


# In[50]:


df.dtypes


# In[51]:


df.select_dtypes(include='number')

# displays all datatypes that are numbers (int and floats)
# if you put (include='integer') - it will only display whole numbers


# In[53]:


df.select_dtypes(include='object')

# displays non-numeric data


# In[54]:


df.select_dtypes(include='float')

#displays floats (numbers with decimals)


# In[ ]:




