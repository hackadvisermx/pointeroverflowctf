# Miscellaneous — A Peculiar Game

**Reto:** A Peculiar Game  
**Oleada:** 4  
**ID de reto:** `86`  
**Estado:** resuelto y validado.

**Nonce aceptado:** `D618BBB084981B76`

## Artefacto

La página entrega un artículo PDF específico del equipo. El SHA-256 publicado
es:

```text
3f39ceab68b8a4241fa746deff0ae271c789863b797546dc0e5708bbb10253be
```

El registro contiene 16 destinos de movimiento. No es una partida legal de
ajedrez; las casillas usadas forman una rejilla de dos filas (`3` y `4`) y
siete columnas (`a`–`g`).

## Resolución

Se lee cada destino como una posición de dos filas, recorriendo por columnas:

```text
a3=0  a4=1  b3=2  b4=3  c3=4  c4=5  d3=6  d4=7
e3=8  e4=9  f3=A  f4=B  g3=C  g4=D
```

Los destinos, en el orden del PGN, son:

```text
g4 d3 a4 e3 f4 f4 f4 a3 e3 c3 e4 e3 a4 f4 d4 d3
```

La traducción produce:

```text
D618BBB084981B76
```

La entrega del nonce respondió `The game concludes.`.

## Reproducción

```bash
python3 solve.py
```

El solver solo decodifica el registro y no contiene credenciales ni realiza
la entrega automáticamente.
