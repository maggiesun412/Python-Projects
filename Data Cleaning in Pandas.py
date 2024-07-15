#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_excel(r"C:\Users\maggi\OneDrive\Documents\Python Pandas\Customer Call List.xlsx")

df


# In[3]:


df = df.drop_duplicates()

df


# In[4]:


df = df.drop(columns = "Not_Useful_Column")

df


# In[5]:


#df["Last_Name"] = df["Last_Name"].str.lstrip("...")
#df["Last_Name"] = df["Last_Name"].str.lstrip("/")
#df["Last_Name"] = df["Last_Name"].str.rstrip("_")

df["Last_Name"] = df["Last_Name"].str.strip("123._/")

df


# In[21]:


#df["Phone_Number"] = df["Phone_Number"].str.replace('[^a-zA-Z0-9]','',regex=True)

#df['Phone_Number'] = df['Phone_Number'].astype(str)

#df["Phone_Number"].apply(lambda x: x[0:3] + '-' + x[3:6] + '-' + x[6:10])

#df["Phone_Number"] = df["Phone_Number"].str.replace('nan--','')

#df["Phone_Number"] = df["Phone_Number"].str.replace('Na--','')

#df["Phone_Number"] = df["Phone_Number"].str.replace('nan','')

#df["Phone_Number"] = df["Phone_Number"].str.replace('Na','')

df


# In[24]:


df[["Street_Address", "State", "Zip_Code"]] = df["Address"].str.split(',',n=2, expand=True)

df


# In[28]:


df["Paying Customer"] = df["Paying Customer"].str.replace('Yes', 'Y')

df["Paying Customer"] = df["Paying Customer"].str.replace('No', 'N')

df


# In[29]:


df["Do_Not_Contact"] = df["Do_Not_Contact"].str.replace('Yes', 'Y')

df["Do_Not_Contact"] = df["Do_Not_Contact"].str.replace('No', 'N')

df


# In[34]:


df = df.replace('N/a', '')

df = df.fillna('')

df


# In[35]:


for x in df.index:
    if df.loc[x, "Do_Not_Contact"] == 'Y':
        df.drop(x, inplace=True)
        
df


# In[36]:


for x in df.index:
    if df.loc[x, "Phone_Number"] == '':
        df.drop(x, inplace=True)
        
df

# alternative code to drop null values: df = df.dropna(subset= "Phone_Number"), inplace=True)


# In[39]:


df = df.reset_index(drop=True)

df


# In[ ]:




