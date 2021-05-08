from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    current_taxi = None
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    quitting = None
    total_fare = 0
    print("Let's drive!")

    while quitting is None:
        print("q)uit, c)hoose taxi, d)rive")
        menu_choice = input(str(">>>")).lower()
        if menu_choice == 'q':
            quitting = 'q'
        elif menu_choice == 'c':
            print('Taxis available:')
            taxi_list(taxis)
            taxi_choice = input("Choose taxi:")
            try:
                int(taxi_choice)
                try:
                    test = taxis[int(taxi_choice)]
                    current_taxi = int(taxi_choice)
                except IndexError:
                    print('Invalid taxi choice')
            except ValueError:
                print('Invalid taxi choice')

            print('Bill to date: ${:.2f}'.format(total_fare))
        elif menu_choice == 'd':
            if current_taxi is None:
                print('You need to choose a taxi before you can drive')
            else:
                drive_distance = input('Drive how far?')
                if drive_distance.isdigit():
                    taxis[current_taxi].start_fare()
                    taxis[current_taxi].drive(int(drive_distance))
                    print('Your {self.name} trip cost you ${}'.format(taxis[current_taxi].get_fare(),self=taxis[current_taxi]))
                    total_fare = total_fare + taxis[current_taxi].get_fare()

            print('Bill to date: ${:.2f}'.format(total_fare))
        else:
            print('Invalid option')
            print('Bill to date: ${:.2f}'.format(total_fare))

    print('Total trip cost: ${:.2f}\n'
          'Taxis are now:\n'.format(total_fare))
    taxi_list(taxis)


def taxi_list(taxis):
    taxi_number = 0
    for taxi in taxis:
        print('{} - {}'.format(taxi_number, taxi))
        taxi_number = taxi_number + 1


main()
