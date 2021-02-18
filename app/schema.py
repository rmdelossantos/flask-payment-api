from flask_inputs import Inputs
from flask_inputs.validators import JsonSchema

payment_request_schema = {
    "type" : "object",
    "properties" :{
        "CreditCardNumber" : {
            "type": "string",
        },
        "CardHolder" : {
            "type": "string",
        },
        "ExpirationDate" : {
            "type": "string",
        },
        "SecurityCode" : {
            "type": "string",
        },
        "Amount" : {
            "type": "string",
        },
    },
    "required": ["CreditCardNumber", "CardHolder", "ExpirationDate", "Amount"]
}

class ProcessPaymentRequestSchema(Inputs):
    json = [JsonSchema(schema=payment_request_schema)]
