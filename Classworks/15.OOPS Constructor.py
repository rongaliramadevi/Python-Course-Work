class Instagram():
    def __init__(self,username,pwd):
        self.username=username
        self.password=pwd
        self.bio=''
        self.followers={}
        self.following={}
        print(f"welcome to the Instagram,have fun!!!")
        print(f"username: {self.username}")
        print(f"password: {self.password}")

Rama=Instagram("Rama","r@2004") 



class Instagram():
    def __init__(self,username,pwd):
        self.username=username
        self.password=pwd
        self.post=[]


Rama=Instagram("Rama","r@2004")
print(f"Before: {Rama.username}")
Rama.username="Devi"
print(f"After: {Rama.username}") 



class Instagram():
    def __init__(self,username,pwd):
        self.username=username
        self.__password=pwd
        self._post=[]

    def getPassword(self):
        return self.__password

    def setPassword(self, newPassword):
        self.__password=newPassword
        print("Password updated")

    @property
    def viewPost(self):
        return self._post
    @viewPost.setter
    def viewPost(self, post):
        self._post.append(post)



rama=Instagram("rama","r@2004")
print(f"Before: {rama.username}")
rama.username="Devi"
print(f"After: {rama.username}")

print(f"Before: {rama.getPassword()}")
rama.setPassword("Devi@1004")
print(f"After: {rama.getPassword()}")

print(rama.viewPost)
rama.viewPost="hello"
rama.viewPost="First Reel"
print(rama.viewPost)



