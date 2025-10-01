#!/usr/bin/env python
# coding: utf-8

# In[8]:


#import Necessary Libraries 
# if not installed Use pip install Library_name to install
import pandas as pd
import numpy as np 
import seaborn as sb
import matplotlib.pyplot as plt


# * client has given the raw data set named as DSataset.csv which is in csv format.
# * Load the data set into a variable as dataframe alias df

# In[9]:


#load the dataset into a variable "Data Frame" as 'df'
df=pd.read_csv("DSataset.csv")


# In[10]:


df.head() # to check the data is loaded to the dataframe or not.


# * the details given by the client **feature_x** is **'order_value'**, **feature_y** is **'unit_price'** and **feature_z** is  **'gross_profit'**.
# * so, rename the dataframe according to the details give by the client
# 

# In[11]:


df.rename(columns={
    'Feature_X': 'Order_Value',
    'Feature_Y': 'Unit_Price',
    'Feature_Z': 'Gross_Profit',
    'Category': 'Product_Category'
},inplace=True)


# In[12]:


df.head() #to verify the is my dataset is renamed or not?


# In[13]:


df.describe() #to understand the data


#  * by this describe function unable to understand the data due to more decimal points.
#  * so i am formating the decimal points as 2 decimal points.
#    

# In[14]:


# to understand the data we are modifying the display format
pd.options.display.float_format = '{:.2f}'.format


# In[15]:


df.head() #verifying is updated on the data frame or not


# In[16]:


df.describe() #to understand the data


# * to make more meaning i am adding order id and no. of units

# In[17]:


# Create a unique Order_ID for each row
df['Order_ID'] = range(1, len(df) + 1)
# Calculate the Number of Units sold
# We divide the total order value by the price per unit as we have total order value.
df['Number_of_Units'] = df['Order_Value'] / df['Unit_Price']


# In[18]:


df.head()# verifying is my new columns are affected in my data frame or not.


# In[19]:


# checking for is there are any null values exists in a data frame or not
df.isnull().sum()


# * by taking cosideration if  order_value or  unit_price is null, The number_of_units also null.
# * so, i am replacing the null rows in the number_of_units as zero and modifying the entire column with floor values/integer values
# * replacing the null values in the order_value and Unit_price with median to make consistance in the data.

# In[20]:


df['Number_of_Units'] = df['Number_of_Units'].fillna(0).round(0).astype(int)


# In[21]:


for i in ['Order_Value','Unit_Price']:
    df[i].fillna(df[i].median(), inplace=True)


# * update the Order_value again for consistancy in the data data frame

# In[22]:


# recalculate the Order_Value to make it consistent. This ensures your analysis is accurate 
# Recalculate Order_Value based on the whole number of units
df['Order_Value'] = df['Unit_Price'] * df['Number_of_Units']


# * Reorder all columns for a clean, logical layout

# In[23]:


final_columns = [
    'Order_ID',
    'Product_Category',
    'Unit_Price',
    'Number_of_Units',
    'Order_Value',
    'Gross_Profit'
]
df = df[final_columns]


# In[24]:


df.head()


# In[25]:


# recheck for is there any null values or not.
df.isnull().sum()


# * drop the duplicates to make more consistancy in the data frame

# In[26]:


df.drop_duplicates()


# * There is no duplicates so don't need to replace it

# In[27]:


df.describe()


# * by the above process we make the structure format of our raw data.
# * by seeing the above describe data we can conclude that in this data the **outliers** migth be present
# * so  i am using IQR method to remove the outliers.
# * The colums which i added is not required for to extract the insights from the data,
# * it's my perspective if you have different perspective to extract insights from the data you can by using the data set.
# * it's my perspective only but based on the user requirements it might be require in future analysis which may help full for other progammers.
# 

# In[28]:


# Set up a figure with two subplots side-by-side
fig, axes = plt.subplots(1, 2, figsize=(16, 7))
fig.suptitle('Distributions Before Outlier Removal', fontsize=18, weight='bold')

# Box Plot for Unit Price
sb.boxplot(ax=axes[0], y=df['Unit_Price'], color='skyblue')
axes[0].set_title(' Unit Price Distribution', fontsize=14)
axes[0].set_ylabel('Unit Price', fontsize=12)

# Box Plot for Order Value
sb.boxplot(ax=axes[1], y=df['Order_Value'], color='lightgreen')
axes[1].set_title(' Order Value Distribution', fontsize=14)
axes[1].set_ylabel('Order Value', fontsize=12)

plt.tight_layout(rect=[0, 0, 1, 0.96]) # Adjust for suptitle
plt.show()


# * it will show the ouliers of both colums of ordervalue and unit price,
# * i am not removing outliers from  grossprofit colum because it can be loss sometime and somtimes profits it's not depend on market volatile.
# * but i can't say that in order value and unit price because it's depends on market volatile and demand of the product.

# In[31]:


original_rows = len(df)
for column in ['Unit_Price', 'Order_Value']:
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    # Overwrite the original DataFrame with the cleaned data
    # This is the key step. We filter df and assign the result back to df itself.
    df = df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]
new_rows = len(df)
# Verify the changes 
print(f"Original number of rows: {original_rows}")
print(f"New number of rows in df: {new_rows}")
print(f"{original_rows - new_rows} outlier rows were removed from the original DataFrame.")

print("\nThe updated DataFrame now looks like this:")
print(df.head())


# In[32]:


# Set up a figure with two subplots side-by-side
fig, axes = plt.subplots(1, 2, figsize=(16, 7))
fig.suptitle('Distributions After Outlier Removal', fontsize=18, weight='bold')

# Box Plot for Unit Price
sb.boxplot(ax=axes[0], y=df['Unit_Price'], color='skyblue')
axes[0].set_title('Cleaned Unit Price Distribution', fontsize=14)
axes[0].set_ylabel('Unit Price', fontsize=12)

# Box Plot for Order Value
sb.boxplot(ax=axes[1], y=df['Order_Value'], color='lightgreen')
axes[1].set_title('Cleaned Order Value Distribution', fontsize=14)
axes[1].set_ylabel('Order Value', fontsize=12)

plt.tight_layout(rect=[0, 0, 1, 0.96]) # Adjust for suptitle
plt.show()


# In[35]:


df.to_csv('Cleaned_Data.csv', index=False)


# * **I used Three different charts to find the the insights from it**
# > 1. Bar chart used for to interprect the which category product has high gross profit
# > 2. histogram used to how my order value is often distributed over frequency
# > 3. pie chart used to calculate on which category have contributes more to my business.

# In[34]:


# Create the Final Analysis Dashboard
# Set the theme for the plots
sb.set_theme(style="whitegrid")
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(18, 14))
fig.suptitle(' Sales Analysis Dashboard', fontsize=24, weight='bold')

# Plot 1 (Top-Left): Bar Chart of Profit by Category
profit_by_category = df.groupby('Product_Category')['Gross_Profit'].sum().sort_values(ascending=False)
sb.barplot(ax=axes[0, 0], x=profit_by_category.index, y=profit_by_category.values, palette='plasma')
axes[0, 0].set_title('Total Gross Profit by Category', fontsize=16)
axes[0, 0].set_xlabel('Product Category', fontsize=12)
axes[0, 0].set_ylabel('Total Gross Profit', fontsize=12)

# Plot 2 (Top-Right): Pie Chart of Sales Count by Category
category_counts = df['Product_Category'].value_counts()
explode = [0.1 if i == 0 else 0 for i in range(len(category_counts))]
axes[0, 1].pie(category_counts, labels=category_counts.index, autopct='%1.1f%%',
               startangle=140, explode=explode, shadow=True,
               colors=sb.color_palette('plasma', len(category_counts)))
axes[0, 1].set_title('Proportion of Sales by Category', fontsize=16)

# Plot 3 (Bottom-Left): Histogram of Order Values
sb.histplot(ax=axes[1, 0], data=df, x='Order_Value', bins=30, kde=True, color=sb.color_palette('plasma')[3])
axes[1, 0].set_title('Distribution of Order Values', fontsize=16)
axes[1, 0].set_xlabel('Order Value', fontsize=12)
axes[1, 0].set_ylabel('Frequency', fontsize=12)

# Slot 4 (Bottom-Right): Key Metrics Summary
axes[1, 1].axis('off')
total_profit = df['Gross_Profit'].sum()
avg_order_value = df['Order_Value'].mean()
most_profitable_cat = profit_by_category.index[0]
avg_unit_price = df['Unit_Price'].mean()
avg_gross_profit = df['Gross_Profit'].mean()

top_two_cats = category_counts.head(2)
top_two_combined_pct = top_two_cats.sum() / category_counts.sum() * 100
cat1_name = top_two_cats.index[0]
cat2_name = top_two_cats.index[1]

summary_text = (
    f"Key Metrics & Insights\n"
    f"----------------------------------\n\n"
    f"Average Order Value: ₹{avg_order_value:,.2f}\n"
    f"Average Unit Price: ₹{avg_unit_price:,.2f}\n"
    f"Average Gross Profit: ₹{avg_gross_profit:,.2f}\n\n"
    f"Most Profitable Category: {most_profitable_cat}\n\n"
    f"Business Dependency:\n"
    f"Categories '{cat1_name}' & '{cat2_name}' combine for\n"
    f"{top_two_combined_pct:.1f}% of all sales transactions."
)

axes[1, 1].text(0.5, 0.5, summary_text,
                horizontalalignment='center',
                verticalalignment='center',
                fontsize=16,
                fontweight='bold',
                wrap=True,
                bbox=dict(boxstyle='round,pad=1', fc='aliceblue', ec='lightsteelblue', lw=2))

# Final layout fixing
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()

