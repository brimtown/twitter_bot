from twitter import *
from twitter_bot import *

#http://www.dev.twitter.com
#http://iag.me/socialmedia/how-to-create-a-twitter-app-in-8-easy-steps/
#These will be on your Twitter app's page
#Make sure to set your access type to Read and Write
CONSUMER_KEY = ""
CONSUMER_SECRET = ""
OAUTH_TOKEN = ""
OAUTH_SECRET = ""

#MARKOV_LEVEL corresponds to how big of chunks TwitterBot will analyze
#Higher levels are more coherent, lower ones tend towards pure gibberish
MARKOV_LEVEL = 4
FILENAME = "./hamlet.txt"

#Read file into a string called 'source'
with open (FILENAME, "r") as myfile:
    source=myfile.read().replace('\n', ' ')

#Create a new instance of TwitterBot
bot = TwitterBot(source, MARKOV_LEVEL)

#Create an instance of the Twitter API using 'twitter'
api = Twitter(auth=OAuth(OAUTH_TOKEN, OAUTH_SECRET, CONSUMER_KEY, CONSUMER_SECRET))

#Post your tweet!
api.statuses.update(status=bot.tweet())