from re import sub
import praw
import string
from operator import itemgetter
def RetrieveComments():
    reddit = praw.Reddit(client_id='TNfRZUVZZUMjI3704YUhRA',
                        client_secret='pTdFTeZv1DMTdi9q82sp7ToQbXdq5g', password='Tyskland8',
                        user_agent='AutoTubeBot-v1.0', username='chhhhristian')
    subreddit = reddit.subreddit('askwomen')
    conversedict = {}
    hot_python = subreddit.hot(limit=20)
    cntr =1
    contact = False
    array = []
    myDict = dict()
    submissionidArray=[]
    for submission in hot_python:
        if cntr > 5 and not submission.stickied:

        
            #print('Title: {}, ups: {}, downs: {}, Have we visited?: {}'.format(submission.title, submission.ups, submission.downs, submission.visited))
            submission.comments.replace_more(limit=0)
            conversedict[submission.id] = [submission.title,{}]
            array.append(submission.title)
            for comment in submission.comments.list():
                
                if comment.parent() == submission.id and comment.ups>50:
                    
                    
                    result = sum([i.strip(string.punctuation).isalpha() for i in comment.body.split()])
                    if result > 10 and result < 50:
                        #print( "\n", comment.parent(), comment.body, "\n")
                        #print("yes")
                        parent = str(comment.parent())
                        array.append([comment.ups, comment.body])
                        """conversedict[submission.id][cntr][comment.id] = [comment.ups, comment.body]
                        cntr+=1"""
                        #print(type(submission.id))
                        
                        #print(result)
                        #print(comment.body)
            #Creating an empty dict
            
            if len(array)>5:
                myDict.setdefault(submission.id, []).append(array)
                submissionidArray.append(submission.id)
            
        

        array=[]
        cntr +=1

    #print("leeeeeeeeeeeeeeeeeeeeeeeee")
    
    return myDict, submissionidArray
    """x = myDict.get(submissionidArray[0])
    x=x[0][1:]
    print(len(x), len(x[0]))
    x= (sorted(x, key=itemgetter(0), reverse=True))"""
