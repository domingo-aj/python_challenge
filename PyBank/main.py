import os
import csv

budgetcsv = os.path.join('Resources', 'budget_data.csv')
findata = open(budgetcsv)
output_path = os.path.join('Analysis', 'analysis.txt')

with findata as fin:
    finread = csv.reader(fin, delimiter=',')

    headerline = next(fin)

    total = 0
    months = len(list(fin))
    
    for row in finread:
        total += int(row[1])

    avgchange = (total/months)
    
    print("Financial Analysis")
    print("---------------------")
    print(f"Total Months: {months}")
    print(f"Total: ${total}")
    print(f"Average Change: ${avgchange}")
    print(f"Greatest Increase in Profits: {greatdate} ({greatnum})")
    print(f"Greatest Decrease in Profits: {baddate} ({badnum})")



