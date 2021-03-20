number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Error, Invalid number")
    number_of_items = int(input("Number of items: "))
total = 0
for i in range(0, number_of_items, 1):
    price = float(input("Price of item: "))
    total = total + price
if total > 100:
    total = total * 0.9
print("Total price for {:.0f} items is {:.2f}".format(number_of_items, total))