
from abc import ABC, abstractmethod


class PaymentStrategy(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class UPIPayment(PaymentStrategy):

    def pay(self, amount):
        print(f"UPI Payment: {amount}")


class CardPayment(PaymentStrategy):

    def pay(self, amount):
        print(f"Card Payment: {amount}")


class PaymentProcessor:

    def __init__(self, strategy):
        self.strategy = strategy

    def process(self, amount):
        self.strategy.pay(amount)


processor = PaymentProcessor(UPIPayment())
processor.process(1000)

processor = PaymentProcessor(CardPayment())
processor.process(2000)

