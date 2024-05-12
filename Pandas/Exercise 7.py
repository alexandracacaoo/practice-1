import pandas as pd

DataFrame = pd.read_csv ( "/mnt/c/Users/user/Downloads/table1Trimmed.csv")
print(DataFrame ['Species'].value_counts())