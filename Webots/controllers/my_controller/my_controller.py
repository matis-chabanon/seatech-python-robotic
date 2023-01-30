"""my_controller controller."""

from controller import Robot, Motor
#from EpuckMotors import EpuckMotors

class InitRobotMotor(Motor):

    def __init__(self, name):
        super().__init__(name)
        self.setPosition(float('inf'))
        self.setVelocity(0)

class RobotMotor():

    def __init__(self,speed=None):
        self.__front_left_wheel_joint = InitRobotMotor('front_left_wheel_joint')
        self.__front_right_wheel_joint = InitRobotMotor('front_right_wheel_joint')
        self.__back_left_wheel_joint = InitRobotMotor('back_left_wheel_joint')
        self.__back_right_wheel_joint = InitRobotMotor('back_right_wheel_joint')
    
    def avancer(self):
        self.__front_left_wheel_joint.setVelocity(10)
        self.__front_right_wheel_joint.setVelocity(10)
        self.__back_left_wheel_joint.setVelocity(10)
        self.__back_right_wheel_joint.setVelocity(10)


    def reculer(self):
        self.__front_left_wheel_joint.setVelocity(-10)
        self.__front_right_wheel_joint.setVelocity(-10)
        self.__back_left_wheel_joint.setVelocity(-10)
        self.__back_right_wheel_joint.setVelocity(-10)
    
    def gauche(self):
        self.__front_left_wheel_joint.setVelocity(7)
        self.__front_right_wheel_joint.setVelocity(10)
        self.__back_left_wheel_joint.setVelocity(7)
        self.__back_right_wheel_joint.setVelocity(10)

    def droite(self):
        self.__front_left_wheel_joint.setVelocity(8)
        self.__front_right_wheel_joint.setVelocity(-2)
        self.__back_left_wheel_joint.setVelocity(13)
        self.__back_right_wheel_joint.setVelocity(-3)

class Combat(Robot):
    def __init__(self):
        super().__init__()
        self.motor=RobotMotor()
    
    def avancer(self):
        self.motor.avancer()

    def reculer(self):
        self.motor.reculer()
    
    def gauche(self):
        self.motor.gauche()
    
    def droite(self):
        self.motor.droite()

    
Tou = Combat()
timestep = int(Tou.getBasicTimeStep())
while Tou.step(timestep) != -1:
    Tou.droite()
    pass

# Enter here exit cleanup code.
