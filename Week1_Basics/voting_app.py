# Task 3: Simple Voting App
# Ask 3 candidates’ names
#
# Allow users to vote by entering a name
#
# Track votes in a dictionary
#
# Show results with vote count at end

candi_list = {}

# Step 1: Add candidates
print("🎯 Register Candidates")
for i in range(3):  # Fixed to 3 as per the task
    name = input(f"Enter candidate #{i+1} name: ")
    candi_list[name] = 0  # Initialize vote count to 0

# Step 2: Voting
num_voters = int(input("\n🗳️ Enter number of voters: "))
print("\nStart voting (type candidate's name exactly):")
for i in range(num_voters):
    vote = input(f"Voter #{i+1}, cast your vote: ")
    if vote in candi_list:
        candi_list[vote] += 1
        print("✅ Vote recorded.")
    else:
        print("❌ Invalid candidate.")

# Step 3: Show Results
print("\n📊 Voting Results:")
for name, votes in candi_list.items():
    print(f"{name}: {votes} vote(s)")
