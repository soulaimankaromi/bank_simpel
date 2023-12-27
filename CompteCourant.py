from Compte import Compte
class CompetCourant(Compte):
    def __init__(self,N,P,S,D,M_D_A):
        super().__init__(N,P,S,D)
        self.__montantDecouvertAutorise = M_D_A
    @property
    def montantDecouvertAutorise(self):
        return self.__montantDecouvertAutorise
    @montantDecouvertAutorise.setter
    def montantDecouvertAutorise(self,value):
        self.__montantDecouvertAutorise = value
    @property
    def __str__(self):
        return f"/and your montantDecouvertAutorise {self.__montantDecouvertAutorise}"
CC1 = CompetCourant(12,23,2,12,12)
print(CC1.__str__)