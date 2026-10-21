import numpy as np
import math


@np.vectorize
def calculate_number_of_shares(current_percent, asset_value, unit_price):
    result = (current_percent * 0.01 * asset_value) / unit_price

    return result


@np.vectorize
def calculate_current_value_of_shares(number_of_shares, unit_price):
    result = float(number_of_shares) * float(unit_price)
    return result


@np.vectorize
def calculate_plan_value(number_to_buy, number_to_sell, unit_price):
    result = (number_to_buy + number_to_sell) * unit_price
    return result


@np.vectorize
def sum_numbers(curr, buy, sell):
    result = curr - sell + buy
    return result


@np.vectorize
def tot_val(curr, plan, deviation):
    if deviation >= 0:
        return curr - plan
    return curr + plan


@np.vectorize
def calculate_number_of_shares_to_buy(deviation, unit_price):
    if deviation == 0:
        return 0
    elif deviation > 0:
        return 0
    elif deviation < 0:
        result = (100000 * abs(deviation) * 0.01) / unit_price
        return result


@np.vectorize
def calculate_number_of_shares_to_sell(deviation, unit_price):
    # Simplify conditions: if deviation is 0 or negative, return 0
    if deviation <= 0:
        return 0

    # Calculate exact theoretical shares
    exact_shares = (100000 * deviation * 0.01) / unit_price
    return exact_shares

