"""flee =  open('coordinates.txt', 'w')

for c in concerts:
	while(1): 
		try:
			location = geolocator.geocode(c)
			break
		except GeocoderTimedOut as e:
			print("geocode failed")

	print("writing " + c)
	flee.write(c + ": " + str(location.latitude) + " " + str(location.longitude) + '\n')

flee.close()"""