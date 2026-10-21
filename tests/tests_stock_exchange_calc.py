import pandas as pd
import pytest

from converters import (
    calculate_number_of_shares_to_buy,
    calculate_number_of_shares_to_sell,
    calc_output_number,
)
from stock_exchange_calc import StockExchangeCalculator


@pytest.mark.parametrize(
    ("deviation", "unit_price", "expected_buy", "expected_sell", "expected_output"),
    [
        (-10, 150, 10000 / 150, 0, 67),  # underweight: buy
        (0, 90, 0, 0, 0),  # at target: no trade
        (10, 220, 0, 10000 / 220, 45),  # overweight: sell
    ],
)
def test_share_recommendation_for_variance(
        deviation, unit_price, expected_buy, expected_sell, expected_output
):
    buy = calculate_number_of_shares_to_buy(deviation, unit_price)
    sell = calculate_number_of_shares_to_sell(deviation, unit_price)

    assert float(buy) == pytest.approx(expected_buy)
    assert float(sell) == pytest.approx(expected_sell)
    assert calc_output_number(buy, sell) == expected_output


@pytest.mark.parametrize(
    ("deviation", "expected_buy", "expected_sell", "expected_output"),
    [
        (-1, 0.5, 0, 0),  # 0.5 buy shares round to even 0
        (-3, 1.5, 0, 2),  # 1.5 buy shares round to even 2
        (1, 0, 0.5, 0),  # 0.5 sell shares round to even 0
        (3, 0, 1.5, 2),  # 1.5 sell shares round to even 2
    ],
)
def test_half_share_recommendations_use_ties_to_even(
        deviation, expected_buy, expected_sell, expected_output
):
    unit_price = 2000
    buy = calculate_number_of_shares_to_buy(deviation, unit_price)
    sell = calculate_number_of_shares_to_sell(deviation, unit_price)

    assert float(buy) == pytest.approx(expected_buy)
    assert float(sell) == pytest.approx(expected_sell)
    assert calc_output_number(buy, sell) == expected_output


def test_csv_output_recommends_correct_shares_for_each_security(
        tmp_path, monkeypatch
):
    monkeypatch.chdir(tmp_path)
    (tmp_path / "input.csv").write_text(
        "Account -ABC with $100 K in total asset (100% is vested),"
        "Security,target [%],current[%],target variance [%],unit price,"
        "outpout number of shres to buy/sell\n"
        ",IBM,20,10,-10,150,???\n"
        ",MSFT,20,20,0,90,???\n"
        ",ORCL,20,30,10,220,???\n"
        ",AAPL,20,20,0,450,???\n"
        ",HD,20,20,0,70,???\n",
        encoding="utf-8",
    )

    calculator = StockExchangeCalculator()
    calculator.build()
    calculator.convert()
    calculator.save_and_print_results()

    result = pd.read_csv(tmp_path / "output.csv")
    recommendations = dict(
        zip(
            result["Security"],
            result["outpout number of shres to buy/sell"],
        )
    )

    assert recommendations == {
        "IBM": 67,
        "MSFT": 0,
        "ORCL": 45,
        "AAPL": 0,
        "HD": 0,
    }
