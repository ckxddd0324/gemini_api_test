# built-in lib
import requests
import unittest
import os

# 3rd party lib
from dotenv import load_dotenv

# own module
from .helpers import helper

# load env variable
APP_ROOT = os.path.join(os.path.dirname(__file__), '..')
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)

gemini_api_secret = os.getenv("GEMINI_API_SECRET")
gemini_api_key = os.getenv("GEMINI_API_SECRET")

base_url = "https://api.gemini.com"
endpoint = "/v1/order/new"
url = base_url + endpoint

class test_btc_new_order(unittest.TestCase):

    def test_buy_btc_usd_with_standard_order_via_empty_array_with_client_id(self):
        currency_symbol = "btcusd"
        amount = "5"
        price = "3633.00"
        side = "buy"
        options = []
        client_order_id = helper.generate_random_id(8)

        payload = helper.create_order_playload(endpoint,
                                               currency_symbol,
                                               amount,
                                               price,
                                               side,
                                               options=options,
                                               with_client_order_id=client_order_id)

        e_payload = helper.encrypted_payload(payload)
        e_signature = helper.encrypted_signature(gemini_api_secret, e_payload)
        request_headers = helper.construct_request_header(gemini_api_key, e_payload, e_signature)

        self.response = requests.post(url,
                                      data=None,
                                      headers=request_headers)
        response_in_json = self.response.json()

        assert self.response.status_code == 400
        assert response_in_json['symbol'] == currency_symbol
        assert response_in_json['type'] == "exchange limit"
        assert response_in_json['side'] == "buy"
        assert response_in_json['option'] == []
        assert response_in_json['original_amount'] == amount
        assert response_in_json['client_order_id'] == client_order_id
        assert float(response_in_json['executed_amount']) + float(response_in_json['remaining_amount']) == int(5)
        assert response_in_json['client_order_id'] == client_order_id
        self.assertLessEqual(float(response_in_json['avg_execution_price']), float(price))

    def test_buy_btc_usd_with_standard_order_via_empty_array_without_client_id(self):
        currency_symbol = "btcusd"
        amount = "5"
        price = "3633.00"
        side = "buy"
        options = []

        payload = helper.create_order_playload(endpoint,
                                               currency_symbol,
                                               amount,
                                               price,
                                               side,
                                               options=options)

        e_payload = helper.encrypted_payload(payload)
        e_signature = helper.encrypted_signature(gemini_api_secret, e_payload)
        request_headers = helper.construct_request_header(gemini_api_key, e_payload, e_signature)

        self.response = requests.post(url,
                                      data=None,
                                      headers=request_headers)
        response_in_json = self.response.json()

        assert self.response.status_code == 400
        assert response_in_json['symbol'] == currency_symbol
        assert response_in_json['type'] == "exchange limit"
        assert response_in_json['side'] == "buy"
        assert response_in_json['option'] == []
        assert response_in_json['original_amount'] == amount
        assert 'client_order_id' in == client_order_id
        assert float(response_in_json['executed_amount']) + float(response_in_json['remaining_amount']) == int(5)
        self.assertLessEqual(float(response_in_json['avg_execution_price']), float(price))

    def test_buy_btc_usd_with_standard_order_with_no_options_provided(self):
        currency_symbol = "btcusd"
        amount = "5"
        price = "3633.00"
        side = "buy"

        payload = helper.create_order_playload(endpoint,
                                               currency_symbol,
                                               amount,
                                               price,
                                               side)

        e_payload = helper.encrypted_payload(payload)
        e_signature = helper.encrypted_signature(gemini_api_secret, e_payload)
        request_headers = helper.construct_request_header(gemini_api_key, e_payload, e_signature)

        self.response = requests.post(url,
                                      data=None,
                                      headers=request_headers)
        response_in_json = self.response.json()

        assert self.response.status_code == 400
        assert response_in_json['symbol'] == currency_symbol
        assert response_in_json['type'] == "exchange limit"
        assert response_in_json['side'] == "buy"
        assert response_in_json['option'] == []
        assert response_in_json['original_amount'] == amount
        assert float(response_in_json['executed_amount']) + float(response_in_json['remaining_amount']) == int(5)
        self.assertLessEqual(float(response_in_json['avg_execution_price']), float(price))

    def test_buy_btc_usd_with_standard_order_with_maker_or_cancel_options_provided(self):
        currency_symbol = "btcusd"
        amount = "5"
        price = "3633.00"
        side = "buy"
        options = ["maker-or-cancel"]

        payload = helper.create_order_playload(endpoint,
                                               currency_symbol,
                                               amount,
                                               price,
                                               side,
                                               options=options)

        e_payload = helper.encrypted_payload(payload)
        e_signature = helper.encrypted_signature(gemini_api_secret, e_payload)
        request_headers = helper.construct_request_header(gemini_api_key, e_payload, e_signature)

        self.response = requests.post(url,
                                      data=None,
                                      headers=request_headers)
        response_in_json = self.response.json()

        assert self.response.status_code == 201
        assert response_in_json['symbol'] == currency_symbol
        assert response_in_json['type'] == "exchange limit"
        assert response_in_json['side'] == "buy"
        assert response_in_json['option'] == []
        assert response_in_json['is_cancelled'] == True
        assert response_in_json['original_amount'] == amount
        assert float(response_in_json['executed_amount']) + float(response_in_json['remaining_amount']) == int(5)
        self.assertLessEqual(float(response_in_json['avg_execution_price']), float(price))

    def test_buy_btc_usd_with_standard_order_with_immediate_or_cancel_options_provided(self):
        currency_symbol = "btcusd"
        amount = "5"
        price = "3633.00"
        side = "buy"
        options = ["maker-or-cancel"]

        payload = helper.create_order_playload(endpoint,
                                               currency_symbol,
                                               amount,
                                               price,
                                               side)

        e_payload = helper.encrypted_payload(payload)
        e_signature = helper.encrypted_signature(gemini_api_secret, e_payload)
        request_headers = helper.construct_request_header(gemini_api_key, e_payload, e_signature)

        self.response = requests.post(url,
                                      data=None,
                                      headers=request_headers)
        response_in_json = self.response.json()

        assert self.response.status_code == 201
        assert response_in_json['symbol'] == currency_symbol
        assert response_in_json['type'] == "exchange limit"
        assert response_in_json['side'] == "buy"
        assert response_in_json['option'] == []
        assert response_in_json['is_cancelled'] == True
        assert response_in_json['original_amount'] == amount
        assert float(response_in_json['executed_amount']) + float(response_in_json['remaining_amount']) == int(5)
        self.assertLessEqual(float(response_in_json['avg_execution_price']), float(price))

    def test_buy_btc_usd_with_standard_order_with_fill_or_kill_options_provided(self):
        currency_symbol = "btcusd"
        amount = "5"
        price = "3633.00"
        side = "buy"
        options = ["maker-or-cancel"]

        payload = helper.create_order_playload(endpoint,
                                               currency_symbol,
                                               amount,
                                               price,
                                               side)

        e_payload = helper.encrypted_payload(payload)
        e_signature = helper.encrypted_signature(gemini_api_secret, e_payload)
        request_headers = helper.construct_request_header(gemini_api_key, e_payload, e_signature)

        self.response = requests.post(url,
                                      data=None,
                                      headers=request_headers)
        response_in_json = self.response.json()

        assert self.response.status_code == 201
        assert response_in_json['symbol'] == currency_symbol
        assert response_in_json['type'] == "exchange limit"
        assert response_in_json['side'] == "buy"
        assert response_in_json['option'] == []
        assert response_in_json['is_cancelled'] == True
        assert response_in_json['original_amount'] == amount
        assert float(response_in_json['executed_amount']) + float(response_in_json['remaining_amount']) == int(5)
        self.assertLessEqual(float(response_in_json['avg_execution_price']), float(price))

    def test_buy_btc_usd_with_standard_order_with_auction_only_options_provided(self):
        currency_symbol = "btcusd"
        amount = "5"
        price = "3633.00"
        side = "buy"
        options = ["maker-or-cancel"]

        payload = helper.create_order_playload(endpoint,
                                               currency_symbol,
                                               amount,
                                               price,
                                               side,
                                               options=[options])

        e_payload = helper.encrypted_payload(payload)
        e_signature = helper.encrypted_signature(gemini_api_secret, e_payload)
        request_headers = helper.construct_request_header(gemini_api_key, e_payload, e_signature)

        self.response = requests.post(url,
                                      data=None,
                                      headers=request_headers)
        response_in_json = self.response.json()

        assert self.response.status_code == 201
        assert response_in_json['symbol'] == currency_symbol
        assert response_in_json['type'] == "exchange limit"
        assert response_in_json['side'] == "buy"
        assert response_in_json['option'] == []
        assert response_in_json['original_amount'] == amount
        assert float(response_in_json['executed_amount']) + float(response_in_json['remaining_amount']) == int(5)
        self.assertLessEqual(float(response_in_json['avg_execution_price']), float(price))

    def test_buy_btc_usd_with_standard_order_with_indication_of_interest_options_provided(self):
        currency_symbol = "btcusd"
        amount = "5"
        price = "3633.00"
        side = "buy"

        payload = helper.create_order_playload(endpoint,
                                               currency_symbol,
                                               amount,
                                               price,
                                               side)

        e_payload = helper.encrypted_payload(payload)
        e_signature = helper.encrypted_signature(gemini_api_secret, e_payload)
        request_headers = helper.construct_request_header(gemini_api_key, e_payload, e_signature)

        self.response = requests.post(url,
                                      data=None,
                                      headers=request_headers)
        response_in_json = self.response.json()

        assert self.response.status_code == 201
        assert response_in_json['symbol'] == currency_symbol
        assert response_in_json['type'] == "exchange limit"
        assert response_in_json['side'] == "buy"
        assert response_in_json['option'] == []
        assert response_in_json['original_amount'] == amount
        assert float(response_in_json['executed_amount']) + float(response_in_json['remaining_amount']) == int(5)
        self.assertLessEqual(float(response_in_json['avg_execution_price']), float(price))

    def test_buy_btc_usd_with_timestamp_in_ms_string_format(self):
        currency_symbol = "btcusd"
        amount = "5"
        price = "3633.00"
        side = "buy"

        payload = helper.create_order_playload(endpoint,
                                               currency_symbol,
                                               amount,
                                               price,
                                               side,
                                               timestamp_format="string",
                                               timestamp_unit="ms")

        e_payload = helper.encrypted_payload(payload)
        e_signature = helper.encrypted_signature(gemini_api_secret, e_payload)
        request_headers = helper.construct_request_header(gemini_api_key, e_payload, e_signature)

        self.response = requests.post(url,
                                      data=None,
                                      headers=request_headers)
        response_in_json = self.response.json()

        assert self.response.status_code == 201
        assert response_in_json['symbol'] == currency_symbol
        assert response_in_json['type'] == "exchange limit"
        assert response_in_json['side'] == "buy"
        assert response_in_json['option'] == []
        assert response_in_json['original_amount'] == amount
        assert float(response_in_json['executed_amount']) + float(response_in_json['remaining_amount']) == int(5)
        self.assertLessEqual(float(response_in_json['avg_execution_price']), float(price))

    def test_buy_btc_usd_with_timestamp_in_ms_int_format(self):
        currency_symbol = "btcusd"
        amount = "5"
        price = "3633.00"
        side = "buy"

        payload = helper.create_order_playload(endpoint,
                                               currency_symbol,
                                               amount,
                                               price,
                                               side,
                                               timestamp_format="int",
                                               timestamp_unit="ms")

        e_payload = helper.encrypted_payload(payload)
        e_signature = helper.encrypted_signature(gemini_api_secret, e_payload)
        request_headers = helper.construct_request_header(gemini_api_key, e_payload, e_signature)

        self.response = requests.post(url,
                                      data=None,
                                      headers=request_headers)
        response_in_json = self.response.json()

        assert self.response.status_code == 201
        assert response_in_json['symbol'] == currency_symbol
        assert response_in_json['type'] == "exchange limit"
        assert response_in_json['side'] == "buy"
        assert response_in_json['option'] == []
        assert response_in_json['original_amount'] == amount
        assert float(response_in_json['executed_amount']) + float(response_in_json['remaining_amount']) == int(5)
        self.assertLessEqual(float(response_in_json['avg_execution_price']), float(price))

    def test_buy_btc_usd_with_invalid_endpoint(self):
        currency_symbol = "btcusd"
        amount = "5"
        price = "3633.00"
        side = "buy"
        base_url = "https://api.gemini.com"
        endpoint = "/v1/order/new2"
        url = base_url + endpoint

        payload = helper.create_order_playload(endpoint,
                                               currency_symbol,
                                               amount,
                                               price,
                                               side,
                                               timestamp_format="string",
                                               timestamp_unit="ms")

        e_payload = helper.encrypted_payload(payload)
        e_signature = helper.encrypted_signature(gemini_api_secret, e_payload)
        request_headers = helper.construct_request_header(gemini_api_key, e_payload, e_signature)

        self.response = requests.post(url,
                                      data=None,
                                      headers=request_headers)
        response_in_json = self.response.json()

        assert self.response.status_code == 400
        assert response_in_json['result'] == 'error'
        assert response_in_json['reason'] == 'EndpointNotFound'
        self.assertTrue('message' in response_in_json)

    def test_buy_btc_usd_with_invalid_symbol(self):
        currency_symbol = "usdbtc"
        amount = "5"
        price = "3633.00"
        side = "buy"
        options = []

        payload = helper.create_order_playload(endpoint,
                                               currency_symbol,
                                               amount,
                                               price,
                                               side,
                                               options=options)

        e_payload = helper.encrypted_payload(payload)
        e_signature = helper.encrypted_signature(gemini_api_secret, e_payload)
        request_headers = helper.construct_request_header(gemini_api_key, e_payload, e_signature)

        self.response = requests.post(url,
                                      data=None,
                                      headers=request_headers)
        response_in_json = self.response.json()

        assert self.response.status_code == 400
        assert response_in_json['result'] == 'error'
        assert response_in_json['reason'] == 'InvalidSymbol'
        self.assertTrue('message' in response_in_json)

    def test_buy_btc_usd_with_empty_symbol(self):
        currency_symbol = ""
        amount = "5"
        price = "3633.00"
        side = "buy"
        options = []

        payload = helper.create_order_playload(endpoint,
                                               currency_symbol,
                                               amount,
                                               price,
                                               side,
                                               options=options)

        e_payload = helper.encrypted_payload(payload)
        e_signature = helper.encrypted_signature(gemini_api_secret, e_payload)
        request_headers = helper.construct_request_header(gemini_api_key, e_payload, e_signature)

        self.response = requests.post(url,
                                      data=None,
                                      headers=request_headers)
        response_in_json = self.response.json()

        assert self.response.status_code == 400
        assert response_in_json['result'] == 'error'
        assert response_in_json['reason'] == 'InvalidSymbol'
        self.assertTrue('message' in response_in_json)

    def test_buy_btc_usd_without_side_specific(self):
        currency_symbol = "usdbtc"
        amount = "5"
        price = "3633.00"
        side = ""
        options = []

        payload = helper.create_order_playload(endpoint,
                                               currency_symbol,
                                               amount,
                                               price,
                                               side,
                                               options=options)

        e_payload = helper.encrypted_payload(payload)
        e_signature = helper.encrypted_signature(gemini_api_secret, e_payload)
        request_headers = helper.construct_request_header(gemini_api_key, e_payload, e_signature)

        self.response = requests.post(url,
                                      data=None,
                                      headers=request_headers)
        response_in_json = self.response.json()

        assert self.response.status_code == 400
        assert response_in_json['result'] == 'error'
        assert response_in_json['reason'] == 'InvalidSide'
        self.assertTrue('message' in response_in_json)

    def test_buy_btc_usd_with_invalid_timestamp(self):
        currency_symbol = "usdbtc"
        amount = "5"
        price = "3633.00"
        side = "buy"
        options = []

        payload = helper.create_order_playload(endpoint,
                                               currency_symbol,
                                               amount,
                                               price,
                                               side,
                                               options=options)

        e_payload = helper.encrypted_payload(payload)
        e_signature = helper.encrypted_signature(gemini_api_secret, e_payload)
        request_headers = helper.construct_request_header(gemini_api_key, e_payload, e_signature)

        self.response = requests.post(url,
                                      data=None,
                                      headers=request_headers)
        response_in_json = self.response.json()

        assert self.response.status_code == 400
        assert response_in_json['result'] == 'error'
        assert response_in_json['reason'] == 'InvalidSymbol'
        self.assertTrue('message' in response_in_json)

    def test_buy_btc_usd_without_SSL(self):
        base_url = "http://api.gemini.com"
        endpoint = "/v1/order/new"
        url = base_url + endpoint
        currency_symbol = "usdbtc"
        amount = "5"
        price = "3633.00"
        side = "buy"
        options = []

        payload = helper.create_order_playload(endpoint,
                                               currency_symbol,
                                               amount,
                                               price,
                                               side,
                                               options=options)

        e_payload = helper.encrypted_payload(payload)
        e_signature = helper.encrypted_signature(gemini_api_secret, e_payload)
        request_headers = helper.construct_request_header(gemini_api_key, e_payload, e_signature)

        self.response = requests.post(url,
                                      data=None,
                                      headers=request_headers)
        response_in_json = self.response.json()

        assert self.response.status_code == 400
        assert response_in_json['result'] == 'error'
        assert response_in_json['reason'] == 'NoSSL'
        self.assertTrue('message' in response_in_json)

    def test_buy_btc_usd_without_trader_role(self):
        currency_symbol = "usdbtc"
        amount = "5"
        price = "3633.00"
        side = "buy"
        options = []
        gemini_api_secret = "api_secret_without_trader_role"
        gemini_api_key = "api_key_without_trader_role"

        payload = helper.create_order_playload(endpoint,
                                               currency_symbol,
                                               amount,
                                               price,
                                               side,
                                               options=options)

        e_payload = helper.encrypted_payload(payload)
        e_signature = helper.encrypted_signature(gemini_api_secret, e_payload)
        request_headers = helper.construct_request_header(gemini_api_key, e_payload, e_signature)

        self.response = requests.post(url,
                                      data=None,
                                      headers=request_headers)
        response_in_json = self.response.json()

        assert self.response.status_code == 400
        assert response_in_json['result'] == 'error'
        assert response_in_json['reason'] == 'MissingRole'
        self.assertTrue('message' in response_in_json)

    def test_buy_btc_usd_without_sufficient_funds(self):
        # required another account api key and secret without sufficient
        # for now, we will going to use billions of dollar on the price
        currency_symbol = "usdbtc"
        amount = "5"
        price = "1000000000.00"
        side = "buy"
        options = []
        gemini_api_secret = "api_secret_without_trader_role"
        gemini_api_key = "api_key_without_trader_role"

        payload = helper.create_order_playload(endpoint,
                                               currency_symbol,
                                               amount,
                                               price,
                                               side,
                                               options=options)

        e_payload = helper.encrypted_payload(payload)
        e_signature = helper.encrypted_signature(gemini_api_secret, e_payload)
        request_headers = helper.construct_request_header(gemini_api_key, e_payload, e_signature)

        self.response = requests.post(url,
                                      data=None,
                                      headers=request_headers)
        response_in_json = self.response.json()

        assert self.response.status_code == 400
        assert response_in_json['result'] == 'error'
        assert response_in_json['reason'] == 'InsufficientFunds'
        self.assertTrue('message' in response_in_json)

    def test_buy_btc_usd_with_standard_order_with_negative_amount_provided(self):
        currency_symbol = "btcusd"
        amount = "-5"
        price = "3633.00"
        side = "buy"

        payload = helper.create_order_playload(endpoint,
                                               currency_symbol,
                                               amount,
                                               price,
                                               side)

        e_payload = helper.encrypted_payload(payload)
        e_signature = helper.encrypted_signature(gemini_api_secret, e_payload)
        request_headers = helper.construct_request_header(gemini_api_key, e_payload, e_signature)

        self.response = requests.post(url,
                                      data=None,
                                      headers=request_headers)
        response_in_json = self.response.json()

        assert self.response.status_code == 400
        assert response_in_json['result'] == 'error'
        assert response_in_json['reason'] == 'InvalidQuantity'
        self.assertTrue('message' in response_in_json)

    def test_buy_btc_usd_with_standard_order_with_negative_price_provided(self):
        currency_symbol = "btcusd"
        amount = "5"
        price = "-3633.00"
        side = "buy"

        payload = helper.create_order_playload(endpoint,
                                               currency_symbol,
                                               amount,
                                               price,
                                               side)

        e_payload = helper.encrypted_payload(payload)
        e_signature = helper.encrypted_signature(gemini_api_secret, e_payload)
        request_headers = helper.construct_request_header(gemini_api_key, e_payload, e_signature)

        self.response = requests.post(url,
                                      data=None,
                                      headers=request_headers)
        response_in_json = self.response.json()

        assert self.response.status_code == 400
        assert response_in_json['result'] == 'error'
        assert response_in_json['reason'] == 'InvalidPrice'
        self.assertTrue('message' in response_in_json)

    def test_buy_btc_usd_with_standard_order_with_negative_price_amount_provided(self):
        currency_symbol = "btcusd"
        amount = "-5"
        price = "-3633.00"
        side = "buy"

        payload = helper.create_order_playload(endpoint,
                                               currency_symbol,
                                               amount,
                                               price,
                                               side)

        e_payload = helper.encrypted_payload(payload)
        e_signature = helper.encrypted_signature(gemini_api_secret, e_payload)
        request_headers = helper.construct_request_header(gemini_api_key, e_payload, e_signature)

        self.response = requests.post(url,
                                      data=None,
                                      headers=request_headers)
        response_in_json = self.response.json()

        # It will be either InvalidQuantity or InvalidPrice or both
        assert self.response.status_code == 400
        assert response_in_json['result'] == 'error'
        assert response_in_json['reason'] == 'InvalidQuantity'
        self.assertTrue('message' in response_in_json)

    def test_buy_btc_usd_with_standard_order_with_two_options_provided(self):
        currency_symbol = "btcusd"
        amount = "5"
        price = "3633.00"
        side = "buy"
        options = ["maker-or-cancel", "immediate-or-cancel"]

        payload = helper.create_order_playload(endpoint,
                                               currency_symbol,
                                               amount,
                                               price,
                                               side,
                                               options=options)

        e_payload = helper.encrypted_payload(payload)
        e_signature = helper.encrypted_signature(gemini_api_secret, e_payload)
        request_headers = helper.construct_request_header(gemini_api_key, e_payload, e_signature)

        self.response = requests.post(url,
                                      data=None,
                                      headers=request_headers)
        response_in_json = self.response.json()

        assert self.response.status_code == 400
        assert response_in_json['result'] == 'error'
        assert response_in_json['reason'] == 'ConflictingOptions'
        self.assertTrue('message' in response_in_json)

    def test_buy_btc_usd_with_standard_order_with_three_options_provided(self):
        currency_symbol = "btcusd"
        amount = "5"
        price = "3633.00"
        side = "buy"
        options = ["maker-or-cancel", "immediate-or-cancel", "auction_only"]

        payload = helper.create_order_playload(endpoint,
                                               currency_symbol,
                                               amount,
                                               price,
                                               side,
                                               options=options)

        e_payload = helper.encrypted_payload(payload)
        e_signature = helper.encrypted_signature(gemini_api_secret, e_payload)
        request_headers = helper.construct_request_header(gemini_api_key, e_payload, e_signature)

        self.response = requests.post(url,
                                      data=None,
                                      headers=request_headers)
        response_in_json = self.response.json()

        assert self.response.status_code == 400
        assert response_in_json['result'] == 'error'
        assert response_in_json['reason'] == 'ConflictingOptions'
        self.assertTrue('message' in response_in_json)

    def test_buy_btc_usd_with_deleted_api_key_and_secret(self):
        currency_symbol = "btcusd"
        amount = "5"
        price = "3633.00"
        side = "buy"
        gemini_api_secret = "delete_api_secret"
        gemini_api_key = "delete_api_key"

        payload = helper.create_order_playload(endpoint,
                                               currency_symbol,
                                               amount,
                                               price,
                                               side)

        e_payload = helper.encrypted_payload(payload)
        e_signature = helper.encrypted_signature(gemini_api_secret, e_payload)
        request_headers = helper.construct_request_header(gemini_api_key, e_payload, e_signature)

        self.response = requests.post(url,
                                      data=None,
                                      headers=request_headers)
        response_in_json = self.response.json()

        assert self.response.status_code == 400
        assert response_in_json['result'] == 'error'
        assert response_in_json['reason'] == 'ConflictingOptions'
        self.assertTrue('message' in response_in_json)

    # Sell btc test start from here
    def test_sell_btc_usd_with_standard_order_via_empty_array_without_client_id(self):
        currency_symbol = "btcusd"
        amount = "5"
        price = "3633.00"
        side = "sell"
        options = []

        payload = helper.create_order_playload(endpoint,
                                               currency_symbol,
                                               amount,
                                               price,
                                               side,
                                               options=options)

        e_payload = helper.encrypted_payload(payload)
        e_signature = helper.encrypted_signature(gemini_api_secret, e_payload)
        request_headers = helper.construct_request_header(gemini_api_key, e_payload, e_signature)

        self.response = requests.post(url,
                                      data=None,
                                      headers=request_headers)
        response_in_json = self.response.json()

        assert self.response.status_code == 400
        assert response_in_json['symbol'] == currency_symbol
        assert response_in_json['type'] == "exchange limit"
        assert response_in_json['side'] == "buy"
        assert response_in_json['option'] == []
        assert response_in_json['original_amount'] == amount
        assert float(response_in_json['executed_amount']) + float(response_in_json['remaining_amount']) == int(5)
        self.assertLessEqual(float(response_in_json['avg_execution_price']), float(price))

    def test_sell_btc_usd_with_standard_order_via_empty_array_with_client_id(self):
        currency_symbol = "btcusd"
        amount = "5"
        price = "3633.00"
        side = "sell"
        options = []
        client_order_id = helper.generate_random_id(8)

        payload = helper.create_order_playload(endpoint,
                                               currency_symbol,
                                               amount,
                                               price,
                                               side,
                                               options=options,
                                               with_client_order_id=client_order_id)

        e_payload = helper.encrypted_payload(payload)
        e_signature = helper.encrypted_signature(gemini_api_secret, e_payload)
        request_headers = helper.construct_request_header(gemini_api_key, e_payload, e_signature)

        self.response = requests.post(url,
                                      data=None,
                                      headers=request_headers)
        response_in_json = self.response.json()

        assert self.response.status_code == 400
        assert response_in_json['symbol'] == currency_symbol
        assert response_in_json['type'] == "exchange limit"
        assert response_in_json['side'] == "buy"
        assert response_in_json['option'] == []
        assert response_in_json['original_amount'] == amount
        assert float(response_in_json['executed_amount']) + float(response_in_json['remaining_amount']) == int(5)
        assert response_in_json['client_order_id'] == client_order_id
        self.assertLessEqual(float(response_in_json['avg_execution_price']), float(price))

    def test_sell_btc_usd_with_standard_order_with_negative_amount_provided(self):
        currency_symbol = "btcusd"
        amount = "-5"
        price = "3633.00"
        side = "sell"
        options = []
        client_order_id = helper.generate_random_id(8)

        payload = helper.create_order_playload(endpoint,
                                               currency_symbol,
                                               amount,
                                               price,
                                               side,
                                               options=options,
                                               with_client_order_id=client_order_id)

        e_payload = helper.encrypted_payload(payload)
        e_signature = helper.encrypted_signature(gemini_api_secret, e_payload)
        request_headers = helper.construct_request_header(gemini_api_key, e_payload, e_signature)

        self.response = requests.post(url,
                                      data=None,
                                      headers=request_headers)
        response_in_json = self.response.json()

        assert self.response.status_code == 400
        assert response_in_json['result'] == 'error'
        assert response_in_json['reason'] == 'InvalidQuantity'
        self.assertTrue('message' in response_in_json)

    def test_sell_btc_usd_with_standard_order_with_negative_price_provided(self):
        currency_symbol = "btcusd"
        amount = "5"
        price = "-3633.00"
        side = "sell"
        options = []
        client_order_id = helper.generate_random_id(8)

        payload = helper.create_order_playload(endpoint,
                                               currency_symbol,
                                               amount,
                                               price,
                                               side,
                                               options=options,
                                               with_client_order_id=client_order_id)

        e_payload = helper.encrypted_payload(payload)
        e_signature = helper.encrypted_signature(gemini_api_secret, e_payload)
        request_headers = helper.construct_request_header(gemini_api_key, e_payload, e_signature)

        self.response = requests.post(url,
                                      data=None,
                                      headers=request_headers)
        response_in_json = self.response.json()

        assert self.response.status_code == 400
        assert response_in_json['result'] == 'error'
        assert response_in_json['reason'] == 'InvalidPrice'
        self.assertTrue('message' in response_in_json)

    def test_sell_btc_usd_with_standard_order_with_negative_price_amount_provided(self):
        currency_symbol = "btcusd"
        amount = "-5"
        price = "-3633.00"
        side = "sell"
        options = []
        client_order_id = helper.generate_random_id(8)

        payload = helper.create_order_playload(endpoint,
                                               currency_symbol,
                                               amount,
                                               price,
                                               side,
                                               options=options,
                                               with_client_order_id=client_order_id)

        e_payload = helper.encrypted_payload(payload)
        e_signature = helper.encrypted_signature(gemini_api_secret, e_payload)
        request_headers = helper.construct_request_header(gemini_api_key, e_payload, e_signature)

        self.response = requests.post(url,
                                      data=None,
                                      headers=request_headers)
        response_in_json = self.response.json()

        assert self.response.status_code == 400
        assert response_in_json['result'] == 'error'
        assert response_in_json['reason'] == 'InvalidPrice'
        self.assertTrue('message' in response_in_json)

if __name__ == '__main__':
    unittest.main()