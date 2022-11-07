#! /usr/bin/env /usr/bin/python3
# Author: Ardit Sulce, Automate Everything with Python, Udemy
# Course URL: https://www.udemy.com/course/automate-everything-with-python/
#
# This script retrieves the posts in a subreddit and outputs those created in the last 24 hours to outfile
#
# Modified by robertay 7 November 2022
# - Get client_sevret credentials for environment variables
# - Use unix time and get posts created in the last delta seconds rather than converting the post.created time to datetime format.  Fewer conversions so should be more efficient when used on a busy subreddit.
# - Added comments to explain what is going on

# Before running this script, got to reddit.com and create a user account if you havn't already.  Then go to: https://www.reddit.com/prefs/apps 
# and click on "create an app".  Give your app a name and select the "script" button.
# You should then see a box with:
# App Name
# personal use script
# App ID (like bo0SvJu45UCd8NPCJA)
# secret (like 2YcAEUC__i4rrXFbA)
# Put all these details into environment variables

import praw   # External module for reddit
from datetime import datetime
from time import time
from os import getenv

subreddit_name='Jokes'
age=8640  # Maximum age of the posts, number of seconds in 2.4 hours
outfile='output.txt'
spacer="-" * 80

# Create an instance of the reddit class with your reddit account details
reddit = praw.Reddit(user_agent=True, 
  client_id=getenv('REDDIT_APP_ID'), 
  client_secret=getenv('REDDIT_APP_SECRET'), 
  username=getenv('REDDIT_USERNAME'),
  password=getenv('REDDIT_PASSWORD'))

# Create a subreddit instance
subreddit = reddit.subreddit(subreddit_name)

# Get the current time
current_time = time()

# Cycle through the recent posts for those created in the last age seconds and write them to the outfile
with open(outfile, 'w') as file:
  for post in subreddit.new():
    delta_time = current_time - post.created
    if delta_time <= age:
      file.write(f'{post.title}\n{post.selftext}\n{spacer}\n\n')

