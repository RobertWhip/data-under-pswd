import sys
import base64
import hashlib
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes

def derive_key(password, salt):
    key = PBKDF2(password, salt, dkLen=32)
    return key

def encrypt(seed_phrase, password):
    salt = get_random_bytes(16)
    key = derive_key(password, salt)
    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(seed_phrase.encode(), AES.block_size))
    return salt + iv + ciphertext

def decrypt(ciphertext, password):
    salt = ciphertext[:16]
    iv = ciphertext[16:32]
    ciphertext = ciphertext[32:]
    key = derive_key(password, salt)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return plaintext.decode()

def hash_password(password):
    return hashlib.sha256(password.encode()).digest()

def pad(data, block_size):
    padding_length = block_size - len(data) % block_size
    padding = bytes([padding_length]) * padding_length
    return data + padding

def unpad(data, block_size):
    padding_length = data[-1]
    if padding_length < 1 or padding_length > block_size:
        raise ValueError("Invalid padding length")
    if data[-padding_length:] != bytes([padding_length]) * padding_length:
        raise ValueError("Invalid padding bytes")
    return data[:-padding_length]

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python3 script.py <encrypt|decrypt> <password> <seed_phrase>")
        sys.exit(1)

    mode = sys.argv[1].lower()
    password = sys.argv[2]
    hashed_password = hash_password(password)

    if mode == "encrypt":
        seed_phrase = " ".join(sys.argv[3:])
        ciphertext = encrypt(seed_phrase, password)
        print("Ciphertext:", base64.b64encode(ciphertext).decode())

    elif mode == "decrypt":
        try:
            ciphertext = base64.b64decode(sys.argv[3])
        except base64.Error:
            print("Error: Incorrect base64 padding.")
            sys.exit(1)
        
        decrypted_seed_phrase = decrypt(ciphertext, password)
        print("Decrypted Seed Phrase:", decrypted_seed_phrase)

    else:
        print("Invalid mode. Please use 'encrypt' or 'decrypt'.")
        sys.exit(1)

