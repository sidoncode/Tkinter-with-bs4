import csv
import os
import sys



import tkinter as tk
import math 
import tkinter.dialog
import tkinter.messagebox


#def search_for_the_key():
    
    #algo for the Scrap_data from the csv file 

####



def main_window():
    window = tk.Tk()
    window.title("The main title of the window")
    window.geometry("400x350")

    title = tk.Label(text = "", )
    title.grid()

    button1 = tk.Button(text="Search for the key",)#command ::lambda = search_for_the_key())
    button1.grid(row= 0, column =1 )


    EntryField = tk.Entry()
    EntryField.grid(row= 0, column =0 )

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