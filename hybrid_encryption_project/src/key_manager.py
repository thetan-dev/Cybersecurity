from Crypto.PublicKey import RSA
from pathlib import Path

# base folders
BASE_DIR = Path(__file__).resolve().parent.parent
KEY_DIR = BASE_DIR / "keys"

# file paths
PRIVATE_KEY_PATH = KEY_DIR / "private.pem"
PUBLIC_KEY_PATH = KEY_DIR / "public.pem"

def generate_keys(bits: int = 2048) -> None:
    """
    Generate an RSA keypair and save to keys/private.pem and keys/public.pem.
    """
    KEY_DIR.mkdir(exist_ok=True)

    key = RSA.generate(bits)
    private_key = key.export_key()
    public_key = key.publickey().export_key()

    with open(PRIVATE_KEY_PATH, "wb") as f:
        f.write(private_key)

    with open(PUBLIC_KEY_PATH, "wb") as f:
        f.write(public_key)

def load_public_key() -> RSA.RsaKey:
    with open(PUBLIC_KEY_PATH, "rb") as f:
        return RSA.import_key(f.read())

def load_private_key() -> RSA.RsaKey:
    with open(PRIVATE_KEY_PATH, "rb") as f:
        return RSA.import_key(f.read())
