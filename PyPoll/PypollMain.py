#create file path across operating systems
import os
#Module for reading csv files
import csv
csvpath=os.path.join("Resources","election_data.csv")

#Declaration of Variables
Number_of_votes=0
Charles_votes=0
Diana_votes=0
Raymon_votes=0

with open(csvpath) as pypoll_file:
#CSV reader specifies delimiter and variable that holds contents
    pypoll_rows=csv.reader(pypoll_file,delimiter=",")
#skip header row 
    next(pypoll_rows)

#iterate through each row
    for row in pypoll_rows:
#count and store the Candidate's name in variable Number_of_votes
        Number_of_votes+=1

        if row[2]== "Charles Casper Stockham":
            Charles_votes+=1
        elif row[2]=="Raymon Anthony Doane":
            Raymon_votes+=1
        elif row[2]== "Diana DeGette":
            Diana_votes+=1
       
#Create dictionary of the two lists we previosuly made IOT find the winner
candi_votes=[Charles_votes,Diana_votes,Raymon_votes]
candi_names=["Charles Casper Stockhom","Diana DeGette","Raymon Anthony Doane"]

dict_candi_votes_and_candi_names=dict(zip(candi_names,candi_votes))
#will determine winner with most votes using the max function 
key=max(dict_candi_votes_and_candi_names,key=dict_candi_votes_and_candi_names.get)

#Carlculations of percentage of votes each candidate received
Charles_percent=(Charles_votes/Number_of_votes)*100
Diana_percent=(Diana_votes/Number_of_votes)*100
Raymon_percent=(Raymon_votes/Number_of_votes)*100

#Print summary table
print(f"Election Results")
print(f"-------------------------")
print(f"Total Votes: {Number_of_votes}")
print(f"--------------------------")
print(f"Charles Casper Stockham: {Charles_percent:.3f}% ({Charles_votes})")
print(f"Diana DeGette: {Diana_percent:.3f}% ({Diana_votes})")
print(f"Raymon Anthony Doane: {Raymon_percent:.3f}% ({Raymon_votes})")
print(f"------------------------------")
print(f"Winner: {key}")
print(f"------------------------------")