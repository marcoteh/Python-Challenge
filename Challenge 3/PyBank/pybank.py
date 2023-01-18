#import dependencies
import os
import csv

#csv path
direct_path = os.path.dirname(__file__)
relative_path = "Resources/budget_data.csv"
csvpath = os.path.join(direct_path, relative_path)

#open csv and read file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)
    csv_header = next(csvreader)

    #for row in csvreader:
        #print(row)

  # months
    data = list(csvreader)
    row_count = len(data)

  # Profit/Losses
    total = 0
    for i in range(0, row_count): 
        total = total + int(data[i][1]) 

  # Averages   
    num1 = 0
    num2 = int(data[0][1])
    diff = 0
    difflist = list()
    for j in range(1, row_count):
        num1 = int(data[j][1])
        diff = num1 - num2
        difflist.append(diff)
        num2 = int(data[j][1])
    avgChange = round(sum(difflist)/len(difflist),2)

  # greatest increase
    maxDiff = max(difflist)
    maxDiffPos = difflist.index(maxDiff)+1
    
  # greatest decrease
    minDiff = min(difflist)
    minDiffPos = difflist.index(minDiff)+1

  #Display results
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {row_count}")
    print(f"Total: ${total:,}")
    print(f"Average Change: ${avgChange:,}")
    print(f"Greatest Increase in Profits: {data[maxDiffPos][0]} (${maxDiff:,})")
    print(f"Greatest Decrease in Profits: {data[minDiffPos][0]} (${minDiff:,})")

#Export to readfile
    exportName = os.path.join(direct_path, "Analysis", "Results.txt")
    with open(exportName, "w") as f:
        f.write("Financial Analysis\n")
        f.write("----------------------------\n")
        f.write(f"Total Months: {row_count:,}\n")
        f.write(f"Total: ${total:,}\n")
        f.write(f"Average Change: ${avgChange:,}\n")
        f.write(f"Greatest Increase in Profits: {data[maxDiffPos][0]} (${maxDiff:,}\n")
        f.write(f"Greatest Decrease in Profits: {data[minDiffPos][0]} (${minDiff:,}\n")
