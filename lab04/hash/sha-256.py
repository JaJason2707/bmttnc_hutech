import hashlib 

def calculate_sha256_hash(data):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(data.encode('utf8'))
    
    return sha256_hash.hexdigest()

data_to_hash = input("Input data")
hash_value = calculate_sha256_hash(data_to_hash)
print("Hash value", hash_value)