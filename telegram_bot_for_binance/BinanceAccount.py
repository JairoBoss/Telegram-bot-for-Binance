import Files
import time
from binance.client import Client
from binance.enums import *

class Binance:
    def __init__(self):
        self.file = Files.Controller()
        self.APIS = self.file.openFile()
        self.client = Client(self.file.getKey(self.APIS[1]), self.file.getKey(self.APIS[2]), tld='com')
        self.moneda = 'BTCUSDT'

    def cryptoPrice(self):
        'Encuentra y retorna el precio de la crypto'
        list_of_tickers = self.client.get_all_tickers()
        for tick_2 in list_of_tickers:
            if tick_2["symbol"] == self.moneda:
                precio = float(tick_2["price"])            
        return precio


        
cuenta = Binance()
print(cuenta.cryptoPrice())
