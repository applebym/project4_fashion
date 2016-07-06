
import praw
import pickle
import pymongo
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.reddit_database
collection_top = db.reddit_top
collection_contro = db.reddit_contro

r = praw.Reddit(user_agent="Chrome:project_fletcher:50.0.2661.102 (by /u/applebym)")

count = 0

# submissions_top = r.get_top(limit=1000)


# for post in submissions_top:
#     print count
#     count += 1
#     post.replace_more_comments(limit=20, threshold=1)
#     comment_list = []
#     for comment in sorted(post.comments, key=lambda x: x.score, reverse=True):
#         comment_list.append([comment.body, comment.score])  

#     document = {'title': post.title,
#                 'url': post.url, 
#                 'comments': comment_list}
#     collection_top.insert(document)                  


submissions_contro = r.get_controversial(limit=210)

for post in submissions_contro:
    print count
    count += 1
    post.replace_more_comments(limit=20, threshold=1)
    comment_list = []
    for comment in sorted(post.comments, key=lambda x: x.score, reverse=True):
        comment_list.append([comment.body, comment.score])  

    document = {'title': post.title,
                'url': post.url, 
                'comments': comment_list}
    collection_contro.insert(document) 

