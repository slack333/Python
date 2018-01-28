import hashlib
from pycoin import ecdsa, encoding
import os
import codecs
import time

def create_addr():
        priv = codecs.encode(os.urandom(32), 'hex').decode()
        secret_exponent= int('0x'+rand, 0)
        public_pair = ecdsa.public_pair_for_secret_exponent(ecdsa.secp256k1.generator_secp256k1, secret_exponent)
        hash160 = encoding.public_pair_to_hash160_sec(public_pair, compressed=True)
        addr =  encoding.hash160_sec_to_bitcoin_address(hash160)
	    return addr, priv

elapsed_time = time.time()
for a in range(100):
        addr,priv = create_addr()

print ('Total time = ' + str(time.time() - elapsed_time))
