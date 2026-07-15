# Excel sheet Generator
#
# Addy wrote version
# 
# given an output filename and location
# importing LinkObject
# and passed an array of sorted linkObjs from LinkSorter
# creates csv (or xlsx?) file with columns containing the broken links
# and their corresponding source pages
#
# References:
# https://docs.python.org/3/library/csv.html
# https://www.geeksforgeeks.org/python/python-save-list-to-csv/
# 
# we import like this so we dont have to type
# LinkObject.LinkObject() to create a link object
from LinkObject import LinkObject
import csv
import tkinter as tk
from tkinter.filedialog import asksaveasfilename

# function that is called by GUI file
# input: array of LinkObjects, filename (default: "brokenlinks.csv"), TODO: later add file location
# output: no return value, but creates a .csv file of filename
def ExcelsheetGenerator (links=LinkObject(None, None), outputFilename="brokenlinks.csv"):
    # define column headers
    colHead = ["Broken Link", "Source Page"]
    # user defines output filename
    file_path = asksaveasfilename(
        defaultextension=".csv",
        filetypes=[("CSV Files","*.csv"),]
    )
    if file_path:
        #if user defined filename correctly
        outputFilename = file_path
        with open(file_path, 'w', newline='') as f:
            writer = csv.writer(f)
            # Writer Header row
            writer.writerow(colHead)
            # loop thru links adding the info to the csv
            for i in links:
                writer.writerow([i.target_link, i.source_link])
    else:
        # default is brokenlinks.csv 
        with open(outputFilename, 'w', newline='') as f:
            writer = csv.writer(f)
            # Writer Header row
            writer.writerow(colHead)
            # loop thru links adding the info to the csv
            for i in links:
                writer.writerow([i.target_link, i.source_link])
    return outputFilename

# Example of how to create LinkObject and generate spreadsheet from array of them
# testLink_a = LinkObject('https://www.images.google.com', 'https://www.google.com')
# testLink_b = LinkObject('https://www.youtube.com/5', 'https://www.youtube.com/5746443534')
# testLink_array = [testLink_a, testLink_b]
# ExcelsheetGenerator(testLink_array, 'testfile_00.csv')
#
# Addy confirms this works on 10/17/2025 @ 2:42PM