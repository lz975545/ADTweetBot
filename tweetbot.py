import tweepy
from time import sleep
from credentials import*

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

my_file = open('quotes.txt')
file_lines = my_file.readlines()
my_file.close()

# Tweet a line every 10 minutes
def tweet():
    for line in file_lines:
        try:
             print(line)
             if line != '\n':
                 api.update_status(line)
                 sleep(10*60)
        except tweepy.TweepError as e:
            print(e.reason)a
            sleep(2)

tweet()