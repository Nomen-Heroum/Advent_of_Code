import src
import hashlib
import itertools

string = 'bgvyzdsv'


def find_hash(key=string, n=5):
    for i in itertools.count():
        hash_input = key + str(i)
        hexa = hashlib.md5(hash_input.encode('utf-8')).hexdigest()
        if hexa[:n] == n * '0':
            print(f"Found number {i} with hash {hexa}.")
            return i


src.clip(find_hash())
src.clip(find_hash(n=6))
