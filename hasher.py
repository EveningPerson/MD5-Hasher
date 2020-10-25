import hashlib

print("MD5 Hasher")
print("By 3v3n1ng")

# Input
word = input('Enter Word to hash: ')

hash_object = hashlib.md5(word.encode())
print(hash_object.hexdigest())
