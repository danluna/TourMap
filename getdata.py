import concert, time
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

date = city = venue = link = None
setlist = []
concerts = {}	# city name -> list of Concert objects "Los Angeles" -> [Concert, Concert, Concert]
coordinates = {}	# city name -> city coordinates tuple e.g.: "Los Angeles" -> (40.234, -12.322)
geolocator = Nominatim()

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

			if link == 'N/A':  # A setlist was not available for this show
				link = "Setlist Not Available"
				lineType = 5

		elif lineType == 5:	# Process setlist
			# Check for end of setlist (empty line)
			if not line.strip():
				# Add a new Concert object to the concerts dict
				if city in concerts:
					concerts[city].append(concert.Concert(date, city, venue, link, setlist))
				else:
					concerts[city] = [concert.Concert(date, city, venue, link, setlist)]
					
					"""# Get coordiantes from geopy
					while(1): 
						try:
							location = geolocator.geocode(city)
							break
						except GeocoderTimedOut as e:
							print("geocode failed")

					
					#print(city + ": %.2f  %.2f" % (coordinates[city][0], coordinates[city][1]))
					#twoe.write(city + ": " + str(location.latitude) + " " + str(location.longitude) + '\n')"""

				lineType = 0	
			else: 
				setlist.append(line)

		if lineType != 5:
			lineType += 1

# Store the coordinates into the coordinates dictionary
with open('coordinates.txt') as f:
	for line in f:
		colonSplit = line.split(': ')
		city = colonSplit[0]
		coordSplit = colonSplit[1].split(" ")
		coordinates[city] = (float(coordSplit[0].strip()), (coordSplit[1].strip()))



