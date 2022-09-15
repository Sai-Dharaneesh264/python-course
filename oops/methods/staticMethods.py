# class Player:
#     teamName: 'Liverpool'

#     def __init__(self, name):
#         self.name = name
    
#     @staticmethod
#     def demo():
#         print("I am a static method")


# p1 = Player('lol')
# p1.demo()

# Player.demo()

class BodyInfo:
    @staticmethod
    def bmi(weight, height):
        return weight / (height ** 2)

    
weight = 75
height = 1.8
print(BodyInfo.bmi(weight, height))