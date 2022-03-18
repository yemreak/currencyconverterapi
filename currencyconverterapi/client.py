from json import load
from urllib.request import urlopen


class CurrencyConverterApi:

    API_BASE = "https://free.currconv.com"

    api_key: str

    def __init__(self, api_key: str = "") -> None:
        assert api_key, "Get free API key from: https://free.currencyconverterapi.com/free-api-key"
        self.api_key = api_key

        self.__currencies: set[str] = set()

    def get(self, url):
        with urlopen(url) as f:
            return load(f)

    @property
    def currencies(self) -> set[str]:
        if not self.__currencies:
            url = f"{CurrencyConverterApi.API_BASE}/api/v7/currencies?apiKey={self.api_key}"
            self.__currencies = set(self.get(url)["results"].keys())
        return self.__currencies

    def is_exist(self, symbol: str) -> bool:
        return symbol.upper() in self.currencies

    def convert(self, amount: float, source: str, destination: str) -> float:
        for symbol in [source, destination]:
            if not self.is_exist(symbol):
                raise ValueError(f"{symbol} is not available currency")

        pair = f"{source.upper()}_{destination.upper()}"
        url = f"{CurrencyConverterApi.API_BASE}/api/v7/convert?q={pair}&compact=ultra&apiKey={self.api_key}"
        return self.get(url)[pair]
