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
    for row in csvreader:
        #tally up votes for each unique candidate
        if row[2] in vote_dict:
            total_votes += 1
            vote_dict[str(row[2])] += 1
        else:
            total_votes += 1
            vote_dict[str(row[2])] = 1
    print(vote_dict)

    #calculate the percentage vote each candidate accumulated and add to new dict
    percentages = {}
    for candidate in vote_dict:
        percentages[candidate] = round(vote_dict[candidate] / total_votes * 100, 3)

    #print results
    print('')
    print('Election Results')
    print('-------------------------')
    print(f'Total Votes: {total_votes}')
    print('-------------------------')
    #for each candidate, print the percentage vote and total vote in parenthesis
    for keys in vote_dict:
        print(f'{keys}: {percentages[keys]}% ({vote_dict[keys]})')
    print('-------------------------')
    #print key with most accumulated votes (code from: https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary)
    print(f'Winner: {max(vote_dict, key=vote_dict.get)}')
    print('-------------------------')
    print('')

#open output file stream
output = os.path.join('analysis', 'Election Results.txt')
with open(output, 'w') as text:
    #print results to text file in same method as the print statements above
    text.write('Election Results\n')
    text.write('-------------------------\n')
    text.write(f'Total Votes: {total_votes}\n')
    text.write('-------------------------\n')
    for keys in vote_dict:
        text.write(f'{keys}: {percentages[keys]}% ({vote_dict[keys]})\n')
    text.write('-------------------------\n')
    text.write(f'Winner: {max(vote_dict, key=vote_dict.get)}\n')
    text.write('-------------------------\n')
    