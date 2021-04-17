from prac_06.guitar import Guitar

Gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
Other_Guitar = Guitar("Other Guitar", 2013, 200.00)

print("Gibson L-5 CES get_age() - Expected 99. Got {}".format(Gibson.get_age()))
print("Another Guitar get_age() - Expected 8. Got {}".format(Other_Guitar.get_age()))
print("Gibson L-5 CES is_vintage() - Expected True. Got {}".format(Gibson.is_vintage()))
print("Other_Guitar is_vintage() - Expected False. Got {}".format(Other_Guitar.is_vintage()))

