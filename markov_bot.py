"""
Author: importantnk@gmail.com
Rath Twitter Bot

This is a simple bot for twitter that is being used for several functions.
The main function of the bot is to provide an easy learning experience with
the Twitter API and pulling information from other sources to post on twitter.
"""
# Imports
import markov
import logging
import sys
from make_dir import makeDir
from twython import Twython
from auth import (consumer_key,
                  consumer_secret,
                  access_token,
                  access_token_secret,
                  )

twitter = Twython(consumer_key,
                  consumer_secret,
                  access_token,
                  access_token_secret
                  )

# Checking if there's an argument for where to log.
if len(sys.argv) == 1:
    path = 'logs/'
else:
    path = str(sys.argv[1])

makeDir(path)

logging.basicConfig(filename=(path+'record.log'), level=logging.INFO,
                    format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')

message = markov.message()

try:
    twitter.update_status(status=message)
    logging.info('I Tweeted!\n')
except Exception as err:
    # This is mostly to catch 405 forbidden's on duplicate tweets
    # Although on this bot it would be astronomical to occur
    logging.info(str(err)+'\n')

exit()
