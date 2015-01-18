import praw
from praw import helpers

#login to the reddit account
r = praw.Reddit("useragent")
r.login('username', 'password')

#create a set of already processed comments
already_done = set()

#scan all comments regardless of subreddit
all_comments = praw.helpers.comment_stream(r, 'all')

#text will be the comment triggering string
#the program will respond to any comment that contains the string in text
text = "string to search for"

#respond will hold the string that you would like to reply
#respond is the comment that will appear in response to a comment containing text
respond = "desired comment response"

#infinte loop
while True:
	print("The bot is running...")
	#for a particular comment in the stream of every comment
	for comment in all_comments:
		#if the comment conatins text and has not already been parsed
		if text in comment.body.lower() and comment.id not in already_done:
			#reply to the comment with respond
			comment.reply(respond)
			#upvote the comment
			comment.upvote()
			#add the comment id to the set to be sure we don't look at it again
			already_done.add(comment.id)
			print(comment)
