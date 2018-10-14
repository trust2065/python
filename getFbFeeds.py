import facebook
# you may need to refresh the token, since it will expired every 2 hours
# https://developers.facebook.com/tools/explorer/
graph = facebook.GraphAPI(access_token='EAAemR6Q27nsBAJ6cyZADCXvuJxpZBt4zHUwcn5zIh7jhzj07m40ZC8h3rbqQlHlBzlpAxS2WVCg9qsTo2Wsj6xKymTW7ZBZBn971hxNTBhj77FEcBfqsGrpkfnJtlSfZBb1r3MQJZB88b1nvUkEX1JX99Qp0B57FZC1DnftgYcfoJIZC5Bo7fJ1YWnh18ZAcBhwLoZD', version='2.7') 
 
# Get the messsage of a post
me = graph.get_object(id='me')
feedList = graph.get_connections(id='me', connection_name='feed')

# print(feedList)

for feed in feedList['data']:
    print(feed['id'])
    print('')
    print(feed['message'])

# like your post(doesn't work)
# postInfo = feedList['data'][0]
# print(postInfo)
# postId = postInfo['id']
# print(postId)

# graph.put_like(postId)


# Get the created_time of the posts
# post_ids = ['665691423504646_1222774031129713', '665691423504646_1209392062467910']
# posts = graph.get_objects(ids=post_ids) 
 
# # Each given id maps to an object.
# for post_id in post_ids:
#  print(posts[post_id]['created_time'])
