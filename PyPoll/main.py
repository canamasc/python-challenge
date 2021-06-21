import csv

filename = 'C:/Users/cdonnelly.EFCLOCAL/Desktop/Bootcamp/python-challenge/PyPoll/Resources/election_data.csv'

totalVotes = 0

with open(filename, 'r') as file:
    reader = csv.reader(file)
    # Store header row
    header = next(reader)
    for row in reader:
        if row != header:
            totalVotes += 1

# Print Results to terminal
print("Election Results \n_________________________________________________________ \n")
print("\nTotal Votes: " + str(totalVotes) + "\n_________________________________________________________ \n")
