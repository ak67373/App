import hashlib


def encrypt(hash_str):
    key = "secret-key-ajsfj"
    hash_str = hash_str + "|" + key
    h = hashlib.sha512()
    h.update(hash_str)
    return h.hexdigest()
