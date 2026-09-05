
# Abstraction means hiding the internal implementation details of a class and exposing only the essential features to the user.

from abc import ABC,abstractmethod 

class Phonepay:
    def senderinfo(self):
        print("You can their mobile number or scanner")
    def amount(self):
        print("You can enter amount")
    def pin(self):
        print("You need enter the pin")

    @abstractmethod
    def transaction(self):
        pass


class HDFC(Phonepay):
    def transaction(self):
        print("Payment using hdfc bank")

class SBI(Phonepay):
    def transaction(self):
        print("Payment using sbi bank")

class BOB(Phonepay):
    def transaction(self):
        print("Payment using bob bank")

class UNION(Phonepay):
    def transaction(self):
        print("Payment using union bank")

class ICIC(Phonepay):
    def transaction(self):
        print("Payment using icic bank")

class AXIS(Phonepay):
    def transaction(self):
        print("Payment using axis bank")


user1=HDFC()
user1.senderinfo()
user1.amount()
user1.pin()
user1.transaction()

user1=SBI()
user1.senderinfo()
user1.amount()
user1.pin()
user1.transaction()


user1=AXIS()
user1.senderinfo()
user1.amount()
user1.pin()
user1.transaction()


user1=UNION()
user1.senderinfo()
user1.amount()
user1.pin()
user1.transaction()

user1=ICIC()
user1.senderinfo()
user1.amount()
user1.pin()
user1.transaction()