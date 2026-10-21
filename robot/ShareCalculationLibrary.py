import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from converters import (  # noqa: E402
    calc_output_number,
    calculate_number_of_shares_to_buy,
    calculate_number_of_shares_to_sell,
)


class ShareCalculationLibrary:
    def calculate_number_of_shares_to_buy(self, variance, unit_price):
        return calculate_number_of_shares_to_buy(
            float(variance), float(unit_price)
        )

    def calculate_number_of_shares_to_sell(self, variance, unit_price):
        return calculate_number_of_shares_to_sell(
            float(variance), float(unit_price)
        )

    def calc_output_number(self, buy_shares, sell_shares):
        return calc_output_number(buy_shares, sell_shares)
