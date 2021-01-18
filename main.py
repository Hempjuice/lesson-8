from car import Car
from boat import Boat


if __name__ == '__main__':
    Vehicle1 = Car('Mercedes')
    #Vehicle1.color = 'черный'
    Vehicle1.refuel()
    Vehicle1.start_moving()
    Vehicle1.stop_moving()

    Vehicle2 = Boat('Titanic', 'белая')
    Vehicle2.start_moving()
    Vehicle2.stop_moving()
