# Miscellaneous — Columns of Holes

**Reto:** Columns of Holes  
**Oleada:** 3  
**ID de reto:** `85`  
**Estado:** resuelto y validado.

**Nonce aceptado:** `101F31EB65350D9A`

## Artefacto

La página entrega un memo PDF específico del equipo y dos punchcards en su
segunda página. El SHA-256 publicado del PDF es:

```text
244cbbf1f3961eb8320c86432285b590489f29d6c2a1a0e88a6c7b6dd728d42e
```

El memo indica que cada tarjeta contiene una parte de ocho caracteres del
nonce. La tarjeta usa el formato Hollerith/IBM: los agujeros combinan las
filas 12, 11 y 0–9 para representar letras, dígitos y signos.

## Decodificación

Las dos tarjetas se identifican como `A` y `B`. Después del encabezado, el
marcador `PAT#` contiene dos dígitos: inicio y stride. El payload comienza
después de los dos espacios de separación:

```text
Tarjeta A: PAT#33 · payload = S461WK0DA1FSFQ73321XZEZTB0ONETVD6UWS
Tarjeta B: PAT#02 · payload = 6R5E3M5T0QDI98ANPPDVQTR74P59FZBB76B1
```

Tomando ocho caracteres desde el índice de inicio y avanzando con el stride,
se obtienen:

```text
A: 101F31EB
B: 65350D9A
```

El memo pide combinar en orden alfabético de sufijo, por lo que el nonce final
es `101F31EB65350D9A`. La entrega del nonce respondió `Correct.`.

## Reproducción

Extrae las dos imágenes de tarjetas de la página 2 del PDF y ejecuta:

```bash
python3 solve.py /ruta/a/card-a.png /ruta/a/card-b.png
```

El solver imprime el nonce y no contiene credenciales ni realiza la entrega
automáticamente.
