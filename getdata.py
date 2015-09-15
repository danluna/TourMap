import concert

date = city = venue = link = None
setlist = []
concerts = {}

lineType = 1  # 1: date, 2: city, 3: venue, 4: link, 5: setlist 6: empty 

with open('metallica_data.txt') as f:
	for line in f:

		if lineType == 1:	# Process date
			date = line.strip()

		elif lineType == 2:	# Process city
			city = line.strip()

		elif lineType == 3:	# Process venue
			venue = line.strip()

		elif lineType == 4:	# Process link
			link = line.strip()

		elif lineType == 5:	# Process setlist
			# Check for end of setlist (empty line)
			if not line.strip():
				# Add a new Concert object to the concerts dict
				if city in concerts:
					concerts[city].append(concert.Concert(date, city, venue, link, setlist))
				else:
					concerts[city] = [concert.Concert(date, city, venue, link, setlist)]

				lineType = 0	
			else: 
				setlist.append(line)

		if lineType != 5:
			lineType += 1

		
for value in concerts["Madrid, Spain"]:
	print(value.date)