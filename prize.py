def which_prize(points):
	prize = None

	if points<50:
		prize = "wooden rabbit"
	elif points<150:
		prize = "No prize"
	elif points<180:
		prize = "wafer-thin mint"
	elif points<200:
		prize = "penguin"	
	else:
		prize = "Oh dear, no prize this time."

	if prize:
		return prize

points = 2*30

print(which_prize(points))