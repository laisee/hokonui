from decimal import Decimal

if __package__ is None:
    import sys
    from os import path

    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
    from hokonui.exchanges.bitfinex import Bitfinex as bfx
else:
    from ..hokonui.exchanges.bitfinex import Bitfinex as bfx


def main():
    """main function, called at the start of the program"""

    print("-" * 20)
    ask = bfx.get_current_ask("USD")
    bid = bfx.get_current_bid("USD")
    print(
        "Bitfinex : Bid %s Ask %s"
        % (format(Decimal(bid), ".2f"), format(Decimal(ask), ".2f"))
    )
    print("-" * 20)


if __name__ == "__main__":
    main()
