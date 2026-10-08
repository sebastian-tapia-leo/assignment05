# Road Trip Planner
# This code can estimate the gas cost of a round trip and the cost per traveler.

print("================================")
print("ROAD TRIP PLANNER")
print("================================")

#  THis is to collect the user's trip information.
user_name = input("\nWhat is your name? ")
destination = input("Where are you traveling? ")
one_way_distance = float(input("How many miles is the trip one way? "))
miles_per_gallon = float(input("What is your vehicle's miles per gallon? "))
gas_price = float(input("What is the gas price per gallon? "))
number_of_travelers = int(input("How many travelers are going? "))

# This is to calculate the round-trip distance and gas costs.
total_miles = one_way_distance * 2
gallons_needed = total_miles / miles_per_gallon
total_gas_cost = gallons_needed * gas_price
cost_per_traveler = total_gas_cost / number_of_travelers

# THis is to display the personalized trip summary.
print("\n================================")
print("TRIP SUMMARY")
print("================================")
print(f"Traveler: {user_name.upper()}")
print(f"Destination: {destination}")
print(f"\nRound-trip miles: {total_miles:.2f}")
print(f"Gallons of gas needed: {gallons_needed:.2f}")
print(f"Total estimated gas cost: ${total_gas_cost:.2f}")
print(f"Cost per traveler: ${cost_per_traveler:.2f}")
print("================================")
print("Have a great trip!")