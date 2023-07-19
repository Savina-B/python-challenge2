import csv
import os

file_to_open = os.path.join("Resources", "election_data.csv")
file_to_save = os.path.join("Analysis", "output.txt")
with open(file_to_open, 'r') as file:
    csv_reader = csv.reader(file)
# skip header
    header = next(csv_reader)


# Settig variables
    total_votes = 0
    candidates = []
    candidate_votes = {}
    winning_candidate = ""
    winning_count = 0

    for row in csv_reader:
        #print(row)
        total_votes += 1

# creating candidate variables
  

        if row[2] not in candidates:
            candidates.append(row[2])
            candidate_votes[row[2]] = 0
        candidate_votes[row[2]] += 1

# candidate name and vote


# print votes cast
    print("Election Results")
    print(f"Total Votes: {total_votes}")

# calculating percentage of votes each candidate won
    percentage = 0
    for candidate in candidates:
        if candidate_votes[candidate] > winning_count: 
            winning_count = candidate_votes[candidate]
            winning_candidate = candidate

        percentage = candidate_votes[candidate]/total_votes * 100

# Printing the candidate's name, percentage of votes received, and total votes received
        print(f"{candidate}: {percentage:.3f}% ({candidate_votes[candidate]})")

# how to find the winner of the election based on popular vote?
    print(f"Winner: {winning_candidate}")

with open(file_to_save, 'w') as txt_file:
        txt_file.write("Election Results\n")
        txt_file.write(f"Total Votes: {total_votes}\n")

        for candidate in candidates:
            percentage = candidate_votes[candidate] / total_votes * 100

            txt_file.write(f"{candidate}: {percentage:.3f}% ({candidate_votes[candidate]})\n")

            if candidate_votes[candidate] > winning_count:
                winning_count = candidate_votes[candidate]
                winning_candidate = candidate

        txt_file.write(f"Winner: {winning_candidate}\n")