import os
import csv

Pybank_csv = os.path.join("Resources", "budget_data.csv")
PyBank_output = os.path.join("Analysis", "budget_analysis.txt")

with open(Pybank_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")

    next(csv_reader)   

    all_rows = list(csv_reader)
    output1 = (
    f"Financial Analysis \n"
    f"----------------------------------------- \n"
    f"Total Months: {len(all_rows)} \n")
    print(output1)
    
    Net_total = 0

    for row in all_rows:
        num = int(row[1])
        Net_total += num

    output2 = (f"Total: ${Net_total} \n")
    print(output2)

    dif_list = []
    for i in range(85):
        dif_list.append(int(all_rows[i+1][1])- int(all_rows[i][1]))
    
    Net_change = 0

    for Change in dif_list:
        Number = int(Change)
        Net_change += Number

    Average_change = round((Net_change/85),2)
    output3 = (f"Total change: ${Average_change} \n")
    print(output3)

    Max_list = dif_list[0]
    for i in range(85):
        if int(dif_list[i]) > int(Max_list):
            Max_list= dif_list[i]

    index_max= dif_list.index(Max_list)

    Max_date = all_rows[int(index_max)+1]
    output4 = (f"Greatest Increase in Profits: {Max_date[0]} (${Max_list}) \n")
    print(output4)

    Min_list = dif_list[0]
    for i in range(85):
        if int(dif_list[i]) < int(Min_list):
            Min_list= dif_list[i]

    index_min= dif_list.index(Min_list)

    Min_date = all_rows[int(index_min)+1]
    output5 = (f"Greatest Decrease in Profits: {Min_date[0]} (${Min_list}) \n")
    print(output5)
    

with open(PyBank_output, "w") as txt_file:
    txt_file.write(output1)
    txt_file.write(output2)
    txt_file.write(output3)
    txt_file.write(output4)
    txt_file.write(output5)

       


