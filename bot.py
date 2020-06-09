import praw
import time
import traceback

def login():
    r = praw.Reddit(user_agent='DankBloonyMonkey v0.1', client_id='k-XYexPxpJXjFA', client_secret='a2RJ6y-k4lLNpmdJOSxEVXQPRS0', username='DankBloonyMonkey', password='thedankbloonymonkey')
    return r

r = login()
sub = "bloonsmemes"

reply_template = 'Hey monkeys, is this joke good? Upvote this comment if its dank, downvote if not.'

while True:
    try:
        for submission in r.subreddit(sub).stream.submissions.new(limit=20):
            if submission not in r.user.me().saved(limit=None):
                submission.reply(reply_template)
                submission.save()
        for comment in r.user.me().comments.new(limit=20):
            if comment.score < -5:
                comment.submission.mod.remove(spam=False)
        time.sleep(30)
    except:
        traceback.print_exc()
        time.sleep(10)
