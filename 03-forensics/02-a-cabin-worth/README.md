# Forensics — A Cabin Worth

**Reto:** A Cabin Worth  
**Identificador visible:** `forensics2`  
**Oleada:** 2  
**Puntos mostrados:** 119  
**Artefacto:** `marchetti-2026-14-joplin.zip`  
**SHA-256 publicado:** `1a99234df943a03c99d04926e57cce3acb67fe9b4bdf3e566c47171f5b743402`  
**Estado:** resuelto y validado.

**Flag:** `POCTF{110.1522.DQHHFVM2GUZXIGGL.WPHVJ7AZHKTPKLZT6WV25WIPFI}`

## Análisis

La base SQLite abierta contiene las notas visibles, pero el artefacto conserva
`database.sqlite-wal`. La tabla `deleted_items` identifica como eliminada la
nota `4b7c9e1f3a5b7c9e1f3a5b7c9e1f3a5b`. En una página antigua del WAL aparece
la fila completa de esa nota, con título `Delacroix — 06/28 confirmation` y un
`encryption_cipher_text` en Base64.

Los ajustes de Joplin revelan el formato de cifrado:

- AES-256-GCM
- PBKDF2-HMAC-SHA256, 200000 iteraciones
- `salt(16) || nonce(12) || ciphertext || tag(16)` en Base64
- `note.password_hint`: `my good widdle boy!`

La nota de compras visible menciona a Horatio y comida para perro; el hint
apunta a ese nombre como contraseña, en minúsculas: `horatio`. Al descifrar la
fila recuperada aparece la transcripción y la flag de trabajo.

La página objetivo confirmó el envío con `ACK :: Correct.`.

## Reproducción

```bash
python3 solve.py marchetti-2026-14-joplin.zip
```

El script conserva el WAL como evidencia y no abre la base SQLite antes de
extraer la página histórica; abrirla primero puede hacer que SQLite
checkpointée y trunque el WAL.
