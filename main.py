import candidates,election,voting,login
from datetime import datetime

# Login System should be in here, still in development


# Check if System Date/Time is valid for voting

if election.electionValid():
    print("the voting time is open")
else:
    print("The voting time is closed")
    # exit() for test

# If date is valid, system starts voting

voting.Voting()
election.countVotes()



#hgfhg



