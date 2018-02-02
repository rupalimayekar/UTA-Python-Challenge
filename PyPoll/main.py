#################################################################################
# This is the main script for the PyPoll Assignment
# The script asks for an input file name in the raw_data folder
# It then processes the poll data and prints the results as well as writes to
# an output file in the same data folder
#################################################################################

import csv
import os

# Get the input filename from the user and create the path to it
inputFile = input("Enter the name of the poll data file:  ")
inputFilePath = os.path.join("raw_data", inputFile)

# Create the output file path
outputFilePath = inputFilePath.split(".csv")[0] + "_result.txt"

# Initialize variables
totalVotes = 0
candidates = {}

# Read the poll data in the input file and process it.
with open(inputFilePath, newline='') as voteFile:

        # create the reader for the employee file
        csvReader = csv.reader(voteFile, delimiter=',')

        # loop through the data rows
        for row in csvReader:
            # ignore the first row
            if row[0] != "Voter ID":
                totalVotes += 1
                name = row[2]
                
                # If the candidate name exists in the dictionary then add 1 to the vote count for the candidate
                # else if the candidate name does not exist then add it with a vote of 1 as this will be the
                # first occurrence of the candidate's vote in the data file
                if name in candidates:
                    candidates[name] = candidates[name] + 1
                else:
                    candidates[name] = 1

#loop through the candidates and see who has the max votes
max = 0
winner = ""
for key, value in candidates.items():
    if value > max:
        max = value
        winner = key

#################################################################################
# Output the results to the screen
#################################################################################
print("-------------------------")
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(totalVotes))
print("-------------------------")
for key, value in candidates.items():
    percentage = round(value*100/totalVotes, 2)
    print(key + ": " + str(percentage) + "% " + "(" + str(value) + ")")
print("-------------------------")
print("Winner: " + winner)
print("-------------------------")

#################################################################################
# Output the results to the output file
#################################################################################
with open(outputFilePath, "w") as op:
    op.write("-------------------------\n")
    op.write("Election Results\n")
    op.write("-------------------------\n")
    op.write("Total Votes: " + str(totalVotes)+ "\n")
    op.write("-------------------------\n")
    for key, value in candidates.items():
        percentage = round(value*100/totalVotes, 2)
        op.write(key + ": " + str(percentage) + "% " + "(" + str(value) + ")\n")
    op.write("-------------------------\n")
    op.write("Winner: " + winner + "\n")
    op.write("-------------------------\n")
    
    