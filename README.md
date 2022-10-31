# MS361
This is a REST API microservice that takes in a currency (by currency code) and amount to be converted (in U.S. dollars), and returns the requested conversion in JSON format.

## Using the service
To use the service, send a GET request to https://ms361.herokuapp.com/convert with the parameters "?curr=<currency_code>&amount=<integer/float>".
For example, https://ms361.herokuapp.com/convert?curr=GBP&amount=100 will convert $100 USD to British pounds. 

## Conversion and response
Once the request is received, the service will call a seperate currency conversion API, perform the conversion in the currency specified, and return a JSON object with the currency and amount.

#### Sample request and response:
Request: https://ms361.herokuapp.com/convert?curr=AED&amount=300

Response: {"currency": "AED", "converted_total": "1101.91"}

## UML Sequence Diagram

![image](https://user-images.githubusercontent.com/39362175/199093337-9ff63e22-f9b7-4baa-9448-a66c7d0ceffe.png)


## Notes:
The microservice supports all currencies, but the correct three-letter currency code must be used. 
