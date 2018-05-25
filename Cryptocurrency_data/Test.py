from Client import OkexClient, OkexTradeClient
import time

class CryptocurrencyData:
    def __init__(self, client, symbol_list, data_file, delay):
        self.client = client
        self.symbol_pair = self._pair_symbol(symbol_list)
        self.file = data_file
        self.delay = delay

    def _pair_symbol(self, symbol_list):
        return [s + '_' + symbol_list[0] for s in symbol_list[1:]]

    def _write_data(self):
        for symbol in self.symbol_pair:
            try:
                self.file.write(str(self.client.ticker(symbol))+'\n')
            except Exception:
                self.file.writelines("Failed\n")
            self.file.flush()
        self.file.write('\n')


    def execute(self):
        while(True):
            print('Process activated...')
            print('Collecting data...')
            self._write_data()
            print('Data has been successfully collected.')
            print('Data file up-to-date.')
            print('Next fetching process will be in 5 minutes...')
            time.sleep(self.delay)

    def stop(self):
        self.file.close()


if __name__ == "__main__":
    BTC = 'btc'
    LTC = 'ltc'
    ETC = 'etc'
    BCH = 'bch'
    ETH = 'eth'
    CTXC = 'ctxc'
    OKB = 'okb'
    ONT = 'ont'
    ENJ = 'enj'
    DADI = 'dadi'
    WFEE = 'wfee'
    REN = 'ren'
    TRA ='tra'
    TRIO = 'trio'
    RFR = 'rfr'

    symbol_list = ['btc', 'ltc', 'etc', 'bch', 'eth', 'ctxc', 'okb',
               'ont', 'enj', 'dadi', 'wfee', 'ren', 'tra', 'trio', 'rfr']


    client = OkexClient(None, None)
    data_file = open('okex_data.txt','a')
    delay = 300

    cb = CryptocurrencyData(client,symbol_list, data_file, delay)
    cb.execute()





