import tweepy
consumer_key=""
consumer_secret=""
access_token=""
access_token_secret=""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

for user in tweepy.Cursor(api.friends, screen_name="TechCrunch").items():
    print('friend: ' + user.screen_name)

for user in tweepy.Cursor(api.followers, screen_name="TechCrunch").items():
    print('follower: ' + user.screen_name)