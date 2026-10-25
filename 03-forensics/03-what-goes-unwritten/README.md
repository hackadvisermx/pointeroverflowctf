# Forensics — What Goes Unwritten

**Reto:** What Goes Unwritten  
**Identificador visible:** `forensics3`  
**Oleada:** 3  
**Puntos mostrados:** 120  
**Artefacto:** `marchetti-2026-14-libws.zip`  
**SHA-256 publicado:** `3fcd9742dc2ba165509fce9ffbfb61033a4b4e9baf0915bcf1a6f4f843ec31aa`  
**Estado:** resuelto y validado.

**Token:** `W5I7RBFIB24R3I26`

## Análisis

El ZIP contiene un minidump de Windows de la sesión de Firefox. Las cadenas
UTF-16 conservan dos fragmentos relevantes en objetos distintos:

- `sessionRestoreToken:W5I7RBFI`
- `B24R3I26|expires:1751659200`

El valor solicitado es la concatenación de los dos fragmentos alfanuméricos,
`W5I7RBFIB24R3I26`, con 16 caracteres del alfabeto base32. No se usó la
mayoría de las cadenas de señuelo del dump.

El objetivo aceptó el token directamente y respondió `ACK :: Correct.`.

## Reproducción

```bash
python3 solve.py marchetti-2026-14-libws.zip
```

El ZIP es específico de la sesión/equipo y no se conserva en el repositorio.
