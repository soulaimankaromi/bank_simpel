from Compte import Compte
class CompetEpargne(Compte):
    def __init__(self,N,P,S,D,I):
        super().__init__(N,P,S,D)
        self.__interet = I
    @property
    def interet(self):
        return self.__interet
    @interet.setter
    def interet(self,value):
        self.__interet = value
    @property
    def __str__(self):
        return f"/and your interet {self.__interet}"
CE1 = CompetEpargne(12,23,2,12,1)
print(CE1.__str__)