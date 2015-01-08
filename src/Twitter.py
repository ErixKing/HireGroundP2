import tweepy

# The consumer keys can be found on your application's Details
# page located at https://dev.twitter.com/apps (under "OAuth settings")
consumer_key="rtSI6qY8er6klGgPFDwNVSWAA"
consumer_secret="1V2k01WMb5zyI40HQwyBuvr7tPSpqtxoDZhsPRDQiyroV7sfuw"

# The access tokens can be found on your applications's Details
# page located at https://dev.twitter.com/apps (located under "Your access token")
access_token="174059917-9sEm5laVY7qKt8U3lCi072yvPOtJBVOCRknw4IqL"
access_token_secret="QhUcqWk06yonYvRYPLonf4c9E3AloLbxCggzoVKkspUb6"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.secure = True
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
query = '#job'
max_tweets = 10
searched_tweets = [status for status in tweepy.Cursor(api.search, q=query).items(max_tweets)]
for x in searched_tweets:
    value = x.text
    #index = value.find('has')
    #print value[index:]
    print(value + '\n')


