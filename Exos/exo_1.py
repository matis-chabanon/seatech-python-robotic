import time

class Robot():
    name = "<unnamed>"
    power = False
    current_speed = 0
    battery_level = 0
    states = ['shutown', 'running']
    
    def __init__(self, name=None):
        if name:
            self.name = name
        self.current_state = self.states[0]
        self.power = False
	
    def allumer(self):
        self.power = True
    
    def eteindre(self):
        self.power = False
    
    def recharger(self):
        while self.battery_level < 100 :
            time.sleep(0.1)
            self.battery_level = self.battery_level +1
            print(self.battery_level)

    def set_deplacement(self , vitesse):
        self.current_speed = vitesse
    
    def get_deplacement(self):
        return self.current_speed
    
    def arret(self):
        self.current_speed = 0


""" print(Robot.name)
print("Robot power is %s"%(Robot.power))

r = Robot(name='Samuel')
print("Name of robot is : %s"%(r.name))
print(r.current_state)

r.allumer()
print("Robot power is : %s"%(r.power))

r.recharger()
print("Battery Level is : %s"%(r.battery_level) + "%")

r.set_deplacement(10)

print("La vitesse est de : %s"%(r.get_deplacement()) + "km/h")

r.arret()
print("La vitesse est de : %s"%(r.get_deplacement()) + "km/h") """