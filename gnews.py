import requests
import inputs
import sanalysis
# import sa_gui

company = inputs.input_company()
from_date = inputs.input_date_from()
# company = sa_gui.get_company()
# from_date = sa_gui.get_date()


url = ('https://newsapi.org/v2/everything?'
	       'q={}&'
	       'from={}&'
	       'sortBy=popularity&'
	       'apiKey=1683f212df3040baa5e7e2ee8899b5a7'.format(company, from_date))

response = requests.get(url)
respone_json = response.json()

articles = respone_json['articles']

for items in articles:
	title = items['title']
	description = items['description']
	url = items['url']
	publishedAt = items['publishedAt']

	print(title)
	print(description)
	print(url)
	print("")
	sanalysis.tb_sentiment(description)
	print("")
