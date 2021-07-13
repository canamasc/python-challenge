import csv
import os
#filename = 'C:/Users/cdonnelly.EFCLOCAL/Desktop/Bootcamp/python-challenge/PyPoll/Resources/election_data.csv'
filename = os.path.join('Resources', 'election_data.csv')
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

# Once we have total vote counts, get % of total vote for each candidate
# % calc only needs total votes and cand_d values, so can compute this in print statement

# Print Results to terminal
print("Election Results \n_________________________________________________________ \n")
print("Total Votes: " + str(totalVotes) + "\n_________________________________________________________ \n")
# Loop through candidate keys and print voter results
# for % calc, we are formatting so the result is printed to 3 decimal places. Cast to string so it can print in same line
for key in cand_d:
    print(key + ": " + str("{:.3f}".format(100*cand_d.get(key)/totalVotes)) + "% (" + str(cand_d.get(key)) + ")\n")
print("_________________________________________________________")
# Get key with max value in dicitonary
# https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
print("\nWinner: " + max(cand_d, key=cand_d.get))
print("_________________________________________________________")


# Write  analysis text file
# Logic/syntax is identical to above segment, where we print to terminal
#anal = open("C:/Users/cdonnelly.EFCLOCAL/Desktop/Bootcamp/python-challenge/PyPoll/analysis/election_results.txt", "w")
anal = open("analysis/election_results.txt", "w")
anal.write("Election Results \n_________________________________________________________ \n")
anal.write("\nTotal Votes: " + str(totalVotes) + "\n_________________________________________________________ \n")
for key in cand_d:
    anal.write(key + ": " + str("{:.3f}".format(100*cand_d.get(key)/totalVotes)) + "% (" + str(cand_d.get(key)) + ")\n")
anal.write("_________________________________________________________")
anal.write("\nWinner: " + max(cand_d, key=cand_d.get))
anal.write("\n_________________________________________________________")
anal.close()