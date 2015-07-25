# SendTweet

##Explanation
Simple Python scritp, with it you can send a tweet via Terminal. You need to have installed Tweepy: 

https://github.com/tweepy/tweepy

And you need to have Python3.

##How to use

First, you have to create an app for twitter:

1. Open a web browser and go to https://apps.twitter.com/app/new
2. Sign in with your normal Twitter username and password if you are not already signed in.
3. Enter a name, description, and temporary website (e.g. http://coming-soon.com)
4. Read and accept the terms and conditions – note principally that you agree not to distribute any of the raw tweet data and to delete tweets from your collection if they should be deleted from Twitter in the future.
5. Click "Create your Twitter application"
6. Click on the "API Keys" tab and then click "Create my access token"
7. Wait a minute or two and press your browser's refresh button (or ctrl+r / cmd+r)
8. You should now see new fields labeled "Access token" and "Access token secret" at the bottom of the page.
9. You now have a Twitter application that can act on behalf of your Twitter user to read data from Twitter.

(This description of how to get the tokens for the keys it's from the ReadMe of: https://github.com/computermacgyver/twitter-python)

Now you have to copy the ConsumerKey, the ConsumerSecret,the Access token and the Access token secret to the keys.py.

Then the only thing you have to do is execute the script!

```
  python sendtweet.py
```

or:

```
  chmod 771 sendtweet.py
  ./sendtweet.py
```

##Author

Francisco Carrillo Pérez

carrilloperezfrancisco@gmail.com

All wrongs reserved
