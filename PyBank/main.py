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

with open(filename, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        counter += 1
        # Ignore header row
        if counter > 1:
            numMonths += 1
            netTotal += int(row[1])
        # only start computing differences from row 3
        if counter > 2:
            changetemp = (int(row[1]) - int(prev[1]))
            changes.append(changetemp)
            if (changetemp > maxp):
                maxp = changetemp
                maxp_month = row[0]
            #print(changetemp)
        prev = row

avgChange = round((sum(changes) / len(changes)),2)

# Write financial analysis text file
anal = open("C:/Users/cdonnelly.EFCLOCAL/Desktop/Bootcamp/python-challenge/PyBank/analysis/financial_analysis.txt", "w")
anal.write("Financial Analysis \n_________________________________________________________ \n")
anal.write("\nTotal Months: " + str(numMonths))
anal.write("\nTotal: $" + str(netTotal))
anal.write("\nAverage Change: $" + str(avgChange))
anal.write("\nGreatest Increase in Profits: "+ maxp_month + " ($" + str(maxp) + ")")
anal.close()