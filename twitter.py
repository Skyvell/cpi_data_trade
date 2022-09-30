import tweepy
import settings


auth = tweepy.OAuthHandler(
    settings.TWITTER_API_KEY, 
    settings.TWITTER_API_SECRET,
    settings.TWITTER_API_ACCESS_TOKEN,
    settings.TWITTER_API_ACCESS_TOKEN_SECRET
    )

api = tweepy.API(auth)

def get_first_tweet(user_name: str) -> str:
    user_tweets = api.user_timeline(
        screen_name = user_name,
        exclude_replies = True,
        include_rts = False,
        count = 2
    )
    return user_tweets[0].text


