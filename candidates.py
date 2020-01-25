# Creating the superclass Candidate which has a name and a position
class Candidate:
    def __init__(self,position,name):
        self.name = name
        self.position = position
        self.votes1 = 0  # vote as a first choice
        self.votes2 = 0  # vote as a second choice
        self.votes3 = 0  # vote as a third choice
        self.votes4 = 0  # vote as a fourth choice

    # Get the votes of a candidate
    def getVotes(self):
        return self.votes1,self.votes2,self.votes3,self.votes4

# Creating the subclasses of Candidate
class GSUOfficer(Candidate):
    def __init__(self,position,name):
        self.index = 0  # We will assign an index for every candidate
        super().__init__(position,name)


class BSOfficer(Candidate):
    def __init__(self,position,name):
        self.index = 0  # We will assign an index for every candidate
        super().__init__(position,name)

class FACHOfficer(Candidate):
    def __init__(self,position,name):
        self.index = 0  # We will assign an index for every candidate
        super().__init__(position,name)

class FEHOfficer(Candidate):
    def __init__(self,position,name):
        self.index = 0  # We will assign an index for every candidate
        super().__init__(position,name)

class President(Candidate):
    def __init__(self,position,name):
        self.index = 0  # We will assign an index for every candidate
        super().__init__(position,name)

# Function to show the Presidents
def showPresidents():
    print("----------------------")
    for i in range(len(Presidents)):
        print(i+1,"-",Presidents[i].name)
    print("----------------------")

# Function to show the GSUOfficers
def showGSUOfficers():
    print("----------------------")
    for i in range(len(GSUOfficers)):
        print(i+1,"-",GSUOfficers[i].name)

# Function to show the FEHOfficers
def showFEHOfficers():
    print("----------------------")
    for i in range(len(FEHOfficers)):
        print(i+1,"-",FEHOfficers[i].name)

# Function to show the BSOfficers
def showBSOfficers():
    print("----------------------")
    for i in range(len(BSOfficers)):
        print(i+1,"-",BSOfficers[i].name)

# Function to show the FACHOfficers
def showFACHOfficers():
    print("----------------------")
    for i in range(len(FACHOfficers)):
        print(i+1,"-",FACHOfficers[i].name)

# Creating 5 lists for 5 different positions
GSUOfficers = []
Presidents = []
BSOfficers = []
FEHOfficers = []
FACHOfficers = []

# open the file containing the name and the position of the candidates as a reading mode
my_file=open("GSUCandidates.txt","r")

for line in my_file:
    # splitting the lines by the coma
    name,position = line.split(",")  # the strings before the come are stored inside name,
                                     # and the string after the coma inside position

    # if position is equal to 'GSUOfficer', then the names will be stored inside the GSUOfficers list
    if position == "GSUOfficer\n":
        GSUOfficers.append(GSUOfficer(position,name))  # if the condition matches, we will append the name
        GSUOfficers[len(GSUOfficers) - 1].index = len(GSUOfficers)-1  # indexing the candidates

    # if position is equal to 'GSUOfficer', then the names will be stored inside the Presidents list
    if position == "president\n":
        Presidents.append(President(position,name))  # if the condition matches, we will append the name
        Presidents[len(Presidents)-1].index = len(Presidents)-1  # indexing the candidates

    # if position is equal to 'GSUOfficer', then the names will be stored inside the BSOfficers list
    if position == "BSOfficer\n":
        BSOfficers.append(BSOfficer(position,name))  # if the condition matches, we will append the name
        Presidents[len(BSOfficers)-1].index = len(BSOfficers)-1  # indexing the candidates

    # if position is equal to 'GSUOfficer', then the names will be stored inside FACHOfficers list
    if position == "FACHOfficer\n":
        FACHOfficers.append(FACHOfficer(position, name))  # if the condition matches, we will append the name
        FACHOfficers[len(FACHOfficers)-1].index = len(FACHOfficers)-1  # indexing the candidates

    # if position is equal to 'GSUOfficer', then the names will be stored inside the FEHOfficers list
    if position == "FEHOfficer\n":
        FEHOfficers.append(FEHOfficer(position,name))  # if the condition matches, we will append the name
        FEHOfficers[len(FEHOfficers)-1].index = len(FEHOfficers)-1  # indexing the candidates

my_file.close()  # close the file

