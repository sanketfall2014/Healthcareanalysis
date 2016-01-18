from tweepy.streaming import StreamListener
import json
import tweepy
from tweepy import Stream
import csv


outfile = open('data.txt', 'w')

config_json = open('config.json', 'r')
config = json.load(config_json)

consumer_key = config["consumer_key"]
consumer_secret = config["consumer_secret"]

access_token = config["access_token"]
access_token_secret = config["access_token_secret"]

csvFile = open('tweepy.csv', 'a')
csvWriter = csv.writer(csvFile)

class StdOutListener(StreamListener):

    def on_status(self, status):

        a = []
        print('Tweet text: ' + status.text.encode('utf-8'))
        a.append(status.text.encode('utf-8'))
        directAttrs = ('place,coordinates,lang,created_at,'
                       'retweeted_status,source source_url').split(',')
        for k in directAttrs:
            value = getattr(status, k, None)
            if value is not None:
                print k, str(value).encode('utf-8')
                #a.append(str(value).encode('utf-8'))

        userAttrs = 'screen_name,location'.split(',')
        for k in userAttrs:
            value = getattr(status, k, None)
            if value is not None:
                print k, str(value).encode('utf-8')
                #a.append(str(value).encode('utf-8'))
        csvWriter.writerow(a)
        return True

    def on_error(self, status_code):
        print('Got an error with status code: ' + str(status_code))
        return True

    def on_timeout(self):
        print('Timeout...')
        return True

if __name__ == '__main__':
    listener = StdOutListener()
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, listener)
    stream.filter(track=['Medical', 'Hospital', 'Doctor', 'Nurse',
                         'dentist', 'cancer', 'heart attack', 'dehydration', 'ebola', 'HIV',
                         'bloodgroup', 'pharmacy', 'novartis', 'asthma', 'tumor', 'flu'])
