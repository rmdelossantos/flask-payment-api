from flask.views import MethodView
from flask import request, jsonify
from flask_expects_json import expects_json
from app.models.process_payment_model import PaymentModel
import json

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

class ProcessPaymentController(MethodView):
    def get(self):
        return "Responding to a GET request"

    @expects_json(payment_request_schema)
    def post(self):
        request_json = request.get_json()
        request_process = PaymentModel()
        return request_process.processpayment(request_json)

    def put(self):
        return "Responding to a PUT request"

    def patch(self):
        return "Responding to a PATCH request"

    def delete(self):
        return "Responding to a DELETE request"