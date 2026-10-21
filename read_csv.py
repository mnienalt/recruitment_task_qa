import pandas as pd
from prettytable import from_csv, PrettyTable

from helpers import (calculate_number_of_shares, calculate_number_of_shares_to_buy, calculate_number_of_shares_to_sell,
                     calculate_current_value_of_shares, calculate_plan_value, sum_numbers, tot_val,calc_output_number)

pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 20)
pd.set_option('display.max_colwidth', None)

asset_value = 100000
input_file="input.csv"
output_file="output.csv"

# Open the CSV file and pass the file object directly to PrettyTable
with open(input_file, "r", encoding="utf-8") as fp:
    mytable = from_csv(fp)

# Print the formatted table to the console

print(f'Presenting input file: {input_file}')
print(mytable)
df = pd.read_csv("input.csv")

#


df['current_number_of_shares'] = calculate_number_of_shares(df['current[%]'], asset_value, df['unit price'])
df['current_value_of_shares'] = calculate_current_value_of_shares(df['current_number_of_shares'], df['unit price'])
df['planned_number_of_shares_to_buy'] = calculate_number_of_shares_to_buy(df['target variance [%]'], df['unit price'])
df['planned_number_of_shares_to_sell'] = calculate_number_of_shares_to_sell(df['target variance [%]'], df['unit price'])
df['planned_value_of_shares_to_be_acquired_or_sold'] = calculate_plan_value(df['planned_number_of_shares_to_buy'],
                                                                            df['planned_number_of_shares_to_sell'],
                                                                            df['unit price'])
df['total_number_of_shares_after_acuired_or_sold'] = sum_numbers(df['current_number_of_shares'],
                                                                 df['planned_number_of_shares_to_buy'],
                                                                 df['planned_number_of_shares_to_sell'])
df['total_value_of_shares_after_acuired_or_sold'] = tot_val(df['current_value_of_shares'],
                                                            df['planned_value_of_shares_to_be_acquired_or_sold'],
                                                            df['target variance [%]'])
# df['planned_number_of_shares_to_sell']

df['outpout number of shres to buy/sell']=calc_output_number(df['planned_number_of_shares_to_buy'],df['planned_number_of_shares_to_sell'])

df = df.fillna('')
df.to_csv('output.csv', index=False)

table = PrettyTable()
table.field_names = df.columns.tolist()


table.add_rows(df.values.tolist())


print(f'Presenting output file - additional columns added: {output_file}')
print(table)


