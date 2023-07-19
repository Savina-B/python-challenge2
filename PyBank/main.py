# import the csv file 
import csv
import os

file_to_open = os.path.join("Resources", "budget_data.csv")
file_to_save = os.path.join("Analysis", "output.txt")

# set variables
total_months = 0
total_profit_loss = 0
previous_profit_loss = 0
profit_loss_changes = []
greatest_increase_date = ""
greatest_increase_amount = float("-inf")
greatest_decrease_date = ""
greatest_decrease_amount = float("inf")

# open csv file
with open(file_to_open,'r') as budget_file:
    budget_reader = csv.reader(budget_file, delimiter = ',')
      
    # skip header row
    header = next(budget_reader) 
    
    
  
    for row in budget_reader:
        # calculate current profit loss
        date = row[0]
        profit_loss = int(row[1])
        
        total_months += 1
        
        total_profit_loss += profit_loss
        
        # calculate previous profit/loss from the previous row
        if total_months > 1:
            profit_loss_change = profit_loss - previous_profit_loss
            profit_loss_changes.append(profit_loss_change)
            
            # greatest increase and decrease in profits
            if profit_loss_change > greatest_increase_amount:
                greatest_increase_date = date
                greatest_increase_amount = profit_loss_change
                
            if profit_loss_change < greatest_decrease_amount:
                greatest_decrease_date = date
                greatest_decrease_amount = profit_loss_change
                
        # set the previous profit/loss for the next iteration
        previous_profit_loss = profit_loss
        
# the average profit/loss change
average_profit_loss_change = sum(profit_loss_changes) / len(profit_loss_changes)

# print results
print("Financial Analysis")
print("-----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_loss}")
print(f"Average Change: ${round(average_profit_loss_change, 2)}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_amount})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_amount})")

with open(file_to_save, 'w') as txt_file:
    txt_file.write('Financial Analysis'
                    f"Total Months: {total_months}"
                    f"Total: ${total_profit_loss}"
                    f"Average Change: ${round(average_profit_loss_change, 2)}"
                    f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_amount})"
                    f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_amount})")


    