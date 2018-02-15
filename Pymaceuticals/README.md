
# Pymaceuticals Analysis

## Overview and Objective

Pymaceuticals Inc. is a burgeoning pharmaceutical company based out of San Diego, CA. Pymaceuticals specializes in drug-based, anti-cancer pharmaceuticals. In their most recent efforts, they've since begun screening for potential treatments to squamous cell carcinoma (SCC), a commonly occurring form of skin cancer.

We have been given access to the complete data from their most recent animal study. In this study, 250 mice were treated through a variety of drug regimes over the course of 45 days. Their physiological responses were then monitored over the course of that time. 

Our objective is to analyze the data to show how four treatments (Capomulin, Infubinol, Ketapril, and Placebo) compare.

As part of the analysis we need to do the following:
* Create a scatter plot that shows how the tumor volume changes over time for each treatment.
* Create a scatter plot that shows how the number of metastatic (cancer spreading) sites changes over time for each treatment.
* Create a scatter plot that shows the number of mice still alive through the course of treatment (Survival Rate)
* Create a bar graph that compares the total % tumor volume change for each drug across the full 45 days.


## Observations:

Amongst the 4 drugs in question - Capomulin, Infubinol, Ketapril, and Placebo, Capomulin seems to give better results than the other three. 

### Observed Trend 1
The Tumor Volume decreases over time with the use of the drug Capomulin. The Tumor Volume increases over time for the other three drugs - Infubinol, Ketapril, and Placebo

### Observed Trend 2
The rate of increase of Metastatic sites in lowest with the use of Capomulin and highest with Placebo.

### Observed Trend 3
The survival rate of mice is higher in those treated with Capomulin and was lower in those treated with Infubinol, Ketapril, and Placebo


```python
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
import numpy as np
from scipy.stats import sem
import warnings
```


```python
trial_df = pd.read_csv('raw_data/clinicaltrial_data.csv')
mouse_df = pd.read_csv('raw_data/mouse_drug_data.csv')
```


```python
trial_df.head()
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
      <th>Mouse ID</th>
      <th>Timepoint</th>
      <th>Tumor Volume (mm3)</th>
      <th>Metastatic Sites</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>b128</td>
      <td>0</td>
      <td>45.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>f932</td>
      <td>0</td>
      <td>45.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>g107</td>
      <td>0</td>
      <td>45.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>a457</td>
      <td>0</td>
      <td>45.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>c819</td>
      <td>0</td>
      <td>45.0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
mouse_df.head()

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
      <th>Mouse ID</th>
      <th>Drug</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>f234</td>
      <td>Stelasyn</td>
    </tr>
    <tr>
      <th>1</th>
      <td>x402</td>
      <td>Stelasyn</td>
    </tr>
    <tr>
      <th>2</th>
      <td>a492</td>
      <td>Stelasyn</td>
    </tr>
    <tr>
      <th>3</th>
      <td>w540</td>
      <td>Stelasyn</td>
    </tr>
    <tr>
      <th>4</th>
      <td>v764</td>
      <td>Stelasyn</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Select Data only for the four drugs that we want to analyze, 
# Combine the two data frames to get a single data frame with only the 4 drugs' data 
four_drugs_df = mouse_df.loc[(mouse_df['Drug']=='Capomulin') | (mouse_df['Drug']=='Infubinol') | (mouse_df['Drug']=='Ketapril') | (mouse_df['Drug']=='Placebo'), :]
full_df = pd.merge(trial_df, four_drugs_df, on='Mouse ID')
full_df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    Int64Index: 777 entries, 0 to 776
    Data columns (total 5 columns):
    Mouse ID              777 non-null object
    Timepoint             777 non-null int64
    Tumor Volume (mm3)    777 non-null float64
    Metastatic Sites      777 non-null int64
    Drug                  777 non-null object
    dtypes: float64(1), int64(2), object(2)
    memory usage: 36.4+ KB


## Plots that show how the tumor volume changes over time for each treatment.




```python
drugs = full_df['Drug'].unique()
drugs
```




    array(['Capomulin', 'Ketapril', 'Infubinol', 'Placebo'], dtype=object)



### Scatter plots - one for each Drug compared against each other show how the Tumor Volume of all the mice for that drug progress over time


```python
# Create subplots to plot data for each of the 4 drugs to compare
fig, axes = plt.subplots(1, 4, figsize=(12,5), sharex=True, sharey=True)

# List of colors for the subplots
colors = ['r', 'b', 'g', 'y']

# loop through the list of Drugs get the data set for each drug and plor it on a separate axes
for i in range(len(drugs)) :
    drug_df = full_df[full_df['Drug']==drugs[i]]
    axes[i].scatter(x=drug_df['Timepoint'], y=drug_df['Tumor Volume (mm3)'], c=colors[i])
    axes[i].set_title(drugs[i])
    axes[i].set_xlabel("Timepoint")
    axes[i].set_ylabel("Tumor Volume (mm3)")
plt.tight_layout()
plt.show()
```


![png](output_9_0.png)


### Scatter plot showing one plot with data for all drugs


```python
# Group the data for mice and get the mean values for the results to compare
full_grp_df = full_df.groupby(['Drug','Timepoint'], as_index=False).mean()

# Calculate the errorbar values using the sem() function.
sem_grp_df = full_df.groupby(['Drug','Timepoint']).sem()
sem_grp_df.reset_index(inplace=True)
# Drop unwanted columns as we only want the errorbar values. Rename the errorbar values
sem_grp_df.drop(['Mouse ID', 'Timepoint', 'Drug'], axis=1, inplace=True)
sem_grp_df.rename(columns={'Tumor Volume (mm3)': 'Tumor Volume (mm3) SEM',
                          'Metastatic Sites': 'Metastatic Sites SEM'}, inplace=True)

# Merge the errorbar values with the original data to get a new table with all values
sem_grp_df = pd.merge(full_grp_df, sem_grp_df, left_index=True, right_index=True)
sem_grp_df.head()
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
      <th>Drug</th>
      <th>Timepoint</th>
      <th>Tumor Volume (mm3)</th>
      <th>Metastatic Sites</th>
      <th>Metastatic Sites SEM</th>
      <th>Tumor Volume (mm3) SEM</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Capomulin</td>
      <td>0</td>
      <td>45.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Capomulin</td>
      <td>5</td>
      <td>44.266086</td>
      <td>0.160000</td>
      <td>0.074833</td>
      <td>0.448593</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Capomulin</td>
      <td>10</td>
      <td>43.084291</td>
      <td>0.320000</td>
      <td>0.125433</td>
      <td>0.702684</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Capomulin</td>
      <td>15</td>
      <td>42.064317</td>
      <td>0.375000</td>
      <td>0.132048</td>
      <td>0.838617</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Capomulin</td>
      <td>20</td>
      <td>40.716325</td>
      <td>0.652174</td>
      <td>0.161621</td>
      <td>0.909731</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Setting up the plot
fig, ax = plt.subplots()

# loop through the drugs and plor the scatter graph and error bars for each drug
for i in range(len(drugs)) :
    drug_sem_df = sem_grp_df[sem_grp_df['Drug']==drugs[i]]
    ax.scatter(x=drug_sem_df['Timepoint'], y=drug_sem_df['Tumor Volume (mm3)'])
    ax.errorbar(drug_sem_df['Timepoint'], drug_sem_df['Tumor Volume (mm3)'], drug_sem_df['Tumor Volume (mm3) SEM'], fmt="o")

# Set the other attributes for the plot
ax.legend(drugs, loc='center left', bbox_to_anchor=(1.0, 0.5))
ax.set_title('Tumor Volume over Tme')
ax.set_xlabel("Timepoint")
ax.set_ylabel("Tumor Volume (mm3)")
plt.show()
```


![png](output_12_0.png)


### Line graph showing one plot with data for all drugs


```python
# Create a pivot table for the Tumor Volume data for all Drugs for all Timepoints
drug_pivot_df = full_grp_df.pivot(index='Timepoint', columns='Drug',values='Tumor Volume (mm3)')
drug_pivot_df
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
      <th>Drug</th>
      <th>Capomulin</th>
      <th>Infubinol</th>
      <th>Ketapril</th>
      <th>Placebo</th>
    </tr>
    <tr>
      <th>Timepoint</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>45.000000</td>
      <td>45.000000</td>
      <td>45.000000</td>
      <td>45.000000</td>
    </tr>
    <tr>
      <th>5</th>
      <td>44.266086</td>
      <td>47.062001</td>
      <td>47.389175</td>
      <td>47.125589</td>
    </tr>
    <tr>
      <th>10</th>
      <td>43.084291</td>
      <td>49.403909</td>
      <td>49.582269</td>
      <td>49.423329</td>
    </tr>
    <tr>
      <th>15</th>
      <td>42.064317</td>
      <td>51.296397</td>
      <td>52.399974</td>
      <td>51.359742</td>
    </tr>
    <tr>
      <th>20</th>
      <td>40.716325</td>
      <td>53.197691</td>
      <td>54.920935</td>
      <td>54.364417</td>
    </tr>
    <tr>
      <th>25</th>
      <td>39.939528</td>
      <td>55.715252</td>
      <td>57.678982</td>
      <td>57.482574</td>
    </tr>
    <tr>
      <th>30</th>
      <td>38.769339</td>
      <td>58.299397</td>
      <td>60.994507</td>
      <td>59.809063</td>
    </tr>
    <tr>
      <th>35</th>
      <td>37.816839</td>
      <td>60.742461</td>
      <td>63.371686</td>
      <td>62.420615</td>
    </tr>
    <tr>
      <th>40</th>
      <td>36.958001</td>
      <td>63.162824</td>
      <td>66.068580</td>
      <td>65.052675</td>
    </tr>
    <tr>
      <th>45</th>
      <td>36.236114</td>
      <td>65.755562</td>
      <td>70.662958</td>
      <td>68.084082</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Create a line graph from the pivot table to show the progression
g =drug_pivot_df.plot(kind='line', title="Tumor Volume over Time")
g.set_ylabel('Tumor Volume (mm3)')

# Set the markers
drug_markers =  ['x','o','v','*']
for i, line in enumerate(g.get_lines()):
    line.set_marker(drug_markers[i])
    
# Set the legend to be outside the plot
g.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
plt.show()
```


![png](output_15_0.png)


## Plots that shows how the number of metastatic (cancer spreading) sites changes over time for each treatment.


### Scatter Plot showing the change in Metastatic Sites over Time


```python
# Setting up the plot
fig, ax = plt.subplots()

# loop through the drugs and plor the scatter graph and error bars for each drug
for i in range(len(drugs)) :
    drug_sem_df = sem_grp_df[sem_grp_df['Drug']==drugs[i]]
    ax.scatter(x=drug_sem_df['Timepoint'], y=drug_sem_df['Metastatic Sites'])
    ax.errorbar(drug_sem_df['Timepoint'], drug_sem_df['Metastatic Sites'], drug_sem_df['Metastatic Sites SEM'], fmt="o")

# Set the other attributes for the plot
ax.legend(drugs, loc='center left', bbox_to_anchor=(1.0, 0.5))
ax.set_title('Metastatic Sites over Tme')
ax.set_xlabel("Timepoint")
ax.set_ylabel("Metastatic Sites")
plt.show()
```


![png](output_18_0.png)


### Line Graph showing the change in Metastatic Sites over Time


```python
# Create a pivot table for the Metastatic Sites data
drug_pivot_df = full_grp_df.pivot(index='Timepoint', columns='Drug',values='Metastatic Sites')
drug_pivot_df
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
      <th>Drug</th>
      <th>Capomulin</th>
      <th>Infubinol</th>
      <th>Ketapril</th>
      <th>Placebo</th>
    </tr>
    <tr>
      <th>Timepoint</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0.160000</td>
      <td>0.280000</td>
      <td>0.304348</td>
      <td>0.375000</td>
    </tr>
    <tr>
      <th>10</th>
      <td>0.320000</td>
      <td>0.666667</td>
      <td>0.590909</td>
      <td>0.833333</td>
    </tr>
    <tr>
      <th>15</th>
      <td>0.375000</td>
      <td>0.904762</td>
      <td>0.842105</td>
      <td>1.250000</td>
    </tr>
    <tr>
      <th>20</th>
      <td>0.652174</td>
      <td>1.050000</td>
      <td>1.210526</td>
      <td>1.526316</td>
    </tr>
    <tr>
      <th>25</th>
      <td>0.818182</td>
      <td>1.277778</td>
      <td>1.631579</td>
      <td>1.941176</td>
    </tr>
    <tr>
      <th>30</th>
      <td>1.090909</td>
      <td>1.588235</td>
      <td>2.055556</td>
      <td>2.266667</td>
    </tr>
    <tr>
      <th>35</th>
      <td>1.181818</td>
      <td>1.666667</td>
      <td>2.294118</td>
      <td>2.642857</td>
    </tr>
    <tr>
      <th>40</th>
      <td>1.380952</td>
      <td>2.100000</td>
      <td>2.733333</td>
      <td>3.166667</td>
    </tr>
    <tr>
      <th>45</th>
      <td>1.476190</td>
      <td>2.111111</td>
      <td>3.363636</td>
      <td>3.272727</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Plot the line graph
g =drug_pivot_df.plot(kind='line', title="Metastatic Site over Time")
g.set_ylabel('Metastatic Sites')

# Set the markers
for i, line in enumerate(g.get_lines()):
    line.set_marker(my_markers[i])
    
# Set the legend to be outside the plot
g.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
plt.show()

```


![png](output_21_0.png)


## Scatter plot that shows the number of mice still alive through the course of treatment (Survival Rate)



```python
# Ge the count of mice at each timepoint for each drug
alive_grp_df = full_df.groupby(['Drug','Timepoint'], as_index=False).count()[['Drug','Timepoint', 'Mouse ID']]

# Setting up the plot
fig, ax = plt.subplots()

# loop through the drugs and plor the scatter graph and error bars for each drug
for i in range(len(drugs)) :
    drug_alive_df = alive_grp_df[alive_grp_df['Drug']==drugs[i]]
    
    ax.scatter(x=drug_alive_df['Timepoint'], y=drug_alive_df['Mouse ID'])

# Set the other attributes for the plot
ax.legend(drugs, loc='center left', bbox_to_anchor=(1.0, 0.5))
ax.set_title('Survival Rate of Mice')
ax.set_xlabel("Timepoint")
ax.set_ylabel("Number of Mice")
plt.show()
```


![png](output_23_0.png)


### Line graph showing the Survival Rate of mice


```python
# Create a pivot table for the Survival Rate
drug_pivot_df = alive_grp_df.pivot(index='Timepoint', columns='Drug',values='Mouse ID')
drug_pivot_df
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
      <th>Drug</th>
      <th>Capomulin</th>
      <th>Infubinol</th>
      <th>Ketapril</th>
      <th>Placebo</th>
    </tr>
    <tr>
      <th>Timepoint</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>25</td>
      <td>25</td>
      <td>25</td>
      <td>25</td>
    </tr>
    <tr>
      <th>5</th>
      <td>25</td>
      <td>25</td>
      <td>23</td>
      <td>24</td>
    </tr>
    <tr>
      <th>10</th>
      <td>25</td>
      <td>21</td>
      <td>22</td>
      <td>24</td>
    </tr>
    <tr>
      <th>15</th>
      <td>24</td>
      <td>21</td>
      <td>19</td>
      <td>20</td>
    </tr>
    <tr>
      <th>20</th>
      <td>23</td>
      <td>20</td>
      <td>19</td>
      <td>19</td>
    </tr>
    <tr>
      <th>25</th>
      <td>22</td>
      <td>18</td>
      <td>19</td>
      <td>17</td>
    </tr>
    <tr>
      <th>30</th>
      <td>22</td>
      <td>17</td>
      <td>18</td>
      <td>15</td>
    </tr>
    <tr>
      <th>35</th>
      <td>22</td>
      <td>12</td>
      <td>17</td>
      <td>14</td>
    </tr>
    <tr>
      <th>40</th>
      <td>21</td>
      <td>10</td>
      <td>15</td>
      <td>12</td>
    </tr>
    <tr>
      <th>45</th>
      <td>21</td>
      <td>9</td>
      <td>11</td>
      <td>11</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Plot the line graph
g =drug_pivot_df.plot(kind='line', title="Survival Rate of mice")
g.set_ylabel('Mice Count')

# Set the markers
for i, line in enumerate(g.get_lines()):
    line.set_marker(my_markers[i])
    
# Set the legend to be outside the plot
g.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
plt.show()


```


![png](output_26_0.png)


## Creating a bar graph that compares the total % tumor volume change for each drug across the full 45 days.


```python
# A function that takes the container of the bar plot and the axes and 
# adds the Y values as labels to the bars
def autolabel(rects, ax):
    # Get y-axis height to calculate label position from.
    (y_bottom, y_top) = ax.get_ylim()
    y_height = y_top - y_bottom

    for rect in rects:
        height = rect.get_height()
        label_position = height + (y_height * 0.01)

        ax.text(rect.get_x() + rect.get_width()/2., label_position,
                '%d' % int(height),
                ha='center', va='bottom')

```


```python
# Create an empty dictionary to store the % Volume change for each drug
changes = {}


# go through the full table for each drug we want and get the Tumor Volume at 
# Timepoints 0 and 45. Then calculate the % Volume change
for drug in drugs :
    start_vol = full_grp_df.loc[(full_grp_df['Drug'] == drug) & (full_grp_df['Timepoint'] == 0), ['Tumor Volume (mm3)']]
    end_vol = full_grp_df.loc[(full_grp_df['Drug'] == drug) & (full_grp_df['Timepoint'] == 45), ['Tumor Volume (mm3)']]
    
    percent_change = ((end_vol.iloc[0,0]-start_vol.iloc[0,0])/start_vol.iloc[0,0])*100
    changes[drug]=percent_change

g = plt.bar(x=[1,2,3,4], height=list(changes.values()), align='center', tick_label=list(changes.keys()),
             color=['g' if v >=0 else 'r' for v in changes.values()])

# set the Y limits
ymin = min(list(changes.values()))
ymax = max(list(changes.values()))
plt.ylim(-25,70)

# set the titles
plt.title("Total % Volume Change across 45 days")
plt.xlabel("Drug")
plt.ylabel("% Volume Change")

# Set the labels on the bars
autolabel(g, plt.axes())

#Ignore the warning 
warnings.filterwarnings('ignore')

plt.show()

```


![png](output_29_0.png)

