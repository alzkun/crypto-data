import krakenex

class KrakenInterface:
    pairs = {
        'BTC_EUR': 'XXBTZEUR',
        'BTC_USD': 'XXBTZUSD',
        'LTC_BTC': 'XLTCXXBT',
        'BCH_BTC': 'BCHXBT',
        'ETH_BTC': 'XETHXXBT',
        'ETC_BTC': 'XETCXXBT'
    }

    def __init__(self):
        self.kraken = krakenex.API()

    def get_data(self):
        pairs_str = ','.join(self.pairs.values())
        res = self.kraken.query_public('Ticker', {'pair': pairs_str})
        
        ret = {}
        for k, v in self.pairs.items():
            ret[k] = [res['result'][v]['c'][0],
                      res['result'][v]['h'][0],
                      res['result'][v]['l'][0]]

        return ret
