#!/usr/bin/env python
# -*- coding:utf-8 -*-

#Francisco Carrillo Pérez
#Github: https://github.com/pacocp
#All wrongs reserved

import tweepy #It is necessary
import keys # Here is where you have to copy your keys, following the instructions
import termcolor #Let's give it some color!
def tweet(t):

    if len(t) > 140:
        raise Exception('status message is too long!')
    auth = tweepy.OAuthHandler(keys.consumer_key, keys.consumer_secret)
    auth.set_access_token(keys.access_token, keys.access_token_secret)
    api = tweepy.API(auth)
    result = api.update_status(status=t)
    return result

def main():
    termcolor.cprint("Type your tweet: ",'cyan')
    t = input()
    tweet(t)
    termcolor.cprint("Your status has been updated!",'cyan')

main()
