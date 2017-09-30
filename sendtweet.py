#!/usr/bin/env python
# -*- coding:utf-8 -*-

#Francisco Carrillo Pérez
#Github: https://github.com/pacocp
#All wrongs reserved

import tweepy #It is necessary
import keys # Here is where you have to copy your keys, following the instructions
import termcolor #Let's give it some color!
from ttp import ttp # twitter-text-python
from functools import reduce

def get_tweet_len(t, conf):
    p = ttp.Parser()
    parsed_tweet = p.parse(t)

    if parsed_tweet.urls:
        # remove urls from tweet text
        tweet_without_urls = reduce(lambda x,y: x.replace(y,'',1),
                                    parsed_tweet.urls, t)
        # get reserved characters for urls
        http_len = conf['short_url_length']
        https_len = conf['short_url_length_https']

        # compute tweet length
        tweet_len = reduce(lambda x,y: x+(https_len if 'https' in y else http_len),
                           parsed_tweet.urls, len(tweet_without_urls))
    else:
        tweet_len = len(t)

    return tweet_len

def tweet(t,api,conf):
    if get_tweet_len(t, conf) > 140:
        raise Exception('status message is too long!')

    result = api.update_status(status=t)
    return result

def get_timeline(api):
    tweets = api.home_timeline()
    return tweets

def get_favorites(api,pages):
    favorites = api.favorites("",pages)
    return favorites

def main():
    auth = tweepy.OAuthHandler(keys.consumer_key, keys.consumer_secret)
    auth.set_access_token(keys.access_token, keys.access_token_secret)
    api = tweepy.API(auth)
    conf = api.configuration()

    termcolor.cprint("WELCOME TO SENDTWEET\n","cyan")
    answ = '0'
    while(answ != '-1'):
        termcolor.cprint("What do you want to do? ","cyan")
        termcolor.cprint("1. Send a tweet ","green")
        termcolor.cprint("2. Get your timeline ","green")
        termcolor.cprint("3. Get your favorites","green")
        termcolor.cprint("--Type -1 for exit--","green")

        termcolor.cprint("Type a number","cyan")

        answ = input()

        if(answ == '2'):

            tweets = get_timeline(api)
            for i in tweets:

                termcolor.cprint("%s: "%i.user.screen_name,"cyan")
                termcolor.cprint("%s"%i.text,"yellow")
                print("\n")

        if(answ == '1'):
            termcolor.cprint("Type your tweet: ",'cyan')
            t = input()
            tweet(t,api,conf)
            termcolor.cprint("Your status has been updated!",'cyan')
            print("\n")
        if(answ == '3'):
            termcolor.cprint("Type the number of pages you want: ",'cyan')
            pages = input()
            favorites = get_favorites(api,pages)
            for i in favorites:
                termcolor.cprint("%s: "%i.user.screen_name,"cyan")
                termcolor.cprint("%s"%i.text,"yellow")
                print("\n")

        if(answ == '-1'):
            termcolor.cprint("THANK YOU! HAVE A NICE DAY!",'cyan')


main()

