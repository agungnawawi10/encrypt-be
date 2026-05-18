# type: ignore
from Crypto.Cipher import AES
import base64

from aeslib.env_loader import get_aes_key

KEY = get_aes_key()


def decrypt(encoded_text):
    data = base64.b64decode(encoded_text)

    nonce = data[:16]
    tag = data[16:32]
    ciphertext = data[32:]

    cipher = AES.new(KEY, AES.MODE_EAX, nonce=nonce)
    decrypted = cipher.decrypt_and_verify(ciphertext, tag)

    return decrypted.decode()
