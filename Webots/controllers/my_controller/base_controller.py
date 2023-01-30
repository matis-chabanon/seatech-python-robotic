from controller import Robot, Motor
#from EpuckMotors import EpuckMotors

class InitRobotMotor(Motor):

    def __init__(self, name="Tou"):
        super().__init__(name)
        self.setPosition(float('inf'))
        self.setVelocity(0)

class RobotMotor():

    def __init__(self,speed=None):
        self.__front_left_wheel_joint = RobotMotor('wheel_1')
        self.__front_right_wheel_joint = RobotMotor('wheel_2')
        self.__back_left_wheel_joint = RobotMotor('wheel_3')
        self.__back_right_wheel_joint = RobotMotor('wheel_4')
    
    def avancer(self):
        self.__front_left_wheel_joint.setVelocity(10)
        self.__front_right_wheel_joint.setVelocity(10)
        self.__back_left_wheel
        _joint.setVelocity(10)
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
        self.__front_left_wheel_joint.setVelocity(10)
        self.__front_right_wheel_joint.setVelocity(7)
        self.__back_left_wheel_joint.setVelocity(10)
        self.__back_right_wheel_joint.setVelocity(7)

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
Tou.avancer