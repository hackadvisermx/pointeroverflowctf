# Steganography — Velocity

**Reto:** Velocity  
**Oleada:** 5  
**ID de reto:** `103`  
**Estado:** resuelto y validado.

**Nonce aceptado:** `C268716976238AAD`

## Artefacto

La página entrega `etude.mid`, un MIDI de formato 0 con una sola pista y 64
notas. SHA-256 del archivo descargado:

```text
1d1b5f991dacd5bb8d73ace4e9f7e8af805c25e951e5be3bb217db33faa14a07
```

## Resolución

El enunciado indica que cada nota aporta un bit y que cada grupo de cuatro
bits forma un dígito hexadecimal. Las notas tienen dos niveles de velocidad:
`0x30` y `0x60`. Se toma `0` para la velocidad baja y `1` para la alta.

La secuencia obtenida es:

```text
1100001001101000011100010110100101110110001000111000101010101101
```

Agrupando de izquierda a derecha en nibbles:

```text
C268716976238AAD
```

El valor se envió al endpoint del reto, que respondió `The signal resolves.`.

## Reproducción

```bash
python3 solve.py etude.mid
```
