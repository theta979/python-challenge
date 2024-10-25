# Import libraries
import csv
import os

# Point to files we need to load and where we want to write our output
input_file = os.path.join("Resources", "election_data.csv") #path to input file
output_file = os.path.join("analysis", "election_analysis.txt") #path to output

# Initialize variables to track the election data

total_votes = 0 # count the total number of votes (we'll use this later)

# Define lists and dictionaries to track candidate names and vote counts

candidate_totals = {}
winning_candidate = ""
winning_total = 0

# Open the CSV file and process it

with open(input_file, encoding='utf-8') as election_data:
    reader = csv.DictReader(election_data) # Store header in Dictionary so it's skipped
    

    # Loop through each row of the dataset and process it
    for row in reader:
        total_votes = total_votes + 1 # Increment the total vote count for each row
        candidate_name = row["Candidate"] # Pointing to the column we get the name from


        if candidate_name not in candidate_totals: # Get the candidate's name from the row
            candidate_totals[candidate_name] = 0 # add candidate to dictionary with 0 count
        
        candidate_totals[candidate_name] += 1 # increment 1 vote to candidates total


# Open file (in Write mode) and write the total vote count to .txt file
with open(output_file, "w") as txt_file:
    election_results = (
          f"\nElection Results\n"
          f"\n------------------------\n"
          f"\n"
          f"Total Votes: {total_votes}\n"
          f"\n--------------------------\n"
    )
     
    # Print election results to the terminal
    print(election_results)
    txt_file.write(election_results) # Write to .txt file
     
    # retrieving pairs from dicitonary to calculate percentage each candidate got 
    for candidate, votes in candidate_totals.items():
        vote_percentage = (votes / total_votes) * 100

        # Determing winner
        if votes > winning_total:
            winning_total = votes
            winning_candidate = candidate
               
        # Calculate and format results        
        candidate_results = f"{candidate}: {vote_percentage: .3f}% ({votes})\n"
        
        print(candidate_results, end="")
        txt_file.write(candidate_results)
    
    # Retrieving winner and formatting for print
    winning_summary = (
         f"-----------------------------\n"
         f"\n"
         f"Winner: {winning_candidate}\n"
         f"\n"
         f"-----------------------------\n"
    )

    print(winning_summary)
    txt_file.write(winning_summary)
          



