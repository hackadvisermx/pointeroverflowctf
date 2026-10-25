# Forensics — Archaeology of Mistakes

**Reto:** Archaeology of Mistakes
**Oleada:** 5
**ID de reto:** `112`
**Estado:** resuelto y validado.

**Token aceptado:** `Z52ZZAOOGSNSKWQ2`

## Artefacto

El reto entrega `marchetti-2026-14-disk.zip`, que contiene una imagen RAW de
40 MiB. SHA-256 del ZIP:

```text
35864b08d37a19858ee0624b0d0dcbfe1681a3ad330e7e6ba02ee9e0a2b27681
```

## Resolución

Se buscan firmas JPEG `FF D8 FF` y finales `FF D9` en la imagen, y se recortan
los nueve JPEGs encontrados. La fotografía relevante es la tomada el 5 de
junio (`DateTimeOriginal = 2026:06:05 19:14:03`), con dimensiones 900×1200;
es también la que presenta el bloque DCT sobrescrito y no renderiza
correctamente.

Su EXIF conserva:

```text
ImageDescription: IMG WJ6OSF6T4WQNYTX4 .
UserComment: Private library annex — east wing shelving. ref=Z52ZZAOOGSNSKWQ2 .
```

El valor después de `ref=` es el token de 16 caracteres Base32. El target
`/challenges/archaeology-of-mistakes/submit` respondió `Correct.` al entregar
`Z52ZZAOOGSNSKWQ2` sin envolverlo. La API autenticada confirmó después
`team_solved: true` para el reto.

## Reproducción

```bash
unzip marchetti-2026-14-disk.zip
grep -abo $'\\xff\\xd8\\xff' marchetti-2026-14/disk.raw
exiftool carve-06.jpg
```

