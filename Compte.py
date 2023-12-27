class Compte:
    def __init__(self,N,P,S,D):
        self.__Numero = N
        self.__Proprietaire = P
        self.__Solde = S 
        self.__dateOuverture =D
    @property
    def Numero(self):
        return self.__Numero
    @property
    def Proprietaire(self):
        return self.__Proprietaire
    @property
    def Solde(self):
        return self.__Solde
    @property
    def dateOuverture(self):
        return self.__dateOuverture
    @Numero.setter
    def Numero(self,value):
        self.__Numero = value
    @Proprietaire.setter
    def Proprietaire(self,value):
        self.__Proprietaire = value
    @Solde.setter
    def Solde(self,value):
        self.__Solde = value
    @dateOuverture.setter
    def dateOuverture(self,value):
        self.__dateOuverture = value
    @property
    def __str__(self):
        return f"your Numero is {self.__Numero}/ and your Proprietaore is{self.__Proprietaire}/ and your solde is {self.__Solde}/ and you dateOuverture is{self.__dateOuverture}"
C1 = Compte(12,23,13,12)
print(C1.__str__)