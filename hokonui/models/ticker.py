""" Ticker module """

import json
import time


class Ticker:  # pylint: disable=too-few-public-methods
    """An instance of market data for a selected exchange, market and currency

    Attributes:
        pair: A string representing the currency pair
        ask:  current market best(lowest) selling price
        bid:  current market best(highest) buying price
        timestamp: unix timestamp(UTC) when prices were captured
    """

    def __init__(self, pair, bid, ask):
        """init"""

        self.pair = pair
        self.bid = bid
        self.ask = ask
        self.timestamp = int(time.time())

    def to_json(self):
        """method for convertingt to Json"""
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)
