#import necessary modules
import os
import csv

#set input path
election_csv = os.path.join('Resources', 'election_data.csv')

#open stream for election_csv
with open(election_csv, 'r') as election_data:
    #tell python how to read file
    csvreader = csv.reader(election_data, delimiter=',')
    #get header of the csv
    csvheader = next(csvreader)
    print(csvheader)

    vote_dict = {}
    total_votes = 0
    for row in election_data:
        #tally up votes for each unique candidate
        if row[2] in vote_dict:
            total_votes += 1
            vote_dict[row[2]] += 1
        else:
            total_votes += 1
            vote_dict[row[2]] = 1
    print(vote_dict)

    percentages = {}
    for candidate in vote_dict:
        percentages[candidate] = vote_dict[candidate] / total_votes

    print('')
    print('Election Results')
    print('-------------------------')
    print(f"Total Votes: {total_votes}")
    print('-------------------------')
    for keys in vote_dict:
        print(f"{keys}: {percentages}")