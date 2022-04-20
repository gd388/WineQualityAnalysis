#!/usr/bin/env python
# coding: utf-8

# 1 .Load the pandas library and create two different data frames, namely, df_red for holding the red wine dataset and df_white for holding the white wine dataset.

# In[4]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# In[5]:


df_red = pd.read_csv(r"C:\Users\dixit\OneDrive\Desktop\redwine.csv")
df_white = pd.read_csv(r"C:\Users\dixit\OneDrive\Desktop\whitewine.csv")


# In[6]:


df_red.columns


# In[7]:


df_red[100:111]


# In[8]:


df_red.info()


# In[76]:


df_white.describe()


# In[10]:


df_red.isnull().sum()


# In[11]:


sns.countplot(x=df_red['quality'])


# # Pairplot

# In[12]:



sns.pairplot(df_red , diag_kind = "hist" )


# # Heatmap

# In[13]:


plt.subplots(figsize = (12,7))
sns.heatmap(df_red.corr() , annot = True , linewidth = 1.50)


# # BoxPlot

# In[14]:


sns.boxplot(x= df_red['quality'] , y= df_red['alcohol'])


# In[15]:


sns.barplot(x= df_red['quality'] , y= df_red['alcohol'])


# In[16]:


sns.jointplot(x= df_red['alcohol'] , y = df_red['pH'] )


# # Correlation Function
# 

# In[17]:


def get_correlation():
    x = input()
    y=input()
    corr = df_red[x].corr(df_red[y])
    return corr

    


# In[19]:


get_correlation()


# In[20]:


print(np.mean(df_red['quality']))
print(np.mean(df_white['quality']))


# In[21]:


df_red['wine_category'] = 'NaN'


# In[23]:


df_white['wine_category']  = 'NaN'


# In[24]:


df_red['quality'].unique()


# In[25]:


df_white['quality'].unique()


# In[68]:



def quality_label():
    for i in range(len(df_red['quality'])):
        if df_red['quality'][i] <= 5:
            df_red['quality_label'].loc[i] = 'Low Quality'
        elif df_red['quality'][i]  > 5 and df_red['quality'][i]  <= 7 :
            df_red['quality_label'].loc[i] = "Medium Quality"
        else:
            df_red['quality_label'].loc[i] = "High Quality"
    return df_red['quality_label']
quality_label()


# In[66]:


df_white['quality_label'] = ''
def quality_label1():
    
    for i in range(len(df_white['quality'])):
        if df_white['quality'][i] <= 5:
            df_white['quality_label'].loc[i] = 'Low Quality'
            
        elif (df_white['quality'][i] > 5 and df_white['quality'][i]  <= 7) :
            df_white['quality_label'].loc[i] = "Medium Quality"
            
        else:
            df_white['quality_label'].loc[i] = "High Quality"
            
    return df_white['quality_label']

quality_label1()


# In[67]:


df_white


# In[98]:


gp = df_red.groupby(by = 'quality_label').size()
gp


# In[73]:


df_white.groupby(by = 'quality_label').size()


# In[74]:


df = df_red.append(df_white)


# In[80]:


df = df.sample(frac=1).reset_index(drop=True)
df.head()


# In[83]:


df['wine_category'] = df['quality_label']


# In[91]:


df = df.drop('quality_label',axis = 1)


# In[92]:


gkk = df.groupby(by = ['alcohol', 'density', 'pH','quality'])
gkk.first()


# In[112]:


sizes = gp
labels = [ 'High' ,'Low' , 'Medium']
explode = [.5,0,0]


# In[125]:


plt.subplots(figsize = (12,7))
plt.subplot(1,2,1)
plt.pie(sizes, labels=labels , autopct='%1.1f%%')

plt.subplot(1,2,2)
plt.hist(df['quality'])
plt.xlabel('quality')


# In[130]:


plt.subplots(figsize = (12,7))
sns.heatmap(df.corr() , annot =True)


# In[96]:


sns.countplot(x=df['wine_category'] , )


# In[ ]:




