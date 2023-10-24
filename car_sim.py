##
# Michael Forsythe and Matt Clifton
# Project 2 Part 2
#
##
total_distance = 0
net_miles = 0

def travel(tank_size: float, miles_per_gallon: float, cost_per_gallon: float) -> str:
    max_distance = find_max_distance(tank_size, miles_per_gallon)
    user_loop(max_distance)
    gallons_used = find_gallons(miles_per_gallon)
    total_cost = find_total_cost(gallons_used, cost_per_gallon)
    report = report_stats(total_cost, gallons_used)
    return report

def find_max_distance(tank_size: float, miles_per_gallon: float) -> float:
    max_distance = tank_size * miles_per_gallon
    return round(max_distance, 2)

def user_loop(max_distance: float) -> None:
    global total_distance, net_miles
    allowed_inputs = [0 , 1, 2]
    action = int(input("Enter 0-Calculate, 1-Forward, 2-Back: "))
    if action in allowed_inputs:
        if action == 1:
            do_choice1(max_distance)
        elif action == 2:
            do_choice2(max_distance)
        elif action == 0:
            return

def find_gallons(miles_per_gallon: float) -> float:
    global total_distance
    try:
        total_gallons = total_distance / miles_per_gallon
        result = total_gallons
    except ZeroDivisionError:
        result = "MPG is Zero!" 
    return result

def find_total_cost(number_gallons: float, cost_per_gallon: float) -> float:
    total_cost = number_gallons * cost_per_gallon
    result = round(total_cost, 2)
    return result

def wallet_status(total_cost: float) -> str:
    if total_cost < 25.00:
        result = "Cha Chiiinng!"
    elif total_cost >= 100.00:
        result = "Ouch!"
    else:
        result = "Wallet getting nervous!"
    return result

def report_stats(total_cost: float, number_gallons: float) -> str:
    global total_distance, net_miles
    stats = (
        "Total Miles Traveled: " + str(total_distance) + "\nNet Miles: " + str(net_miles) + 
        "\nGallons Used: " + str(find_gallons(miles_per_gallon)) + "\n\nTotal Cost: " + 
        str(find_total_cost(number_gallons, cost_per_gallon)) + 
        "\n" + wallet_status(total_cost)
    )
    return stats
    
def do_choice1(max_distance: float) -> None:
    global total_distance, net_miles
    distance_forward = int(input("Distance Forward:"))
    new_total_distance = distance_forward + total_distance
    if new_total_distance > max_distance:
        result = ("Not Enough Fuel!" + "\n" + str(new_total_distance - max_distance) + 
        " miles too far!" + "\n" + "Try Again!"
        )
        print(result)
    else:
        total_distance = new_total_distance
        go_forward(distance_forward)

def go_forward(miles_forward: int) -> None:
    global net_miles
    while miles_forward > 0:
        net_miles = net_miles + 1
        miles_forward = miles_forward - 1

def do_choice2(max_distance: float) -> None:
    global total_distance, net_miles
    distance_backward = int(input("Distance Backward:"))
    new_total_distance = distance_backward + total_distance
    if new_total_distance > max_distance:
        result = ("Not Enough Fuel!" + "\n" + str(new_total_distance - max_distance) + 
        " miles too far!" + "\n" + "Try Again!"
        )
        print(result)
    else:
        total_distance = new_total_distance
        go_back(distance_backward)

def go_back(miles_backward: int) -> None:
    global net_miles
    while miles_backward > 0:
        net_miles = net_miles - 1
        miles_backward = miles_backward - 1