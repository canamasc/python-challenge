import csv

filename = 'C:/Users/cdonnelly.EFCLOCAL/Desktop/Bootcamp/python-challenge/PyBank/Resources/budget_data.csv'

numMonths = 0
netTotal = 0
# list of month to month changes
changes = []
changetemp = 0
avgChange = 0
# counter lets us know what row we're on
counter = 0

# max  increase in profits
maxp = 0
maxp_month = ""
# max decrease in profits
minp = 0
minp_month = ""

with open(filename, 'r') as file:
    reader = csv.reader(file)
    # Store header row
    header = next(reader)
    for row in reader:
        counter += 1
        if counter == 2:
            maxp = int(row[1])
            minp = int(row[1])
        # Ignore header row
        if counter > 1:
            numMonths += 1
            netTotal += int(row[1])
        # only start computing differences from row 3
        if counter > 2:
            changetemp = (int(row[1]) - int(prev[1]))
            changes.append(changetemp)
            # Find max increase and decrease 
            if (changetemp > maxp):
                maxp = changetemp
                maxp_month = row[0]
            if (changetemp < minp):
                minp = changetemp
                minp_month = row[0]
        # prev always points to row above
        prev = row

avgChange = round((sum(changes) / len(changes)),2)

# Write financial analysis text file
anal = open("C:/Users/cdonnelly.EFCLOCAL/Desktop/Bootcamp/python-challenge/PyBank/analysis/financial_analysis.txt", "w")
anal.write("Financial Analysis \n_________________________________________________________ \n")
anal.write("\nTotal Months: " + str(numMonths))
anal.write("\nTotal: $" + str(netTotal))
anal.write("\nAverage Change: $" + str(avgChange))
anal.write("\nGreatest Increase in Profits: "+ maxp_month + " ($" + str(maxp) + ")")
anal.write("\nGreatest Decrease in Profits: "+ minp_month + " ($" + str(minp) + ")")
anal.close()

#Print findings to terminal
print("Financial Analysis \n_________________________________________________________ \n")
print("\nTotal Months: " + str(numMonths))
print("\nTotal: $" + str(netTotal))
print("\nAverage Change: $" + str(avgChange))
print("\nGreatest Increase in Profits: "+ maxp_month + " ($" + str(maxp) + ")")
print("\nGreatest Decrease in Profits: "+ minp_month + " ($" + str(minp) + ")")