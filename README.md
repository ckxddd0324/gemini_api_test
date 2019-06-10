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
![Test Case Mind Map](https://coggle-downloads-production.s3.eu-west-1.amazonaws.com/21a3d1dcc4fb7cd1ce2ea5c40093f914e411491a9f150b99e24ff733209962ba/v1ordernew.png?AWSAccessKeyId=ASIA4YTCGXFHERF6XXV7&Expires=1560081066&Signature=pc5bVY%2FyRsFEmKwXxdYwsufVWTA%3D&x-amz-security-token=AgoJb3JpZ2luX2VjEEUaCWV1LXdlc3QtMSJIMEYCIQCz7UDO0t8Yz1Dj3gZvKdTKmDp9uwY%2B9U%2FI0rFd3w30cgIhAMqfGoqbQNBhjmlZ00oRQZ3xsmWTEiNydx%2BMoMGySEWmKpMCCG4QABoMODc3NDUzMDMxNzU4IgxbguzBBJ1EtH46%2BmYq8AGtYeZvFyVf0FwswmiZhrnKLegmL5o9OetaV8vNkacZSoHTVQmnfIUL3bvC6Asg2icSa5oyMCqVjhCznbGVV0hUmksgLh7DdOxmDaOfcIIuEcfQg4uu3AzBFTkCUSM7AhjDGCcUAc08xXApERHCnhL36vopobGDpaALKE8m195NB1Dgyk5QYQh6S92W0KpF2Y%2FPzN5lQ6BVMGZ9c4W8OdzKk6tHNuHKKA98hUc5X1pW98K7aPspllTBSVPZcb6TLGNd3ioxW8WQHbTqWtat65vMc1Ko7D7pdo8HVhe9lMJXN%2F6JIKCV3Hl5kx6RlyX6A7ow2Zvy5wU6swHhAoMNlMrGrUmnjQO51Z2JkrxOiC34KZX1UAqpyVv1%2BO1ef6Qu5Pa1k1HOdlbsyi6bmmdxytUDIwPskjOugLYhWJEdllOg%2BX1ppuzwwNQv8qDAiV52sKo5jKRUDaLgfeULX3KqkDMbx06c%2BZoOZwCMcIbEufTZWxYP7Cxb87IboNqflTrFCeKTSrsxSP5QS4GGB3w2pqBDuUuDFkHvcwYfsO74yY0gE%2Fa%2BcIt2bxzkHgu6eg%3D%3D)
