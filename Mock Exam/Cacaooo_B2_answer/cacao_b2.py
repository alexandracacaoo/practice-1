import pandas as pd 

def read_csv():
    with open("/mnt/c/Users/user/Downloads/Exam_Table.csv", "r", ) as file:
        rows = file.readlines ()
        return rows
    
def write_file(interval):
    with open("./b1_outputt.csv", "w", ) as file:
        file.writelines(interval)

table = read_csv()
interval = []