
#  import needed Libraries
import csv
import os


# point to the resource file we're looking to work with & where we want to write our file
input_file = os.path.join("Resources", "budget_data.csv")
output_file = os.path.join("Analysis", "budget-data-output.txt")

# Set the conditions for loop
#-------------------------------------------------------------
# set month count and total amount to 0

month_count = 0
final_sum = 0

# Build empty lists
months = []
monthly_changes = []

highest_rise = {"month": "", "change": float("-inf")}

highest_fall = {"month": "", "change": float("inf")}


with open(input_file) as input_data:
    reader = csv.DictReader(input_data)
    first_row = next(reader)

    #begin counting months as we go

    month_count = month_count + 1
    final_sum = final_sum + int(first_row['Profit/Losses'])
    previous_value = int(first_row['Profit/Losses'])

    # iterate 
    for row in reader:
        month_count = month_count + 1
        current_value = int(row['Profit/Losses'])
        final_sum = final_sum + current_value

        # calculate and track monthly changes
        monthly_change = current_value - previous_value
        previous_value = current_value

        # Add to the list as we go
        months.append(row['Date'])
        monthly_changes.append(monthly_change)

        # then determine the highest rise & fall in the dataset
        if monthly_change > highest_rise["change"]:
            highest_rise["month"] = row['Date']
            highest_rise["change"] = monthly_change

        if monthly_change < highest_fall["change"]:
            highest_fall["month"] = row["Date"]
            highest_fall["change"] = monthly_change


# calculate the average change of the dataset

average_change = sum(monthly_changes) / len(monthly_changes)

# then output it formatted for Terminal and write to .txt file

output = (
    f"\nFinancial Analysis\n"
    f"------------------------------------\n"
    f"\nTotal Months: {month_count}\n"
    f"Total Change: ${final_sum}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {highest_rise['month']} (${highest_rise["change"]})\n"
    f"Greatest Decrease in Profits: {highest_fall['month']} (${highest_fall["change"]})\n"
)

print(output)

# open and write to the .txt file
with open(output_file, "w") as txt_file:
    txt_file.write(output)
        





