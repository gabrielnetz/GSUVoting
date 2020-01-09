from datetime import datetime
import candidates

class Election:
    def __init__(self,startdate,enddate):
        self.startdate = startdate
        self.enddate = enddate


def createElection(y1,m1,d1,y,m,d):
     d1 = datetime(y1,m1,d1,23,59,59)
     d2 = datetime(y,m,d,23,59,59)
     return Election(d1,d2)


def electionValid():
    if GSUElections.startdate < datetime.now() and GSUElections.enddate > datetime.now():
        return True
    else:
        return False

def sortVote1():
    candidates.Presidents.sort(key=lambda x: x.votes1, reverse=True)
    candidates.GSUOfficers.sort(key=lambda x: x.votes1, reverse=True)
    candidates.BSOfficers.sort(key=lambda x: x.votes1, reverse=True)
    candidates.FACHOfficers.sort(key=lambda x: x.votes1, reverse=True)
    candidates.FEHOfficers.sort(key=lambda x: x.votes1, reverse=True)

def STVPres():
    candidates.Presidents.sort(key=lambda x: x.votes1, reverse=True)
    for i in range(len(candidates.Presidents)):
        if candidates.Presidents[i].votes1 != candidates.Presidents[0].votes1:
            candidates.Presidents.pop(i)
    candidates.Presidents.sort(key=lambda x: x.votes2, reverse=True)
    for i in range(len(candidates.Presidents)):
        if candidates.Presidents[i].votes2 != candidates.Presidents[0].votes2:
            candidates.Presidents.pop(i)
    candidates.Presidents.sort(key=lambda x: x.votes3, reverse=True)
    for i in range(len(candidates.Presidents)):
        if candidates.Presidents[i].votes3 != candidates.Presidents[0].votes3:
            candidates.Presidents.pop(i)
    candidates.Presidents.sort(key=lambda x: x.votes4, reverse=True)
    for i in range(len(candidates.Presidents)):
        if candidates.Presidents[i].votes4 != candidates.Presidents[0].votes4:
            candidates.Presidents.pop(i)

def STVGsu():
    candidates.GSUOfficers.sort(key=lambda x: x.votes1, reverse=True)
    for i in range(len(candidates.GSUOfficers)):
        if candidates.GSUOfficers[i].votes1 != candidates.GSUOfficers[0].votes1:
            candidates.GSUOfficers.pop(i)
    candidates.GSUOfficers.sort(key=lambda x: x.votes2, reverse=True)
    for i in range(len(candidates.GSUOfficers)):
        if candidates.GSUOfficers[i].votes2 != candidates.GSUOfficers[0].votes2:
            candidates.GSUOfficers.pop(i)
    candidates.GSUOfficers.sort(key=lambda x: x.votes3, reverse=True)
    for i in range(len(candidates.GSUOfficers)):
        if candidates.GSUOfficers[i].votes3 != candidates.GSUOfficers[0].votes3:
            candidates.GSUOfficers.pop(i)
    candidates.GSUOfficers.sort(key=lambda x: x.votes4, reverse=True)
    for i in range(len(candidates.GSUOfficers)):
        if candidates.GSUOfficers[i].votes4 != candidates.GSUOfficers[0].votes4:
            candidates.GSUOfficers.pop(i)

def STVFACH():
    candidates.FACHOfficers.sort(key=lambda x: x.votes1, reverse=True)
    for i in range(len(candidates.FACHOfficers)):
        if candidates.FACHOfficers[i].votes1 != candidates.FACHOfficers[0].votes1:
            candidates.FACHOfficers.pop(i)
    candidates.FACHOfficers.sort(key=lambda x: x.votes2, reverse=True)
    for i in range(len(candidates.FACHOfficers)):
        if candidates.FACHOfficers[i].votes2 != candidates.FACHOfficers[0].votes2:
            candidates.FACHOfficers.pop(i)
    candidates.FACHOfficers.sort(key=lambda x: x.votes3, reverse=True)
    for i in range(len(candidates.FACHOfficers)):
        if candidates.FACHOfficers[i].votes3 != candidates.FACHOfficers[0].votes3:
            candidates.FACHOfficers.pop(i)
    candidates.FACHOfficers.sort(key=lambda x: x.votes4, reverse=True)
    for i in range(len(candidates.FACHOfficers)):
        if candidates.FACHOfficers[i].votes4 != candidates.FACHOfficers[0].votes4:
            candidates.FACHOfficers.pop(i)

def STVFEH():
    candidates.FEHOfficers.sort(key=lambda x: x.votes1, reverse=True)
    for i in range(len(candidates.FEHOfficers)):
        if candidates.FEHOfficers[i].votes1 != candidates.FEHOfficers[0].votes1:
            candidates.FEHOfficers.pop(i)
    candidates.FEHOfficers.sort(key=lambda x: x.votes2, reverse=True)
    for i in range(len(candidates.FEHOfficers)):
        if candidates.FEHOfficers[i].votes2 != candidates.FEHOfficers[0].votes2:
            candidates.FEHOfficers.pop(i)
    candidates.FEHOfficers.sort(key=lambda x: x.votes3, reverse=True)
    for i in range(len(candidates.FEHOfficers)):
        if candidates.FEHOfficers[i].votes3 != candidates.FEHOfficers[0].votes3:
            candidates.FEHOfficers.pop(i)
    candidates.FEHOfficers.sort(key=lambda x: x.votes4, reverse=True)
    for i in range(len(candidates.FEHOfficers)):
        if candidates.FEHOfficers[i].votes4 != candidates.FEHOfficers[0].votes4:
            candidates.FEHOfficers.pop(i)

def STVBS():
    candidates.BSOfficers.sort(key=lambda x: x.votes1, reverse=True)
    for i in range(len(candidates.BSOfficers)):
        if candidates.BSOfficers[i].votes1 != candidates.BSOfficers[0].votes1:
            candidates.BSOfficers.pop(i)
    candidates.BSOfficers.sort(key=lambda x: x.votes2, reverse=True)
    for i in range(len(candidates.BSOfficers)):
        if candidates.BSOfficers[i].votes2 != candidates.BSOfficers[0].votes2:
            candidates.BSOfficers.pop(i)
    candidates.BSOfficers.sort(key=lambda x: x.votes3, reverse=True)
    for i in range(len(candidates.BSOfficers)):
        if candidates.BSOfficers[i].votes3 != candidates.BSOfficers[0].votes3:
            candidates.BSOfficers.pop(i)
    candidates.BSOfficers.sort(key=lambda x: x.votes4, reverse=True)
    for i in range(len(candidates.BSOfficers)):
        if candidates.BSOfficers[i].votes4 != candidates.BSOfficers[0].votes4:
            candidates.BSOfficers.pop(i)







GSUElections = createElection(2020,1,1,2020,4,3)
finalist = []


def countVotes():
    PresVotes = open("votesPres.txt","r")
    for line in PresVotes:
        vote1,vote2,vote3,vote4 = line.split(",")
        vote1 = int(vote1)
        vote2 = int(vote2)
        vote3 = int(vote3)
        vote4 = int(vote4)
        candidates.Presidents[vote1].votes1 = candidates.Presidents[vote1].votes1 + 1
        candidates.Presidents[vote2].votes2 = candidates.Presidents[vote2].votes2 + 1
        candidates.Presidents[vote3].votes3 = candidates.Presidents[vote3].votes3 + 1
        candidates.Presidents[vote4].votes4 = candidates.Presidents[vote4].votes4 + 1

    PresVotes.close()
    GSUVotes = open("votesGSU.txt", "r")
    for line in GSUVotes:
        vote1, vote2, vote3, vote4 = line.split(",")
        vote1 = int(vote1)
        vote2 = int(vote2)
        vote3 = int(vote3)
        vote4 = int(vote4)
        candidates.GSUOfficers[vote1].votes1 = candidates.GSUOfficers[vote1].votes1 + 1
        candidates.GSUOfficers[vote2].votes2 = candidates.GSUOfficers[vote2].votes2 + 1
        candidates.GSUOfficers[vote3].votes3 = candidates.GSUOfficers[vote3].votes3 + 1
        candidates.GSUOfficers[vote4].votes4 = candidates.GSUOfficers[vote4].votes4 + 1

    GSUVotes.close()

    FEHVotes = open("votesFEH.txt", "r")
    for line in FEHVotes:
        vote1, vote2, vote3, vote4 = line.split(",")
        vote1 = int(vote1)
        vote2 = int(vote2)
        vote3 = int(vote3)
        vote4 = int(vote4)
        candidates.FEHOfficers[vote1].votes1 = candidates.FEHOfficers[vote1].votes1 + 1
        candidates.FEHOfficers[vote2].votes2 = candidates.FEHOfficers[vote2].votes2 + 1
        candidates.FEHOfficers[vote3].votes3 = candidates.FEHOfficers[vote3].votes3 + 1
        candidates.FEHOfficers[vote4].votes4 = candidates.FEHOfficers[vote4].votes4 + 1


    FEHVotes.close()

    FACHVotes = open("votesFACH.txt", "r")
    for line in FACHVotes:
        vote1, vote2, vote3, vote4 = line.split(",")
        vote1 = int(vote1)
        vote2 = int(vote2)
        vote3 = int(vote3)
        vote4 = int(vote4)
        candidates.FACHOfficers[vote1].votes1 = candidates.FACHOfficers[vote1].votes1 + 1
        candidates.FACHOfficers[vote1].votes2 = candidates.FACHOfficers[vote2].votes2 + 1
        candidates.FACHOfficers[vote1].votes3 = candidates.FACHOfficers[vote3].votes3 + 1
        candidates.FACHOfficers[vote1].votes4 = candidates.FACHOfficers[vote4].votes4 + 1



    FACHVotes.close()
    BSVotes = open("votesBS.txt", "r")
    for line in BSVotes:
        vote1, vote2, vote3, vote4 = line.split(",")
        vote1 = int(vote1)
        vote2 = int(vote2)
        vote3 = int(vote3)
        vote4 = int(vote4)
        candidates.BSOfficers[vote1].votes1 = candidates.BSOfficers[vote1].votes1 + 1
        candidates.BSOfficers[vote2].votes2 = candidates.BSOfficers[vote2].votes2 + 1
        candidates.BSOfficers[vote3].votes3 = candidates.BSOfficers[vote3].votes3 + 1
        candidates.BSOfficers[vote4].votes4 = candidates.BSOfficers[vote4].votes4 + 1
    BSVotes.close()
    # Now for Counting

    sortVote1()
    printPres = candidates.Presidents.copy()
    printGSU = candidates.GSUOfficers.copy()
    printBS = candidates.BSOfficers.copy()
    printFACH = candidates.FACHOfficers.copy()
    printFEH = candidates.FEHOfficers.copy()



    print("--------------------------")
    print("Winner:")
    print("1 -", candidates.Presidents[0].name)
    print("first options -", candidates.Presidents[0].votes1)
    print("second options -", candidates.Presidents[0].votes2)
    print("third options -", candidates.Presidents[0].votes3)
    print("fourth options -", candidates.Presidents[0].votes4)
    print("--------------------------")
    print("Runner Up:")
    print("2 -", printPres[1].name)
    print("first options -", printPres[1].votes1)
    print("second options -", printPres[1].votes2)
    print("third options -", printPres[1].votes3)
    print("fourth options -", printPres[1].votes4)
    print("--------------------------")
    print("Third Place:")
    print("3 -", printPres[2].name)
    print("first options -", printPres[2].votes1)
    print("second options -", printPres[2].votes2)
    print("third options -", printPres[2].votes3)
    print("fourth options -", printPres[2].votes4)
    print("--------------------------")
    print("Fourth Place:")
    print("4 -", printPres[3].name)
    print("first options -", printPres[3].votes1)
    print("second options -", printPres[3].votes2)
    print("third options -", printPres[3].votes3)
    print("fourth options -", printPres[3].votes4)



























