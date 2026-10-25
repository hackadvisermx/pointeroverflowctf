# Miscellaneous — Conditional Existence

**Reto:** Conditional Existence
**Oleada:** 5
**ID de reto:** `87`
**Estado:** resuelto y validado.

**Flag aceptada:** `POCTF{87.1522.27e1a10ff080f79e.2U242DAMZBBVISEBOB2NOIUEFO}`

## Artefacto

El reto entrega `conditional_existence.c` dentro de un ZIP. El binario solo
imprime la flag cuando `POCTF_INCANTATION` contiene 12 caracteres hexadecimales
mayúsculos. La incantación se obtiene calculando SHA-256 sobre cuatro respuestas
concatenadas con espacios y tomando los primeros 12 caracteres hexadecimales.

## Resolución

Las cuatro pistas producen:

```text
A = 1928       (The Secret Teachings of All Ages)
B = spare       (Austin Osman Spare)
C = opava       (Franz Bardon)
D = daemon      (primer término del lema de Yeats)
```

La frase exacta es:

```text
1928 spare opava daemon
```

Su SHA-256 comienza por `08E7795B4080`, que al usarse como incantación
descifra el ciphertext y satisface el hash esperado por el programa. El
plaintext resultante es la flag anterior.

La entrega mediante `POST /api/challenges/87/submit` respondió `ok: true` y
`solved: true`.

## Reproducción

```bash
inc=$(printf %s '1928 spare opava daemon' | sha256sum | cut -c1-12 | tr '[:lower:]' '[:upper:]')
POCTF_INCANTATION="$inc" ./cx
```

El solver no contiene credenciales ni realiza la entrega automáticamente.
