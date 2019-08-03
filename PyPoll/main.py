import os
import csv
import sys

#Creating the output file
output_file = open('Election Output', 'w', newline='')

#Declaring variables, lists, dictionaries
vote_total = 0
candidates = {}
share = []
winner = ""
threshold = 0

#Opening the source file
csvpath = os.path.join('election_data.csv')

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csv_header = next(csvreader)
    
#Calculating Votes, Total Unique Candidates, and Assigning Values
    for row in csvreader:
        vote_total = vote_total + 1
        
        candidate_name = row[2]
        if candidate_name in candidates:
            candidates[candidate_name] += 1
        else:
            candidates[candidate_name] = 1


#Printing the outputs in both the Terminal and the Output File
    print("Election Results")
    output_file.write("Election Results")
    output_file.write(os.linesep)
    print("---------------------")
    output_file.write("---------------------")
    output_file.write(os.linesep)
    print("Total Votes: " + str(vote_total))
    output_file.write("Total Votes: " + str(vote_total))
    output_file.write(os.linesep)
    print("---------------------")
    output_file.write("---------------------")
    output_file.write(os.linesep)

#Calculating percentage of votes and determining the winner
    for x in candidates:
        share = candidates[x] / vote_total
        print(x + ": " + str("{:.2%}".format(share)) + " (" + str(candidates[x]) + ")")
        output_file.write(x + ": " + str("{:.2%}".format(share)) + " (" + str(candidates[x]) + ")")
        output_file.write(os.linesep)
     
        if candidates[x] > threshold:
            threshold = candidates[x]
            winner = x 


#Printing remaining outputs        
print("---------------------")  
output_file.write("---------------------")
output_file.write(os.linesep)     
print("Winner: " + winner)
output_file.write("Winner: " + winner)
output_file.write(os.linesep) 
print("---------------------")
output_file.write("---------------------")  

output_file.close()



    
