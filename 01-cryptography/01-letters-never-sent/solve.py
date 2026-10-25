#!/usr/bin/env python3
"""Descifra Letters Never Sent con Beaufort y la clave MEDIUM."""

CIPHERTEXT = "XQBPP{2.1522.A267IGZCDQZK4673.UO6YFMSMCKJQI3EFOJQPY2FAJY}"
KEY = "MEDIUM"


def beaufort_decrypt(ciphertext: str, key: str) -> str:
    """Aplica P = K - C (mod 26), avanzando la clave solo sobre letras."""
    plaintext = []
    key_index = 0

    for char in ciphertext:
        if not char.isalpha():
            plaintext.append(char)
            continue

        cipher_value = ord(char.upper()) - ord("A")
        key_value = ord(key[key_index % len(key)].upper()) - ord("A")
        plain_value = (key_value - cipher_value) % 26
        plaintext.append(chr(ord("A") + plain_value))
        key_index += 1

    return "".join(plaintext)


if __name__ == "__main__":
    print(beaufort_decrypt(CIPHERTEXT, KEY))
