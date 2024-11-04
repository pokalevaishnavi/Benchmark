import hashlib

def sha384_hash(text):
    return hashlib.sha384(text.encode()).hexdigest()

def sha512_hash(text):
    return hashlib.sha512(text.encode()).hexdigest()

if __name__ == "__main__":
    input_text = "Hello World"
    hash_result_384 = sha384_hash(input_text)
    print(f"SHA-384 hash of '{input_text}': {hash_result_384}")
    
    hash_result_512 = sha512_hash(input_text)
    print(f"SHA-512 hash of '{input_text}': {hash_result_512}")
