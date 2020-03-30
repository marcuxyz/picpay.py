import json
from urllib.parse import urljoin

from .download import Downloader

PICPAY_URL = "https://appws.picpay.com/ecommerce/public/payments/"
CANCEL_URL = urljoin(PICPAY_URL, "{}/cancellations")
STATUS_URL = urljoin(PICPAY_URL, "{}/status")


class Picpay:
    def __init__(self, token: str):
        _headers = {
            "Content-Type": "application/json",
            "x-picpay-token": token,
        }
        self.downloader = Downloader(_headers)

    def payment(self, payment_data: dict):
        response = self.downloader.post(PICPAY_URL, data=json.dumps(payment_data))
        return response

    async def payment_async(self, payment_data: dict):
        return await self.downloader.post_async(
            PICPAY_URL, data=json.dumps(payment_data)
        )

    def get_status(self, reference_id: str):
        return self.downloader.get(STATUS_URL.format(reference_id))

    async def get_status_async(self, reference_id: str):
        return await self.downloader.get_async(STATUS_URL.format(reference_id))

    def cancel_payment(self, reference_id: str, authorization_id: str):
        data = json.dumps({"authorizationId": authorization_id})
        return self.downloader.post(CANCEL_URL.format(reference_id), data=data)

    async def cancel_payment_async(self, reference_id: str, authorization_id: str):
        data = json.dumps({"authorizationId": authorization_id})
        return await self.downloader.post_async(
            CANCEL_URL.format(reference_id), data=data
        )
