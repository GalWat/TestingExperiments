from functools import wraps

import requests
from posixpath import join as urljoin

from requests import JSONDecodeError


def try_return_json(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        response = func(*args, **kwargs)

        try:
            return response.json()
        except JSONDecodeError:
            return response.text

    return wrapper


class BaseApi:
    def __init__(self, service_url: str):
        self.service_url = service_url
        self.global_headers = {}

    @try_return_json
    def get(self, handler, params: dict = None):
        return requests.get(urljoin(self.service_url, handler), params=params, headers=self.global_headers)

    @try_return_json
    def post(self, handler, json):
        return requests.post(urljoin(self.service_url, handler), json=json, headers=self.global_headers)


class BaseHandlers:
    def __init__(self, client):
        self.client = client
