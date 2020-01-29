import requests


class Downloader:
    def __init__(self):
        self.session = requests.Session()

    def get(self, url, params=None, cookies=None, headers=None):
        return self.session.get(url, params=params, cookies=cookies, headers=headers)

    def post(self, url, data=None, params=None, cookies=None, headers=None):
        return self.session.post(
            url, data=data, params=params, headers=headers, cookies=cookies,
        )

    def close(self):
        self.session.close()
