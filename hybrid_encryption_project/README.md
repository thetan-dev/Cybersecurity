# Hybrid Encryption Project (RSA + AES)

A simple hybrid encryption system that combines **RSA** asymmetric encryption with **AES‑256** symmetric encryption to secure files and text messages. The project automatically manages RSA key pairs and uses them to protect randomly generated AES session keys, which then encrypt the actual data.[web:20][web:29]

---

## Features

- RSA‑2048 key generation and storage in `keys/`.[web:20][web:144]  
- AES‑256 (EAX mode) encryption for:
  - Files (`.txt`, `.pdf`, images, etc.).
  - Plain text entered in the terminal.[web:20][web:104]
- Hybrid scheme:
  - AES key is randomly generated per encryption.
  - AES key is encrypted with RSA‑OAEP (public key).
  - Data is encrypted with AES, then decrypted using the recovered AES key and RSA private key.[web:20][web:110]
- Simple menu‑driven CLI in `main.py`.

---

## Project Structure
```text
hybrid_encryption_project/   
├─ keys/                        # Generated RSA keys (private.pem, public.pem)
├─ data/                        # Input/output files for demo
├─ src/                         
│  ├─ key_manager.py            # RSA key generation, load/save 
│  ├─ crypto_core.py            # Hybrid AES+RSA encrypt/decrypt 
│  └─ file_encryptor.py         # File helpers using the hybrid core 
├─ main.py                      # CLI: file & text encryption/decryption 
├─ README.md                    # Documentation 
└─ requirements.txt             # Dependencies 

```
---

## Setup

1. Install dependencies:
    pip install -r requirements.txt


2. Make sure you are in the project folder:
    cd path/to/hybrid_encryption_project


3. Run the main script once; it will generate RSA keys automatically in `keys/`:
    python main.py


Key generation and usage follow the standard hybrid example from the PyCryptodome documentation (RSA‑OAEP + AES‑EAX).[web:20][web:29]

---

## Usage

### 1. File encryption and decryption

1. Place any file in the `data/` folder, for example `data/secret.txt`.
2. Run:
    python main.py

3. Menu options:

- **Option 1 – Encrypt a file**
  - Enter the path, e.g. `data/secret.txt`.
  - Output: `data/secret.txt.enc` (binary ciphertext).

- **Option 2 – Decrypt a file**
  - Enter the path, e.g. `data/secret.txt.enc`.
  - Output: `data/secret.dec.txt` (decrypted copy of the original file).

Internally, the program generates a random AES‑256 key, encrypts the file with AES, then encrypts that AES key using the RSA public key.[web:20][web:32]

---

### 2. Text encryption and decryption (terminal)

From the same `main.py` menu:

- **Option 3 – Encrypt text**
- Type a message in the terminal.
- The program:
 - Loads the RSA public key.
 - Encrypts your text using AES‑256 with a random key.
 - Encrypts the AES key with RSA.
 - Prints a base64‑encoded ciphertext string you can copy.

- **Option 4 – Decrypt text**
- Paste the base64 ciphertext from Option 3.
- The program:
 - Uses the RSA private key to recover the AES key.
 - Decrypts the text and prints the original message.

This demonstrates hybrid encryption for both files and interactive text messages.[web:20][web:110]

---

## How It Works (High Level)

1. **Key generation**
- RSA‑2048 keypair is generated and saved as `keys/private.pem` and `keys/public.pem`.[web:20][web:144]

2. **Encryption**
- Generate random 32‑byte AES key.
- Encrypt data with AES‑EAX (provides confidentiality and integrity).
- Encrypt AES key with RSA‑OAEP using the public key.
- Package: length of encrypted AES key + encrypted AES key + nonce + tag + ciphertext.[web:20][web:104]

3. **Decryption**
- Read the package and extract encrypted AES key, nonce, tag, and ciphertext.
- Use RSA private key to decrypt the AES key.
- Use AES key, nonce, and tag to decrypt and verify the data.[web:20][web:110]

This design matches common AES‑RSA hybrid cryptosystem patterns used in academic and practical implementations.[web:32][web:111]

