from unittest import result

from stock_exchange_calc import StockExchangeCalculator


def sum_of_values_for_target_percentage_column_should_equal(percentage_value):
    data = StockExchangeCalculator()
    data.build()
    data.convert()
    data.save_and_print_results_simplified()
    sum_of_values_from_target_percentage_column = data.df['target [%]'].sum()
    assert int(sum_of_values_from_target_percentage_column) == int(
        percentage_value), f"{sum_of_values_from_target_percentage_column} different from {percentage_value}"


def sum_of_values_for_current_percentage_column_should_equal(percentage_value):
    data = StockExchangeCalculator()
    data.build()
    data.convert()
    data.save_and_print_results_simplified()
    sum_of_values_from_current_percentage_column = data.df['current[%]'].sum()
    assert int(sum_of_values_from_current_percentage_column) == int(
        percentage_value), f"{sum_of_values_from_current_percentage_column} different from {percentage_value}"


def target_variance_is_calculated_correctly():
    data = StockExchangeCalculator()
    data.build()
    data.convert()
    data.save_and_print_results_simplified()
    result = data.df['target variance [%]'].equals(data.df['current[%]'] - data.df['target [%]'])
    assert result, f"check {data.input_file} because some target variance is calculated incorrectly (should be current minus target)!"

    # from pdb import set_trace
    # set_trace()


def target_percent_between_0_and_100():
    data = StockExchangeCalculator()
    data.build()
    data.convert()
    data.save_and_print_results_simplified()

    all_equal_or_greater_than_zero = (data.df['target [%]'] >= 0).all()
    all_equal_or_less_than_hundred = (data.df['target [%]'] <= 100).all()

    result = all_equal_or_greater_than_zero & all_equal_or_less_than_hundred

    assert result, f"check {data.input_file} because some target percent value is out of range <0;100>"


def current_percent_between_0_and_100():
    data = StockExchangeCalculator()
    data.build()
    data.convert()
    data.save_and_print_results_simplified()

    all_equal_or_greater_than_zero = (data.df['current[%]'] >= 0).all()
    all_equal_or_less_than_hundred = (data.df['current[%]'] <= 100).all()

    result = all_equal_or_greater_than_zero & all_equal_or_less_than_hundred

    assert result, f"check {data.input_file} because some current percent value is out of range <0;100>"


def calculated_output_number_of_shares_is_correct():
    data = StockExchangeCalculator()
    data.build()
    data.convert()
    data.save_and_print_results_simplified()
    for index, row in data.df.iterrows():
        check = row['outpout number of shres to buy/sell'] * row['unit price'] == row[
            'planned_value_of_shares_to_be_acquired_or_sold']
        assert check, f"test failed because {row['outpout number of shres to buy/sell']}*{row['unit price']}!={row['planned_value_of_shares_to_be_acquired_or_sold']}"


def simulate_output_number_of_shares_is_incorrect():
    data = StockExchangeCalculator()
    data.build()
    data.convert()

    # we spoil calculated value for purpose it is like monkey patch in pytyest
    data.df.loc[3, 'outpout number of shres to buy/sell'] = 10

    data.save_and_print_results_simplified()

    for index, row in data.df.iterrows():
        check = row['outpout number of shres to buy/sell'] * row['unit price'] == row[
            'planned_value_of_shares_to_be_acquired_or_sold']
        assert check, f"test failed because {row['outpout number of shres to buy/sell']}*{row['unit price']}!={row['planned_value_of_shares_to_be_acquired_or_sold']}"


        # Access columns using bracket notation: row['ColumnName']
        # print(index, row['column_name'])
        # from pdb import set_trace
        # set_trace()

if __name__ == "__main__":
    simulate_output_number_of_shares_is_incorrect()
