from perpetual_usdt import place_market_order
from twitter import get_first_tweet

while True:
    tweet = get_first_tweet("Tree_of_Alpha")

core_cpi, all_cpi = extract_cpi(tweet)

# If CPI bla --> long. If cpi blu --> short.



def extract_cpi(tweet):
    pass

