import pandas as pd
from prettytable import from_csv, PrettyTable

from converters import (calculate_number_of_shares, calculate_number_of_shares_to_buy,
                        calculate_number_of_shares_to_sell,
                        calculate_current_value_of_shares, calculate_plan_value, sum_numbers_of_shares, total_value,
                        calc_output_number)

pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 20)
pd.set_option('display.max_colwidth', None)


class StockExchangeCalculator:
    def __init__(self):
        self.asset_value = 100000
        self.input_file = 'input.csv'
        self.output_file = 'output.csv'

    def build(self):
        with open(self.input_file, "r", encoding="utf-8") as fp:
            mytable = from_csv(fp)

        print(f'Presenting input file: {self.input_file}')
        print(mytable)
        self.df = pd.read_csv("input.csv")

    #

    def convert(self):
        self.df['current_number_of_shares'] = calculate_number_of_shares(self.df['current[%]'], self.asset_value,
                                                                         self.df['unit price'])
        self.df['current_value_of_shares'] = calculate_current_value_of_shares(self.df['current_number_of_shares'],
                                                                               self.df['unit price'])
        self.df['planned_number_of_shares_to_buy'] = calculate_number_of_shares_to_buy(self.df['target variance [%]'],
                                                                                       self.df['unit price'])
        self.df['planned_number_of_shares_to_sell'] = calculate_number_of_shares_to_sell(self.df['target variance [%]'],
                                                                                         self.df['unit price'])
        self.df['planned_value_of_shares_to_be_acquired_or_sold'] = calculate_plan_value(
            self.df['planned_number_of_shares_to_buy'],
            self.df['planned_number_of_shares_to_sell'],
            self.df['unit price'])
        self.df['total_number_of_shares_after_acquired_or_sold'] = sum_numbers_of_shares(
            self.df['current_number_of_shares'],
            self.df[
                'planned_number_of_shares_to_buy'],
            self.df[
                'planned_number_of_shares_to_sell'])
        self.df['total_value_of_shares_after_acquired_or_sold'] = total_value(self.df['current_value_of_shares'],
                                                                              self.df[
                                                                                  'planned_value_of_shares_to_be_acquired_or_sold'],
                                                                              self.df['target variance [%]'])

        self.df['outpout number of shres to buy/sell'] = calc_output_number(self.df['planned_number_of_shares_to_buy'],
                                                                            self.df['planned_number_of_shares_to_sell'])

    def save_and_print_results(self):
        self.df = self.df.fillna('')
        self.df.to_csv(self.output_file, index=False)

        table = PrettyTable()
        table.field_names = self.df.columns.tolist()

        table.add_rows(self.df.values.tolist())

        print(f'Presenting output file - additional columns added: {self.output_file}')
        print(table)


if __name__ == '__main__':
    stock_ex_calc = StockExchangeCalculator()
    stock_ex_calc.build()
    stock_ex_calc.convert()
    stock_ex_calc.save_and_print_results()
