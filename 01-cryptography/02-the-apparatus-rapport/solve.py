#!/usr/bin/env python3
"""Resuelve The Apparatus, Rapport mediante el orden del tablero."""

PRIMARY = "RVHUN}<32=4935XLL_TMOMUUaH<XR6DWFU^[JNBNZ9_BOM`G[UGJ<OPC%"
SECONDARY = "D!%tin{%bvf'gz(czm-(d!%upg'gsmc{m!lth|o(d|y!vq{%smv|womf3%xm\"vufv\"{mf(yh~/"
KEY = "CHFBI"


def decrypt_printable_ascii(ciphertext: str, key: str) -> str:
    """Descifra con desplazamientos A=0..I=8 sobre ASCII 32..126."""
    result = []

    for index, char in enumerate(ciphertext):
        shift = ord(key[index % len(key)]) - ord("A")
        value = (ord(char) - 32 - shift) % 95 + 32
        result.append(chr(value))

    return "".join(result)


if __name__ == "__main__":
    print("Secondary:", decrypt_printable_ascii(SECONDARY, KEY))
    print("Primary:", decrypt_printable_ascii(PRIMARY, KEY))
