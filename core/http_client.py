import json
import os
import requests

from core.log_base import logger

class HttpClient:
    DOMAIN = os.getenv('BASE_URL', 'http://localhost:8000')
    DEFAULT_TIMEOUT = 30

    def make_request(self, method, url, body: dict | None = None, headers: dict | None = None, timeout: int | None = None):

        if timeout is None:
            timeout = self.DEFAULT_TIMEOUT

        response = requests.request(
            method,
            self.DOMAIN + url,
            data=json.dumps(body) if body else None,
            headers=headers,
            timeout=timeout
        )

        try:
            response.raise_for_status()

            if not response.text:
                logger.info('%s: No content (status %s)', response.url, response.status_code)
                return None

            response_json = response.json()
            logger.info('%s:: %s', response.url, response_json)

            return response_json

        except requests.exceptions.HTTPError as err:
            logger.error('HTTP Error: %s', err)

            raise

    def get(self, url, headers: dict | None = None):
        return self.make_request('GET', url, headers=headers)

    def post(self, url, body: dict | None = None, headers: dict | None = None):
        return self.make_request('POST', url, body=body, headers=headers)

    def put(self, url, body: dict | None = None, headers: dict | None = None):
        return self.make_request('PUT', url, body=body, headers=headers)

    def delete(self, url, headers: dict | None = None):
        return self.make_request('DELETE', url, headers=headers)
