import csv

filename = 'C:/Users/cdonnelly.EFCLOCAL/Desktop/Bootcamp/python-challenge/PyBank/Resources/budget_data.csv'

numMonths = 0
netTotal = 0
changes = []
changetemp = 0
avgChange = 0
counter = 0
with open(filename, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        counter += 1
        if counter > 1:
            numMonths += 1
            netTotal += int(row[1])
        if counter > 2:
            changetemp = (int(row[1]) - int(prev[1]))
            changes.append(changetemp)
            print(changetemp)
        prev = row

avgChange = sum(changes) / len(changes)

anal = open("C:/Users/cdonnelly.EFCLOCAL/Desktop/Bootcamp/python-challenge/PyBank/analysis/financial_analysis.txt", "w")
anal.write("Financial Analysis \n_________________________________________________________ \n")
anal.write("\nTotal Months: " + str(numMonths))
anal.write("\nTotal: $" + str(netTotal))
anal.write("\nAverage Change: $" + str(avgChange))
anal.close()