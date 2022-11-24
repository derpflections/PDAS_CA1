import numpy as np 
import matplotlib as mpl
counter = 0 

secondaryData = np.genfromtxt('PDAS CA1 Files\PDAS_CA1\sourcefiles\enrolment-secondary-by-level-and-course.csv', delimiter = ',', skip_header = 1, dtype = [('year','i8'),('level','U255'),('course','U255'),('gender','U255'),('enrolment','i8')])

#print(f"**Analysis of course intake and enrolment for secondary schools**")
#print(f"There are {len(secondaryData)} rows and {len(secondaryData[1])} columns in this dataset\n")
#
#print(f"The names and datatypes of these columns are: ")
#print(f"- {secondaryData.dtype.names[0]} {type(secondaryData['year'][1])}, isnumeric = {np.issubdtype(type(secondaryData['year'][1]), np.number)}")
#print(f"- {secondaryData.dtype.names[1]} {type(secondaryData['level'][1])}, isnumeric = {np.issubdtype(type(secondaryData['level'][1]), np.number)}")
#print(f"- {secondaryData.dtype.names[2]} {type(secondaryData['course'][1])}, isnumeric = {np.issubdtype(type(secondaryData['course'][1]), np.number)}")
#print(f"- {secondaryData.dtype.names[3]} {type(secondaryData['gender'][1])}, isnumeric = {np.issubdtype(type(secondaryData['gender'][1]), np.number)}")
#print(f"- {secondaryData.dtype.names[4]} {type(secondaryData['enrolment'][1])}, isnumeric = {np.issubdtype(type(secondaryData['enrolment'][1]), np.number)}\n")
#
#print(f"There are {len(np.unique(secondaryData['year']))} unique values in the column \"{secondaryData.dtype.names[0]}\"")
#print(f"There are {len(np.unique(secondaryData['level']))} unique values in the column \"{secondaryData.dtype.names[1]}\"")
#print(f"There are {len(np.unique(secondaryData['course']))} unique values in the column \"{secondaryData.dtype.names[2]}\"")
#print(f"There are {len(np.unique(secondaryData['gender']))} unique values in the column \"{secondaryData.dtype.names[3]}\"")
#print(f"There are {len(np.unique(secondaryData['enrolment']))} unique values in the column \"{secondaryData.dtype.names[4]}\"")

counter = 0
for i in secondaryData[1]:
    print(f"- {secondaryData.dtype.names[counter]} {type(secondaryData[secondaryData.dtype.names[counter]][1])}, isnumeric = {np.issubdtype(type(secondaryData[secondaryData.dtype.names[counter]][1]), np.number)}")
    counter += 1

counter = 0 
for i in secondaryData[1]:
    print(f"There are {len(np.unique(secondaryData[secondaryData.dtype.names[counter]]))} unique values in the column \"{secondaryData.dtype.names[counter]}\"")
    counter += 1