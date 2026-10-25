# Steganography — Invisible Ink

**Reto:** Invisible Ink  
**Oleada:** 1  
**ID de reto:** `102`  
**Estado:** resuelto y validado.

**Flag aceptada:** `POCTF{WPFHZJFKNCCRYYDK}`

## Artefacto

La página entrega `invisible_text.py`, generado para el equipo. SHA-256 del
archivo descargado:

```text
f230fba9970d8898248dc698ea3025146f30693b2905a790dc4ccc92b26bb6de
```

## Resolución

El programa reconstruye 44 fragmentos Base64, los descomprime con zlib y
imprime 33 líneas de caracteres Braille. Al renderizarlas aparece una figura
humana ditherizada: es una capa visual de distracción, no la bandera.

La carga real está en el whitespace al final del código fuente. Las líneas
impares 1–45 contienen siete caracteres finales formados solo por espacios y
tabuladores. Se interpretan como ASCII de 7 bits, de izquierda a derecha:

```text
espacio = 0
tab     = 1
orden   = MSB-first
```

Por ejemplo, la primera línea termina en `1010000`, que es `0x50`, la letra
`P`. Extrayendo las 23 líneas portadoras se obtiene:

```text
POCTF{WPFHZJFKNCCRYYDK}
```

El servidor respondió `Correct.` al enviarla.

## Reproducción

```bash
python3 solve.py /ruta/a/invisible_text.py
```

El extractor conserva el whitespace, toma los últimos siete caracteres de
las líneas 1, 3, …, 45 y valida el resultado con el formato `POCTF{...}`.
