from poloniex import Poloniex

class PoloniexInterface:
    pairs = {
        'LTC_BTC': 'BTC_LTC',
        'BCH_BTC': 'BTC_BCH',
        'ETH_BTC': 'BTC_ETH',
        'ETC_BTC': 'BTC_ETC'
    }

    def __init__(self):
        self.polo = Poloniex()

    def get_data(self):
        res = self.polo.returnTicker()

        ret = {}
        for k, v in self.pairs.items():
            ret[k] = [res[v]['last'],
                      res[v]['high24hr'],
                      res[v]['low24hr']]

        return ret
