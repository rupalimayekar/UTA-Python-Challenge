
# Heroes of Pymoli
Below is the Analysis for a company's most recent fantasy game, Heroes of Pymoli. This Analysis is done using Python's Data Analytics library - Pandas

Like many others in its genre, the game is free-to-play, but players are encouraged to purchase optional items that enhance their playing experience. As a first task, we generate a report that breaks down the game's purchasing data into meaningful insights.

## Observed Trend 1
There are a lot more Male players than Female and Other/Non Disclosed Gender players. The male population of players is 81% which is significantly higher than the non-male population. This shows that boys/men purchase/play more video games

## Observed Trend 2
There are also significantly more players in the 18-26 yrs Age group. Players in the 14-18yrs age group are the next higest in numbers but that's half of the the 18-26years. This shows that the younger generation comprises of the maximum player population

## Observed Trend 3
The most popular games have additional items that are lower in price. Perhaps they are more popular because the add-ons are more affordable, and the players get a lot more to play for that price. However the most profitable games are the ones that have the add-ons that are higher in price. These bring in more revenue to the company than the more popular items.


## Reading the data file and preparing for the Analysis. 
Take a peek at what the data looks like. The script here assumes that the data is in the form of a .json file. The script reads this file and imports the data. It looks at how much data there is and what the data types are, for correct processing of the data.



    Enter the name of the data file to import:   purchase_data.json







<div>
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



    Total Number of Players = 573


## Purchasing Analysis (Total)
* Number of Unique Items
* Average Purchase Price
* Total Number of Purchases
* Total Revenue



    Number of Unique Items = 183
    Average Purchase Price = $2.93
    Total Number of Purchases = 780
    Total Revenue = $2286.33


## Gender Demographics
* Percentage and Count of Male Players
* Percentage and Count of Female Players
* Percentage and Count of Other / Non-Disclosed




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






<div>
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







<div>
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







<div>
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







<div>
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






<div>
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







<div>
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


