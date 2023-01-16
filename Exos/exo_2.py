from exo_1 import Robot

class Human():  
    name = "<unnamed>"
    sexe = "<undefined>"
    pass

    def __init__(self, name=None, sexe=None):
        if name:
            self.name = name
            self.sexe = sexe
    
    def set_choose_sexe(self, sexe):
        self.sexe = sexe
    
    def get_sexe(self, sexe):
        return self.sexe

    def manger(self,aliment):
        print(self.name + " mange " + aliment)
    
    def digerer(self):
        print(self.name + " a digéré !")

class Cyborg(Human, Robot):

    def __init__(self, name, sexe, human_name): 
        Robot.__init__(self, name)
        Human.__init__(self, sexe, human_name)




if __name__ == "__main__" :
    cyborg = Cyborg('M', 'Deus Ex Machina', 'Richard')
    print(cyborg.name, 'sexe', cyborg.sexe)
    print('Charging battery...')
    cyborg.recharger()
    #cyborg.status()
    cyborg.manger('banana')
    #cyborg.eat(['coca', 'chips'])
    cyborg.digerer()