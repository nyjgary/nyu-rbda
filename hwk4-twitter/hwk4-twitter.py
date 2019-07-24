#!/usr/bin/env python
# coding: utf-8

import sys
import argparse 
import tweepy
import numpy as np
import pandas as pd 
pd.set_option('display.max_colwidth', -1)

API_KEY = "REDACTED"
API_SECRET = "REDACTED"

def main(query_text, output_path, n_items, tweet_lang):
    
    """ Searches and outputs tweets to a CSV file. Excludes retweets. 
    
    Parameters
    ----------
    query_text: string
        Text to search Twitter 
        
    output_path: text 
        Path to CSV file that stores output tweets 
        
    n_items: integer (default: 1000)
        Maximum number of items to return 
        
    tweet_lang: string (default: en)
        Language of tweets to filter on 
            
    Returns
    -------
    result: dataframe
        Pandas dataframe containing search results. Each row is an original tweet (retweets excluded), containing
        fields: tweet_id, screen_name, date_created, retweet_count, text  
    (also saves dataframe as CSV to output_path)
        
    """
    
    # authenticate
    auth = tweepy.AppAuthHandler(consumer_key=API_KEY, consumer_secret=API_SECRET)
    api = tweepy.API(auth)

    # modify input arguments 
    query_text_ = query_text + ' -filter:retweets' # to filter out retweets 

    # use tweepy to retrieve tweets 
    results = [] 
    for tweet in tweepy.Cursor(api.search, q=query_text_, tweet_mode='extended', lang=tweet_lang).items(n_items):
        new_tweet = {}
        new_tweet['tweet_id'] = tweet.id_str
        new_tweet['screen_name'] = tweet.user.screen_name
        new_tweet['date_created'] = tweet.created_at
        new_tweet['retweet_count'] = tweet.retweet_count
        new_tweet['text'] = tweet.full_text            
        results.append(new_tweet)
    
    # convert list of dicts to dataframe 
    results_df = pd.DataFrame(results)
    results_df = results_df[['tweet_id', 'screen_name', 'date_created', 'retweet_count', 'text']]
    results_df.to_csv(output_path, index=False)

    print("Search for '{}' returned {} ({}) tweets. Saved to {}.".format(output_path, len(results_df), tweet_lang, output_path))

    return results_df 

if __name__ == '__main__': 

    # parse arguments 
    parser = argparse.ArgumentParser(description='This is a simple program to search and output tweets to CSV')
    parser.add_argument("query_text", help="Text to search Twitter")
    parser.add_argument("output_path", help="Path to CSV file that stores output tweets")
    parser.add_argument("--items", help="Maximum number of items to return (default=1000)", default=1000, type=int)
    parser.add_argument("--lang", help="Language of tweets to filter on (default=en)", default='en')
    args = parser.parse_args()

    # run function 
    main(query_text=args.query_text, output_path=args.output_path, n_items=args.items, tweet_lang=args.lang)
