import praw
import prawcore
from time import sleep
import traceback

def login():
    r = praw.Reddit(user_agent='DankBloonyMonkey v0.1', client_id='k-XYexPxpJXjFA', client_secret='a2RJ6y-k4lLNpmdJOSxEVXQPRS0', username='DankBloonyMonkey', password='thedankbloonymonkey')
    return r

r = login()
sub = "bloonsmemes"
downvote_threshold = -5
upvote_threshold = 5

reply_template = 'Hey monkeys, is this joke good? Upvote this comment if its dank, downvote if not.'

while True:
    try:
        for submission in r.subreddit(sub).new():
            if submission not in r.user.me().saved(limit=20):
                submission.reply(reply_template)
                print("Posted initial comment")
                submission.save()
                print("Submission saved")
            
        for comment in r.user.me().comments.new(limit=None):
            if comment.score <= downvote_threshold:
                comment.delete()
                print("Comment removed; post isn't dank")
            elif comment.score >= upvote_threshold:
                c = r.user.get_comments().next()
                c.edit("Dank")
        
        print("Will resume after 30 seconds.")
        sleep(30)
        
    except:
        traceback.print_exc()
        print("Will resume after 10 seconds.")
        sleep(10)

