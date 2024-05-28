# Question 1
# Create a function named calculate_discount(price, discount_percent) that calculates the final price after applying a discount. The function should take the original price (price) and the discount percentage (discount_percent) as parameters. If the discount is 20% or higher, apply the discount; otherwise, return the original price.

def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        final_price = price - ((discount_percent/100)*price)
        return f"The final price is: {final_price}"
    else:
        final_price = price
        return f"The final price is: {final_price}"
        
Final_price = calculate_discount(300, 30)
print(Final_price)

# Question 2
# Using the calculate_discount function, prompt the user to enter the original price of an item and the discount percentage. Print the final price after applying the discount, or if no discount was applied, print the original price.

price = float(input("Enter price: \n"))
discount_percent = float(input("Enter discount offered: \n"))
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        final_price = price - ((discount_percent/100)*price)
        return f"The final price is: {final_price}"
    else:
        final_price = price
        return f"The final price is: {final_price}"
        
Final_price = calculate_discount(price,  discount_percent)
print(Final_price)
