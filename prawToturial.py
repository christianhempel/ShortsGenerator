import praw
def RetrieveComments():
    reddit = praw.Reddit(client_id='TNfRZUVZZUMjI3704YUhRA',
                        client_secret='pTdFTeZv1DMTdi9q82sp7ToQbXdq5g', password='Tyskland8',
                        user_agent='AutoTubeBot-v1.0', username='chhhhristian')
    subreddit = reddit.subreddit('askwomen')
    conversedict = {}
    hot_python = subreddit.hot(limit=10)

    for submission in hot_python:
        if not submission.stickied:
            #print('Title: {}, ups: {}, downs: {}, Have we visited?: {}'.format(submission.title, submission.ups, submission.downs, submission.visited))
            submission.comments.replace_more(limit=0)
            conversedict[submission.id] = [submission.title,{}]
            for comment in submission.comments.list():
                #print(submission.id)
                if comment.parent() == submission.id:
                    #print( "\n", comment.parent(), comment.body, "\n")
                    #print("yes")
                    parent = str(comment.parent())
                    conversedict[submission.id][1][comment.id] = [comment.ups, comment.body]


    # Dictionary Format#
    '''
    conversedict = {post_id: [Title, comment_content, {reply_id:[votes, reply_content],
                                                reply_id:[votes, reply_content],
                                                reply_id:[votes, reply_content]}],

                    post_id: [Title, comment_content, {reply_id:[votes, reply_content],
                                                reply_id:[votes, reply_content],
                                                reply_id:[votes, reply_content]}],
                                                
                    post_id: [Title, comment_content, {reply_id:[votes, reply_content],
                                                reply_id:[votes, reply_content],
                                                reply_id:[votes, reply_content]}],
                    }


    '''
    return conversedict
    """for post_id in conversedict:
        title = conversedict[post_id][0]
        message = conversedict[post_id][1]
        replies = conversedict[post_id][2]
    print('Original Message: {}'.format(message))"""
"""
        if len(replies) > 1:
        print('Original Message: {}'.format(message))
        print(35*'_')
        print('Replies:')
        for reply in replies:
            print(replies[reply])
"""