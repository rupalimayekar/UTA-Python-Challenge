
# Academy of Py

The Chief Data Scientist for a city's school district is helping the school board and mayor make strategic decisions regarding future school budgets and priorities. As a first task, she has been asked to analyze the district-wide standardized test results. She is given access to every student's math and reading scores, as well as various information on the schools they attend. Her responsibility is to aggregate the data and showcase obvious trends in school performance. Below is the Analysis done for the district.


## Input files

The script assumes two input files used for this analysis. They need to be .csv files as described below:

* One file contains the school data with the following columns : School ID, name, type, size, budget
* The other file contains student data with the following columns : Student ID, name, gender, grade, school, reading_score, math score


## Sneak peak at the input data

The script asks for the user to input the school file name (or relative path) and the student file name (or relative path). It reads them and then proceeds with the analysis



    Enter the name of the school data file: raw_data/schools_complete.csv
    Enter the name of the student data file: raw_data/students_complete.csv




### School Data File






<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School ID</th>
      <th>name</th>
      <th>type</th>
      <th>size</th>
      <th>budget</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>Huang High School</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Figueroa High School</td>
      <td>District</td>
      <td>2949</td>
      <td>1884411</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Shelton High School</td>
      <td>Charter</td>
      <td>1761</td>
      <td>1056600</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>Hernandez High School</td>
      <td>District</td>
      <td>4635</td>
      <td>3022020</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Griffin High School</td>
      <td>Charter</td>
      <td>1468</td>
      <td>917500</td>
    </tr>
  </tbody>
</table>
</div>





    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 15 entries, 0 to 14
    Data columns (total 5 columns):
    School ID    15 non-null int64
    name         15 non-null object
    type         15 non-null object
    size         15 non-null int64
    budget       15 non-null int64
    dtypes: int64(3), object(2)
    memory usage: 680.0+ bytes


### Student Data File






<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Student ID</th>
      <th>name</th>
      <th>gender</th>
      <th>grade</th>
      <th>school</th>
      <th>reading_score</th>
      <th>math_score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>Paul Bradley</td>
      <td>M</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>66</td>
      <td>79</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Victor Smith</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>94</td>
      <td>61</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Kevin Rodriguez</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>90</td>
      <td>60</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>Dr. Richard Scott</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>67</td>
      <td>58</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Bonnie Ray</td>
      <td>F</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>97</td>
      <td>84</td>
    </tr>
  </tbody>
</table>
</div>





    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 39170 entries, 0 to 39169
    Data columns (total 7 columns):
    Student ID       39170 non-null int64
    name             39170 non-null object
    gender           39170 non-null object
    grade            39170 non-null object
    school           39170 non-null object
    reading_score    39170 non-null int64
    math_score       39170 non-null int64
    dtypes: int64(3), object(4)
    memory usage: 2.1+ MB


## District Summary

High level snapshot (in table form) of the district's key metrics, including:

* Total Schools
* Total Students
* Total Budget
* Average Math Score
* Average Reading Score
* % Passing Math
* % Passing Reading
* Overall Passing Rate (Average of the above two)






<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Schools</th>
      <th>Total Students</th>
      <th>Total Budget</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Overall Passing Rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>15</td>
      <td>39170</td>
      <td>24649428</td>
      <td>78.985371</td>
      <td>81.87784</td>
      <td>74.980853</td>
      <td>85.805463</td>
      <td>80.393158</td>
    </tr>
  </tbody>
</table>
</div>



## School Summary

Overview table that summarizes key metrics about each school, including:

* School Name
* School Type
* Total Students
* Total School Budget
* Per Student Budget
* Average Math Score
* Average Reading Score
* % Passing Math
* % Passing Reading
* Overall Passing Rate (Average of the above two)







<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School Name</th>
      <th>School Type</th>
      <th>Total Students</th>
      <th>Total School Budget</th>
      <th>Per Student Budget</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Overall Passing Rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Huang High School</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
      <td>655.0</td>
      <td>76.63</td>
      <td>81.18</td>
      <td>65.68</td>
      <td>81.32</td>
      <td>73.50</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Figueroa High School</td>
      <td>District</td>
      <td>2949</td>
      <td>1884411</td>
      <td>639.0</td>
      <td>76.71</td>
      <td>81.16</td>
      <td>65.99</td>
      <td>80.74</td>
      <td>73.36</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Shelton High School</td>
      <td>Charter</td>
      <td>1761</td>
      <td>1056600</td>
      <td>600.0</td>
      <td>83.36</td>
      <td>83.73</td>
      <td>93.87</td>
      <td>95.85</td>
      <td>94.86</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Hernandez High School</td>
      <td>District</td>
      <td>4635</td>
      <td>3022020</td>
      <td>652.0</td>
      <td>77.29</td>
      <td>80.93</td>
      <td>66.75</td>
      <td>80.86</td>
      <td>73.81</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Griffin High School</td>
      <td>Charter</td>
      <td>1468</td>
      <td>917500</td>
      <td>625.0</td>
      <td>83.35</td>
      <td>83.82</td>
      <td>93.39</td>
      <td>97.14</td>
      <td>95.27</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Wilson High School</td>
      <td>Charter</td>
      <td>2283</td>
      <td>1319574</td>
      <td>578.0</td>
      <td>83.27</td>
      <td>83.99</td>
      <td>93.87</td>
      <td>96.54</td>
      <td>95.20</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Cabrera High School</td>
      <td>Charter</td>
      <td>1858</td>
      <td>1081356</td>
      <td>582.0</td>
      <td>83.06</td>
      <td>83.98</td>
      <td>94.13</td>
      <td>97.04</td>
      <td>95.59</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Bailey High School</td>
      <td>District</td>
      <td>4976</td>
      <td>3124928</td>
      <td>628.0</td>
      <td>77.05</td>
      <td>81.03</td>
      <td>66.68</td>
      <td>81.93</td>
      <td>74.31</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Holden High School</td>
      <td>Charter</td>
      <td>427</td>
      <td>248087</td>
      <td>581.0</td>
      <td>83.80</td>
      <td>83.81</td>
      <td>92.51</td>
      <td>96.25</td>
      <td>94.38</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Pena High School</td>
      <td>Charter</td>
      <td>962</td>
      <td>585858</td>
      <td>609.0</td>
      <td>83.84</td>
      <td>84.04</td>
      <td>94.59</td>
      <td>95.95</td>
      <td>95.27</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Wright High School</td>
      <td>Charter</td>
      <td>1800</td>
      <td>1049400</td>
      <td>583.0</td>
      <td>83.68</td>
      <td>83.95</td>
      <td>93.33</td>
      <td>96.61</td>
      <td>94.97</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Rodriguez High School</td>
      <td>District</td>
      <td>3999</td>
      <td>2547363</td>
      <td>637.0</td>
      <td>76.84</td>
      <td>80.74</td>
      <td>66.37</td>
      <td>80.22</td>
      <td>73.29</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Johnson High School</td>
      <td>District</td>
      <td>4761</td>
      <td>3094650</td>
      <td>650.0</td>
      <td>77.07</td>
      <td>80.97</td>
      <td>66.06</td>
      <td>81.22</td>
      <td>73.64</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Ford High School</td>
      <td>District</td>
      <td>2739</td>
      <td>1763916</td>
      <td>644.0</td>
      <td>77.10</td>
      <td>80.75</td>
      <td>68.31</td>
      <td>79.30</td>
      <td>73.80</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Thomas High School</td>
      <td>Charter</td>
      <td>1635</td>
      <td>1043130</td>
      <td>638.0</td>
      <td>83.42</td>
      <td>83.85</td>
      <td>93.27</td>
      <td>97.31</td>
      <td>95.29</td>
    </tr>
  </tbody>
</table>
</div>



## Top Performing Schools (By Passing Rate)

This table highlights the top 5 performing schools based on Overall Passing Rate. Include:

* School Name
* School Type
* Total Students
* Total School Budget
* Per Student Budget
* Average Math Score
* Average Reading Score
* % Passing Math
* % Passing Reading
* Overall Passing Rate (Average of the above two)






<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School Name</th>
      <th>School Type</th>
      <th>Total Students</th>
      <th>Total School Budget</th>
      <th>Per Student Budget</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Overall Passing Rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Cabrera High School</td>
      <td>Charter</td>
      <td>1858</td>
      <td>1081356</td>
      <td>582.0</td>
      <td>83.06</td>
      <td>83.98</td>
      <td>94.13</td>
      <td>97.04</td>
      <td>95.59</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Thomas High School</td>
      <td>Charter</td>
      <td>1635</td>
      <td>1043130</td>
      <td>638.0</td>
      <td>83.42</td>
      <td>83.85</td>
      <td>93.27</td>
      <td>97.31</td>
      <td>95.29</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Griffin High School</td>
      <td>Charter</td>
      <td>1468</td>
      <td>917500</td>
      <td>625.0</td>
      <td>83.35</td>
      <td>83.82</td>
      <td>93.39</td>
      <td>97.14</td>
      <td>95.27</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Pena High School</td>
      <td>Charter</td>
      <td>962</td>
      <td>585858</td>
      <td>609.0</td>
      <td>83.84</td>
      <td>84.04</td>
      <td>94.59</td>
      <td>95.95</td>
      <td>95.27</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Wilson High School</td>
      <td>Charter</td>
      <td>2283</td>
      <td>1319574</td>
      <td>578.0</td>
      <td>83.27</td>
      <td>83.99</td>
      <td>93.87</td>
      <td>96.54</td>
      <td>95.20</td>
    </tr>
  </tbody>
</table>
</div>



## Lowest Performing Schools (By Passing Rate)

This table highlights the bottom 5 performing schools based on Overall Passing Rate. Include:

* School Name
* School Type
* Total Students
* Total School Budget
* Per Student Budget
* Average Math Score
* Average Reading Score
* % Passing Math
* % Passing Reading
* Overall Passing Rate (Average of the above two)








<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School Name</th>
      <th>School Type</th>
      <th>Total Students</th>
      <th>Total School Budget</th>
      <th>Per Student Budget</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Overall Passing Rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Rodriguez High School</td>
      <td>District</td>
      <td>3999</td>
      <td>2547363</td>
      <td>637.0</td>
      <td>76.84</td>
      <td>80.74</td>
      <td>66.37</td>
      <td>80.22</td>
      <td>73.29</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Figueroa High School</td>
      <td>District</td>
      <td>2949</td>
      <td>1884411</td>
      <td>639.0</td>
      <td>76.71</td>
      <td>81.16</td>
      <td>65.99</td>
      <td>80.74</td>
      <td>73.36</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Huang High School</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
      <td>655.0</td>
      <td>76.63</td>
      <td>81.18</td>
      <td>65.68</td>
      <td>81.32</td>
      <td>73.50</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Johnson High School</td>
      <td>District</td>
      <td>4761</td>
      <td>3094650</td>
      <td>650.0</td>
      <td>77.07</td>
      <td>80.97</td>
      <td>66.06</td>
      <td>81.22</td>
      <td>73.64</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Ford High School</td>
      <td>District</td>
      <td>2739</td>
      <td>1763916</td>
      <td>644.0</td>
      <td>77.10</td>
      <td>80.75</td>
      <td>68.31</td>
      <td>79.30</td>
      <td>73.80</td>
    </tr>
  </tbody>
</table>
</div>



## Math Scores by Grade

This table lists the average Math Score for students of each grade level (9th, 10th, 11th, 12th) at each school.





<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>grade</th>
      <th>10th</th>
      <th>11th</th>
      <th>12th</th>
      <th>9th</th>
    </tr>
    <tr>
      <th>school</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Bailey High School</th>
      <td>77.00</td>
      <td>77.52</td>
      <td>76.49</td>
      <td>77.08</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <td>83.15</td>
      <td>82.77</td>
      <td>83.28</td>
      <td>83.09</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>76.54</td>
      <td>76.88</td>
      <td>77.15</td>
      <td>76.40</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>77.67</td>
      <td>76.92</td>
      <td>76.18</td>
      <td>77.36</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>84.23</td>
      <td>83.84</td>
      <td>83.36</td>
      <td>82.04</td>
    </tr>
    <tr>
      <th>Hernandez High School</th>
      <td>77.34</td>
      <td>77.14</td>
      <td>77.19</td>
      <td>77.44</td>
    </tr>
    <tr>
      <th>Holden High School</th>
      <td>83.43</td>
      <td>85.00</td>
      <td>82.86</td>
      <td>83.79</td>
    </tr>
    <tr>
      <th>Huang High School</th>
      <td>75.91</td>
      <td>76.45</td>
      <td>77.23</td>
      <td>77.03</td>
    </tr>
    <tr>
      <th>Johnson High School</th>
      <td>76.69</td>
      <td>77.49</td>
      <td>76.86</td>
      <td>77.19</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <td>83.37</td>
      <td>84.33</td>
      <td>84.12</td>
      <td>83.63</td>
    </tr>
    <tr>
      <th>Rodriguez High School</th>
      <td>76.61</td>
      <td>76.40</td>
      <td>77.69</td>
      <td>76.86</td>
    </tr>
    <tr>
      <th>Shelton High School</th>
      <td>82.92</td>
      <td>83.38</td>
      <td>83.78</td>
      <td>83.42</td>
    </tr>
    <tr>
      <th>Thomas High School</th>
      <td>83.09</td>
      <td>83.50</td>
      <td>83.50</td>
      <td>83.59</td>
    </tr>
    <tr>
      <th>Wilson High School</th>
      <td>83.72</td>
      <td>83.20</td>
      <td>83.04</td>
      <td>83.09</td>
    </tr>
    <tr>
      <th>Wright High School</th>
      <td>84.01</td>
      <td>83.84</td>
      <td>83.64</td>
      <td>83.26</td>
    </tr>
  </tbody>
</table>
</div>



## Reading Scores by Grade

This table lists the average Reading Score for students of each grade level (9th, 10th, 11th, 12th) at each school.






<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>grade</th>
      <th>10th</th>
      <th>11th</th>
      <th>12th</th>
      <th>9th</th>
    </tr>
    <tr>
      <th>school</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Bailey High School</th>
      <td>80.91</td>
      <td>80.95</td>
      <td>80.91</td>
      <td>81.30</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <td>84.25</td>
      <td>83.79</td>
      <td>84.29</td>
      <td>83.68</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>81.41</td>
      <td>80.64</td>
      <td>81.38</td>
      <td>81.20</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>81.26</td>
      <td>80.40</td>
      <td>80.66</td>
      <td>80.63</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>83.71</td>
      <td>84.29</td>
      <td>84.01</td>
      <td>83.37</td>
    </tr>
    <tr>
      <th>Hernandez High School</th>
      <td>80.66</td>
      <td>81.40</td>
      <td>80.86</td>
      <td>80.87</td>
    </tr>
    <tr>
      <th>Holden High School</th>
      <td>83.32</td>
      <td>83.82</td>
      <td>84.70</td>
      <td>83.68</td>
    </tr>
    <tr>
      <th>Huang High School</th>
      <td>81.51</td>
      <td>81.42</td>
      <td>80.31</td>
      <td>81.29</td>
    </tr>
    <tr>
      <th>Johnson High School</th>
      <td>80.77</td>
      <td>80.62</td>
      <td>81.23</td>
      <td>81.26</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <td>83.61</td>
      <td>84.34</td>
      <td>84.59</td>
      <td>83.81</td>
    </tr>
    <tr>
      <th>Rodriguez High School</th>
      <td>80.63</td>
      <td>80.86</td>
      <td>80.38</td>
      <td>80.99</td>
    </tr>
    <tr>
      <th>Shelton High School</th>
      <td>83.44</td>
      <td>84.37</td>
      <td>82.78</td>
      <td>84.12</td>
    </tr>
    <tr>
      <th>Thomas High School</th>
      <td>84.25</td>
      <td>83.59</td>
      <td>83.83</td>
      <td>83.73</td>
    </tr>
    <tr>
      <th>Wilson High School</th>
      <td>84.02</td>
      <td>83.76</td>
      <td>84.32</td>
      <td>83.94</td>
    </tr>
    <tr>
      <th>Wright High School</th>
      <td>83.81</td>
      <td>84.16</td>
      <td>84.07</td>
      <td>83.83</td>
    </tr>
  </tbody>
</table>
</div>



## Scores by School Spending

This table breaks down school performances based on average Spending Ranges (Per Student). We've used 4 reasonable bins to group school spending. Included in the table are each of the following:

* Average Math Score
* Average Reading Score
* % Passing Math
* % Passing Reading
* Overall Passing Rate (Average of the above two)







<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Spending Range Per Student</th>
      <th>Avg Reading Score</th>
      <th>Avg Math Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Overall Passing Rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>577-597</td>
      <td>83.96</td>
      <td>83.36</td>
      <td>93.70</td>
      <td>96.69</td>
      <td>95.19</td>
    </tr>
    <tr>
      <th>1</th>
      <td>597-617</td>
      <td>83.84</td>
      <td>83.53</td>
      <td>94.12</td>
      <td>95.89</td>
      <td>95.01</td>
    </tr>
    <tr>
      <th>2</th>
      <td>617-637</td>
      <td>81.31</td>
      <td>77.86</td>
      <td>70.32</td>
      <td>83.41</td>
      <td>76.86</td>
    </tr>
    <tr>
      <th>3</th>
      <td>637-657</td>
      <td>81.23</td>
      <td>77.54</td>
      <td>68.74</td>
      <td>82.15</td>
      <td>75.44</td>
    </tr>
  </tbody>
</table>
</div>



## Scores by School Size

This table breaks down school performances based on a reasonable approximation of school size (Small, Medium, Large). We've used 4 reasonable bins to group school size. Included in the table are each of the following:

* Average Math Score
* Average Reading Score
* % Passing Math
* % Passing Reading
* Overall Passing Rate (Average of the above two)






<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School Size</th>
      <th>Avg Reading Score</th>
      <th>Avg Math Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Overall Passing Rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Small</td>
      <td>83.88</td>
      <td>83.44</td>
      <td>93.66</td>
      <td>96.67</td>
      <td>95.17</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Medium</td>
      <td>81.65</td>
      <td>78.16</td>
      <td>72.34</td>
      <td>83.84</td>
      <td>78.09</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Large</td>
      <td>80.93</td>
      <td>77.07</td>
      <td>66.47</td>
      <td>81.11</td>
      <td>73.79</td>
    </tr>
  </tbody>
</table>
</div>



## Scores by School Types

This table breaks down school performances based on school type (Charter vs. District).Included in the table are each of the following:

* Average Math Score
* Average Reading Score
* % Passing Math
* % Passing Reading
* Overall Passing Rate (Average of the above two)







<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School Type</th>
      <th>Avg Reading Score</th>
      <th>Avg Math Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Overall Passing Rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Charter</td>
      <td>83.90</td>
      <td>83.41</td>
      <td>93.70</td>
      <td>96.65</td>
      <td>95.17</td>
    </tr>
    <tr>
      <th>1</th>
      <td>District</td>
      <td>80.96</td>
      <td>76.99</td>
      <td>66.52</td>
      <td>80.91</td>
      <td>73.71</td>
    </tr>
  </tbody>
</table>
</div>


