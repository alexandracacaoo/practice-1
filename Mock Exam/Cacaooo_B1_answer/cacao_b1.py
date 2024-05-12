import pandas as pd 

def read_csv():
    with open("/mnt/c/Users/User/Downloads/Exam_Table.csv" , "r" ) as file:
        list = file.readlines()
        return list
    
def write_file(interval):
    with open("./b1_outputt.csv", "w", ) as file:
        file.writelines(interval)

table = read_csv()
interval = []

for i in range (0, 60):
    table [i] = table[i].split(",")
    if i == 0:
        interval.append(table[i])
for j in range (0, 12):
        if j ==7:
             if [i][j] == "30-0":
                print (interval)

