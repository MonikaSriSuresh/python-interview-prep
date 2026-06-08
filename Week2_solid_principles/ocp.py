"""
Open Closed Principle
"""

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


payment = UPIPayment()

payment.pay()