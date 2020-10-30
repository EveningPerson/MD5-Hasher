import hashlib

author = """
  ______               _             _____                          
 |  ____|             (_)           |  __ \                         
 | |____   _____ _ __  _ _ __   __ _| |__) |__ _ __ ___  ___  _ __  
 |  __\ \ / / _ \ '_ \| | '_ \ / _` |  ___/ _ \ '__/ __|/ _ \| '_ \ 
 | |___\ V /  __/ | | | | | | | (_| | |  |  __/ |  \__ \ (_) | | | |
 |______\_/ \___|_| |_|_|_| |_|\__, |_|   \___|_|  |___/\___/|_| |_|
                                __/ |                               
                               |___/                                """
print(author)
print("MD5Hasher")

# Input
print("")
word = input('Enter Word to hash: ')

hash_object = hashlib.md5(word.encode())
print(hash_object.hexdigest())
print("")
input("Press enter to exit")
