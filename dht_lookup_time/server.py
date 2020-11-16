import time

from flask import Flask
import ipfshttpclient


current_milli_time = lambda: int(round(time.time() * 1000))
ipfs = ipfshttpclient.connect()

app = Flask(__name__)
@app.route('/receive_hash/<ipfs_hash>')
def receive_hash(ipfs_hash):
    ipfs.cat(ipfs_hash)
    return str(current_milli_time())

app.run(host='0.0.0.0')
