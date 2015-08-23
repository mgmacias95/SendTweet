#!/usr/bin/env python
# -*- coding:utf-8 -*-

#Francisco Carrillo Pérez
#Github: https://github.com/pacocp
#All wrongs reserved

import tweepy #It is necessary
import keys # Here is where you have to copy your keys, following the instructions
import termcolor #Let's give it some color!
def tweet(t,auth):

    if len(t) > 140:
        raise Exception('status message is too long!')

    api = tweepy.API(auth)
    result = api.update_status(status=t)
    return result

def get_timeline(auth):
    api = tweepy.API(auth)
    tweets = api.home_timeline()
    return tweets
def get_favorites(auth,pages):
    api = tweepy.API(auth)
    favorites = api.favorites("",pages)
    return favorites
def main():
    auth = tweepy.OAuthHandler(keys.consumer_key, keys.consumer_secret)
    auth.set_access_token(keys.access_token, keys.access_token_secret)

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

            tweets = get_timeline(auth)
            for i in tweets:

                termcolor.cprint("%s: "%i.user.screen_name,"cyan")
                termcolor.cprint("%s"%i.text,"yellow")
                print("\n")

        if(answ == '1'):
            termcolor.cprint("Type your tweet: ",'cyan')
            t = input()
            tweet(t,auth)
            termcolor.cprint("Your status has been updated!",'cyan')
            print("\n")
        if(answ == '3'):
            termcolor.cprint("Type the number of pages you want: ",'cyan')
            pages = input()
            favorites = get_favorites(auth,pages)
            for i in favorites:
                termcolor.cprint("%s: "%i.user.screen_name,"cyan")
                termcolor.cprint("%s"%i.text,"yellow")
                print("\n")

        if(answ == '-1'):
            termcolor.cprint("THANK YOU! HAVE A NICE DAY!",'cyan')



main()
