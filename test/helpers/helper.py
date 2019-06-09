import datetime, time
import json
import base64
import hmac
import hashlib
import random
import string


def create_order_playload(request,
                        symbol,
                        amount,
                        price,
                        side,
                        options=[],
                        timestamp_format="string",
                        timestamp_unit="second",
                        with_client_order_id=None):

    t = datetime.datetime.now()
    unix_timestamp_second = int(time.mktime(t.timetuple()))
    nonce = unix_timestamp_second * 1000 if timestamp_unit == "ms" else unix_timestamp_second
    nonce = str(nonce) if timestamp_format == "string" else nonce

    payload = {
        "request": request,
        "nonce": nonce,
        "symbol": symbol,
        "amount": amount,
        "price": price,
        "side": side,
        "type": "exchange limit",
        "options": options
    }

    if with_client_order_id:
        payload['client_order_id']= with_client_order_id

    return payload

def encrypted_payload(payload):
    encoded_payload = json.dumps(payload).encode()
    return base64.b64encode(encoded_payload)

def encrypted_signature(secret, payload):
    return hmac.new(secret.encode(), payload, hashlib.sha3_384).hexdigest()

def construct_request_header(api_key, payload, signature):
    return {
        "Content-Type": "text/plain",
        "Content-Length": "0",
        "X-GEMINI-APIKEY": api_key,
        "X-GEMINI-PAYLOAD": payload,
        "signature": signature,
        "Cache-Control": "no-cache"
    }

def generate_random_id(length=1, letter_format='mixed', with_num=True, with_acceptable_symbols=True):
    acceptable_symbols = '#-.:_'
    string_combo = ''

    if letter_format != 'mixed':
        if letter_format.lower() == 'upper':
            string_combo += string.ascii_uppercase
        elif letter_format.lower() == 'lower':
            string_combo += string.ascii_lowercase

    string_combo += string.digits if with_num else string_combo
    string_combo += acceptable_symbols if with_acceptable_symbols else string_combo
    return ''.join([random.choice(string_combo) for n in range(length)])
