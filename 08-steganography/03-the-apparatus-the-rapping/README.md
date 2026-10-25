# Steganography — The Apparatus, The Rapping

**Reto:** The Apparatus, The Rapping  
**Oleada:** 5  
**ID de reto:** `101`  
**Estado:** resuelto y validado.

**Nonce aceptado:** `AAED9D899DD8B64E`

## Artefacto

La página entrega `recording.wav`, una grabación mono PCM de 22050 Hz.
SHA-256 del archivo:

```text
a07d2802d2316e62750b308090ae7476c5c99a7c34c3f464f0b57ec80a5d986e
```

## Resolución

La señal contiene 57 golpes separados por silencios. Medir la envolvente RMS
en ventanas de 10 ms muestra dos duraciones principales: aproximadamente 80 ms
para punto y 240 ms para raya. Los silencios de aproximadamente 80 ms separan
golpes dentro de una letra y los de aproximadamente 240 ms separan letras.

La secuencia Morse resultante es:

```text
.-  .-  .  -..  ----.  -..  ---..  ----.  ----.  -..  -..  ---..  -...  -....  ....-  .
```

Decodificada:

```text
AAED9D899DD8B64E
```

El servidor aceptó el nonce con `The signal resolves.`.

## Reproducción

```bash
python3 solve.py recording.wav
```
