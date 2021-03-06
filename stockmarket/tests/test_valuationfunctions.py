"""This file runs tests for all functions in valuation functions"""

import pytest
from stockmarket.stock import Stock
from stockmarket.firms import Firm
from stockmarket.valuationfunctions import *
from numpy.testing import assert_equal
from numpy.testing import assert_almost_equal


@pytest.fixture()
def stock():
    return (Stock(Firm("Firm1", 10000, [200, 300, 400, 300], 1), 100),
            Stock(Firm("Firm1", 8774, [215, 359, 233, 246], 1), 100))


def test_extrapolate(stock):
    # natural number
    assert_equal(extrapolate_average_profit(stock[0], 4), 60)
    # faction
    assert_almost_equal(extrapolate_average_profit(stock[1], 3), 55.8666666)
    # memory > history
    assert_equal(extrapolate_average_profit(stock[0], 6), 60)


def test_ma_price(stock):
    # normal
    stock[0].price_history = [200, 210, 220, 230, 240]
    assert_equal(extrapolate_ma_price(stock[0], 3, 5), 235)
    # price history too short
    stock[0].price_history = [200, 210, 220, 230]
    assert_equal(extrapolate_ma_price(stock[0], 3, 5), None)

