# PyBoss
## Goal
This exercise is meant to help a small, rural town modernize its vote-counting process. The python script `main.py` reads two input csv files containing poll data, analyzes the votes and calculates each of the following:

* The total number of votes cast
* A complete list of candidates who received votes
* The percentage of votes each candidate won
* The total number of votes each candidate won
* The winner of the election based on popular vote.

The script handles any such similarly-structured dataset. It prints the analysis to the screen and exports a text file with the results.

## Input
The script assumes the following about the input data:
* The input file name that the user provides is in a folder called "raw_data" within the folder from where the script is run
* The input file is a csv file that is composed of three columns: `Voter ID`, `County`, and `Candidate`. 

### Sample Input csv files
```
Voter ID,County,Candidate
1405627,Harsaw,Vestal
1711723,Mershville,Vestal
1550639,Matterdawn,Vestal
1042621,Harsaw,Vestal
1583965,Matterdawn,Vestal
```
## Output
The Poll Analysis is output on to the screen as well as to an output text file (.txt) in the same folder as the input file. The name of the output file is the same as the name of the input file with "_result" appended to it.

### Sample output
As an example, the analysis looks like the one below:

```
-------------------------
Election Results
-------------------------
Total Votes: 803000
-------------------------
Vestal: 48.0% (385440)
Torres: 44.0% (353320)
Seth: 5.0% (40150)
Cordin: 3.0% (24090)
-------------------------
Winner: Vestal
-------------------------
```