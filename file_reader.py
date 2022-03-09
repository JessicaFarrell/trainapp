import sys
import os
import csv

'''
    Function to read in csv files and return a dictionary of their contents
    
    argument in: Name of the csv file (string)
    arugment out: Contents (Dictionary)
'''
def CSV_reader (filename):
    
    if filename == '':
        print("Please provide a filename")
    if not os.path.exists(filename):
        print("Could not find ", filename, ". Please try again.")
    else:
        with open(filename, 'r') as file:
            csv_file = csv.DictReader(file)
            contents = []
            for line in csv_file:
                contents.append(line)
            file.close()
            return contents


#print(connections_list)

