import argparse

from kraken_interface import KrakenInterface
from poloniex_interface import PoloniexInterface

from prettytable import PrettyTable

def ratio_btc(cur):
    ex = KrakenInterface()
    tk = ex.get_data()
    return float(tk[cur][0])

def amount(argv, data):
    coins = {
            'BTC': [argv.btc, float(1.0)],
            'LTC': [argv.ltc, float(data['LTC_BTC'][0])],
            'BCH': [argv.bch, float(data['BCH_BTC'][0])],
            'ETH': [argv.eth, float(data['ETH_BTC'][0])],
            'ETC': [argv.etc, float(data['ETC_BTC'][0])]
    }

    ret = {}

    for k, v in coins.items():
        if (v[0] != None):
            ret[k] = [v[0], v[0]*v[1], v[0]*v[1]*ratio_btc('BTC_EUR')]

    return ret

def main(argv):
    if (argv.exchange == 'polo'):
        exchange = PoloniexInterface()
    else:
        exchange = KrakenInterface()

    ticker_data = exchange.get_data()

    pairs_table = PrettyTable(['Pair', 'Last', 'High', 'Low'])
    for k, v in sorted(ticker_data.items()):
        pairs_table.add_row([k, v[0], v[1], v[2]])

    print(pairs_table)

    current_coins = amount(argv, ticker_data)

    if (current_coins):
        summary = [0.0, 0.0]

        coins_table = PrettyTable(['Coin', 'QTY', 'BTC', 'EUR'])
        for k, v in sorted(current_coins.items()):
            coins_table.add_row([k, round(v[0], 8), round(v[1], 8), round(v[2], 2)])
            summary = [summary[0]+v[1], summary[1]+v[2]]

        coins_table.add_row(['', '', '', ''])
        coins_table.add_row(['', '', round(summary[0], 8), round(summary[1], 2)])
        print(coins_table)


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
