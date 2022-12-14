import os
import unittest
from isaac_martin_sdk.sdk import TheOneSDK


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        url = 'https://the-one-api.dev/v2'
        token = os.environ['API_TOKEN']
        TheOneSDK(url=url, authentication_token=token)