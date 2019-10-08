#!/usr/bin/python


import csv
import os
import sys



'''
import math                         
import lambda
import DictReader
'''


import tkinter as tk
import tkinter.dialog
import tkinter.messagebox


def search_for_the_key():
    print("The search_for_the_key function has been executed")
    if EntryField1.get() == "sid":
        print("The if statement has been executed")
    if var == "sid":
        print("the 2nd if statement has been executed")
    #algo for the Scrap_data from the csv file 


#the entry field will be the key for the data parsing of the csv file 



def main_window():
    def stmnt():
        if EntryField1.get() == "sid":
            print("The stmnt function has been executed")
    
    window = tk.Tk()
    window.title("CSV reader")
    window.geometry("400x350")

    title = tk.Label(text = "", )
    title.grid()

    button1 = tk.Button(text="Search for the key",command = lambda : stmnt())
    button1.grid(row= 0, column =1 )


    EntryField1 = tk.Entry()
    EntryField1.grid(row= 0, column =0 )

    if EntryField1.get() == "sid":
        print("the .get() function has been succesfully executed")
  
    

    window.mainloop() #for the tkinter algo execution 



main_window();




'''def Scrap_data():
    with open("C:\\Users\\Sidd\\Desktop\\wescrap\\Tkinter With Bs4\\Tkinter-with-bs4\\test.csv","rt") as f:
    #data = csv.reader(f)
        data = csv.DictReader(f)
        rownumber = 1
        key = float(input("Enter the key for performing the search\n"))
        for row in data:
                if(float(row["P/B"] ) == float(key)):
                    print("found....row id : " + str(rownumber))
                elif(float(row["P/E"] )== float(key)):
                    print("Found... row id : " + str(rownumber))
                elif(str(row["Date"] ) == float(key)):
                    print("Found... row id : " + str(rownumber))
                elif(float(row["Div Yield"]) == float(key)):
                    print("Found... row id: " + str(rownumber))
                rownumber = rownumber + 1
                #print(row["Date"] + "###" + row["P/E"] + "###" + row["P/B"] )
'''