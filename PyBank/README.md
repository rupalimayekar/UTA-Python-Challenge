# PyBank 
## Goal
This python script, analyzes the financial records of a company. There are two sets of revenue data (`budget_data_1.csv` and `budget_data_2.csv`). Each dataset is composed of two columns: `Date` and `Revenue`.
The script handles any such similarly structured dataset and prints the analysis to the terminal and export a text file with the results.

The script analyzes the records to calculate each of the following:

* The total number of months included in the dataset

* The total amount of revenue gained over the entire period

* The average change in revenue between months over the entire period

* The greatest increase in revenue (date and amount) over the entire period

* The greatest decrease in revenue (date and amount) over the entire period

## Sample output
As an example, the analysis looks like below:
```
Financial Analysis
----------------------------
Total Months: 25
Total Revenue: $1241412
Average Revenue Change: $216825
Greatest Increase in Revenue: Sep-16 ($815531)
Greatest Decrease in Revenue: Aug-12 ($-652794)
```
