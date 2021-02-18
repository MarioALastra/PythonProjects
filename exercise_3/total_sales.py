#   Total Sales
#   Driver: Tilak Patel (U32922919) Navigator: Mario Lastra (U43655957)
#   This script will calculate the total sales of the week

week = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
sales_week = []
total_sales = 0

for day in week:
    user_input = int(input("Enter the sales for {}: ".format(day)))

    while user_input < 0:
        user_input = int(input("Input was invalid. Re-enter the sales for {}: ".format(day)))
    
    sales_week.append(user_input)
    total_sales += user_input

print("The total sales is: ${:.2f}".format(total_sales))
print("The minimum sale amount was: ${:.2f}".format(min(sales_week)))
print("The maximum sale amount was: ${:.2f}".format(max(sales_week)))