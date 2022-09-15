# make the class variables as private
# write getters and setter to get and update the variables  

class Users:
    def __init__(self, u=None):
        self.__username = u
    
    def setUsername(self, x):
        self.__username = x

    def getUsername(self):
        return (self.__username)


sai = Users('sai dharaneesh')

sai.__username="dharaneesh"

print('before setting:', sai.getUsername())
sai.setUsername("gurram sai dharaneesh")
print('after setting', sai.getUsername())


class User:
    def __init__(self, userName=None, password=None):
        self.__userName = userName
        self.__password = password
    
    def login(self, userName, password):
        if ((self.__userName.lower() == userName.lower()) and (self.__password == password)):
            print('Access Granted against username:', self.__userName.lower(), "and password:", self.__password)
        else:
            print('Invalid Credentials!')



sai = User('sai', '1234')
sai.login('Sai', '1234')

dharaneesh = User('dharaneesh', '12345')
dharaneesh.login('dharaneesh', '1234')