class Engine:
    volume = 0
    number_of_horsepower = 0
    type = ''
    torque_moment = 0
    fuel_type=''
    def __init__(self, volume, number_of_horsepower, type, torque_moment, fuel_type):
        self.volume=volume
        self.number_of_horsepower=number_of_horsepower
        self.type=type
        self.torque_moment = torque_moment
        self.fuel_type=fuel_type
class Wheels:
    diam=0
    type=''
    season =''
    def __init__(self, diam, type, season):
        self.diam=diam
        self.type=type
        self.season=season
class Body:
    metal=''
    weight=''
    type =''
    def __init__(self,metal,weight,type):
        self.metal=metal
        self.weight=weight
        self.type=type
class automobile:
    name=''
    type_of_transmission =''
    def __init__(self, name, type_of_transmission, engine, wheels,body):
        self.type_of_transmission=type_of_transmission
        self.engine=engine
        self.wheels=wheels
        self.body=body
        self.name=name
engine1=Engine(1.8, 140,'injector', 145, 'dizel')
wheels1=Wheels(23, 'lit', 'let')
body1= Body('zink', 800, 'sedan')

automobile1=automobile('lada', 'automat',engine1, wheels1,body1)
print(automobile1.engine.volume)







