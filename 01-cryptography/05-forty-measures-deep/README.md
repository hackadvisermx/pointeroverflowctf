# Cryptography — Forty Measures Deep

**Reto:** Forty Measures Deep
**Oleada:** 5
**ID de reto:** `74`
**Estado:** resuelto y validado.

**Flag aceptada:** `POCTF{74.1522.GZ44OWHG7JTPD6GN.RB7Q2GJBYEDZ3SNUPTKI5FFNGE}`

## Artefacto

El reto entrega `score.mid`. Su SHA-256 es:

```text
abfecc2d859e2fc2a830960a1aa8e9518f6fe169660d8a702fffff2028dbcf48
```
La página indica que la partitura usa un alfabeto musical privado y proporciona
`POCTF` como texto conocido.

## Resolución

Se extraen las 60 alturas de nota del MIDI y se interpretan como bytes de un
cifrado por sustitución. Los primeros valores producen `KJ>OA;`; el texto
conocido `POCTF{` permite inferir la transformación: los caracteres imprimibles
alfanuméricos se desplazan cinco posiciones en ASCII, los dígitos se mantienen
y los separadores especiales se transforman como `:` → `.`, `;` → `{` y
`V` → `}`. Al aplicar esa sustitución a toda la secuencia se obtiene la flag
anterior.

La entrega mediante `POST /api/challenges/74/submit` respondió:

```json
{"ok":true,"solved":true,"first_blood":false}
```
