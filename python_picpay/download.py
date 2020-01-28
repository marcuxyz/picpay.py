import requests
from collections import namedtuple

Response = namedtuple("Response", "referenceId paymentUrl expiresAt qrcode status_code")
ResponseErrror = namedtuple("ResponseError", "message errors status_code")


class Downloader:
    def __init__(self):
        self.session = requests.Session()

    def post(self, url, data=None, params=None, cookies=None, headers=None):
        response = self.session.post(
            url,
            data=data,
            params=params,
            verify=True,
            headers=headers,
            cookies=cookies,
        )

        if response.status_code == 200:
            return Response(
                referenceId=response.json()["referenceId"],
                paymentUrl=response.json()["paymentUrl"],
                expiresAt=response.json()["expiresAt"],
                qrcode=response.json()["qrcode"],
                status_code=response.status_code,
            )

        return ResponseErrror(
            message=response.json()["message"],
            errors=response.json().get("errors", {}), 
            status_code=response.status_code
        )

    def close(self):
        self.session.close()
