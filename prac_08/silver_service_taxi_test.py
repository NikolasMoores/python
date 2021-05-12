from prac_08.silver_service_taxi import SilverServiceTaxi

silver_taxi = SilverServiceTaxi('Fancy Car', 200, 2)
silver_taxi.drive(18)
print(silver_taxi)
print("The fare has come to ${:.2f}".format(silver_taxi.get_fare()))
