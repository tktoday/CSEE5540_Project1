import tweepy
import json
from config import CONSUMER_KEY
from config import CONSUMER_SECRET
from config import ACCESS_TOKEN_KEY
from config import ACCESS_TOKEN_SECRET


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


# This listener will print out all Tweets it receives
class PrintListener(tweepy.StreamListener):
    def on_data(self, data):
        # Decode the JSON data
        tweet = json.loads(data)
        if tweet['entities'] != []:
            if tweet['entities']['hashtags'] != []:
                Hashtags = tweet['entities']['hashtags'][0]['text']
                file = open("Hashtags.csv", "a")
                file.write(json.dumps(Hashtags, indent=2) + "\n")
                file.close()
            if tweet['entities']['urls'] != []:
                URL = tweet['entities']['urls'][0]['url']
                file = open("URLs.csv", "a")
                file.write(json.dumps(URL, indent=2) + "\n")
                file.close()
        # write tweets to .csv file
        file = open("tweets2.csv", "a")
        file.write(json.dumps(tweet, indent=2) + "," + "\n")
        file.close()

        # Print out the Tweet
        print('@%s: %s' % (tweet['user']['screen_name'], tweet['text'].encode('ascii', 'ignore')))
    def on_error(self, status):
        print(status)


if __name__ == '__main__':
    listener = PrintListener()

    # Show system message
    print('I will now print Tweets containing "NBA" and save them in a csv file ==>')

    # Authenticate
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)

    # Connect the stream to our listener
    stream = tweepy.Stream(auth, listener)
    stream.filter(track=['America'])
