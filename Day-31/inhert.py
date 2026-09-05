''' 
.........multilevel inheritance.........(single parent, single child)..........

class whatsappV1:
    def messaging(self):
        print("you can message")


class whatsappV2(whatsappV1):
    def calls(self):
        print("you can audio and video calls")

class whatsappV3(whatsappV2):
    def status(self):
        print("you can add the status for 24 hours")

    
a = whatsappV1()
a.messaging()

b=whatsappV2()
b.messaging()
b.calls()

c=whatsappV3()
c.messaging()
c.calls()
c.status()

'''



'''
.....multiple..................(multiple parents,single child)...........

class whatsappV1:
    def messaging(self):
        print("you can message")


class whatsappV2():
    def calls(self):
        print("you can audio and video calls")

class whatsappV3(whatsappV1,whatsappV2):
    def status(self):
        print("you can add the status for 24 hours")

    
a = whatsappV1()
a.messaging()

b=whatsappV2()
b.calls()

c=whatsappV3()
c.messaging()
c.calls()
c.status()

'''

'''

...........hierarchy.........(single parent multiple childs).........

class whatsappV1:
    def messaging(self):
        print("you can message")


class whatsappV2(whatsappV1):
    def calls(self):
        print("you can audio and video calls")

class whatsappV3(whatsappV1):
    def status(self):
        print("you can add the status for 24 hours")

    
a = whatsappV1()
a.messaging()

b=whatsappV2()
b.messaging()
b.calls()

c=whatsappV3()
c.messaging()
c.status()


'''


'''
......hybrid.........(combination of two or more types of inheritance).........

class whatsappV1:
    def messaging(self):
        print("you can message")

class whatsappV2:
    def extramessages(self):
        print("you can emojis,stickers and gifs")


class whatsappV3(whatsappV1,whatsappV2):
    def calls(self):
        print("you can audio and video calls")

class whatsappV4(whatsappV3):
    def status(self):
        print("you can add the status for 24 hours")

    
a = whatsappV1()
a.messaging()

b=whatsappV2()
b.extramessages()

c=whatsappV3()
c.messaging()
c.extramessages()


c=whatsappV4()
c.messaging()
c.status()
c.extramessages()


'''
'''


.....using super method........

class whatsappV1:
    def status(self):
        print("you can add images and videos")

class whatsappV2(whatsappV1):
    def status(self):
        super().status()
        print("you can add music and stickers")


class whatsappV3(whatsappV2):
    def status(self):
        super().status()
        print("you can like and you can add reaction")

a=whatsappV1()
a.status()

b=whatsappV2()
b.status()

c=whatsappV2()
c.status()

'''


class whatsappV1:
    def status(self):
        print("you can add images and videos")

class whatsappV2(whatsappV1):
    def status(self):
        print("you can add music and stickers")


class whatsappV3():
    def status(self):
        whatsappV1.status(self)
        whatsappV2.status(self)
        print("you can like and you can add reaction")

a=whatsappV1()
a.status()

b=whatsappV2()
b.status()

c=whatsappV2()
c.status()
