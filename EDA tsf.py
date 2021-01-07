#!/usr/bin/env python
# coding: utf-8

# # THE SPARKS FOUNDATION
# ## DATA SCIENCE AND BUSINESS ANALYTICS INTERNSHIP JAN21
# ### TASK 3: EXPLORATORY DATA ANALYSIS - RETAIL
# #### QUESTION : Perform exploratory Data Analysis on the given dataset and as a business manager,try to find the weak areas where you can work to make more profit. Also, dervive all the business problems.
# ### Name: Chiranthana R R

# ## IMPORTING LIBRARIES

# In[2]:


import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns


# ## READING DATASET

# In[3]:


df = pd.read_csv('SampleSuperstore.csv')


# In[4]:


df.head()


# ## DATA INSIGHTS
# 
# 

# In[5]:


df.describe()


# In[6]:


df.info()


# In[7]:


df.shape


# In[8]:


df.isnull().sum() ##checking for duplicate values


# In[9]:


df.columns


# In[10]:


df.nunique()


# In[11]:


avg_profit = df['Profit'].astype('float').mean()
print("The average is {}".format(avg_profit))


# In[12]:


## total sales 
total_sales=df['Sales'].sum()
## total profit
total_profit=df['Profit'].sum()
print(total_sales)
print(total_profit)


# In[13]:


df['Profit'].max()


# In[14]:


loss=df['Profit']<avg_profit
loss.sum()


# In[15]:


Top_10_Sales = df.groupby("State").Sales.sum().nlargest(n =10)
Top_10_Profits = df.groupby("State").Profit.sum().nlargest(n =10)


# In[16]:


Top_10_Sales


# In[17]:


Top_10_Profits


# ### visualising top sales and profits

# In[18]:


plt.style.use('seaborn')
Top_10_Sales.plot(kind ='bar', figsize =(10,10), fontsize =14,color= 'red')
plt.xlabel("States", fontsize =13)
plt.ylabel("Total Sales",fontsize =13)
plt.title("Top 10 States by Sales",fontsize =16)
plt.show()


# In[19]:


plt.style.use('seaborn')
Top_10_Profits.plot(kind ='bar', figsize =(10,10), fontsize =14,color='green')
plt.xlabel("States", fontsize =13)
plt.ylabel("Total profit",fontsize =13)
plt.title("Top 10 States by Profit",fontsize =16)
plt.show()


# In[20]:


sns.pairplot(df,hue='Region')


# In[21]:


sns.pairplot(df,hue='Category')


# In[22]:


sns.pairplot(df,hue='Sub-Category')


# In[23]:


sns.heatmap(df.corr(), annot = True)


# In[29]:


plt.figure(figsize=(8,5))
sns.countplot(x=df['Ship Mode'])


# In[30]:


sns.catplot("Ship Mode", hue="Segment", data=df, kind="count", aspect=1.5, palette="Set1")


# In[35]:


plt.figure(figsize=(20,10))
sns.countplot(x=df["Sub-Category"],palette='twilight')

plt.title('Sub-Category', fontsize=35)
plt.xticks(rotation = 270, fontsize=15)

plt.show()


# In[39]:


sns.lmplot(x='Category',y='Sales',data=df,fit_reg=False,hue='Sub-Category',legend=True,palette='winter',size=10)
plt.title("Sales per Category and Sub-Category",fontsize=30)


# In[41]:


shipmode1=df.groupby(['Ship Mode'])['Sales','Discount','Profit'].sum()
shipmode1.plot.pie(autopct='%1.lf%%', label=shipmode1.index,subplots=True,figsize=(21,10))
plt.show()


# In[44]:


#statewise graph plot
sales_profit=df.groupby(['Sub-Category'])['Profit','Sales'].agg(['sum'])
sales_profit.plot.bar(rot=0,figsize=(20,10))

plt.title('Sales Profit per Category',fontsize=35)
plt.show(block=True)


# ## CONCLUSIONS DRAWN:
# 

# ### a) California is on top at both sales and profit 
# ### b)  Sales is highest in south
# ### c)  Profit is highest in central
# ### d) Under category, technology has highest sales and profits
# ### e) Under category, discount is more given to office supplies
# ### f)  Sales and Profit has a positive increament, if the discount is less
# ### Overall, the sales and profit ratio is huge, it is more wastage of resources , as the company is actually not making the profit it should inspite of all the maximum sales.
# ### Solution : Focus more on loss, less sales, less neccessity in the regions, drawbacks of more discount , least preferred product. Becuase working on losses can bring the company to sustained growth if not profit which is key factor for company growth in the market today .
# 
