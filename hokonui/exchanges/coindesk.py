""" Module for testing Coindesk API """

# pylint: disable=duplicate-code, line-too-long

from hokonui.exchanges.base import Exchange as Base
from hokonui.utils.helpers import apply_format, get_response


class CoinDesk(Base):
    """Class for testing Coindesk API"""

    NAME = "CoinDesk"

    @classmethod
    def _current_ticker_extractor(cls, data):
        """Method for extracting ticker"""

    @classmethod
    def _current_price_extractor(cls, data):
        """Method for extracting current price"""

    @classmethod
    def _current_bid_extractor(cls, data):
        """Method for extracting bid price"""

    @classmethod
    def _current_ask_extractor(cls, data):
        """Method for extracting ask price"""

    @classmethod
    def _current_orders_extractor(cls, data, max_qty=100):
        """Method for extracting ask price"""

    @classmethod
    def get_current_price(cls, ccy=Base.CCY_DEFAULT, params=None, body=None, header=None):
        """Method for retrieving current price"""
        url = "https://data-api.coindesk.com/spot/v1/latest/tick?market=coinbase&instruments=BTC-%s&apply_mapping=true"
        data = get_response(url, ccy)
        price = data["Data"][f"BTC-{ccy}"]["PRICE"]
        return apply_format(price)

    @classmethod
    def get_past_price(cls, ccy=Base.CCY_DEFAULT):
        """Method for retrieving past price"""
        url = "https://data-api.coindesk.com/spot/v1/latest/tick?market=coinbase&instruments=BTC-%s&apply_mapping=true"
        data = get_response(url,ccy)
        price = data["Data"][f"BTC-{ccy}"]["MOVING_7_DAY_OPEN"]
        return apply_format(str(price))

    @classmethod
    def get_historical_data(cls, timestamp, ccy=Base.CCY_DEFAULT):
        """Method for retrieving historical data"""
        url = f"https://data-api.coindesk.com/spot/v1/historical/days?market=kraken&instrument=BTC-%s&limit=10&aggregate=1&fill=true&apply_mapping=true&response_format=JSON&to_ts={timestamp}"
        return get_response(url, ccy)
