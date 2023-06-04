import os
import csv

PyPoll_csv = os.path.join("Resources", "election_data.csv")
PyPoll_output = os.path.join("Analysis","election_analysis.txt")

with open(PyPoll_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter= ",")

    next(csv_reader)

    all_rows = list(csv_reader)
    Total_votes = len(all_rows)
    output1 = (
    f"Election Results \n"
    f"----------------------------------------- \n"
    f"Total Votes: {Total_votes} \n"
    f"----------------------------------------- \n")
    print(output1)

    name_list = []

    for i in range(Total_votes):
        name = (all_rows[i][2])
        name_list.append(name)

    unique_names = list(set(name_list))

    name0 = unique_names[0]
    name1 = unique_names[1]
    name2 = unique_names[2]

    num_vote0= name_list.count(name0)
    num_vote1= name_list.count(name1)
    num_vote2= name_list.count(name2)

    Percent_vote0 = round((num_vote0/Total_votes * 100),3)
    Percent_vote1 = round((num_vote1/Total_votes * 100),3)
    Percent_vote2 = round((num_vote2/Total_votes * 100),3)

    output2 = (
    f"{name1}: {Percent_vote1}% ({num_vote1}) \n"
    f"{name0}: {Percent_vote0}% ({num_vote0}) \n"
    f"{name2}: {Percent_vote2}% ({num_vote2}) \n"
    f"----------------------------------------- \n")
    print(output2)

    Vote_summary = [[name0, num_vote0], [name1, num_vote1], [name2, num_vote2]]

    winner = []
    for i in range(len(Vote_summary)-1):

        if Vote_summary[i][1] > Vote_summary[i+1][1]:
            
            Winner = Vote_summary[i][0]
        else:
            Winner = Vote_summary[i+1][0]
        
    output3 = (
    f"Winner: {Winner} \n"
    f"----------------------------------------- \n")
    print(output3)

with open(PyPoll_output, "w") as txt_file:
    txt_file.write(output1)
    txt_file.write(output2)
    txt_file.write(output3)

    
