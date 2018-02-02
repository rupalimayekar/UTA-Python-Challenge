# PyBank 
## Goal
This exercise is meant to analyze the financial records of a company. The python script `main.py` promits the user for an input file name, does the analysis on the file and then prints the results to the screen as well as to an output file. The script handles any such similarly structured dataset in the form of a csv file. It analyzes the records to calculate the following:

* The total number of months included in the dataset
* The total amount of revenue gained over the entire period
* The average change in revenue between months over the entire period
* The greatest increase in revenue (date and amount) over the entire period
* The greatest decrease in revenue (date and amount) over the entire period

## Input
This scripts assumes that the input file name that the user provides is in a folder called "raw_data" which is in the folder from where the script is run. The script assumes the following about the input data:
* The input file is in a folder called raw_data within the folder where the script is run
* The data has two columns `Date` and `Revenue` with the respective column headers
* There are no gaps in the data and the data is sorted in increasing order of date i.e. the months are consecutive
* The date format is irrelevant. The Revenue numbers are assumed to be in $

### Sample Input csv files
```
Date,Revenue
Jan-2009,943690
Feb-2009,1062565
Mar-2009,210079
Apr-2009,-735286
May-2009,842933
```

```
Date,Revenue
Oct-12,1154293
Nov-12,885773
Dec-12,-448704
Jan-13,563679
Feb-13,555394
```

## Output
The script prints the output to the screen and also writes it to an output file. The output file is a text file (.txt), is placed in the same folder as the input file and has the same name as the input file. The Date format in the output is the same as the input Date format

### Sample output
As an example, the analysis looks like below:
```
---------------------------------------------
Financial Analysis for: budget_data.csv
---------------------------------------------
Total Months: 41
Total Revenue: $18971412
Average Revenue Change: $-6758.98
Greatest Increase in Revenue: Feb-16 ($1837235)
Greatest Decrease in Revenue: Aug-14 ($-1779747)
```
