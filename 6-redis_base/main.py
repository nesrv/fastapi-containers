import redis
 

r = redis.Redis(host='localhost', port=6380, db=0, username='my_user', password='my_user_password')
r.set('test_py_key', 'test py value')
 
redis_get = r.get('test_py_key')
print(redis_get)

# работает