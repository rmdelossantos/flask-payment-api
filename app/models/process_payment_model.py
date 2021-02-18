from flask import jsonify

class PaymentModel():
    def processpayment(self, request_json):
        try:
            amount = float(request_json["Amount"])
            if amount < 20 and amount > 0:
                return self.__cheappaymentgateway()
            elif amount >= 20 and amount <= 500:
                return self.__expensivepaymentgateway()
            else:
                return self.__premiumpaymentgateway()
        except:
            response = jsonify({"message": str("An Error has occured"), "status": "ERROR", "code": 400})
            response.headers["Content-Type"] = "application/json"
            return response


    def __premiumpaymentgateway(self):
        response = jsonify({"message": str("Payment Processed via Premium Gateway"), "status": "PROCESSED", "code": 200})
        response.headers["Content-Type"] = "application/json"
        return response

    def __expensivepaymentgateway(self):
        response = jsonify({"message": str("Payment Processed via Expensive Gateway"), "status": "PROCESSED", "code": 200})
        response.headers["Content-Type"] = "application/json"
        return response

    def __cheappaymentgateway(self):
        response = jsonify({"message": str("Payment Processed"), "Status": "PROCESSED", "code": 200})
        response.headers["Content-Type"] = "application/json"
        return response
