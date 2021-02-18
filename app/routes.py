from app import app
from flask.views import MethodView
from app.controllers.process_payment_controller import ProcessPaymentController

app.add_url_rule("/api/processpayment", view_func=ProcessPaymentController.as_view("processpayment_api"))

if __name__ == "__main__":
    app.run()