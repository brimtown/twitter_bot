twitter_bot

twitter_bot allows for the simple creation of parody twitter bots based upon a given source text.
Place a corpus of text you wish to create a bot off of, and specify the filename in the tweet.py file.
Then, after creating a Twitter app at http://dev.twitter.com, you can fill in your account information
and set your creation loose.

twitter_bot uses an algorithm based on Markov Chains to generate the tweets. The accuracy or "gibberish level"
can be tweaked with the MARKOV_LEVEL parameter in tweet.py.