#create file path across operating systems
import os
#Module for reading csv files
import csv
csvpath=os.path.join("Resources","budget_data.csv")
#Declaration of Variables
date=[]
months=[]
year=[]
profit_losses=[]
total_months=[]
profit_changes=[]
total_profit=[]



#with open(csvpath) as csvfile:
with open(csvpath) as csvfile:
#CSV reader specifies delimiter and variable that holds contents
    csvreader=csv.reader(csvfile,delimiter=",")
    print(csvreader)
#read header row first
    csv_header=next(csvreader)
    #next(csvreader)
    print(f"CSV Header: {csv_header}")
    for row in csvreader:
        date.append(row[0])
#split date into months and years
        split_date= row[0].split("-")
        months.append(split_date[0])
        year.append(split_date[1])
#create list of just profit/losses    
        profit_losses.append(row[1])

       
    #print(len(months))
    print(f"Total Months: {len(months)}")
    #print(profit_losses)
    total_profit=(int(x)for x in profit_losses)
    total_profit_sum=sum(total_profit)
    total_profit_average= total_profit_sum/len(profit_losses)

   #print(total_profit_sum)
    print(f"Total: ${total_profit_sum}")
    print(f"Average Change: ${total_profit_average}")


