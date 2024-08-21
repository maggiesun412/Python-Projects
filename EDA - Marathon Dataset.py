#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns

df = pd.read_csv(r'C:\Users\maggi\OneDrive\Documents\Python Projects\Marathon Dataset\TWO_CENTURIES_OF_UM_RACES.csv')


# In[2]:


df.head(10)


# In[3]:


df.shape


# In[4]:


df.dtypes


# In[5]:


# USA Races, 50k or 50 mile, 2020
# combine 50k and 50 mile

df[(df['Event distance/length'].isin(['50km','50mi'])) & (df['Year of event'] == 2020)]


# In[6]:


df[df['Event name'] == 'Everglades 50 Mile Ultra Run (USA)']['Event name'].str.split('(').str.get(1).str.split(')').str.get(0)


# In[7]:


df[df['Event name'].str.split('(').str.get(1).str.split(')').str.get(0) == 'USA']


# In[8]:


# combine all the filters together

df[(df['Event distance/length'].isin(['50km','50mi'])) & (df['Year of event'] == 2020) & (df['Event name'].str.split('(').str.get(1).str.split(')').str.get(0) == 'USA')]


# In[9]:


df2 = df[(df['Event distance/length'].isin(['50km','50mi'])) & (df['Year of event'] == 2020) & (df['Event name'].str.split('(').str.get(1).str.split(')').str.get(0) == 'USA')]


# In[10]:


df2.head(10)


# In[11]:


df2.shape


# In[12]:


# remove (USA) from event name

df2['Event name'].str.split('(').str.get(0)


# In[13]:


df2['Event name'] = df2['Event name'].str.split('(').str.get(0)


# In[14]:


df2.head()


# In[15]:


# clean up athlete age

df2['athlete_age'] = 2020 - df2['Athlete year of birth']


# In[16]:


# remove h from athlete perfomance

df2['Athlete performance'] = df2['Athlete performance'].str.split(' ').str.get(0)


# In[17]:


df2.head(5)


# In[18]:


# drop columns: Athlete Club, Athlete Country, Athlete year of birth, Athlete age category

df2 = df2.drop(['Athlete club', 'Athlete country', 'Athlete year of birth', 'Athlete age category'], axis = 1)


# In[19]:


df2.head()


# In[20]:


# clean up null values

df2.isna().sum()


# In[21]:


df2[df2['athlete_age'].isna()==1]


# In[22]:


df2 = df2.dropna()


# In[23]:


df2.shape


# In[24]:


# check for duplicates

df2[df.duplicated() == True]


# In[25]:


# reset index

df2.reset_index(drop = True)


# In[26]:


# fix data types

df2.dtypes


# In[28]:


df2['athlete_age'] = df2['athlete_age'].astype(int)


# In[29]:


df2['Athlete average speed'] = df2['Athlete average speed'].astype(float)


# In[30]:


df2.dtypes


# In[31]:


# rename columns 

#Year of event                  int64
#Event dates                   object
#Event name                    object
#Event distance/length         object
#Event number of finishers      int64
#Athlete performance           object
#Athlete gender                object
#Athlete average speed        float64
#Athlete ID                     int64
#athlete_age                    int32


# In[32]:


df2 = df2.rename(columns = {'Year of event':'year',
                            'Event dates':'race_day',
                            'Event name':'race_name',
                            'Event distance/length':'race_length',
                            'Event number of finishers':'race_number_of_finishers',
                            'Athlete performance':'athlete_performance',
                            'Athlete gender':'athlete_gender',
                            'Athlete average speed':'athlete_average_speed',
                            'Athlete ID':'athlete_id'})


# In[33]:


df2.head()


# In[34]:


# reorder columns

df3 = df2[['race_day', 'race_name', 'race_length', 'race_number_of_finishers', 'athlete_id', 'athlete_gender', 'athlete_age', 'athlete_performance', 'athlete_average_speed']]


# In[35]:


df3.head()


# In[36]:


# find 2 races ran in 2020 - Sarasota / Everglades

df3[df3['race_name'] == 'Everglades 50 Mile Ultra Run ']


# In[37]:


df3[df3['athlete_id'] == 222509]


# In[38]:


# comparing 50k and 50 mile

sns.histplot(df3['race_length'])


# In[39]:


# comparing males and females

sns.histplot(df3, x = 'race_length', hue = 'athlete_gender')


# In[40]:


sns.displot(df3[df3['race_length'] == '50mi']['athlete_average_speed'])


# In[42]:


sns.violinplot(data = df3, x = 'race_length', y = 'athlete_average_speed', hue = 'athlete_gender', split = True, inner = 'quart', linewidth = 1)


# In[44]:


# comparing athlete age and gender

sns.lmplot(data = df3, x = 'athlete_age', y = 'athlete_average_speed', hue = 'athlete_gender')


# In[45]:


#race_day
#race_name
#race_length
#race_number_of_finishers
#athlete_id
#athlete_gender
#athlete_age
#athlete_performance
#athlete_average_speed


# In[46]:


# difference in speed for the 50k and 50mi for male to female

df3.groupby(['race_length', 'athlete_gender'])['athlete_average_speed'].mean()


# In[49]:


# age groups that are the best in the 50mi race (20+ race min)

df3.query('race_length == "50mi"').groupby('athlete_age')['athlete_average_speed'].agg(['mean', 'count']).sort_values('mean', ascending = False).query('count>19').head(15)


# In[50]:


# what age groups are the worst in the 50mi race

df3.query('race_length == "50mi"').groupby('athlete_age')['athlete_average_speed'].agg(['mean', 'count']).sort_values('mean', ascending = True).query('count>19').head(20)


# In[51]:


# seasons for the data -> slower in summer than winter?

# spring 3-5
# summer 6-8
# fall 9-11
# winter 12-2

df3['race_month'] = df3['race_day'].str.split('.').str.get(1).astype(int)


# In[53]:


df3['race_season'] = df3['race_month'].apply(lambda x: 'Winter' if x > 11 else 'Fall' if x > 8 else 'Summer' if x > 5 else 'Spring' if x > 2 else 'Winter')


# In[54]:


df3.head(25)


# In[56]:


df3.groupby('race_season')['athlete_average_speed'].agg(['mean', 'count']).sort_values('mean', ascending = False)


# In[58]:


# 50 mile only

df3.query('race_length == "50mi"').groupby('race_season')['athlete_average_speed'].agg(['mean', 'count']).sort_values('mean', ascending = False)


# In[ ]:




