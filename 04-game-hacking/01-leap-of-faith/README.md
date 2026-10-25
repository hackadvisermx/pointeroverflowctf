# Game Hacking — Leap of Faith

**Reto:** Leap of Faith  
**Identificador visible:** `GH 200`  
**Oleada:** 2  
**ID de API:** `47`  
**Estado:** resuelto y validado.

**Flag:** `POCTF{47.1522.5f090656e3d0be9dde88567bd80f5175.U7ZVKZXBPVN4K4A637LIBIUAFW}`

## Análisis

La página entrega un binario Godot para Linux y un ZIP de credenciales de
equipo con `game.token` y `team.key`. La página advierte que se publicó una
versión de prueba del juego; el objetivo original requería modificar la
altura del salto para alcanzar la última plataforma.

La lógica relevante del cliente se puede reproducir sin guardar las
credenciales:

1. `GET /api/challenges/47/instance` con los headers
   `X-POCTF-GAME-TOKEN` y `X-POCTF-TEAM-KEY` devuelve un nonce de equipo.
2. `POST /api/challenges/47/complete` con esos headers y
   `X-POCTF-CHALLENGE-NONCE` devuelve el marcador.

Es importante usar un cliente autónomo sin reenviar la cookie de sesión del
navegador: el servidor aplica una rama CSRF distinta cuando se combina esa
cookie con el endpoint del juego. El `solve.py` reproduce exactamente el
flujo que usa el binario y solo imprime la respuesta recibida.

El binario Linux descargado coincidió con el SHA-256 publicado:
`d82dd861ae8dd30ef5fd8219cbba7e2cc2e998425a39d632433b252200d0a07b`.

La flag se envió al formulario oficial y respondió `Landed. Nicely done.`.

## Reproducción

Extrae el bundle de credenciales junto al solver y ejecútalo:

```bash
python3 solve.py --credentials-dir /ruta/al/directorio
```

El directorio debe contener los archivos entregados por la página, `game.token`
y `team.key`. No se incluyen en el repositorio.
