import csv
with open("NIFTY50all28-08-2018-TO-27-08-2019.csv","rb") as NIFTY50:
    NIFTY50reader = csv.reader(NIFTY50)
    x = csv.reader(NIFTY50,delimiter=',',quotechar='|') #transformed from stackoverflow
    NIFTY50list = []
for row in x:
    print(x)
    '''if len(row) != 0:
        NIFTY50list = NIFTY50list + [row]
NIFTY50.close()
print(NIFTY50)
with open("NIFTY50all28-08-2018-TO-27-08-2019.csv","r") as NIFTY50:
    x = csv.reader(NIFTY50,delimiter=',',quotechar='|')
    pe = (input("Enter the pe value for the csv file"))
    NIFTY50reader = csv.reader(NIFTY50)
for row in x: 
    print(row)
'''