
# Heroes of Pymoli
Below is the Analysis for their most recent fantasy game, Heroes of Pymoli.

Like many others in its genre, the game is free-to-play, but players are encouraged to purchase optional items that enhance their playing experience. As a first task, we generate a report that breaks down the game's purchasing data into meaningful insights.

## Observed Trend 1
There are a lot more Male players than Female and Other/Non Disclosed Gender players. The male population of players is 81% which is significantly higher than the non-male population. This shows that boys/men purchase/play more video games

## Observed Trend 2
There are also significantly more players in the 18-26 yrs Age group. Players in the 14-18yrs age group are the next higest in numbers but that's half of the the 18-26years. This shows that the younger generation comprises of the maximum player population

## Observed Trend 3
The most popular games have additional items that are lower in price. Perhaps they are more popular because the add-ons are more affordable, and the players get a lot more to play for that price. However the most profitable games are the ones that have the add-ons that are higher in price. These bring in more revenue to the company than the more popular items.


## Reading the data file and preparing for the Analysis. 
Take a peek at what the data looks like. Get an idea of what the data types are so that you can do the right kind of processing on it.


```python
# Import the necessary libraries
import os
import numpy as np
import pandas as pd
```


```python
# Prompt for the filename
filename = input("Enter the name of the data file to import:   ")
```

    Enter the name of the data file to import:   purchase_data.json



```python
# Read the data file into a Data Frame
game_df = pd.read_json(filename)
game_df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>SN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>38</td>
      <td>Male</td>
      <td>165</td>
      <td>Bone Crushing Silver Skewer</td>
      <td>3.37</td>
      <td>Aelalis34</td>
    </tr>
    <tr>
      <th>1</th>
      <td>21</td>
      <td>Male</td>
      <td>119</td>
      <td>Stormbringer, Dark Blade of Ending Misery</td>
      <td>2.32</td>
      <td>Eolo46</td>
    </tr>
    <tr>
      <th>2</th>
      <td>34</td>
      <td>Male</td>
      <td>174</td>
      <td>Primitive Blade</td>
      <td>2.46</td>
      <td>Assastnya25</td>
    </tr>
    <tr>
      <th>3</th>
      <td>21</td>
      <td>Male</td>
      <td>92</td>
      <td>Final Critic</td>
      <td>1.36</td>
      <td>Pheusrical25</td>
    </tr>
    <tr>
      <th>4</th>
      <td>23</td>
      <td>Male</td>
      <td>63</td>
      <td>Stormfury Mace</td>
      <td>1.27</td>
      <td>Aela59</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Check te data types of the columns to get an idea and ensure you process them correctly
game_df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    Int64Index: 780 entries, 0 to 779
    Data columns (total 6 columns):
    Age          780 non-null int64
    Gender       780 non-null object
    Item ID      780 non-null int64
    Item Name    780 non-null object
    Price        780 non-null float64
    SN           780 non-null object
    dtypes: float64(1), int64(2), object(3)
    memory usage: 42.7+ KB


## Player Count
* Total Number of Players


```python
# Get the total number of players. This is the number of unique SN values as 
# SN looks like it is some kind of player ID
num_players = len(game_df['SN'].unique())
print("Total Number of Players = " + str(num_players))
```

    Total Number of Players = 573


## Purchasing Analysis (Total)
* Number of Unique Items
* Average Purchase Price
* Total Number of Purchases
* Total Revenue


```python
# Get the number of unique items. Using Item ID as the unique Identifier for the items
num_unique_items = len(game_df['Item ID'].unique())
print("Number of Unique Items = " + str(num_unique_items))

# Get the average purchase price. This is the mean of the Price column
avg_price = game_df['Price'].mean()
print("Average Purchase Price = ${0:.2f}".format(avg_price))

# Get the Total Number of Purchases. This is the total number of rows
num_purchases = len(game_df)
print("Total Number of Purchases = " + str(num_purchases))

# Get the Total Revenue. This is the sum of the Price column
total_revenue = game_df['Price'].sum()
print("Total Revenue = ${0:.2f}".format(total_revenue))
```

    Number of Unique Items = 183
    Average Purchase Price = $2.93
    Total Number of Purchases = 780
    Total Revenue = $2286.33


## Gender Demographics
* Percentage and Count of Male Players
* Percentage and Count of Female Players
* Percentage and Count of Other / Non-Disclosed



```python
# The SN column is a player id and for each unique value, the gender and age corresponds to the
# player's information. So extract these values into a separate data frame and remove any duplicates
# This will give us the info on each player and from that the Gender Demographics
player_df = game_df[['SN', 'Gender', 'Age']]
player_df = player_df.drop_duplicates()
player_df.reset_index(drop=True, inplace=True)
player_df['Gender'].value_counts()
```




    Male                     465
    Female                   100
    Other / Non-Disclosed      8
    Name: Gender, dtype: int64




```python
# Get the numbers for each value of Gender
num_male_players = player_df['Gender'].value_counts()['Male']
num_female_players = player_df['Gender'].value_counts()['Female']
num_other_players = num_players - num_male_players - num_female_players

# Get the percentages for each value of Gender
percent_male_players = (num_male_players/num_players)*100
percent_female_players = (num_female_players/num_players)*100
percent_other_players = (num_other_players/num_players)*100

#Print the numbers
print("Count of Male Players = " + str(num_male_players))
print("Percentage of Male Players = {0:.2f}%\n".format(percent_male_players))

print("Count of Female Players = " + str(num_female_players))
print("Percentage of Female Players = {0:.2f}%\n".format(percent_female_players))

print("Count of Other/Non Disclosed Players = " + str(num_other_players))
print("Percentage of Other/Non Disclosed Players = {0:.2f}%\n".format(percent_other_players))


```

    Count of Male Players = 465
    Percentage of Male Players = 81.15%
    
    Count of Female Players = 100
    Percentage of Female Players = 17.45%
    
    Count of Other/Non Disclosed Players = 8
    Percentage of Other/Non Disclosed Players = 1.40%
    


## Purchasing Analysis (by Gender)
Get the numbers below each broken by gender
* Purchase Count
* Average Purchase Price
* Total Purchase Value
* Normalized Totals


```python
# Group the data by Gender to get the needed numbers
grouped_data = game_df.groupby(game_df['Gender'], as_index=False)

# Count of items in the data set for each gender will give the purchase count for each gender
grouped_by_gender_df = grouped_data.count()[['Gender', 'Item ID']]
grouped_by_gender_df.rename(columns={'Item ID':'Purchase Count'}, inplace=True)

# The mean of the Price for each gender will give the Avg Purchase price per Gender
avg_purchase_price_by_gender_df = grouped_data.mean()[['Gender', 'Price']]

# Rename the column and format the data
avg_purchase_price_by_gender_df.rename(columns={'Price':'Avg Purchase Price'}, inplace=True)
avg_purchase_price_by_gender_df['Avg Purchase Price'] = avg_purchase_price_by_gender_df['Avg Purchase Price'].map("${0:,.2f}".format)

# merge the two to add the Avg Purchase Price to the grouped_by_gender_df
grouped_by_gender_df = pd.merge(grouped_by_gender_df, avg_purchase_price_by_gender_df, on='Gender')

# The sum of the Price for each gender will give the Total Purchase Value per Gender
total_price_by_gender_df = grouped_data.sum()[['Gender', 'Price']]

# Store the totals into variables before formatting. These will be used later
total_pp_female = total_price_by_gender_df.iloc[0,1]
total_pp_male = total_price_by_gender_df.iloc[1,1]
total_pp_other = total_price_by_gender_df.iloc[2,1]

# Rename the column and format the data
total_price_by_gender_df.rename(columns={'Price':'Total Purchase Value'}, inplace=True)
total_price_by_gender_df['Total Purchase Value'] = total_price_by_gender_df['Total Purchase Value'].map("${0:,.2f}".format)

# merge the two to add the Total Purchase Value to the grouped_by_gender_df
grouped_by_gender_df = pd.merge(grouped_by_gender_df, total_price_by_gender_df, on='Gender')

# Normalized Totals here are the purchase total per gender, divided by the player count per gender.
norm_total_female = total_pp_female/num_female_players
norm_total_male = total_pp_male/num_male_players
norm_total_other = total_pp_other/num_other_players

# Add the normalized values as a separate column. The order is considered here. Format the column
grouped_by_gender_df['Normalized Total Purchase Price'] = [norm_total_female, norm_total_male, norm_total_other]
grouped_by_gender_df['Normalized Total Purchase Price'] = grouped_by_gender_df['Normalized Total Purchase Price'].map("${0:,.2f}".format)
grouped_by_gender_df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Gender</th>
      <th>Purchase Count</th>
      <th>Avg Purchase Price</th>
      <th>Total Purchase Value</th>
      <th>Normalized Total Purchase Price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Female</td>
      <td>136</td>
      <td>$2.82</td>
      <td>$382.91</td>
      <td>$3.83</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Male</td>
      <td>633</td>
      <td>$2.95</td>
      <td>$1,867.68</td>
      <td>$4.02</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Other / Non-Disclosed</td>
      <td>11</td>
      <td>$3.25</td>
      <td>$35.74</td>
      <td>$4.47</td>
    </tr>
  </tbody>
</table>
</div>



## Age Demographics

Get the below listed numbers each broken into bins of 4 years (i.e. <10, 10-14, 15-19, etc.)
* Purchase Count
* Average Purchase Price
* Total Purchase Value
* Normalized Totals



```python
# Create the bins for the player ages. The first bin has ages 0 to 10. After that the bins increase in 
# increments of 4 till the maximum age in the dataset is accounted for.

max_age = game_df['Age'].max()

# create the age bins list
age_bins_arr = np.arange(10, max_age+4, 4)
age_bins = [0] + age_bins_arr.tolist()

# Create the labels for the bins
age_labels = []
for i in range(len(age_bins)):
    age_labels.append(str(age_bins[i-1]) + "-" + str(age_bins[i]))
# We remove the first label as it isn't needed 
age_labels.pop(0)

# Group the game data into the bins
game_df['Age Group'] = pd.cut(game_df['Age'], bins=age_bins, labels=age_labels)
game_df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>SN</th>
      <th>Age Group</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>38</td>
      <td>Male</td>
      <td>165</td>
      <td>Bone Crushing Silver Skewer</td>
      <td>3.37</td>
      <td>Aelalis34</td>
      <td>34-38</td>
    </tr>
    <tr>
      <th>1</th>
      <td>21</td>
      <td>Male</td>
      <td>119</td>
      <td>Stormbringer, Dark Blade of Ending Misery</td>
      <td>2.32</td>
      <td>Eolo46</td>
      <td>18-22</td>
    </tr>
    <tr>
      <th>2</th>
      <td>34</td>
      <td>Male</td>
      <td>174</td>
      <td>Primitive Blade</td>
      <td>2.46</td>
      <td>Assastnya25</td>
      <td>30-34</td>
    </tr>
    <tr>
      <th>3</th>
      <td>21</td>
      <td>Male</td>
      <td>92</td>
      <td>Final Critic</td>
      <td>1.36</td>
      <td>Pheusrical25</td>
      <td>18-22</td>
    </tr>
    <tr>
      <th>4</th>
      <td>23</td>
      <td>Male</td>
      <td>63</td>
      <td>Stormfury Mace</td>
      <td>1.27</td>
      <td>Aela59</td>
      <td>22-26</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Get the Purchase Count:  groupby Age Group and get a count on the Item ID column and rename the column
age_group = game_df.groupby('Age Group', as_index=False)
age_group_df = age_group.count()[['Age Group', 'Item ID']]
age_group_df.rename(columns={'Item ID':'Purchase Count'}, inplace=True)

# Average Purchase Price - Get the mean of the Price column, rename the column and format the column data
avg_price_age_group = age_group.mean()[['Age Group', 'Price']]
avg_price_age_group.rename(columns={'Price':'Avg Purchase Price'}, inplace=True)
avg_price_age_group['Avg Purchase Price'] = avg_price_age_group['Avg Purchase Price'].map("${0:,.2f}".format)

# Merge with the age_group_df to add the Avg Purchase Price column to it
age_group_df = pd.merge(age_group_df, avg_price_age_group, on='Age Group')

# Total Purchase Value - Get the sum of the Price column and rename and format the column
total_price_age_group_df = age_group.sum()[['Age Group', 'Price']]
total_price_age_group_df.rename(columns={'Price':'Total Purchase Value'}, inplace=True)

# Merge with the age_group_df to add the Total Purchase Value column
age_group_df = pd.merge(age_group_df, total_price_age_group_df, on='Age Group')

# Normalized Totals - These are the Purchase totals divided by the count of players grouped by age
# Get the count of players by age use these counts to calculate the normalized total
player_count_age_group_df = age_group.count()[['Age Group', 'SN']]

# Add the new calculated normalized column and drop the Total Purchase Price column here as we
# have captured it above in age_group_df
total_price_age_group_df['Normalized Total Price'] = total_price_age_group_df['Total Purchase Value']/player_count_age_group_df['SN']
total_price_age_group_df.drop('Total Purchase Value', axis=1, inplace=True)

# Merge with the age_group_df to get the Normalized Total Price added
age_group_df = pd.merge(age_group_df, total_price_age_group_df, on='Age Group')

# Format columns
age_group_df['Total Purchase Value'] = age_group_df['Total Purchase Value'].map("${0:,.2f}".format)
age_group_df['Normalized Total Price'] = age_group_df['Normalized Total Price'].map("${0:,.2f}".format)

#norm_total_age_group_df.drop(['Total Price'], axis=1, inplace=True)
age_group_df

```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age Group</th>
      <th>Purchase Count</th>
      <th>Avg Purchase Price</th>
      <th>Total Purchase Value</th>
      <th>Normalized Total Price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0-10</td>
      <td>32</td>
      <td>$3.02</td>
      <td>$96.62</td>
      <td>$3.02</td>
    </tr>
    <tr>
      <th>1</th>
      <td>10-14</td>
      <td>31</td>
      <td>$2.70</td>
      <td>$83.79</td>
      <td>$2.70</td>
    </tr>
    <tr>
      <th>2</th>
      <td>14-18</td>
      <td>111</td>
      <td>$2.88</td>
      <td>$319.32</td>
      <td>$2.88</td>
    </tr>
    <tr>
      <th>3</th>
      <td>18-22</td>
      <td>231</td>
      <td>$2.93</td>
      <td>$676.20</td>
      <td>$2.93</td>
    </tr>
    <tr>
      <th>4</th>
      <td>22-26</td>
      <td>207</td>
      <td>$2.94</td>
      <td>$608.02</td>
      <td>$2.94</td>
    </tr>
    <tr>
      <th>5</th>
      <td>26-30</td>
      <td>63</td>
      <td>$2.98</td>
      <td>$187.99</td>
      <td>$2.98</td>
    </tr>
    <tr>
      <th>6</th>
      <td>30-34</td>
      <td>46</td>
      <td>$3.07</td>
      <td>$141.24</td>
      <td>$3.07</td>
    </tr>
    <tr>
      <th>7</th>
      <td>34-38</td>
      <td>37</td>
      <td>$2.81</td>
      <td>$104.06</td>
      <td>$2.81</td>
    </tr>
    <tr>
      <th>8</th>
      <td>38-42</td>
      <td>20</td>
      <td>$3.13</td>
      <td>$62.56</td>
      <td>$3.13</td>
    </tr>
    <tr>
      <th>9</th>
      <td>42-46</td>
      <td>2</td>
      <td>$3.26</td>
      <td>$6.53</td>
      <td>$3.26</td>
    </tr>
  </tbody>
</table>
</div>



## Top Spenders
Identify the top 5 spenders in the game by total purchase value, then list (in a table):
* SN
* Purchase Count
* Average Purchase Price
* Total Purchase Value




```python
# Group the data by the player i.e. SN column
player_group = game_df.groupby('SN', as_index=False)

# Get the total purchase value per spender and get the top 5 spenders
top_player_grouped_df = player_group.sum()[['SN', 'Price']].sort_values('Price', ascending=False)
top_5_player_grouped_df = top_player_grouped_df.iloc[0:5, :]

# Get the Purchase Count by doing a count on Item ID
count_player_grouped_df = player_group.count()[['SN', 'Item ID']]

# Add the Item ID count and rename the columns
top_5_player_grouped_df = pd.merge(top_5_player_grouped_df, count_player_grouped_df, on = 'SN')
top_5_player_grouped_df.rename(columns={'Item ID':'Purchase Count', 'Price':'Total Purchase Value'}, inplace = True)
top_5_player_grouped_df['Total Purchase Value'] = top_5_player_grouped_df['Total Purchase Value'].map("${0:,.2f}".format)


# Add the mean of Price, format it and rename to Avg Purchase Price
avg_price_player_grouped_df = player_group.mean()[['SN', 'Price']]
avg_price_player_grouped_df['Price'] = avg_price_player_grouped_df['Price'].map("${0:,.2f}".format)

top_5_player_grouped_df = pd.merge(top_5_player_grouped_df, avg_price_player_grouped_df, on = 'SN')
top_5_player_grouped_df.rename(columns={'Price':'Avg Purchase Price'}, inplace = True)

# Reorder the columns
top_5_player_grouped_df = top_5_player_grouped_df[['SN', 'Purchase Count', 'Avg Purchase Price', 'Total Purchase Value']]
top_5_player_grouped_df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>SN</th>
      <th>Purchase Count</th>
      <th>Avg Purchase Price</th>
      <th>Total Purchase Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Undirrala66</td>
      <td>5</td>
      <td>$3.41</td>
      <td>$17.06</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Saedue76</td>
      <td>4</td>
      <td>$3.39</td>
      <td>$13.56</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Mindimnya67</td>
      <td>4</td>
      <td>$3.18</td>
      <td>$12.74</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Haellysu29</td>
      <td>3</td>
      <td>$4.24</td>
      <td>$12.73</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Eoda93</td>
      <td>3</td>
      <td>$3.86</td>
      <td>$11.58</td>
    </tr>
  </tbody>
</table>
</div>



## Most Popular Items
Identify the 5 most popular items by purchase count, then list (in a table):
* Item ID
* Item Name
* Purchase Count
* Item Price
* Total Purchase Value


```python
# Group the data by Item ID
item_group = game_df.groupby('Item ID', as_index=False)

# Get the count on the Item Name, sort by the descending order of count and get the top 5
top_item_grouped_df = item_group.count()[['Item ID','Item Name']].sort_values('Item Name', ascending=False)
top_item_grouped_df = top_item_grouped_df.iloc[0:5, :]

# Rename the column
top_item_grouped_df.rename(columns={'Item Name':'Purchase Count'}, inplace=True)

# Get the Item Name and Price for each Item ID. Merge to get the top 5, rename columns
item_name_grouped_df = item_group.min()[['Item ID','Item Name', 'Price']]
item_name_grouped_df.rename(columns={'Price':'Item Price'}, inplace=True)
top_item_grouped_df = pd.merge(top_item_grouped_df, item_name_grouped_df, on = 'Item ID')

# Get the sum of Price to get the Total Purchase Value. Merge to get the top 5 and rename columns
total_item_grouped_df = item_group.sum()[['Item ID', 'Price']]
top_item_grouped_df = pd.merge(top_item_grouped_df, total_item_grouped_df, on = 'Item ID')
top_item_grouped_df.rename(columns={'Price':'Total Purchase Value'}, inplace=True)

# Reorder  and format columns
top_item_grouped_df = top_item_grouped_df[['Item ID', 'Item Name', 'Purchase Count', 'Item Price', 'Total Purchase Value']]
top_item_grouped_df['Item Price'] = top_item_grouped_df['Item Price'].map("${0:,.2f}".format)
top_item_grouped_df['Total Purchase Value'] = top_item_grouped_df['Total Purchase Value'].map("${0:,.2f}".format)

top_item_grouped_df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Purchase Count</th>
      <th>Item Price</th>
      <th>Total Purchase Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>39</td>
      <td>Betrayal, Whisper of Grieving Widows</td>
      <td>11</td>
      <td>$2.35</td>
      <td>$25.85</td>
    </tr>
    <tr>
      <th>1</th>
      <td>84</td>
      <td>Arcane Gem</td>
      <td>11</td>
      <td>$2.23</td>
      <td>$24.53</td>
    </tr>
    <tr>
      <th>2</th>
      <td>31</td>
      <td>Trickster</td>
      <td>9</td>
      <td>$2.07</td>
      <td>$18.63</td>
    </tr>
    <tr>
      <th>3</th>
      <td>175</td>
      <td>Woeful Adamantite Claymore</td>
      <td>9</td>
      <td>$1.24</td>
      <td>$11.16</td>
    </tr>
    <tr>
      <th>4</th>
      <td>13</td>
      <td>Serenity</td>
      <td>9</td>
      <td>$1.49</td>
      <td>$13.41</td>
    </tr>
  </tbody>
</table>
</div>



## Most Profitable Items
Identify the 5 most profitable items by total purchase value, then list (in a table):
* Item ID
* Item Name
* Purchase Count
* Item Price
* Total Purchase Value



```python
# We will reuse the item_grouped_df from above as we need to group by Item ID again
# To get the most profitable items, get the sum of the Price column, then
# sort by descending sum value and get the top 5
top_profit_grouped_df = item_group.sum()[['Item ID','Price']].sort_values('Price', ascending=False)
top_profit_grouped_df = top_profit_grouped_df.iloc[0:5, :]
top_profit_grouped_df.rename(columns={'Price':'Total Purchase Value'}, inplace=True)

# Reuse the item_name_grouped_df to get the Item Name and Price for all items and 
# merge them with the top 5 profitable items above to get the top 5 Item Names and their Price. 
top_profit_grouped_df = pd.merge(top_profit_grouped_df, item_name_grouped_df, on = 'Item ID')

# Get the count of one of the columns to get the Purchase Count, add to the top 5 and rename column
pur_count_grouped_df = item_group.count()[['Item ID','Price']]
top_profit_grouped_df = pd.merge(top_profit_grouped_df, pur_count_grouped_df, on = 'Item ID')
top_profit_grouped_df.rename(columns={'Price':'Purchase Count'}, inplace=True)

# Reorder the columns
top_profit_grouped_df = top_profit_grouped_df[['Item ID', 'Item Name', 'Item Price', 'Purchase Count', 'Total Purchase Value']]
top_profit_grouped_df['Item Price'] = top_profit_grouped_df['Item Price'].map("${0:,.2f}".format)
top_profit_grouped_df['Total Purchase Value'] = top_profit_grouped_df['Total Purchase Value'].map("${0:,.2f}".format)
top_profit_grouped_df

```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Item Price</th>
      <th>Purchase Count</th>
      <th>Total Purchase Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>34</td>
      <td>Retribution Axe</td>
      <td>$4.14</td>
      <td>9</td>
      <td>$37.26</td>
    </tr>
    <tr>
      <th>1</th>
      <td>115</td>
      <td>Spectral Diamond Doomblade</td>
      <td>$4.25</td>
      <td>7</td>
      <td>$29.75</td>
    </tr>
    <tr>
      <th>2</th>
      <td>32</td>
      <td>Orenmir</td>
      <td>$4.95</td>
      <td>6</td>
      <td>$29.70</td>
    </tr>
    <tr>
      <th>3</th>
      <td>103</td>
      <td>Singed Scalpel</td>
      <td>$4.87</td>
      <td>6</td>
      <td>$29.22</td>
    </tr>
    <tr>
      <th>4</th>
      <td>107</td>
      <td>Splitter, Foe Of Subtlety</td>
      <td>$3.61</td>
      <td>8</td>
      <td>$28.88</td>
    </tr>
  </tbody>
</table>
</div>


