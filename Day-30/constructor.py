'''

class Flipkart:
    products = {'shirts':1000,'handbag':2000,'pants':3000}
    discount = 30

    @classmethod
    def display(cls):
        print(cls.products)

    def userinfo(self,name,phone,address):
        self.name = name
        self.phone = phone
        self.address = address
        print(f"Hello {self.name}, Welcome to the Flipkart")


    @staticmethod  #helper function
    def displaydiscount():
        print(f"{Flipkart.discount}% is going to provide discount")

avinash = Flipkart()
avinash.userinfo('avinash',8106686988,'hyd')
avinash.display()
avinash.displaydiscount()
print(avinash.products)
print(avinash.name)

Flipkart.displaydiscount()
Flipkart.display()
print(Flipkart.products)

bharat = Flipkart()
bharat.userinfo('bharat',9925357291,'che')
bharat.display()
bharat.displaydiscount()

ganesh = Flipkart()
ganesh.userinfo('ganesh',6282965272,'ban')
ganesh.display()
ganesh.displaydiscount()

'''

'''
class Flipkart:
    def __init__(self,name,phone):
        self.name = name
        self.phone = phone
        print(f"Hello {self.name},Welcome to the flipkart")

avinash = Flipkart('avinash',8106686988)
lokesh = Flipkart('lokesh',6304939976)
bharat = Flipkart('bharat',9876543210)

'''

