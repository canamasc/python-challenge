# python-challenge
Georgia Tech Data Science Bootcamp

PyBank:
- Open csv file in read only mode.
- Save header row
- Loop through all rows in csv file (excluding header)
  - for max/min profit, start by setting values to second row P/L minus first row P/L. All subsequent deltas will be compared to this one and replace it if they are      larger/smaller, respectively for max profit increase / max profit decrease. corresponding months are updated at this time as well. 

  - For each row we loop through, our count of total months increases by 1
  - netTotal is just the sum of all values in the P/L column
  - at every row, a new P/L delta is computed. In addition to comparing to existing max/min values, we also append to an ongoing list of monthly P/L deltas.
  - At the end of loop, when we have all monthly deltas saved in list, we can retrieve the average
  
 end by writing results to text file and terminal.
 
 
 PyPoll:
 - Open csv file in read only mode.
- Save header row
- Loop through all rows in csv file (excluding header)
- total votes count increases by 1 for each row
- make a dictionary for candidates' specific vote counts. every time we encounter a new candidate name, we add it as a key to the dictionary and start to keep count of his/her/their votes, starting with 0
- if candidate name already exists in dictionary cand_d, then just increment value by 1 using dictionary update method
- percent of total vote for each candidate: = dictionary value for that candidate / total votes.
- The percent is multiplied by 100 so the percentage is between 0 and 100%. 
- to match the instructions example, we format the resulting number such that it keeps trailing zeroes out to 3 decimal points

In printing results to terminal and text file, we loop through all keys in the candidate dictionary to fetch their results, including % of vote and vote count
Use max function to get key (i.e. candidate name) with max matching value (i.e. vote count)

