import sys
import argparse

from kraken_interface import KrakenInterface
from poloniex_interface import PoloniexInterface

from prettytable import PrettyTable

def main(argv):
    if (argv.exchange == 'polo'):
        exchange = PoloniexInterface()
    else:
        exchange = KrakenInterface()

    ticker_data = exchange.get_data()

    pairs_table = PrettyTable(['Pair', 'Last', 'High', 'Low'])
    for k, v in ticker_data.items():
        pairs_table.add_row([k, v[0], v[1], v[2]])

    print(pairs_table)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = 'Show ticker data for major crypto currencies.')
    parser.add_argument('--polo', '--poloniex', dest='exchange', action='store_const', const='polo', default='kraken', help='Poloniex exchange')
    parser.add_argument('--btc', type=float, help='# of BTC (Bitcoin)')
    parser.add_argument('--ltc', type=float, help='# of LTC (Litecoin)')
    parser.add_argument('--bch', type=float, help='# of BCH (Bitcoin Cash)')
    parser.add_argument('--eth', type=float, help='# of ETH (Ethereum)')
    parser.add_argument('--etc', type=float, help='# of ETC (Ethereum Classic)')
    argv = parser.parse_args()

    main(argv)
