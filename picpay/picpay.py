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
        self.downloader = Downloader()

    def payment(self, payment_data: dict):
        url = urljoin(PICPAY_DEFAULT_URL, "payments")

        response = self.downloader.post(
            url, data=json.dumps(payment_data), headers=self.headers
        )

        return response

    def get_status(self, referenceId: str):
        url = urljoin(PICPAY_DEFAULT_URL, f"payments/{referenceId}/status")

        return self.downloader.get(url, headers=self.headers)

    def cancel_payment(self, referenceId: str, authorizationId: str):
        url = urljoin(PICPAY_DEFAULT_URL, f"payments/{referenceId}/cancellations")

        response = self.downloader.post(
            url,
            data=json.dumps({"authorizationId": authorizationId}),
            headers=self.headers,
        )

        return response
