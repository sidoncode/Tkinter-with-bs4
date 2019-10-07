import csv
import os
import sys

with open("C:\\Users\\Sidd\\Desktop\\wescrap\\Tkinter With Bs4\\Tkinter-with-bs4\\test.csv","rt") as f:
  #data = csv.reader(f)
  data = csv.DictReader(f)
  rownumber = 1
  key = float(input("Enter the key for performing the search\n"))
  for row in data:
        if(float(row["P/B"] ) == float(key)):
            print("found....row id : " + str(rownumber))
        if(float(row["P/E"] )== float(key)):
            print("Found... row id : " + str(rownumber))
        if(float(row["Date"] ) == float(key)):
            print("Found... row id : " + str(rownumber))
        if(float(row["Div Yield"]) == float(key)):
            print("Found... row id: " + str(rownumber))
        rownumber = rownumber + 1
        #print(row["Date"] + "###" + row["P/E"] + "###" + row["P/B"] )
