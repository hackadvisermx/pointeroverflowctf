# Miscellaneous — Frequency and Consequence

**Reto:** Frequency and Consequence  
**Identificador visible:** `MISC/WAVE-02`  
**Oleada:** 2  
**ID de reto:** `91`  
**Estado:** resuelto y validado.

**Nonce/flag aceptada:** `M6N2OZJ2AGH26YWQ`

## Análisis

El archivo `signal.wav` es PCM mono a 44.1 kHz. Cada símbolo ocupa un slot
de 500 ms y su frecuencia es `500 + 50 * índice`, con el alfabeto base32
`A-Z2-7`.

Se calcula la FFT de cada slot y se compara la energía en las 32 frecuencias
permitidas. El primer y último slot contienen ruido de sincronización; la
secuencia útil de 16 slots decodifica como:

```text
M6N2OZJ2AGH26YWQ
```

La página especifica que acepta el nonce o el marcador completo. La entrega
del nonce respondió `Correct. 73.`.

El WAV descargado tuvo SHA-256
`4d3bd957f9d9103b30315680a4573fca2ca4eb3f1eb9e29dd7b1613ac5f327dd`.

## Reproducción

```bash
python3 solve.py /ruta/a/signal.wav
```

El solver imprime el nonce y no contiene credenciales ni realiza la entrega
automáticamente.
