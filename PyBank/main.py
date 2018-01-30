################################################################################################
# This is the main script to calculate the financial records for a given company
# as specified by the PyBank exercise. The scripts assumes the following about the input data:
# 1 - The data has two columns "Date", "Revenue" with the respective column headers
# 2 - There are no gaps in the data and the data is sorted in increasing order of date
# i.e. the months are consecutive
# 3 - The input file is in a folder called raw_data within the folder where the script is run
# The output file is placed in the same folder as the main.py script
################################################################################################

import os
import csv

#Get the filename as input from the user and create the path to open
fileName = input("Enter the name of the Budget Data input file from the raw_data folder:  ")
csvPath = os.path.join('raw_data', fileName)

# The name of the outputfile will be the same as the name of the input file but with a .txt extension
outputFile = fileName.split(".csv")[0] + ".txt"

# Initialize all the variables and lists
months = [] 
revenues = []
revenueChanges = []
dateList = []

totalRevenue = 0
totalChange = 0
averageChange = 0.0
greatestIncrease = 0
greatestDecrease = 0
greatestIncreaseMonth = ""
greatestIncreaseMonth = ""


#Open the Budget Data file from the path created above
with open(csvPath, newline='') as budFile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(budFile, delimiter=',')
    
    # read the file row by row. The first row is skipped. Extract each month into the months list
    # and each revenue number into the revenues list. These lists will later be used for the analysis
    # Also while we are looping through the data we get the total of the revenue numbers
    for row in csvreader:
        if row[0] != "Date":
            months.append(row[0])
            revenues.append(row[1])
            totalRevenue += int(row[1])

    # traverse the revenues and calculate the change in revenue for each month. There will be no
    # change recorded for the first month. Also while we are looping, we get the total of change
    # to be used later to calculate the average change
    for i in range(len(revenues)-1):
        change = int(revenues[i+1]) - int(revenues[i])
        revenueChanges.append(change)
        totalChange += change
    
    # Now calculate all the remaining Financial Analysis numbers
    averageChange = totalChange/len(revenueChanges)
    greatestIncrease = max(revenueChanges)
    greatestIncreaseMonth = months[revenueChanges.index(greatestIncrease)+1]
    
    # the Decrease will be printed only if there is a negative number in the revenueChanges
    greatestDecrease = min(revenueChanges) if min(revenueChanges) < 0 else 0
    greatestDecreaseMonth = "" if greatestDecrease == 0 else months[revenueChanges.index(greatestDecrease)+1]
    

    ##################################################
    #  Output printed on the screen
    ###################################################
    print("---------------------------------------------")
    print("Financial Analysis for: " + fileName)
    print("---------------------------------------------")
    print ("Total Months: " + str(len(months)))
    print ("Total Revenue: $" + str(totalRevenue))
    print ("Average Revenue Change: $%.2f" % averageChange)
    print ("Greatest Increase in Revenue: " + greatestIncreaseMonth + " ($" + str(greatestIncrease) + ")")
    print ("Greatest Decrease in Revenue: " + greatestDecreaseMonth + " ($" + str(greatestDecrease) + ")")

    ##################################################
    #  Output printed to a file
    ###################################################
    with open(outputFile, "w+") as f:
        f.write("---------------------------------------------\n")
        f.write("Financial Analysis for: " + fileName + "\n")
        f.write("---------------------------------------------\n")
        f.write ("Total Months: " + str(len(months)) + "\n")
        f.write ("Total Revenue: $" + str(totalRevenue) + "\n")
        f.write ("Average Revenue Change: $%.2f" % averageChange + "\n")
        f.write ("Greatest Increase in Revenue: " + greatestIncreaseMonth + " ($" + str(greatestIncrease) + ")" + "\n")
        f.write ("Greatest Decrease in Revenue: " + greatestDecreaseMonth + " ($" + str(greatestDecrease) + ")" + "\n")

    
