#!/usr/bin/env python
# encoding: utf-8

import tweepy #https://github.com/tweepy/tweepy
import csv



#Twitter API credentials
consumer_key = "7VD1q53peHiSxeyKdDZ4MeLTe"
consumer_secret = "tNw2e0Dp75NW8a8DGQoN84hZursRFdEbJX02dTjG0QAj4Ux4XI"
access_key = "615463144-Pkvw6qROqNpfu4B3ATcYfiRPqG9dzffsoY5Glqzb"
access_secret = "HDM3l2UGYrWFQ0RdndxnDFQmnWsSnNRwsScv4gf3S4LKN"

listOwner = "DetlefBurkhardt"
listSlug = "Best-IT-Events"


def get_all_tweets(screen_name): #Twitter only allows access to a users most recent 3240 tweets with this method

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret) #authorize twitter, initialize tweepy
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    allLists = []
    myLists = api.lists_all()
    allLists.extend(myLists)
    #print allLists

    allMembers = [] #initialize a list to hold all the tweepy Tweets

    #new_tweets = api.user_timeline(screen_name = screen_name,count=200) #make initial request for most recent tweets (200 is the maximum allowed count)

    members = api.list_members(owner_screen_name=listOwner,slug=listSlug,count=200)

    allMembers.extend(members) #save most recent tweets
    #oldest = alltweets[-1].id - 1 #save the id of the oldest tweet less one

    #print allMembers


    #while len(new_tweets) > 0: #keep grabbing tweets until there are no tweets left to grab
        #print "getting tweets before %s" % (oldest)

        #new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest) #all subsiquent requests use the max_id param to prevent duplicates
        #alltweets.extend(new_tweets) #save most recent tweets
        #oldest = alltweets[-1].id - 1 #update the id of the oldest tweet less one

        #print "...%s tweets downloaded so far" % (len(alltweets))


    outputMembers = [[
        member.id_str,
        member.screen_name,
        member.name.encode("utf-8"),
        member.location.encode("utf-8"),
        member.url,
        member.description.encode("utf-8"),
        member.verified,
        member.followers_count,
        member.friends_count,
        member.listed_count,
        member.favourites_count,
        member.statuses_count,
        member.created_at,
        member.lang,
        member.profile_background_image_url,
        member.profile_image_url 
    ] for member in allMembers] 
    
    with open('%s_list_members.csv' % screen_name, 'wb') as f: #write the csv 
        writer = csv.writer(f, delimiter=';')
        writer.writerow([
            "id",
            "screen_name",
            "name",
            "location",
            "url",
            "description",
            "verified",
            "follower",
            "following",
            "lists",
            "likes",
            "tweets",
            "created",
            "lang",
            "bkg-image",
            "profile-image"
        ])
        writer.writerows(outputMembers)
    pass


if __name__ == '__main__':
    get_all_tweets("DetlefBurkhardt") #pass in the username of the account you want to download