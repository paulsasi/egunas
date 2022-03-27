import requests
import time


def get_article_from_server(url: str):
    print("Fetching article from server...")
    response = requests.get(url)
    return response.text

def get_article(url):
    print("Getting article")
    if url not in cache:
        cache[url] = get_article_from_server(url)

    return cache[url]


cache = dict()


start_time = time.time()
get_article("https://realpython.com/sorting-algorithms-python/")
t1 = time.time() - start_time
print('Time request 1: {}'.format(t1))


start_time = time.time()
get_article("https://realpython.com/sorting-algorithms-python/")
t2 = time.time() - start_time
print('Time request 2: {}'.format(t2))
