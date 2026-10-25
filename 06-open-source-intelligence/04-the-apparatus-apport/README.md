# Open-Source Intelligence — The Apparatus, Apport

**Reto:** The Apparatus, Apport  
**Oleada:** 4  
**ID de reto:** `93`  
**Estado:** resuelto y validado.

**Respuesta aceptada:** `BRITTEN_1870`

## Artefactos

La página entrega un ZIP específico del equipo con cinco archivos y publica el
SHA-256 `19d02fecbfe60957f6184f89de5bc633a32a2995d8f4bc7e8b357271a4cb0f52`.
Los cuatro archivos útiles son una fotografía, un fragmento de transcripción,
un correo y un GPX; `unaccounted_transmission.txt` es el elemento que no
cohesiona con la biografía.

## Resolución

Las coordenadas y fechas señalan:

- Bristol, nacimiento en `1823`.
- Nueva York, inicio del viaje estadounidense en `1856`.
- Nueva York, publicación de la historia estadounidense en `1870`.
- Manchester, residencia desde `1878`.

La correspondencia confirma que la autora se mudó de Nueva York a Manchester,
editó *Two Worlds* hasta su muerte en `1899` y que su volumen de historia
estadounidense de `1870` es la referencia del período temprano. La figura es
Emma Hardinge Britten, escritora y figura del espiritualismo.

Se envió `BRITTEN_1870` al endpoint y respondió `Identified. The archive is
closed.`.

## Reproducción

```bash
unzip -l archive.zip
pdftotext transcript.pdf -
sed -n '1,160p' correspondence.eml
sed -n '1,160p' coordinates.gpx
```
