import csv

filename = 'C:/Users/cdonnelly.EFCLOCAL/Desktop/Bootcamp/python-challenge/PyPoll/Resources/election_data.csv'

totalVotes = 0
cand_d = {}
with open(filename, 'r') as file:
    reader = csv.reader(file)
    # Store header row
    header = next(reader)
    for row in reader:
        # header row should not count towards votes
        if row != header:
            totalVotes += 1
            # Get unique candidates name
            # Note: this could also be done using 2 lists
            if row[2] not in cand_d:
                cand_d.update({row[2] : 0})
            # Increment candidate vote count by 1
            val = cand_d.get(row[2])
            val += 1
            cand_d.update({row[2] : val})


# Print Results to terminal
print("Election Results \n_________________________________________________________ \n")
print("\nTotal Votes: " + str(totalVotes) + "\n_________________________________________________________ \n")
# Loop through candidate keys and print voter results
for key in cand_d:
    print(key + " (" + str(cand_d.get(key)) + ")\n")