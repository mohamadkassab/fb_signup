import threading
import requests
import queue

q = queue.Queue()
valid_proxies = []

with open("lists.txt", "r") as f:
    proxies = f.read().split("\n")
    for p in proxies:
        q.put(p)
        

def check_proxies():
    global q
    while not q.empty():
        proxy=q.get()
        try:
            res = requests.get("http://facebook.com",
                               proxies={"http":proxy,
                                        "https":proxy},
                               timeout=5
                               )
        except:
            continue
        if res.status_code == 200:
            print(proxy)
            
for _ in range(10):
    threading.Thread(target=check_proxies).start()
    