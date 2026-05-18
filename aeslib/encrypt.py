# type: ignore
from Crypto.Cipher import AES
import base64

from aeslib.env_loader import get_aes_key

KEY = get_aes_key()


def encrypt(text):
    cipher = AES.new(KEY, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(text.encode())

    return base64.b64encode(cipher.nonce + tag + ciphertext).decode()
