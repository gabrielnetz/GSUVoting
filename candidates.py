class Candidate:
    def __init__(self,position,name):
        self.name = name
        self.position = position
        self.votes1 = 0
        self.votes2 = 0
        self.votes3 = 0
        self.votes4 = 0

    def getVotes(self):
        return self.votes1,self.votes2,self.votes3,self.votes4



class GSUOfficer(Candidate):
    def __init__(self,position,name):
        self.index = 0
        super().__init__(position,name)


class BSOfficer(Candidate):
    def __init__(self,position,name):
        self.index = 0
        super().__init__(position,name)

class FACHOfficer(Candidate):
    def __init__(self,position,name):
        self.index = 0
        super().__init__(position,name)

class FEHOfficer(Candidate):
    def __init__(self,position,name):
        self.index = 0
        super().__init__(position,name)

class President(Candidate):
    def __init__(self,position,name):
        self.index = 0
        super().__init__(position,name)







def showPresidents():
    print("----------------------")
    for i in range(len(Presidents)):
        print(i+1,"-",Presidents[i].name)
    print("----------------------")

def showGSUOfficers():
    print("----------------------")
    for i in range(len(GSUOfficers)):
        print(i+1,"-",GSUOfficers[i].name)

def showFEHOfficers():
    print("----------------------")
    for i in range(len(FEHOfficers)):
        print(i+1,"-",FEHOfficers[i].name)

def showBSOfficers():
    print("----------------------")
    for i in range(len(BSOfficers)):
        print(i+1,"-",BSOfficers[i].name)

def showFACHOfficers():
    print("----------------------")
    for i in range(len(FACHOfficers)):
        print(i+1,"-",FACHOfficers[i].name)

GSUOfficers = []
Presidents = []
BSOfficers = []
FEHOfficers = []
FACHOfficers = []


my_file=open("GSUCandidates.txt","r")
for line in my_file:
    name,position = line.split(",")
    if position == "GSUOfficer\n":
        GSUOfficers.append(GSUOfficer(position,name))
        GSUOfficers[len(GSUOfficers) - 1].index = len(GSUOfficers)-1
    if position == "president\n":
        Presidents.append(President(position,name))
        Presidents[len(Presidents)-1].index = len(Presidents)-1
    if position == "BSOfficer\n":
        BSOfficers.append(BSOfficer(position,name))
        Presidents[len(BSOfficers)-1].index = len(BSOfficers)-1
    if position == "FACHOfficer\n":
        FACHOfficers.append(FACHOfficer(position, name))
        FACHOfficers[len(FACHOfficers)-1].index = len(FACHOfficers)-1
    if position == "FEHOfficer\n":
        FEHOfficers.append(FEHOfficer(position,name))
        FEHOfficers[len(FEHOfficers)-1].index = len(FEHOfficers)-1

my_file.close()

