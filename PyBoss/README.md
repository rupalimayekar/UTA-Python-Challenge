# PyBoss
## Goal
In this exercise, the boss of a company oversees hundreds of employees across the country developing Tuna 2.0, a world-changing snack food based on canned tuna fish. The company recently decided to purchase a new HR system, and, the new system requires employee records be stored completely differently.

The Python script 'main.py' converts the employee records to the required format. It imports two employee data files, converts the data into the new format and writes it in a new csv file. In summary, the required conversions are as follows:

* The `Name` column is split into separate `First Name` and `Last Name` columns.
* The `DOB` data is re-written into `DD/MM/YYYY` format.
* The `SSN` data is re-written such that the first five numbers are hidden from view.
* The `State` data is re-written as simple two-letter abbreviations.

The `us_state-abbrev.py` file is a supporting python file that maps all the state names of USA into their corresponding two letter abbreviations. It is used by the main script to convert the State column data.

## Input
The scripts assumes the following about the input data:
* The input files are in a folder called "raw_data" which is in the folder from where the script is run
* The two input file names are `employee_data1.csv` and `employee_data2.csv`
* The input files are csv files that is composed of these columns: `Emp ID`, `Name`, `DOB`, `SSN`, and `State`. 

### Sample Input csv files
```
Emp ID,Name,DOB,SSN,State
214,Sarah Simpson,1985-12-04,282-01-8166,Florida
15,Samantha Lara,1993-09-08,848-80-7526,Colorado
411,Stacy Charles,1957-12-20,658-75-8526,Pennsylvania
```

## Output
The output is a resulting csv file with the name `new_employee_data.csv` and is placed in the same folder as the input files.

### Sample output csv file
```
Emp ID,First Name,Last Name,DOB,SSN,State
214,Sarah,Simpson,12/04/1985,***-**-8166,FL
15,Samantha,Lara,09/08/1993,***-**-7526,CO
411,Stacy,Charles,12/20/1957,***-**-8526,PA
```
