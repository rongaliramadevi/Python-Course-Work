class Whatsapp_v1:
    def messaging(self):
        print("you can message")

    def sharepics(self):
        print("you can send pictures")
        
#single Inheritance
class Whatsapp_v2(Whatsapp_v1):
    def status(self):
        print("You can upload status")

    def videos(self):
        print("You can share videos")

#multilevel inheritance

class Whatsapp_v3(Whatsapp_v2):
    def calls(self):
        print("You can do video and audio calls")

    def groups(self):
        print("You can share videos")

class Community:
    def clubgroup(self):
        print("you can create a community with clubing  the groups")
        
#base meta class
class Meta:
    def chat(self):
        print("you can chat")
        
#single
class Meta1(Meta):
    def ai_images(self):
        print("You can generate images")

#single
class Meta2(Meta):
    def human_emotions(self):
        print("Now you can share your feelings")
        
#multiple
class Meta3(Meta1,Meta2):
    def technical(self):
        print("you can ask technicl questions also. Meta can provide all kind of things")

#hybrid
class Whatsapp_v4(Whatsapp_v3,Community,Meta3):
    def channel(self):
        print("You can create channel to engage with followers") 
        
rama=Whatsapp_v1()#object 
print("rama-v1")
rama.messaging()
rama.sharepics()


santosh=Whatsapp_v2()
print("santosh-v2")
santosh.status()
santosh.videos()
santosh.messaging()
santosh.sharepics()


harsha=Whatsapp_v3()
print("\n\nharsh-v3")
harsha.calls()
harsha.groups()
harsha.status()
harsha.videos()
harsha.messaging()
harsha.sharepics() 


randheer=Whatsapp_v4()
print("\n\nRandheer-v4")
randheer.calls()
randheer.groups()
randheer.status()
randheer.videos()
randheer.messaging()
randheer.sharepics()
randheer.channel()
randheer.clubgroup()
randheer.chat()
randheer.ai_images()
randheer.human_emotions()
randheer.technical()