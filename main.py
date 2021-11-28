#https://www.pythoncentral.io/hashing-strings-with-python/

import hashlib

if __name__ == '__main__':
#    print("Bye") #TODO a random todo
#    print("Bye")
    print("Pycharm is awsome")
#print(hashlib.algorithms_available)
#print(hashlib.algorithms_guaranteed)

hash_object = hashlib.md5(b'Hello World')
print(hash_object.hexdigest())
print(hash_object.digest())

mystring = input('Enter String to hash: ')
# Assumes the default UTF-8
hash_object = hashlib.md5(mystring.encode())
print(hash_object.hexdigest())
