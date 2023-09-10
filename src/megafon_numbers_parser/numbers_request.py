import requests
import json


class NumbersUrlNotFound(Exception):
    "Raised when server returns 404 status code for url"
    pass


class NumbersRequest():
    def __init__(self, url, offset=0, limit=1000):
        self.url = url
        self.offset = offset
        self.limit = limit

    def obtain(self):
        response = requests.get(self.url, params={"offset": self.offset, "limit": self.limit})
        if response:
            if response.status_code == 404:
                raise NumbersUrlNotFound("{} returns 404 error code".format(self.url))
            elif response.status_code == 200:
                return self._parseContent(json.loads(response.content))

        return []

    def _parseContent(self, content):
        numbers = []
        for payload in content.get('numbers', []):
            numbers.extend(
                str(phone) for phone in payload.get('phones', [])
            )

        return numbers
