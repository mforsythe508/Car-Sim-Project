##
# Michael Forsythe and Matt Clifton
# Project 2 Part 1
#
##
import car_sim
def main() -> None:
    tank_size = float(input("Tank Size (Gallons): "))
    miles_per_gallon = float(input("MPG: "))
    cost_per_gallon = float(input("Cost Per Gallon: "))
    result = car_sim.travel(tank_size, miles_per_gallon, cost_per_gallon)
    print(result)

if __name__ == "__main__":
    main()