#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import datetime

#Variables that contains the user credentials to access Twitter API 
access_token = "xxxxxxxxxx-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
access_token_secret = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
consumer_key = "xxxxxxxxxxxxxxxxxxxxxxxxx"
consumer_secret = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"


#Basic listener, edited to save results to a new file every day
class StdOutListener(StreamListener):

    def on_data(self, data):
        f = self.give_me_file()
        f.write(data)
        return True
    #creates writeable file, also closes previous file
    def create_file(self):
        if hasattr(self, "f"):
            self.f.close()
        self.date = datetime.datetime.now().date()
        name = str(self.date) + '.txt'
        self.f = open(name, 'w')
    #creates a new file for a new day
    def give_me_file(self):
        if hasattr(self, "f") and self.date == datetime.datetime.now().date():
            return self.f
        else: 
            self.create_file()
            return self.f
    #outputs errors
    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords:
    stream.filter(track=['whiskey', 'whisky', 'gin', 'vodka', 'rum', 'tequila', 'brandy', 'moonshine', 'absinthe', 'schnapps'])
