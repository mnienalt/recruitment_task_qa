import numpy as np


@np.vectorize(otypes=[float])
def calculate_number_of_shares(current_percent, asset_value, unit_price):
    result = (current_percent * 0.01 * asset_value) / unit_price

    return result


@np.vectorize(otypes=[float])
def calculate_current_value_of_shares(number_of_shares, unit_price):
    result = float(number_of_shares) * float(unit_price)
    return result


@np.vectorize(otypes=[float])
def calculate_plan_value(number_to_buy, number_to_sell, unit_price):
    result = (number_to_buy + number_to_sell) * unit_price
    return result


@np.vectorize(otypes=[float])
def sum_numbers(curr, buy, sell):
    result = curr - sell + buy
    return result


@np.vectorize(otypes=[float])
def tot_val(curr, plan, deviation):
    if deviation >= 0:
        return curr - plan
    return curr + plan


@np.vectorize(otypes=[float])
def calculate_number_of_shares_to_buy(deviation, unit_price):
    if deviation == 0:
        return 0
    elif deviation > 0:
        return 0
    elif deviation < 0:
        result = (100000 * abs(deviation) * 0.01) / unit_price
        return result


@np.vectorize(otypes=[float])
def calculate_number_of_shares_to_sell(deviation, unit_price):
    if deviation <= 0:
        return 0.0
    exact_shares = (100000 * deviation * 0.01) / unit_price
    return exact_shares

@np.vectorize
def calc_output_number(number_to_buy,number_to_sell):
    return round(max(number_to_buy, number_to_sell))


