
# two sets
invited_friends = {"Alex", "Sam", "Leo", "Mina"}
rsvped = {"Mina", "Sam", "Jordan"}

# everyone who was invited (union), everyone who RSVP'd, and those who haven't replied (difference)
print("Everyone who was invited:", invited_friends | rsvped)
print("Everyone who RSVP'd:", rsvped)
print("Those who haven't replied yet:", invited_friends - rsvped)

# two new names to invited_friends
invited_friends.update(["Chris", "Taylor"])

# One of the people canceled - remove them from rsvped
canceled = "Sam"
rsvped.discard(canceled)
print(f"{canceled} canceled and was removed from rsvped.")

# Print how many total confirmed guests are attending
print("Total confirmed guests:", len(rsvped))

# Check if "Leo" is still coming - print a message depending on result
if "Leo" in rsvped:
	print("Leo is still coming!")
else:
	print("Leo is not coming.")
