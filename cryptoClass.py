import requests
import json
from cryptoConfig import currency

class ConvertionException(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def convert(quote:str, base:str, amount:str):
        if quote == base:
            raise ConvertionException('ConvertationError: Нельзя проводить конвертацию с одной валютой')
        
        try:
            quote_ticket = currency[quote]
        except KeyError:
            raise ConvertionException(f'Не удается обработать валюту {quote}')
    
        try:
            base_ticket = currency[base]
        except KeyError:
            raise ConvertionException(f'Не удается обработать валюту {base}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticket}&tsyms={base_ticket}')
        total_base = json.loads(r.content)[currency[base]]
        return total_base * int(amount)
