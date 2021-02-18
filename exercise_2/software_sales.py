#Software Sales
#Driver: Kalluri Deekshitha Chowdary (U22127044) Navigator: Mario Lastra (U43655957)

#Assigning Variables
PRICE = 99
packages_purchased = int(input("Enter the number of packages purchased:"))
discount = 0
discount_price = 0

#Checking the amount purchased
if packages_purchased >= 10 and packages_purchased < 20:
    discount = 0.10
    discount_price = (PRICE*packages_purchased*discount)
    print("Discount Amount @ {:.0%} : ${:.2f}".format(discount, discount_price))
elif packages_purchased >= 20 and packages_purchased < 50:
    discount = 0.20
    discount_price = (PRICE*packages_purchased*discount)
    print("Discount Amount @ {:.0%} : ${:.2f}".format(discount, discount_price))
elif packages_purchased >= 50 and packages_purchased < 100:
    discount = 0.30
    discount_price = (PRICE*packages_purchased*discount)
    print("Discount Amount @ {:.0%} : ${:.2f}".format(discount, discount_price))
elif packages_purchased >= 100:
    discount = 0.40
    discount_price = (PRICE*packages_purchased*discount)
    print("Discount Amount @ {:.0%} : ${:.2f}".format(discount, discount_price))
else:
    discount = 0.0
    discount_price = (PRICE*packages_purchased*discount)
    print("Discount Amount @ {:.0%} : ${:.2f}".format(discount, discount_price))

#Calculating final price
final_amount = (PRICE*packages_purchased) - discount_price
print("Total amount: ${:.2f}".format(final_amount))