# gemini_api_test
API test for Gemini /v1/order/new endpoint
The tests are going to primarily focusing on the currency symbo- btcusd.

# Installation 
- Install Python 3.7
- Install virtualenv with pip/pip3
	1. After installation of virtualenv, run virtualenv test_env
	2. source test_env/bin/activate
	3. pip3 install -r requirements.txt

## Setup API key and secret
Copy the .env_sample and rename it to .env. Then update the key and secret with your created credential. 

## Run test
`Run the following command on terminal- nose2 `

## Test Cases Mind Map
Documenting things/fields to test on create-order
![Test Case Mind Map](doc/test_case_mind_map.png)
