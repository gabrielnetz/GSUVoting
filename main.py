import candidates,election,voting,login
from datetime import datetime

login.Login()

# Check if System Date/Time is valid for voting

if election.electionValid():
    print("the voting time is open")
else:
    print("The voting time is closed")
    #exit()

# If date is valid, system starts voting

voting.Voting()
election.countVotes()







