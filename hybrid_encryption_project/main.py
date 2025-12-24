import base64
from pathlib import Path
from src.key_manager import generate_keys, PUBLIC_KEY_PATH, PRIVATE_KEY_PATH, load_public_key, load_private_key
from src.file_encryptor import encrypt_file, decrypt_file
from src.crypto_core import hybrid_encrypt, hybrid_decrypt

def ensure_keys():
    # generate keys if they don't exist
    if not (PUBLIC_KEY_PATH.exists() and PRIVATE_KEY_PATH.exists()):
        print("RSA keys not found, generating...")
        generate_keys()
        print(f"Keys saved at: {PUBLIC_KEY_PATH} and {PRIVATE_KEY_PATH}")

def main():
    ensure_keys()

    while True:
        print("\n=== Hybrid Encryption Project ===")
        print("1) Encrypt a file")
        print("2) Decrypt a file")
        print("3) Encrypt text")
        print("4) Decrypt text")
        print("5) Exit")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            path = input("Enter path of file to encrypt: ").strip()
            try:
                out = encrypt_file(path)
                print(f"Encrypted file saved as: {out}")
            except Exception as e:
                print(f"Error encrypting: {e}")

        elif choice == "2":
            path = input("Enter path of .enc file to decrypt: ").strip()
            try:
                out = decrypt_file(path)
                print(f"Decrypted file saved as: {out}")
            except Exception as e:
                print(f"Error decrypting: {e}")

        elif choice == "3":
            # Encrypt text
            public_key = load_public_key()
            plain = input("Enter text to encrypt: ")
            packet = hybrid_encrypt(plain.encode("utf-8"), public_key)
            b64 = base64.b64encode(packet).decode("ascii")
            print("\nCiphertext (base64). Copy this text:")
            print(b64)

        elif choice == "4":
            # Decrypt text
            private_key = load_private_key()
            b64 = input("Paste base64 ciphertext: ").strip()
            try:
                packet = base64.b64decode(b64)
                plain = hybrid_decrypt(packet, private_key).decode("utf-8")
                print("\nDecrypted text:", plain)
            except Exception as e:
                print(f"Error decrypting text: {e}")

        elif choice == "5":
            print("Exiting.")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
