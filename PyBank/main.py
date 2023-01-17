#import necessary modules
import os
import csv

#set the path that is needed
budget_csv = os.path.join("Resources", "budget_data.csv")

#open stream for budget_csv
with open(budget_csv, 'r') as budget_data:
    #tell python how to read a csv using the csv module
    csvreader = csv.reader(budget_data, delimiter=',')
    #get the header of the csv
    csvheader = next(csvreader)
    print(csvheader)
    
    months = 0
    revenue = 0
    profit_loss = []
    j = 0
    max_change = 0
    max_date = None
    min_change = 0
    min_date = None
    for row in csvreader:
        #number of months = number of rows, so calculate that using an iterator
        months += 1
        #tally up revenue from the second column in each row
        revenue += int(row[1])
        #append the change from last row to current row to a list then update last row
        profit_loss.append(int(row[1]) - int(j))
        if (int(row[1]) - int(j)) > int(max_change):
            max_date = row[0]
            max_change = row[1]
        elif (int(row[1]) - int(j)) < int(min_change):
            min_date = row[0]
            min_change = row[1]
        j = row[1]
    
    #total all changes
    total_change = sum(profit_loss)
    
    #find the average change
    avg_change = total_change / months

    print(months)
    print(revenue)
    print(avg_change)
    print(max_date)
    print(max_change)
    print(min_date)
    print(min_change)