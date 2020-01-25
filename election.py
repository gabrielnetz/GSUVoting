from datetime import datetime  # datetime library will allow us to set the voting day
import candidates
import logging


# We have a start date and an end date
class Election:
    def __init__(self, startdate, enddate):
        self.startdate = startdate
        self.enddate = enddate


# the date is in the following format: YYYY, MM, DD
def createElection(y1, m1, d1, y, m, d):
    d1 = datetime(y1, m1, d1, 23, 59, 59)
    d2 = datetime(y, m, d, 23, 59, 59)
    return Election(d1, d2)


def electionValid():
    # if the range of time is valid we can vote, otherwise is not possible to vote
    if GSUElections.startdate < datetime.now() and GSUElections.enddate > datetime.now():
        return True
    else:
        return False


def sortVote():
    # sorting the votes and reversing to have the list from the max value to the min
    candidates.Presidents.sort(key=lambda x: (x.votes1, x.votes2, x.votes3, x.votes4), reverse=True)
    candidates.GSUOfficers.sort(key=lambda x: (x.votes1, x.votes2, x.votes3, x.votes4), reverse=True)
    candidates.BSOfficers.sort(key=lambda x: (x.votes1, x.votes2, x.votes3, x.votes4), reverse=True)
    candidates.FACHOfficers.sort(key=lambda x: (x.votes1, x.votes2, x.votes3, x.votes4), reverse=True)
    candidates.FEHOfficers.sort(key=lambda x: (x.votes1, x.votes2, x.votes3, x.votes4), reverse=True)


# Creating the election date
GSUElections = createElection(2020, 1, 1, 2020, 4, 3)
finalist = []


def countVotes():
    PresVotes = open("votesPres.txt", "r")  # Read the votes file of presidents
    for line in PresVotes:
        vote1, vote2, vote3, vote4 = line.split(",")  # votes are organized in: 0,1,2,3
        vote1 = int(vote1)  # converting the string into int
        vote2 = int(vote2)
        vote3 = int(vote3)
        vote4 = int(vote4)
        # adding one for every time that is voted
        candidates.Presidents[vote1].votes1 = candidates.Presidents[vote1].votes1 + 1
        candidates.Presidents[vote2].votes2 = candidates.Presidents[vote2].votes2 + 1
        candidates.Presidents[vote3].votes3 = candidates.Presidents[vote3].votes3 + 1
        candidates.Presidents[vote4].votes4 = candidates.Presidents[vote4].votes4 + 1

    PresVotes.close()  # close the file

    GSUVotes = open("votesGSU.txt", "r")  # Read the votes file of GSU
    for line in GSUVotes:
        vote1, vote2, vote3, vote4 = line.split(",")
        vote1 = int(vote1)  # converting the string into int
        vote2 = int(vote2)
        vote3 = int(vote3)
        vote4 = int(vote4)
        # adding one for every time that is voted
        candidates.GSUOfficers[vote1].votes1 = candidates.GSUOfficers[vote1].votes1 + 1
        candidates.GSUOfficers[vote2].votes2 = candidates.GSUOfficers[vote2].votes2 + 1
        candidates.GSUOfficers[vote3].votes3 = candidates.GSUOfficers[vote3].votes3 + 1
        candidates.GSUOfficers[vote4].votes4 = candidates.GSUOfficers[vote4].votes4 + 1

    GSUVotes.close()

    FEHVotes = open("votesFEH.txt", "r")
    for line in FEHVotes:
        vote1, vote2, vote3, vote4 = line.split(",")
        vote1 = int(vote1)  # converting the string into int
        vote2 = int(vote2)
        vote3 = int(vote3)
        vote4 = int(vote4)
        # adding one for every time that is voted
        candidates.FEHOfficers[vote1].votes1 = candidates.FEHOfficers[vote1].votes1 + 1
        candidates.FEHOfficers[vote2].votes2 = candidates.FEHOfficers[vote2].votes2 + 1
        candidates.FEHOfficers[vote3].votes3 = candidates.FEHOfficers[vote3].votes3 + 1
        candidates.FEHOfficers[vote4].votes4 = candidates.FEHOfficers[vote4].votes4 + 1

    FEHVotes.close()

    FACHVotes = open("votesFACH.txt", "r")
    for line in FACHVotes:
        vote1, vote2, vote3, vote4 = line.split(",")
        vote1 = int(vote1)  # converting the string into int
        vote2 = int(vote2)
        vote3 = int(vote3)
        vote4 = int(vote4)
        # adding one for every time that is voted
        candidates.FACHOfficers[vote1].votes1 = candidates.FACHOfficers[vote1].votes1 + 1
        candidates.FACHOfficers[vote1].votes2 = candidates.FACHOfficers[vote2].votes2 + 1
        candidates.FACHOfficers[vote1].votes3 = candidates.FACHOfficers[vote3].votes3 + 1
        candidates.FACHOfficers[vote1].votes4 = candidates.FACHOfficers[vote4].votes4 + 1

    FACHVotes.close()
    BSVotes = open("votesBS.txt", "r")
    for line in BSVotes:
        vote1, vote2, vote3, vote4 = line.split(",")
        vote1 = int(vote1)  # converting the string into int
        vote2 = int(vote2)
        vote3 = int(vote3)
        vote4 = int(vote4)
        # adding one for every time that is voted
        candidates.BSOfficers[vote1].votes1 = candidates.BSOfficers[vote1].votes1 + 1
        candidates.BSOfficers[vote2].votes2 = candidates.BSOfficers[vote2].votes2 + 1
        candidates.BSOfficers[vote3].votes3 = candidates.BSOfficers[vote3].votes3 + 1
        candidates.BSOfficers[vote4].votes4 = candidates.BSOfficers[vote4].votes4 + 1
    BSVotes.close()

    # Now for Counting:
    sortVote()
    # get the votes for each candidate
    printPres = candidates.Presidents.copy()
    printGSU = candidates.GSUOfficers.copy()
    printBS = candidates.BSOfficers.copy()
    printFACH = candidates.FACHOfficers.copy()
    printFEH = candidates.FEHOfficers.copy()

    votesPres = candidates.Presidents[0].votes1 + candidates.Presidents[0].votes2 + candidates.Presidents[0].votes3 + \
                candidates.Presidents[0].votes4

    votesGSU = candidates.GSUOfficers[0].votes1 + candidates.GSUOfficers[0].votes2 + candidates.GSUOfficers[0].votes3 + \
               candidates.GSUOfficers[0].votes4

    votesFACH = candidates.FACHOfficers[0].votes1 + candidates.FACHOfficers[0].votes2 + candidates.FACHOfficers[
        0].votes3 + \
                candidates.FACHOfficers[0].votes4

    votesBS = candidates.BSOfficers[0].votes1 + candidates.BSOfficers[0].votes2 + candidates.BSOfficers[0].votes3 + \
              candidates.BSOfficers[0].votes4

    votesFEH = candidates.FEHOfficers[0].votes1 + candidates.FEHOfficers[0].votes2 + candidates.FEHOfficers[0].votes3 + \
               candidates.FEHOfficers[0].votes4

    # Txt file of the voting results
    file = open("votingresults.txt", "w")
    # Clear the txt file before printing the result
    file.write("")

    # appending all the strings and results below into 'votingresults.txt'
    # President results
    print("--------------------------", file=open("votingresults.txt", "a"))
    print("President Elections", file=open("votingresults.txt", "a"))
    print("Voting Students =", votesPres, file=open("votingresults.txt", "a"))

    # Print the percentage of votes received only by the winner
    # 1st
    print("Winner:", file=open("votingresults.txt", "a"))
    print("1 -", candidates.Presidents[0].name, file=open("votingresults.txt", "a"))
    print("first options -", candidates.Presidents[0].votes1, " - Percentage",
          candidates.Presidents[0].votes1 * 100 / votesPres, "%", file=open("votingresults.txt", "a"))
    print("second options -", candidates.Presidents[0].votes2, " - Percentage",
          candidates.Presidents[0].votes2 * 100 / votesPres, "%", file=open("votingresults.txt", "a"))
    print("third options -", candidates.Presidents[0].votes3, " - Percentage",
          candidates.Presidents[0].votes3 * 100 / votesPres, "%", file=open("votingresults.txt", "a"))
    print("fourth options -", candidates.Presidents[0].votes4, " - Percentage",
          candidates.Presidents[0].votes4 * 100 / votesPres, "%", file=open("votingresults.txt", "a"))
    print("--------------------------", file=open("votingresults.txt", "a"))

    # 2nd
    print("Runner Up:", file=open("votingresults.txt", "a"))
    print("2 -", printPres[1].name, file=open("votingresults.txt", "a"))
    print("first options -", printPres[1].votes1, file=open("votingresults.txt", "a"))
    print("second options -", printPres[1].votes2, file=open("votingresults.txt", "a"))
    print("third options -", printPres[1].votes3, file=open("votingresults.txt", "a"))
    print("fourth options -", printPres[1].votes4, file=open("votingresults.txt", "a"))
    print("--------------------------", file=open("votingresults.txt", "a"))

    # 3rd
    print("Third Place:", file=open("votingresults.txt", "a"))
    print("3 -", printPres[2].name, file=open("votingresults.txt", "a"))
    print("first options -", printPres[2].votes1, file=open("votingresults.txt", "a"))
    print("second options -", printPres[2].votes2, file=open("votingresults.txt", "a"))
    print("third options -", printPres[2].votes3, file=open("votingresults.txt", "a"))
    print("fourth options -", printPres[2].votes4, file=open("votingresults.txt", "a"))
    print("--------------------------", file=open("votingresults.txt", "a"))

    # 4th
    print("Fourth Place:", file=open("votingresults.txt", "a"))
    print("4 -", printPres[3].name, file=open("votingresults.txt", "a"))
    print("first options -", printPres[3].votes1, file=open("votingresults.txt", "a"))
    print("second options -", printPres[3].votes2, file=open("votingresults.txt", "a"))
    print("third options -", printPres[3].votes3, file=open("votingresults.txt", "a"))
    print("fourth options -", printPres[3].votes4, file=open("votingresults.txt", "a"))
    print("--------------------------", file=open("votingresults.txt", "a"))
    print()

    # GSU officers results
    print("GSU Elections", file=open("votingresults.txt", "a"))
    print("Voting Students =", votesGSU, file=open("votingresults.txt", "a"))

    # 1st
    print("Winner:", file=open("votingresults.txt", "a"))
    print("1 -", candidates.GSUOfficers[0].name, file=open("votingresults.txt", "a"))
    print("first options -", candidates.GSUOfficers[0].votes1, " - Percentage",
          candidates.GSUOfficers[0].votes1 * 100 / votesGSU, "%", file=open("votingresults.txt", "a"))
    print("second options -", candidates.GSUOfficers[0].votes2, " - Percentage",
          candidates.GSUOfficers[0].votes2 * 100 / votesGSU, "%", file=open("votingresults.txt", "a"))
    print("third options -", candidates.GSUOfficers[0].votes3, " - Percentage",
          candidates.GSUOfficers[0].votes3 * 100 / votesGSU, "%", file=open("votingresults.txt", "a"))
    print("fourth options -", candidates.GSUOfficers[0].votes4, " - Percentage",
          candidates.GSUOfficers[0].votes4 * 100 / votesGSU, "%", file=open("votingresults.txt", "a"))
    print("--------------------------", file=open("votingresults.txt", "a"))

    # 2nd
    print("Runner Up:", file=open("votingresults.txt", "a"))
    print("2 -", printGSU[1].name, file=open("votingresults.txt", "a"))
    print("first options -", printGSU[1].votes1, file=open("votingresults.txt", "a"))
    print("second options -", printGSU[1].votes2, file=open("votingresults.txt", "a"))
    print("third options -", printGSU[1].votes3, file=open("votingresults.txt", "a"))
    print("fourth options -", printGSU[1].votes4, file=open("votingresults.txt", "a"))
    print("--------------------------", file=open("votingresults.txt", "a"))

    # 3rd
    print("Third Place:", file=open("votingresults.txt", "a"))
    print("3 -", printGSU[2].name, file=open("votingresults.txt", "a"))
    print("first options -", printGSU[2].votes1, file=open("votingresults.txt", "a"))
    print("second options -", printGSU[2].votes2, file=open("votingresults.txt", "a"))
    print("third options -", printGSU[2].votes3, file=open("votingresults.txt", "a"))
    print("fourth options -", printGSU[2].votes4, file=open("votingresults.txt", "a"))
    print("--------------------------", file=open("votingresults.txt", "a"))

    # 4th
    print("Fourth Place:", file=open("votingresults.txt", "a"))
    print("4 -", printGSU[3].name, file=open("votingresults.txt", "a"))
    print("first options -", printGSU[3].votes1, file=open("votingresults.txt", "a"))
    print("second options -", printGSU[3].votes2, file=open("votingresults.txt", "a"))
    print("third options -", printGSU[3].votes3, file=open("votingresults.txt", "a"))
    print("fourth options -", printGSU[3].votes4, file=open("votingresults.txt", "a"))
    print("--------------------------", file=open("votingresults.txt", "a"))
    print()

    # FACH Officers results
    print("FACH Elections", file=open("votingresults.txt", "a"))
    print("Voting Students =", votesFACH, file=open("votingresults.txt", "a"))

    # 1st
    print("Winner:", file=open("votingresults.txt", "a"))
    print("1 -", candidates.FACHOfficers[0].name, file=open("votingresults.txt", "a"))
    print("first options -", candidates.FACHOfficers[0].votes1, " - Percentage",
          candidates.FACHOfficers[0].votes1 * 100 / votesFACH, "%", file=open("votingresults.txt", "a"))
    print("second options -", candidates.FACHOfficers[0].votes2, " - Percentage",
          candidates.FACHOfficers[0].votes2 * 100 / votesFACH, "%", file=open("votingresults.txt", "a"))
    print("third options -", candidates.FACHOfficers[0].votes3, " - Percentage",
          candidates.FACHOfficers[0].votes3 * 100 / votesFACH, "%", file=open("votingresults.txt", "a"))
    print("fourth options -", candidates.FACHOfficers[0].votes4, " - Percentage",
          candidates.FACHOfficers[0].votes4 * 100 / votesFACH, "%", file=open("votingresults.txt", "a"))
    print("--------------------------", file=open("votingresults.txt", "a"))

    # 2nd
    print("Runner Up:", file=open("votingresults.txt", "a"))
    print("2 -", printFACH[1].name, file=open("votingresults.txt", "a"))
    print("first options -", printFACH[1].votes1, file=open("votingresults.txt", "a"))
    print("second options -", printFACH[1].votes2, file=open("votingresults.txt", "a"))
    print("third options -", printFACH[1].votes3, file=open("votingresults.txt", "a"))
    print("fourth options -", printFACH[1].votes4, file=open("votingresults.txt", "a"))
    print("--------------------------", file=open("votingresults.txt", "a"))

    # 3rd
    print("Third Place:", file=open("votingresults.txt", "a"))
    print("3 -", printFACH[2].name, file=open("votingresults.txt", "a"))
    print("first options -", printFACH[2].votes1, file=open("votingresults.txt", "a"))
    print("second options -", printFACH[2].votes2, file=open("votingresults.txt", "a"))
    print("third options -", printFACH[2].votes3, file=open("votingresults.txt", "a"))
    print("fourth options -", printFACH[2].votes4, file=open("votingresults.txt", "a"))
    print("--------------------------", file=open("votingresults.txt", "a"))

    # 4th
    print("Fourth Place:", file=open("votingresults.txt", "a"))
    print("4 -", printFACH[3].name, file=open("votingresults.txt", "a"))
    print("first options -", printFACH[3].votes1, file=open("votingresults.txt", "a"))
    print("second options -", printFACH[3].votes2, file=open("votingresults.txt", "a"))
    print("third options -", printFACH[3].votes3, file=open("votingresults.txt", "a"))
    print("fourth options -", printFACH[3].votes4, file=open("votingresults.txt", "a"))
    print("--------------------------", file=open("votingresults.txt", "a"))
    print()

    # FEH officers results
    print("FEH Elections", file=open("votingresults.txt", "a"))
    print("Voting Students =", votesFEH, file=open("votingresults.txt", "a"))

    # 1st
    print("Winner:", file=open("votingresults.txt", "a"))
    print("1 -", candidates.FEHOfficers[0].name, file=open("votingresults.txt", "a"))
    print("first options -", candidates.FEHOfficers[0].votes1, " - Percentage",
          candidates.FEHOfficers[0].votes1 * 100 / votesFEH, "%", file=open("votingresults.txt", "a"))
    print("second options -", candidates.FEHOfficers[0].votes2, " - Percentage",
          candidates.FEHOfficers[0].votes2 * 100 / votesFEH, "%", file=open("votingresults.txt", "a"))
    print("third options -", candidates.FEHOfficers[0].votes3, " - Percentage",
          candidates.FEHOfficers[0].votes3 * 100 / votesFEH, "%", file=open("votingresults.txt", "a"))
    print("fourth options -", candidates.FEHOfficers[0].votes4, " - Percentage",
          candidates.FEHOfficers[0].votes4 * 100 / votesFEH, "%", file=open("votingresults.txt", "a"))
    print("--------------------------", file=open("votingresults.txt", "a"))

    # 2nd
    print("Runner Up:", file=open("votingresults.txt", "a"))
    print("2 -", printFEH[1].name, file=open("votingresults.txt", "a"))
    print("first options -", printFEH[1].votes1, file=open("votingresults.txt", "a"))
    print("second options -", printFEH[1].votes2, file=open("votingresults.txt", "a"))
    print("third options -", printFEH[1].votes3, file=open("votingresults.txt", "a"))
    print("fourth options -", printFEH[1].votes4, file=open("votingresults.txt", "a"))
    print("--------------------------", file=open("votingresults.txt", "a"))

    # 3rd
    print("Third Place:", file=open("votingresults.txt", "a"))
    print("3 -", printFEH[2].name, file=open("votingresults.txt", "a"))
    print("first options -", printFEH[2].votes1, file=open("votingresults.txt", "a"))
    print("second options -", printFEH[2].votes2, file=open("votingresults.txt", "a"))
    print("third options -", printFEH[2].votes3, file=open("votingresults.txt", "a"))
    print("fourth options -", printFEH[2].votes4, file=open("votingresults.txt", "a"))
    print("--------------------------", file=open("votingresults.txt", "a"))

    # 4th
    print("Fourth Place:", file=open("votingresults.txt", "a"))
    print("4 -", printFEH[3].name, file=open("votingresults.txt", "a"))
    print("first options -", printFEH[3].votes1, file=open("votingresults.txt", "a"))
    print("second options -", printFEH[3].votes2, file=open("votingresults.txt", "a"))
    print("third options -", printFEH[3].votes3, file=open("votingresults.txt", "a"))
    print("fourth options -", printFEH[3].votes4, file=open("votingresults.txt", "a"))
    print("--------------------------", file=open("votingresults.txt", "a"))
    print()

    # BS officers results
    print("BS Elections", file=open("votingresults.txt", "a"))
    print("Voting Students =", votesBS, file=open("votingresults.txt", "a"))

    # 1st
    print("Winner:", file=open("votingresults.txt", "a"))
    print("1 -", candidates.BSOfficers[0].name, file=open("votingresults.txt", "a"))
    print("first options -", candidates.BSOfficers[0].votes1, " - Percentage",
          candidates.BSOfficers[0].votes1 * 100 / votesBS, "%", file=open("votingresults.txt", "a"))
    print("second options -", candidates.BSOfficers[0].votes2, " - Percentage",
          candidates.BSOfficers[0].votes2 * 100 / votesBS, "%", file=open("votingresults.txt", "a"))
    print("third options -", candidates.BSOfficers[0].votes3, " - Percentage",
          candidates.BSOfficers[0].votes3 * 100 / votesBS, "%", file=open("votingresults.txt", "a"))
    print("fourth options -", candidates.BSOfficers[0].votes4, " - Percentage",
          candidates.BSOfficers[0].votes4 * 100 / votesBS, "%", file=open("votingresults.txt", "a"))
    print("--------------------------", file=open("votingresults.txt", "a"))

    # 2nd
    print("Runner Up:", file=open("votingresults.txt", "a"))
    print("2 -", printBS[1].name, file=open("votingresults.txt", "a"))
    print("first options -", printBS[1].votes1, file=open("votingresults.txt", "a"))
    print("second options -", printBS[1].votes2, file=open("votingresults.txt", "a"))
    print("third options -", printBS[1].votes3, file=open("votingresults.txt", "a"))
    print("fourth options -", printBS[1].votes4, file=open("votingresults.txt", "a"))
    print("--------------------------", file=open("votingresults.txt", "a"))

    # 3rd
    print("Third Place:", file=open("votingresults.txt", "a"))
    print("3 -", printBS[2].name, file=open("votingresults.txt", "a"))
    print("first options -", printBS[2].votes1, file=open("votingresults.txt", "a"))
    print("second options -", printBS[2].votes2, file=open("votingresults.txt", "a"))
    print("third options -", printBS[2].votes3, file=open("votingresults.txt", "a"))
    print("fourth options -", printBS[2].votes4, file=open("votingresults.txt", "a"))
    print("--------------------------", file=open("votingresults.txt", "a"))

    # 4th
    print("Fourth Place:", file=open("votingresults.txt", "a"))
    print("4 -", printBS[3].name, file=open("votingresults.txt", "a"))
    print("first options -", printBS[3].votes1, file=open("votingresults.txt", "a"))
    print("second options -", printBS[3].votes2, file=open("votingresults.txt", "a"))
    print("third options -", printBS[3].votes3, file=open("votingresults.txt", "a"))
    print("fourth options -", printBS[3].votes4, file=open("votingresults.txt", "a"))


countVotes()
