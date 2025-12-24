from pathlib import Path
from .key_manager import load_public_key, load_private_key
from .crypto_core import hybrid_encrypt, hybrid_decrypt

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)


def encrypt_file(input_path: str, output_path: str | None = None) -> str:
    inp = Path(input_path)

    if output_path is None:
        output_path = str(inp.with_suffix(inp.suffix + ".enc"))

    with open(inp, "rb") as f:
        plaintext = f.read()

    public_key = load_public_key()
    packet = hybrid_encrypt(plaintext, public_key)

    with open(output_path, "wb") as f:
        f.write(packet)

    return output_path


def decrypt_file(input_path: str, output_path: str | None = None) -> str:
    inp = Path(input_path)

    if output_path is None:
        if inp.suffix == ".enc":
            output_path = str(inp.with_suffix(".dec.txt"))
        else:
            output_path = str(inp) + ".dec"

    with open(inp, "rb") as f:
        packet = f.read()

    private_key = load_private_key()
    plaintext = hybrid_decrypt(packet, private_key)

    with open(output_path, "wb") as f:
        f.write(plaintext)

    return output_path
