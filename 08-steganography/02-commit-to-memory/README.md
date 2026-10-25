# Steganography — Commit to Memory

**Reto:** Commit to Memory  
**Oleada:** 5  
**ID de reto:** `100`  
**Estado:** resuelto y validado.

**Flag aceptada:** `POCTF{100.1522.O3LQSCM4LKUZA77M.A55ROYEXI4RH73CCNTZLMIIIDU}`

## Artefactos

La página entrega un bundle Git y un README. SHA-256 del bundle:

```text
7fac4b1220221625919ecf391940b426747bf3f7c112a18c48380f4e66273579
```

## Resolución

El contenido de los dos archivos no contiene la flag. El bundle tiene 60
commits consecutivos. Al convertir cada timestamp Unix a la diferencia en
segundos con el commit anterior, aparecen valores ASCII:

```text
80 79 67 84 70 123 49 48 48 46 49 53 50 50 46 ... 68 85 125
```

La conversión completa produce directamente:

```text
POCTF{100.1522.O3LQSCM4LKUZA77M.A55ROYEXI4RH73CCNTZLMIIIDU}
```

La entrega respondió `Correct. Committed.`.

## Reproducción

```bash
python3 solve.py commits.bundle
```
