import threading
import requests


n = 20
bariera = threading.Barrier(5)


def f():
    bariera.wait()
    r = requests.get("http://localhost:8888/test?cifra=1")
    r = requests.get("http://localhost:8888/test?cifra=2")
    r = requests.get("http://localhost:8888/test?cifra=3")


t = []
for i in range(0, n):
    t += [threading.Thread(target=f)]
for _th in t: _th.start()
for _th in t: _th.join()