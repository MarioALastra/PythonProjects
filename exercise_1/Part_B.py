#   Program for calculating tip
#   Driver: Collin Reynolds (U78898749)     Navigator:Mario Lastra (U43655957)

#   Assigning variables
subtotal = float(input('Enter the subtotal:'))
gratuity = float(input('Enter tip amount as a %:'))

#   Calculating tip and total
tip_amount = subtotal * (gratuity / 100)
total =  subtotal + tip_amount

#   Returning values
print('Subtotal: $', '{:,.2f}'.format(subtotal))
print('Tip: $', '{:,.2f}'.format(tip_amount))
print('Total: $', '{:,.2f}'.format(total))
