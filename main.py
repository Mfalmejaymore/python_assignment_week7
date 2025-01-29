print("starting the assignment")

# for personalisation of the final output ;)
gen = input("what's your gender (M/F)? ")
if(gen == "m" or gen == "M"):
    prefix = "sir"
else:
    prefix = "madam"

import pandas as pd
import matplotlib.pyplot as plt

# load dataset and do basic data cleaning
default_values = {'Name' : 'Anonymous','Age' : 0,'Shares (thousands)' : 0,'Nationality' : 'unknown','Gender' : 'NA'}
df = pd.read_csv('ware_industries_shareholders.csv').fillna(default_values)
record_count = df.shape[0]

df['Age'].astype(int)
df['Shares (thousands)'].astype(int)



print(df.head(5))
print(f"\n showing 5 of {record_count} records")
print("\n--------------------------------\n")

# sort based on shares
print("The top 5 shareholders\n")
df_sorted = df.sort_values(by="Shares (thousands)",ascending=False)
print(df_sorted.head(5))
print(f"\n showing 5 of {record_count} records")
print("\n--------------------------------\n")

# show all records
showcon = input("would you like to only see the sorted records? (Y/N) ")

if(showcon == "y" or showcon == "Y"):
    print("showing all sorted records\n")
    print(df_sorted)
else:
    print("showing all records\n")
    print(df)

print("\n--------------------------------\n")

# summarise stuff
print("\nShowing summaries for Age and Shares\n")
data_summary = df.describe()
print(data_summary)
print("\n--------------------------------\n")

# group the data in the dataset
print("\nShowing average shares per nationality\n")
df_grouped = df.groupby(by='Nationality')['Shares (thousands)'].mean()
print(df_grouped)
print("\n--------------------------------\n")

# group the data in the dataset
print("\nShowing average shares per gender\n")
df_grouped = df.groupby(by='gender')['Shares (thousands)'].mean()
print(df_grouped)
print("\n--------------------------------\n")

# data analysis findings
mean_Age = df["Age"].mean()
mean_Shares = df["Shares (thousands)"].mean()
common_nat = df["Nationality"].mode()
common_gender = df['gender'].mode()

if(common_gender[0] == "Male"):
    verdict = "less"
else:
    verdict = "more"

print("data analysis results\n")
print(f"Most shareholders are {common_nat[0]}")
print(f"There are {verdict} Women than men")
print(f"\nmean shares : {mean_Shares}\nAverage Age : {mean_Age}\nMost common Nationality : {common_nat[0]}")

# data visualisation
# line graph showing ages distribution
plt.plot(df['Name'],df['Age'],scalex=True)
plt.title = "Age distribution"
plt.show()

# bar graph showing shares distribution
df_sorted.groupby('Name')['Shares (thousands)'].mean().plot(kind='bar')
plt.xlabel = "name"
plt.ylabel = "Shares"
plt.title = "Shares per holder"
plt.show()

# histogram for age distribution
df['Age'].plot(kind='hist', bins=10)
plt.title = "Ages"
plt.show()

# scatter for shares distribution
df.plot(kind='scatter',x='Shares (thousands)',y="Name")
plt.title = "Shares scatter chart"
plt.show()

# and we're done
print(f"\nData analysis assignment cmplete, Have a good day {prefix} :)\n")