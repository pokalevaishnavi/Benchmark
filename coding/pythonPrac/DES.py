#pip install pycryptodome

from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import binascii

def des_encrypt(plaintext, key):
    cipher = DES.new(key, DES.MODE_CBC)
    padded_plaintext = pad(plaintext.encode('utf-8'), DES.block_size)
    ciphertext = cipher.encrypt(padded_plaintext)

    return binascii.hexlify(cipher.iv + ciphertext).decode('utf-8')

def des_decrypt(ciphertext_hex, key):
    ciphertext = binascii.unhexlify(ciphertext_hex)
    iv = ciphertext[:DES.block_size]
    ciphertext = ciphertext[DES.block_size:]
    cipher = DES.new(key, DES.MODE_CBC, iv)
    padded_plaintext = cipher.decrypt(ciphertext)
    plaintext = unpad(padded_plaintext, DES.block_size).decode('utf-8')
    return plaintext

key = b'abcdefgh'  # Key must be 8 bytes long
plaintext = "varada"
ciphertext = des_encrypt(plaintext, key)
print(f"Encrypted: {ciphertext}")

decrypted_text = des_decrypt(ciphertext, key)
print(f"Decrypted: {decrypted_text}")
