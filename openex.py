import requests
from cachetools import cached, TTLCache
from dotenv import load_dotenv
import config

load_dotenv()


class OpenExchangeClient:
    def __init__(self, app_id):
        self.app_id = app_id

    @property
    @cached(cache=TTLCache(maxsize=1024, ttl=1800))
    def latest(self):
        return requests.get(f"{config.Config.ENDPOINT}?app_id={config.Config.APP_ID}").json()

    def convert(self, amount, to_currency):
        rates = self.latest["rates"]
        to_rate = rates[to_currency]
        return amount * to_rate
