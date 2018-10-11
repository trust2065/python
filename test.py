import facebook
graph = facebook.GraphAPI(access_token='', version='2.7') 
 
# Get the messsage of a post
post = graph.get_object(id='1902194509828194_1898238116890500')
 
print(post['message']) 
# Get the created_time of the posts
 
# post_ids = ['665691423504646_1222774031129713', '665691423504646_1209392062467910']
# posts = graph.get_objects(ids=post_ids) 
 
# # Each given id maps to an object.
# for post_id in post_ids:
#  print(posts[post_id]['created_time'])