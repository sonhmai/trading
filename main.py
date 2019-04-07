from binance.client import Client
import redis
import time

api_key = 'p57TEZpxdiAJyqBNrLqc9SgIXFTyMalaBwiJBvHTsf8HgR5Bs8j6hCsTHPaHSEZe'
secret_key = 'rHB2svc0r4OlwNmaOerGVHKhlQXYlwNbM4JhVOM0CW27Gk3DTJtLEavfrGMBnSuz'
client = Client(api_key, secret_key)

host = '10.0.0.3'
port = '6379'
r = redis.Redis(host, port)


def get_price_and_cache(symbol, client):
    depth = client.get_order_book(symbol=symbol)
    # get required data from depth
    asks_1st_lowest = depth['asks'][0][0]
    asks_2nd_lowest = depth['asks'][1][0]
    bids_1st_highest = depth['bids'][0][0]
    bids_2nd_highest = depth['bids'][1][0]

    price_dict = {
    'asks1': asks_1st_lowest,
    'asks2': asks_2nd_lowest,
    'bids1': bids_1st_highest,
    'bids2': bids_2nd_highest,
    }   

    # write depth result to cache
    res = r.hmset(symbol, price_dict)
    return res

if __name__ == '__main__':
    symbol = 'BNBBTC'
    starttime = time.time()
    while True:
        get_price_and_cache(symbol, client)
    
        depth_cached = r.hgetall(symbol)
        print(depth_cached)
        # time.sleep(60.0 - (time.time() - starttime) % 60)

