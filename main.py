import election,voting,login

# Check if System Date/Time is valid for voting
if election.electionValid():
    print("the voting time is open")
else:
    print("The voting time is closed")
    exit()
# If date is valid, system starts voting

login.Login()  # Login and authenticate based on the StudentRecords.txt
voting.Voting()  # Vote and save records to votes.txt
election.countVotes()  # Count,sort and display the votes from the files







