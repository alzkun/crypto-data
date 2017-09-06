# crypto-data
Show ticker data for major Crypto Currencies and keep track of your portfolio.

# Install (Fedora Linux)
```
dnf install python3 python3-virtualenv python3-pip
git clone https://github.com/alzkun/crypto-data.git
cd crypto-data
virtualenv-3 venv
source venv/bin/activate
pip3 install -r requirements.txt
```

# Usage
```
usage: crypto_data.py [-h] [--polo] [--btc BTC] [--ltc LTC] [--bch BCH]
                      [--eth ETH] [--etc ETC]

optional arguments:
  -h, --help          show this help message and exit
  --polo, --poloniex  Poloniex exchange
  --btc BTC           # of BTC (Bitcoin)
  --ltc LTC           # of LTC (Litecoin)
  --bch BCH           # of BCH (Bitcoin Cash)
  --eth ETH           # of ETH (Ethereum)
  --etc ETC           # of ETC (Ethereum Classic)
```
