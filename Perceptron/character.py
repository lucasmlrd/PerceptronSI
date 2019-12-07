class Character:
    name = ""
    first_name = ""
    age = 0
    profession = ""
    moralBoost = 0.0

    def __init__(self, name, first_name, age, profession, moralBoost):
        """Constructeur de notre classe"""
        self.name = name
        self.first_name = first_name
        self.age = age
        self.profession = profession
        self.moralBoost = moralBoost

    """Getters"""

    def getName(self):
        return self.name

    def getFirstName(self):
        return self.first_name

    def getAge(self):
        return self.age

    def getProfession(self):
        return self.profession

    def getMoralBoost(self):
        return self.moralBoost

    """Setters"""

    def setName(self, name):
        self.name = name

    def setFirstName(self, first):
        self.first_name = first

    def setAge(self, age):
        self.age = age

    def setProfession(self, pro):
        self.profession = pro

    def setMoralBoost(self, mo):
        self.moralBoost = mo

    def __str__(self):
        string = "Name : {}\nFirst Name : {}\nAge : {}\nProfession : {}\nMoral Boost : {}\n".format(self.getName(),self.getFirstName(),self.getAge(),self.getProfession(),self.getMoralBoost())
        return string
