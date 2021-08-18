# Hokonui
Python library for querying Bitcoin exchange tickers, order books. 

Forked from <https://github.com/dursk/bitcoin-price-api>

[![CodeQL](https://github.com/laisee/hokonui/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/laisee/hokonui/actions/workflows/codeql-analysis.yml)
[![OSSAR](https://github.com/laisee/hokonui/actions/workflows/ossar-analysis.yml/badge.svg)](https://github.com/laisee/hokonui/actions/workflows/ossar-analysis.yml)
[![SL Scan](https://github.com/laisee/hokonui/actions/workflows/shiftleft-analysis.yml/badge.svg)](https://github.com/laisee/hokonui/actions/workflows/shiftleft-analysis.yml)
[![DevSkim](https://github.com/laisee/hokonui/actions/workflows/devskim-analysis.yml/badge.svg)](https://github.com/laisee/hokonui/actions/workflows/devskim-analysis.yml)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/cf037d2688d24eb5917e4797af7199b6)](https://www.codacy.com/gh/laisee/hokonui/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=laisee/hokonui&amp;utm_campaign=Badge_Grade)
[![Semgrep](https://github.com/laisee/hokonui/actions/workflows/semgrep.yml/badge.svg)](https://github.com/laisee/hokonui/actions/workflows/semgrep.yml)


## Exchanges included
- BTC-E
- Bitfinex
- BitFlyer
- Bitstamp
- BitX
- CoinBase
- Huobi
- itBit
- OKCoin
- Liquid
 ... and more 

## Data Providers
- CoinDesk
- Coinapult

## Features
- single API for multiple exchanges, data providers
- full set of tests using nose tool
- MIT license
- active development
- minimal code dependencies
 
## TODO
- add simple arbitrage between selected exchanges
- add session class for querying account balances
- add buy/sell order handling
- add account management (balances, funding, withdrawals, addresses)
- add library to PyPi
- add support for Python 3
