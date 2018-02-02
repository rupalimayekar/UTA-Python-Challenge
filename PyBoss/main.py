#################################################################################
# This is the main script for the PyBoss Assignment
# The script reads two employee files and converts the data in the two files
# into the new employee data format and wites the new employee data into 
# a single output csv file
#################################################################################

import csv
import os
import datetime
import us_state_abbrev as st

#################################################################################
# This function takes in a list of employee information in a specific order and
# it creates a list of Employee information with the following changes:
# 1 - The employee name is split into first and last names as two separate values
# 2 - The employee DOB format is changed to DD/MM/YYYY
# 3 - The first 5 digits of the SSN is replaced with asterisks
# 4 - The state name is changed to state abbreviation
# The function then returns the list of the modified employee info
#################################################################################
def createEmpInfo(emp):
    empInfo = [ emp[0],
                emp[1].split(" ")[0],
                emp[1].split(" ")[1],
                datetime.datetime.strptime(emp[2], '%Y-%m-%d').strftime('%d/%m/%Y'),
                "***-**-" + emp[3].split("-")[2],
                st.us_state_abbrev[emp[4]]
    ]
    return empInfo

#################################################################################
# This function takes in a csv file writer object and a  filename for the file
# from which to read the employee data. It reads the emp data and writes into
# the output file for which the file writer object is passed in
#################################################################################
def writeEmployeeData(writeFile, readFileName):
    # Open the employee file and read the data for processing
    with open(readFileName, newline='') as empFile:

        # create the reader for the employee file
        csvReader = csv.reader(empFile, delimiter=',')

        #loop through all the rows of the employee file
        for csvRow in csvReader:

            # process the employee info if this is not the header row
            if csvRow[0] != "Emp ID":
                writeFile.writerow(createEmpInfo(csvRow))

#################################################################################
# Begin main body of script
#################################################################################

# create the paths for the two input files and one output file
empFilename1 = os.path.join("raw_data", "employee_data1.csv")
empFilename2 = os.path.join("raw_data", "employee_data2.csv")
outFilename = os.path.join("raw_data", "new_employee_data.csv")

#open the output file for writing
with open(outFilename, "w", newline='') as outFile:
    csvwriter = csv.writer(outFile, delimiter=",")

    # Write the header row into the output file
    csvwriter.writerow(["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State"])

    # Write the employee info from the first employee file into the output file
    writeEmployeeData(csvwriter, empFilename1)

    # Write the employee info from the second employee file into the output file
    writeEmployeeData(csvwriter, empFilename2)

#################################################################################
# End of main body of script
#################################################################################
