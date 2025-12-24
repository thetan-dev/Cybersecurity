from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
import struct

AES_KEY_SIZE = 32        # 32 bytes = 256 bits
NONCE_SIZE = 16          # GCM/EAX nonce size
TAG_SIZE = 16            # auth tag size

def hybrid_encrypt(plaintext: bytes, rsa_public: RSA.RsaKey) -> bytes:
    """
    Encrypt arbitrary bytes using hybrid RSA + AES (GCM-like layout).

    Layout of result:
    [2 bytes: len(enc_aes_key)] [enc_aes_key] [nonce(16)] [tag(16)] [ciphertext]
    """
    # 1) random AES key
    aes_key = get_random_bytes(AES_KEY_SIZE)

    # 2) AES encrypt (authenticated)
    cipher_aes = AES.new(aes_key, AES.MODE_EAX)
    ciphertext, tag = cipher_aes.encrypt_and_digest(plaintext)

    # 3) RSA encrypt the AES key
    cipher_rsa = PKCS1_OAEP.new(rsa_public)
    enc_aes_key = cipher_rsa.encrypt(aes_key)

    # 4) pack everything together
    header = struct.pack("H", len(enc_aes_key))
    packet = header + enc_aes_key + cipher_aes.nonce + tag + ciphertext
    return packet

def hybrid_decrypt(packet: bytes, rsa_private: RSA.RsaKey) -> bytes:
    """
    Reverse of hybrid_encrypt.
    """
    idx = 0
    (enc_key_len,) = struct.unpack("H", packet[idx:idx+2])
    idx += 2

    enc_key = packet[idx:idx+enc_key_len]
    idx += enc_key_len

    nonce = packet[idx:idx+NONCE_SIZE]
    idx += NONCE_SIZE

    tag = packet[idx:idx+TAG_SIZE]
    idx += TAG_SIZE

    ciphertext = packet[idx:]

    # 1) recover AES key with RSA
    cipher_rsa = PKCS1_OAEP.new(rsa_private)
    aes_key = cipher_rsa.decrypt(enc_key)

    # 2) decrypt data
    cipher_aes = AES.new(aes_key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher_aes.decrypt_and_verify(ciphertext, tag)
    return plaintext
