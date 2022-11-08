#! /usr/bin/env /usr/bin/python3
# Author: Ardit Sulce, Automate Everything with Python, Udemy
# Course URL: https://www.udemy.com/course/automate-everything-with-python/
#
# This script posts to the pythonsandlot subreddit
#
# NO LONGER WORKS! pythonsandlot subreddit is now restricted
# ================
# Modified by robertay 7 November 2022
# - Get client_sevret credentials for environment variables
# - Added comments so we know what is going on

# Before running this script, got to reddit.com and create a user account if you havn't already.  Then go to: https://www.reddit.com/prefs/apps 
# and click on "create an app".  Give your app a name and select the "script" button.
# You should then see a box with:
# App Name
# personal use script
# App ID (like bo0SvJu45UCd8NPCJA)
# secret (like 2YcAEUC__i4rrXFbA)
# Put all these details into environment variables

import praw   # External module for reddit
from os import getenv
from time import time
from datetime import timedelta

recent=int(timedelta(hours=24).total_seconds())
#print(type(recent),recent)

subreddit_name='glassblowing'

# Create an instance of the reddit class with your reddit account details
reddit = praw.Reddit(user_agent=True, 
  client_id=getenv('REDDIT_APP_ID'), 
  client_secret=getenv('REDDIT_APP_SECRET'), 
  username=getenv('REDDIT_USERNAME'),
  password=getenv('REDDIT_PASSWORD'))

# Create a subreddit instance
subreddit = reddit.subreddit(subreddit_name)
subreddit.validate_on_submit=True   # Avoids a deprecation warning

now = time()

# Iterate through the recent posts in this subreddit
for post in subreddit.new():
  if now - post.created < recent:  # post created in the last recent time
    if "christmas" in post.title.lower():
      print(f'replying to post: {post.title}')
      post.reply('Merry Christmas!')  # Reply to post

      # We can also iterate through the comments to a post and reply to comments:
      for comment in post.comments:
        if "christmas is coming" in comment.body.lower():
          comment.reply("Yeah, it's coming!")
          pass
  