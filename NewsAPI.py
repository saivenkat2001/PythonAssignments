from newsapi import NewsApiClient

api_key = "ff06ee95ba2d4fafa5cc94e18280e008"
newsapi = NewsApiClient(api_key=api_key)

#these are the end point which are available in the newsAPI
#.get_top_headlines
#get_everything
#get_sources

data = newsapi.get_everything(q='jupyter labs', language='en', page_size=20)
# print(type(data))
# print(data.keys())

articles = data['articles']

# for key, value in articles[0].items():
#     print(key, value)
#

for x,y in enumerate(articles):
    print(f'{x}   {y["title"]}')