#import dependencies
import os
import csv

#csv path
direct_path = os.path.dirname(__file__)
relative_path = "Resources/election_data.csv"
csvpath = os.path.join(direct_path, relative_path)

#csvpath = os.path.join("Resources", "election_data.csv")


#open csv and read file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)
    csv_header = next(csvreader)

    #for row in csvreader:
        #print(row)

#vote data
    data = list(csvreader)
    row_count = len(data)

#candidates
    candidates = list()
    tally = list()
    for i in range (0,row_count):
        candidate = data[i][2]
        tally.append(candidate)
        if candidate not in candidates:
            candidates.append(candidate)
    can_count = len(candidates)

#votes tally
    votes = list()
    percentage = list()
    for j in range (0,can_count):
        name = candidates[j]
        votes.append(tally.count(name))
        vprct = votes[j]/row_count
        percentage.append(vprct)

#Winner
    winner = votes.index(max(votes))

#Display results
    print("Election Results")
    print("----------------------------")
    print(f"Total Votes: {row_count:,}")
    print("----------------------------")
    for k in range (0,can_count): 
        print(f"{candidates[k]}: {percentage[k]:.3%} ({votes[k]:,})")
    print("----------------------------")
    print(f"Winner: {candidates[winner]}")
    print("----------------------------")

#Export to readfile
    exportName = os.path.join(direct_path, "Analysis", "Results.txt")
    with open(exportName, "w") as f:
        f.write("Election Results\n")
        f.write("----------------------------\n")
        f.write(f"Total Votes: {row_count:,}\n")
        f.write("----------------------------\n")
        for k in range (0,can_count): 
            f.write(f"{candidates[k]}: {percentage[k]:.3%} ({votes[k]:,})\n")
        f.write("----------------------------\n")
        f.write(f"Winner: {candidates[winner]}\n")
        f.write("----------------------------\n")

    #print("Election Results", file=open("PyPoll.txt", "a"))
    #print("----------------------------", file=open("PyPoll.txt", "a"))
    #print(f"Total Votes: {row_count:,}", file=open("PyPoll.txt", "a"))
    #print("----------------------------", file=open("PyPoll.txt", "a"))
    #for k in range (0,can_count): 
        #print(f"{candidates[k]}: {percentage[k]:.3%} ({votes[k]:,})", file=open("PyPoll.txt", "a"))
    #print("----------------------------", file=open("PyPoll.txt", "a"))
    #print(f"Winner: {candidates[winner]}", file=open("PyPoll.txt", "a"))
    #print("----------------------------", file=open("PyPoll.txt", "a"))
