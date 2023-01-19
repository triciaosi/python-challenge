#Create file path across operating systems
import os
#Module for reading csv files
import csv
#creating file path
csvpath=os.path.join("Resources","budget_data.csv")
#Declaration of Variables
date=[]
months=[]
year=[]
total_months=[]
total_profit=[]
profit_losses=[]
profit_change=[]

with open(csvpath) as pybank_file:
#CSV reader specifies delimiter and variable that holds contents
    pybank_rows=csv.reader(pybank_file,delimiter=",")

#Skip header row 
    next(pybank_rows)

    for row in pybank_rows:
        date.append(row[0])
#split date into months and years
        split_date= row[0].split("-")
        months.append(split_date[0])
        year.append(split_date[1])
#create list of just profit/losses    
        profit_losses.append(int(row[1]))
# Iterate through the profits in order to get the monthly change in profits
    for x in range(len(profit_losses)-1):
        profit_change.append(profit_losses[x+1]-profit_losses[x])  

        
# Obtain the maximum and minimum of the the montly profit change list
    max_increase_value = max(profit_change)
    max_decrease_value = min(profit_change)

# Correlate maximum and minimum to the proper month using month list and index from max and min
#We use the plus 1 at the end since month associated with change is the + 1 month or next month
    maximum_increase = profit_change.index(max(profit_change)) + 1
    maximum_decrease = profit_change.index(min(profit_change)) + 1
      
    total_profit=(int(x)for x in profit_losses)
    total_profit_sum=sum(total_profit)
    total_profit_average= total_profit_sum/len(profit_losses)

#Final results   
    print("Financial Analysis")
    print("-----------------------")
    print(f"Total Months: {len(months)}")
    print(f"Total: ${total_profit_sum}")
    print(f"Average Change: ${round(sum(profit_change)/len(profit_change),2)}")
    print(f"Greatest Increase in Profits: {date[maximum_increase]} ${max_increase_value}")
    print(f"Greatest Decrease in Profits: {date[maximum_decrease]} ${max_decrease_value}")
