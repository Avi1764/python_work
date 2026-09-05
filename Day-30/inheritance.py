class whatsappV1:
    def __init__(self,name):
        self.name = name
        print(f"welcome to whatsapp-V1{self.name}!")

    def messaging(self):
        print("you can send message")


class whatsappV2:
    def __init__(self,name):
        self.name=name
        print(f"welcome to whatsapp-V1{self.name}!")

    
avinash = whatsappV1('avinash')
avinash.messaging()

lokesh=whatsappV2('lokesh')
lokesh.messaging()