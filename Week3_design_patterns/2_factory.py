
from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def pay(self):
        pass


class UPIPayment(Payment):

    def pay(self):
        print("UPI Payment")


class CardPayment(Payment):

    def pay(self):
        print("Card Payment")


class PaymentFactory:

    @staticmethod
    def create_payment(payment_type):

        if payment_type == "UPI":
            return UPIPayment()

        elif payment_type == "CARD":
            return CardPayment()

        raise ValueError("Invalid Payment Type")


payment = PaymentFactory.create_payment("UPI")
payment.pay()

