import redis

host = '10.0.0.3'
port = '6379'

r = redis.Redis(host, port)

symbol = 'BNBBTC'

result = r.hgetall(symbol)
print(result)
