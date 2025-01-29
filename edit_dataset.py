# this code combines everything ive learnt and makes application of them
# i wanted to use an existing dataset but thought it better to make my own
# note that i first made it in excel before saving it to this location

import pandas as pd

def readDataset():
    df = pd.read_csv('Ware_industries_shareholders.csv')
    print(df)
    print("\n-------------------------------------------\n")

con = True
while(con):
    readDataset()

    writeit = input("do you like to add a new record (Y/N)? ")
    con = writeit == "y" or writeit == "Y"

    try:
        if(con):
            # name, age, Shares, nationalty, gender
            the_name = input("enter the name: ")
            the_age = input("enter the age: ")
            the_Shares = input("enter the Shares: ")
            the_nationalty = input("enter the nationalty: ")
            the_gender = input("enter the gender: ")

            the_line = f"\n{the_name},{the_age},{the_Shares},{the_nationalty},{the_gender}"

            thefile = open('Ware_industries_shareholders.csv','a+')

            with(thefile):
                thefile.write(the_line)
                print("written to file\n")
    except:
        print("there was an error saving your data\n")

print("\ndata written successfully")