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

base_url = "https://api.gemini.com"
endpoint = "/v1/order/new"
url = base_url + endpoint
gemini_api_secret = os.getenv("GEMINI_API_SECRET")
gemini_api_key = os.getenv("GEMINI_API_SECRET")
print(gemini_api_key)
#
# print(helper.create_order_playload(endpoint, "btcusd", "5", "3633.00", "buy", "exchange limit", "maker-or-cancel"))
# print(helper.create_order_playload(endpoint, "btcusd", "5", "3633.00", "buy", "exchange limit", "maker-or-cancel", timestamp_format="number"))
# print(helper.create_order_playload(endpoint, "btcusd", "5", "3633.00", "buy", "exchange limit", "maker-or-cancel", timestamp_unit='ms'))
# print(helper.create_order_playload(endpoint, "btcusd", "5", "3633.00", "buy", "exchange limit", "maker-or-cancel", timestamp_format="number", timestamp_unit='ms'))
# print(helper.create_order_playload(endpoint, "btcusd", "5", "3633.00", "buy", "exchange limit", "maker-or-cancel", timestamp_format="number", timestamp_unit='ms', with_client_order_id="SDADSSADSA"))
# client_id = helper.generate_random_id(12, letter_format='Upper', with_acceptable_symbols=True)
# print(helper.create_order_playload(endpoint, "btcusd", "5", "3633.00", "buy", "exchange limit", "maker-or-cancel", timestamp_format="number", timestamp_unit='ms', with_client_order_id=client_id))
#
#

payload = helper.create_order_playload(endpoint, "btcusd", "5", "3633.00", "buy", "exchange limit", "maker-or-cancel")
print(type(payload))

e_payload = helper.encrypted_payload(payload)

print(e_payload)

e_signature = helper.encrypted_signature(gemini_api_secret, e_payload)

print(e_signature)

request_headers = helper.construct_request_header(gemini_api_key, e_payload, e_signature)
print(request_headers)
#
# print(helper.generate_random_id(12))
# print(helper.generate_random_id(12, letter_format='Upper'))
# print(helper.generate_random_id(12, letter_format='lower', with_num=False))
print('_'*9)
print(helper.generate_random_id(12, letter_format='Upper', with_acceptable_symbols=False))




class ApiTest(unittest.TestCase):
    def setUp(self):
        self.response = requests.post(url,
                         data=None,
                         headers=request_headers).json()

    def test_default_widget_size(self):
        print(self.response)

if __name__ == '__main__':
    unittest.main()