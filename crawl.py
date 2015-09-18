import requests
from bs4 import BeautifulSoup

unicode_Error_Counter = 0

def tour_spider(max_year):
	year = 1982
	page = 1
	fw = open('metallica_data.txt', 'w')

	while year <= max_year:
		url = 'http://www.metallica.com/tour_date_list.asp?year=' + str(year) + '&page=' + str(page)
		source_code = requests.get(url)
		plain_text = source_code.text
		soup = BeautifulSoup(plain_text, "html.parser")

		data = soup.find('table', class_="DDT-wrap").find('tbody')

		try:
			for date_set in data.findAll('tr'):

				fw.write(date_set.contents[1].string + '\n')
				fw.write(date_set.contents[3].a.string + '\n')
				fw.write(date_set.contents[5].string + '\n')
				a_tag = date_set.contents[7].a

				try:
					# Go to the setlist page and get the songs
					fw.write(a_tag.get('href') + '\n')
					setlist_url = a_tag.get('href')
					source_code = requests.get(setlist_url)
					plain_text = source_code.text
					soup2 = BeautifulSoup(plain_text, "html.parser")
					data = soup2.find('table', class_="DDT-panel")

					firstItem = True
					for song in data.findAll('tr'):
						# Skip the first item, it's not a song, only a title
						if firstItem: 
							firstItem = False
							continue

						try:
							print(song.find('a').string.strip())
							fw.write(song.find('a').string.encode('utf-8').strip())
							fw.write('\n')
						except AttributeError:
							try:
								print(song.contents[3].contents[1].strip())
								fw.write(song.contents[3].contents[1].strip() + '\n')
							except IndexError:
								print("ENCORE HERE")
					

				except AttributeError:
					# Get the link fromt he <a> tag and href attribute since there is no setlist link
					setlist_url = date_set.contents[3].a.get('href')
					print(setlist_url)
					fw.write(setlist_url.strip())
					fw.write('\n')


				fw.write('\n')

		except AttributeError:
			# No tour dates this given year
		
		# Check for more pages for this year
		liTags = soup.find(attrs={'class': 'next_page'})
		if not liTags:
			year+=1
			page=1
		else:
			page+=1

	# End of spider, close file write
	fw.close()

// Start the crawler
tour_spider(2015)