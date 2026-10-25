# Game Hacking — Health Is a Social Construct

**Reto:** Health Is a Social Construct  
**Identificador visible:** `GH 200`  
**Oleada:** 4  
**ID de API:** `48`  
**Estado:** resuelto y validado.

**Flag:** `POCTF{48.1522.452bd25ee4a2282cc14d4da936256c32.FP2MOSQ7D6SOWSZLTR7N47VBHT}`

## Análisis

El reto entrega un shooter Godot con tres habitaciones y un boss final cuyo
HP y daño hacen inviable derrotarlo por métodos normales. El cliente incluye
el mismo esquema de autenticación que el reto anterior:

1. `GET /api/challenges/48/instance` con `game.token` y `team.key` devuelve
   un nonce.
2. `POST /api/challenges/48/complete` con el nonce devuelve el marcador.

El endpoint de completado no comprueba que el boss haya muerto, que se haya
visitado la habitación final ni que se haya alterado la salud o el daño. Por
eso basta reproducir el flujo autenticado del cliente; no se necesita
reenviar la cookie del navegador ni disparar el juego. La flag se envió al
formulario oficial y respondió `Landed. Nicely done.`.

El binario Linux descargado coincidió con el SHA-256 publicado:
`8d6c82050f18460903eb99ea9055e2663b9f4b0343b58494ac0a816a3adc50f7`.

## Reproducción

Extrae las credenciales junto al solver y ejecútalo:

```bash
python3 solve.py --credentials-dir /ruta/al/directorio
```

El directorio debe contener `game.token` y `team.key`. No se incluyen
credenciales ni cookies en el repositorio.
