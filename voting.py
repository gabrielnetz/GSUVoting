import candidates

def selectOptions():
    a = int(input("select your first option")) - 1
    b = int(input("select your second option")) - 1
    while b == a:
        b = int(input("you cant select the same option twice, please insert someone else")) - 1
    c = int(input("select your third option")) - 1
    while c == a or c == b:
        c = int(input("you cant select the same option twice, please insert someone else")) - 1
    d = int(input("select your fourth option")) - 1
    while d == a or d == b or d == c:
        d = int(input("you cant select the same option twice, please insert someone else")) - 1
    return a, b, c, d

def writeGSUOfficers(a,b,c,d):
    f = open("votesGSU.txt", "a")
    f.write("%s,%s,%s,%s\n" % (a, b, c, d))

def writeFEHOfficers(a,b,c,d):
    f = open("votesFEH.txt", "a")
    f.write("%s,%s,%s,%s\n" % (a, b, c, d))

def writeFACHOfficers(a,b,c,d):
    f = open("votesFACH.txt", "a")
    f.write("%s,%s,%s,%s\n" % (a, b, c, d))

def writeBSOfficers(a,b,c,d):
    f = open("votesBS.txt", "a")
    f.write("%s,%s,%s,%s\n" % (a, b, c, d))

def writePresidents(a,b,c,d):
    f = open("votesPres.txt", "a")
    f.write("%s,%s,%s,%s\n" % (a, b, c, d))

def Voting():
    candidates.showGSUOfficers()
    a,b,c,d = selectOptions()
    writeGSUOfficers(a,b,c,d)

    candidates.showFEHOfficers()
    a, b, c, d = selectOptions()
    writeFEHOfficers(a,b,c,d)

    candidates.showFACHOfficers()
    a, b, c, d = selectOptions()
    writeFACHOfficers(a,b,c,d)

    candidates.showBSOfficers()
    a, b, c, d = selectOptions()
    writeBSOfficers(a,b,c,d)

    candidates.showPresidents()
    a, b, c, d = selectOptions()
    writePresidents(a,b,c,d)

    print("your votes were cast")



