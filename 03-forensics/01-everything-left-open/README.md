# Forensics — Everything Left Open

**Reto:** Everything Left Open  
**Identificador visible:** `forensics1`  
**Oleada:** 1  
**Puntos mostrados:** 67  
**Artefacto:** `left-open-profile.zip`  
**SHA-256 publicado:** `22ed2e106538b3af1c83bcfdb8b5b2a76f828a021af5df048cd0fc70b64b6a6d`  
**Estado:** resuelto y validado.

**Flag:** `POCTF{109.1522.AHW6RBPH2NJVDNSO.V7QANSZ6LX5MKYXDXQ346RFARF}`

## Análisis

El ZIP es un perfil de Firefox recuperado de un equipo que quedó desbloqueado.
Además de `places.sqlite`, `logins.json` y `formhistory.sqlite`, contiene
`sessionstore-backups/recovery.jsonlz4`.

El archivo de recuperación conserva el formulario abierto en una página
interna. Al buscar el patrón `POCTF{...}` en ese artefacto aparece el campo
`artifact-flag`, que contiene la flag específica del equipo. No fue necesario
descifrar las credenciales de `logins.json` ni visitar los sitios incluidos.

La flag se envió en la página objetivo y respondió `Correct.`.

## Reproducción

```bash
python3 solve.py left-open-profile.zip
```

El ZIP generado por la plataforma es específico de la sesión y no se guarda
en el repositorio.
