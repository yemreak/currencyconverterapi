from dataclasses import dataclass, field
from os import environ
from pathlib import Path
from time import time

from ruamel.yaml import YAML, yaml_object

yaml = YAML()


@yaml_object(yaml)
@dataclass
class PairCache:

    CACHE_TIME = 60 * 10

    pair: str
    value: float
    timestamp: float = field(init=False)

    def __post_init__(self):
        self.timestamp = time()

    def is_outdated(self) -> bool:
        return time() - self.timestamp > PairCache.CACHE_TIME


@yaml_object(yaml)
@dataclass
class Settings:

    PATH = Path(f"{environ['HOME']}/currencyconverterapi.yml")

    api_key: str = field(default="")
    currencies: set[str] = field(default_factory=set)
    cached_pairs: dict[str, PairCache] = field(default_factory=dict)

    @classmethod
    def from_file(cls):
        return yaml.load(Settings.PATH) if Settings.PATH.exists() else cls()

    def save(self):
        yaml.dump(self, Settings.PATH)

    def cache_api_key(self, api_key: str):
        self.api_key = api_key
        self.save()

    def cache_pair(self, pair: str, value: float):
        self.cached_pairs[pair] = PairCache(pair, value)
        self.save()
