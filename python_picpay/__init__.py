__version__ = "1.0.0"

import json
from urllib.parse import urljoin

from .download import Downloader

PICPAY_DEFAULT_URL = "https://appws.picpay.com/ecommerce/public/"


class Picpay:
    def __init__(self, token: str):
        self.token = token
        self.headers = {
            "Content-Type": "application/json",
            "x-picpay-token": self.token,
        }

    def payment(self, payment_data: dict):
        payment_url = urljoin(PICPAY_DEFAULT_URL, "payments")

        response = Downloader().post(
            payment_url, data=json.dumps(payment_data), headers=self.headers
        )

        return response
