import secrets

import ipfshttpclient

current_milli_time = lambda: int(round(time.time() * 1000))
ipfs = ipfshttpclient.connect()

hash = ipfs.add_bytes(secrets.token_bytes(8))
start_time = current_milli_time()
print(hash)
