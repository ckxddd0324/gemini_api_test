# built-in lib
import requests
import unittest
import os

# 3rd party lib
from dotenv import load_dotenv

# own module
import helper

# load env variable
APP_ROOT = os.path.join(os.path.dirname(__file__), '..')
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)

gemini_api_secret = os.getenv("GEMINI_API_SECRET")
gemini_api_key = os.getenv("GEMINI_API_SECRET")

base_url = "https://api.gemini.com"
endpoint = "/v1/order/new"
url = base_url + endpoint

class ApiTest(unittest.TestCase):

    def test_default_widget_size(self):
        payload = helper.create_order_playload(endpoint,
                                               "btcusd",
                                               "5",
                                               "3633.00",
                                               "buy",
                                               "exchange limit",
                                               "maker-or-cancel")

        e_payload = helper.encrypted_payload(payload)
        e_signature = helper.encrypted_signature(gemini_api_secret, e_payload)
        request_headers = helper.construct_request_header(gemini_api_key, e_payload, e_signature)

        self.response = requests.post(url,
                                      data=None,
                                      headers=request_headers).json()
        print(self.response)
        
if __name__ == '__main__':
    unittest.main()