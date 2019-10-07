import os
import sys
import csv
def pe_ratio():
    obj = float(input("enter the value of the pe pe_ratio"))
    with open('NIFTY50all28-08-2018-TO-27-08-2019.csv','rb') as File:
        reader = csv.reader(File, delimiter=',', quotechar=',',quoting=csv.QUOTE_MINIMAL)
        for row in reader:
            if obj == row[1]:
                print(row)
pe_ratio()