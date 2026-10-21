from prettytable import from_csv
import pandas as pd

# Open the CSV file and pass the file object directly to PrettyTable
with open("input.csv", "r", encoding="utf-8") as fp:
    mytable = from_csv(fp)

# Print the formatted table to the console
print(mytable)
df=pd.read_csv("input.csv")

from pdb import set_trace
set_trace()

