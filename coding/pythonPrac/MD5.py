import hashlib

def md5hash(text):
    md5 = hashlib.md5()
    md5.update(text.encode('utf-8'))
    return md5.hexdigest()


text = "varada"
result = md5hash(text)
print(f"MD5 hash of '{text}': {result}")