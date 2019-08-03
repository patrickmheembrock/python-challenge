import os
import csv
import sys

# #Creating the output file
output_file = open('Budget Output', 'w', newline='')

#Declare Lists
Month = 0
Month_List = []
Profit_Losses = []
Change_List = []


#Open the Source File
csvpath = os.path.join('budget_data.csv')

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csv_header = next(csvreader)
    

#Running variable to track the number of months
    for row in csvreader:
        Month += 1

    #Add the the running profits to a list
        Profit_Losses.append(float(row[1]))

    #Add Changes of each month to a list
    #Ensure variable is defined
        try:
            Prev_Month
        except NameError:
            Prev_Month = None
       
       #Find List of monthly changes
       #Test whether variable is defined to be None
        if Prev_Month is None:
            change = 0
            Prev_Month = float(row[1])
        else:
            change = float(row[1]) - Prev_Month
            Change_List.append(change)
            Prev_Month = float(row[1])
            Month_List.append(row[0])
            
   #Count Total Profit/Losses
   #Average Change Each Month
    Total_Profit_Losses = sum(Profit_Losses)
    Average_Change = sum(Change_List)/(Month-1)
#Find Greatest Increase and Decrease
    Greatest_Increase = max(Change_List)
    Greatest_Decrease = min(Change_List)
    Monthly_Changes = dict(zip(Change_List,Month_List))
    Date_I = Monthly_Changes[Greatest_Increase]
    Date_D = Monthly_Changes[Greatest_Decrease]
#print(Profit_Losses)
    print("Financial Analysis")
    print("------------------------")
    print("Total Months: " + str(Month))
    print("Total Profit/Losses: " + str("${:,.2f}".format(Total_Profit_Losses)))
    print("Average Change: " + str("${:,.2f}".format(Average_Change)))
    print("Greatest Increase: " + Date_I + " with "+ str("${:,.2f}".format(Greatest_Increase)))
    print("Greatest Decrease: " + Date_D + " with "+ str("${:,.2f}".format(Greatest_Decrease)))
  

    output_file.write("Financial Analysis")
    output_file.write(os.linesep)
    output_file.write("---------------------")
    output_file.write(os.linesep) 
    output_file.write("Total Months: " + str(Month))
    output_file.write(os.linesep)  
    output_file.write("Total Profit/Losses: " + str("${:,.2f}".format(Total_Profit_Losses)))
    output_file.write(os.linesep)
    output_file.write("Average Change: " + str("${:,.2f}".format(Average_Change)))
    output_file.write(os.linesep)
    output_file.write("Greatest Increase: " + Date_I + " with "+ str("${:,.2f}".format(Greatest_Increase)))
    output_file.write(os.linesep)
    output_file.write("Greatest Decrease: " + Date_D + " with "+ str("${:,.2f}".format(Greatest_Decrease))) 
    
    
    
output_file.close()




	