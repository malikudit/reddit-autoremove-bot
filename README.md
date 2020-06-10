# Reddit Autoremove Bot
This is a simple Python script based on the PRAW API that automatically comments on every new post in a subreddit and asks users to rate the original submission. If the bot comment score reaches a positive threshold, the comment is edited to an approval message; if the bot comment score reaches the negative threshold, the comment can either be deleted for the mods to review the submission, or the original submission can be deleted too (with a few changes in the code.)

# Using the bot
First, you need to create your own Reddit app from the account which you will be using as the bot. You can do so [here](https://ssl.reddit.com/prefs/apps/) and then obtain your personal client_id and client_secret. You can now install the dependencies by going to the terminal, navigating to the directory of the bot, and typing:
```
pip install -r requirements.txt
```

Now, make appropriate changes to the following fields in bot.py:
```
r = praw.Reddit(user_agent='BOT_NAME', client_id='CLIENT_ID', client_secret='CLIENT_SECRET', username='REDDIT_USERNAME', password='REDDIT_PASSWORD')
```

Change the following variables to the name of the subreddit, the negative and positive thresholds you need, and the content of the comment made by the bot:
``` 
sub = "INSERT_SUBREDDIT_NAME"
downvote_threshold = "NEGATIVE_SCORE"
upvote_threshold = "POSITIVE_SCORE"
reply_template = "THIS_IS_A_COMMENT"
```

To change the content of the comment if it hits the positive threshold, edit:
```
c = r.user.get_comments().next()
c = edit("INSERT_NEW_COMMENT_CONTENT_HERE")
```
