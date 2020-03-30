import httpx
from httpx import Response


class Downloader:
    def __init__(self, headers=None):
        self.sess_async = httpx.AsyncClient(headers=headers)
        self.sess = httpx.Client(headers=headers)

    def get(self, url, params=None, headers=None) -> Response:
        return self.sess.get(url, params=params)

    def post(self, url, data=None, params=None, headers=None) -> Response:
        return self.sess.post(url, data=data, params=params)

    async def get_async(self, url, params=None, headers=None) -> Response:
        response = await self.sess_async.get(url, params=params)
        return response

    async def post_async(self, url, data=None, params=None, headers=None) -> Response:
        response = await self.sess_async.post(url, data=data, params=params)

        return response
