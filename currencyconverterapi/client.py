from json import load
from urllib.request import urlopen

from .models import PairCache, Settings


class CurrencyConverterApi:

    API_BASE = "https://free.currconv.com"

    __settings: Settings

    def __init__(self, api_key: str = "") -> None:
        self.__settings = Settings.from_file()
        if api_key:
            self.__settings.cache_api_key(api_key)
        assert self.__settings.api_key, "Get free API key from: https://free.currencyconverterapi.com/free-api-key"

        self.fetch_currencies()
        self.__settings.save()

    def get(self, url):
        with urlopen(url) as f:
            return load(f)

    @property
    def api_key(self) -> str:
        return self.__settings.api_key

    @property
    def currencies(self) -> set[str]:
        self.fetch_currencies()
        return self.__settings.currencies

    @property
    def cached_pairs(self) -> dict[str, PairCache]:
        return self.__settings.cached_pairs

    def fetch_currencies(self):
        if not self.__settings.currencies:
            url = f"{CurrencyConverterApi.API_BASE}/api/v7/currencies?apiKey={self.api_key}"
            self.__settings.currencies = set(self.get(url)["results"].keys())

    def is_cached(self, pair: str) -> bool:
        return pair in self.cached_pairs and not self.cached_pairs[pair].is_outdated()

    def is_exist(self, symbol: str) -> bool:
        return symbol.upper() in self.currencies

    def convert(self, amount: float, source: str, destination: str) -> float:
        for symbol in [source, destination]:
            if not self.is_exist(symbol):
                raise ValueError(f"{symbol} is not available currency")

        pair = f"{source.upper()}_{destination.upper()}"
        if not self.is_cached(pair):
            print("Fetching...")
            url = f"{CurrencyConverterApi.API_BASE}/api/v7/convert?q={pair}&compact=ultra&apiKey={self.api_key}"
            self.__settings.cache_pair(pair, self.get(url)[pair])
        return self.cached_pairs[pair].value
