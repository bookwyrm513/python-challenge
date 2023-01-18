#import necessary modules
import os
import csv

#set the path that is needed
budget_csv = os.path.join('Resources', 'budget_data.csv')

#open stream for budget_csv
with open(budget_csv, 'r') as budget_data:
    #tell python how to read a csv using the csv module
    csvreader = csv.reader(budget_data, delimiter=',')
    #get the header of the csv
    csvheader = next(csvreader)
    
    months = 0
    revenue = 0
    total_change = 0
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
        change = int(row[1]) - int(j)
        #tally total change as well
        total_change += change
        if change > int(max_change):
            max_date = row[0]
            max_change = change
        elif change < int(min_change):
            min_date = row[0]
            min_change = change
        j = row[1]
    
    #find the average change
    avg_change = total_change / months

    #print results into command terminal
    print('')
    print('Financial Analysis')
    print('----------------------------')
    print(f'Total Months: {months}')
    print(f'Total: ${revenue}')
    print(f'Average Change: ${round(avg_change, 2)}')
    print(f'Greatest Increase in Profits: {max_date} (${max_change})')
    print(f'Greatest Decrease in Profits: {min_date} (${min_change})')
    print('')

#create and open text file to print results to in same method of print statements above
output = os.path.join('analysis', 'Financial Analysis.txt')
with open(output, 'w') as text:
    text.write('Financial Analysis\n')
    text.write('----------------------------\n')
    text.write(f'Total Months: {months}\n')
    text.write(f'Total: ${revenue}\n')
    text.write(f'Average Change: ${round(avg_change, 2)}\n')
    text.write(f'Greatest Increase in Profits: {max_date} (${max_change})\n')
    text.write(f'Greatest Decrease in Profits: {min_date} (${min_change})\n')
