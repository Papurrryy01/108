# tuple called "travel_bag" with at least 5 items
travel_bag = ("shirt", "socks", "shoes", "toothbrush", "jacket")

# Print the SECOND and FOURTH items in your bag
print("Second item:", travel_bag[1])
print("Fourth item:", travel_bag[3])

# Check if "shoes" is in your travel bag
if "shoes" in travel_bag:
	print("You are ready to walk!")
else:
	print("you forgot your shoes!!!")

# Make a new tuple called "essentials" with 3 must-have items
essentials = ("passport", "phone", "wallet")

# Combine both tuples into one called "final_bag"
final_bag = travel_bag + essentials

# Print how many total items you now have using len()
print("Total items in final_bag:", len(final_bag))

# Print the last item in your "final_bag"
print("Last item in final_bag:", final_bag[-1])
