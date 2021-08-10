# Hokonui
Python library for querying Bitcoin exchange tickers, order books. 

Forked from <https://github.com/dursk/bitcoin-price-api>

[![CodeQL](https://github.com/laisee/hokonui/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/laisee/hokonui/actions/workflows/codeql-analysis.yml)
[![OSSAR](https://github.com/laisee/hokonui/actions/workflows/ossar-analysis.yml/badge.svg)](https://github.com/laisee/hokonui/actions/workflows/ossar-analysis.yml)
[![SL Scan](https://github.com/laisee/hokonui/actions/workflows/shiftleft-analysis.yml/badge.svg)](https://github.com/laisee/hokonui/actions/workflows/shiftleft-analysis.yml)
[![DevSkim](https://github.com/laisee/hokonui/actions/workflows/devskim-analysis.yml/badge.svg)](https://github.com/laisee/hokonui/actions/workflows/devskim-analysis.yml)

[![Codacy Security Scan](https://github.com/laisee/hokonui/actions/workflows/codacy-analysis.yml/badge.svg)](https://github.com/laisee/hokonui/actions/workflows/codacy-analysis.yml)

[![Semgrep](https://github.com/laisee/hokonui/actions/workflows/semgrep.yml/badge.svg)](https://github.com/laisee/hokonui/actions/workflows/semgrep.yml)

[![Semgrep](https://github.com/laisee/hokonui/actions/workflows/semgrep-analysis.yml/badge.svg)](https://github.com/laisee/hokonui/actions/workflows/semgrep-analysis.yml)


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
