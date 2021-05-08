"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from prac_08.taxi import Taxi

my_taxi = Taxi('Prius 1', 100)
my_taxi.drive(40)
print(my_taxi, "fare=",my_taxi.get_fare())
my_taxi.start_fare()
my_taxi.drive(100)
print(my_taxi, "fare=",my_taxi.get_fare())
