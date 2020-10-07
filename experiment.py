import secrets
import time
import sys

import requests
import ipfshttpclient
import matplotlib.pyplot as plt
import numpy as np

current_milli_time = lambda: int(round(time.time() * 1000))
ipfs = ipfshttpclient.connect()

def run_test():
    hash = ipfs.add_bytes(secrets.token_bytes(32))
    start_time = current_milli_time()
    end_time = int(requests.get(sys.argv[1] + '/receive_hash/' + hash).content)
    return end_time-start_time

x = []
for i in range(100):
    t = run_test()
    print(t)
    x.append(t)

plt.hist(x)
plt.ylabel('Probability')
plt.xlabel('Latency (ms)');
plt.savefig('graph.pdf')
