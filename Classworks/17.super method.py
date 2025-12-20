#super method

class Whatsapp_v1:
    def status(self):
        print("upload picture and videos with limited duration")

class Whatsapp_v2:
    def status(self):
        print("yOU CAN LIKE THE STATUS AND AND MENTION THE PEOPLE")

class Whatsapp_v3(Whatsapp_v1,Whatsapp_v2):
    def status(self):
        Whatsapp_v1.status(self)
        Whatsapp_v2.status(self)
        
        print("you can add music and share the stroy to different apps")
        
        
    
rama=Whatsapp_v3()
rama.status()

