#!/usr/bin/env python
# encoding: utf-8

import tweepy #https://github.com/tweepy/tweepy
import csv



#Twitter API credentials
consumer_key = "7VD1q53peHiSxeyKdDZ4MeLTe"
consumer_secret = "tNw2e0Dp75NW8a8DGQoN84hZursRFdEbJX02dTjG0QAj4Ux4XI"
access_key = "615463144-Pkvw6qROqNpfu4B3ATcYfiRPqG9dzffsoY5Glqzb"
access_secret = "HDM3l2UGYrWFQ0RdndxnDFQmnWsSnNRwsScv4gf3S4LKN"


def get_all_tweets(screen_name): #Twitter only allows access to a users most recent 3240 tweets with this method

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret) #authorize twitter, initialize tweepy
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    alltweets = [] #initialize a list to hold all the tweepy Tweets

    new_tweets = api.user_timeline(screen_name = screen_name,count=200) #make initial request for most recent tweets (200 is the maximum allowed count)
    alltweets.extend(new_tweets) #save most recent tweets
    oldest = alltweets[-1].id - 1 #save the id of the oldest tweet less one

    while len(new_tweets) > 0: #keep grabbing tweets until there are no tweets left to grab
        print "getting tweets before %s" % (oldest)
        new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest) #all subsiquent requests use the max_id param to prevent duplicates
        alltweets.extend(new_tweets) #save most recent tweets
        oldest = alltweets[-1].id - 1 #update the id of the oldest tweet less one

        print "...%s tweets downloaded so far" % (len(alltweets))
        
    outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8"),tweet.retweet_count,tweet.favorite_count] for tweet in alltweets] #transform the tweepy tweets into a 2D array that will populate the csv    
    
    #write the csv    
    with open('%s_tweets.csv' % screen_name, 'wb') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow(["id","created_at","text","retweet_count","favorite_count"])
        writer.writerows(outtweets)
    
    pass


if __name__ == '__main__':
    #pass in the username of the account you want to download
    get_all_tweets("DetlefBurkhardt")