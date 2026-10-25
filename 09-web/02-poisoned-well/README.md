# Web — Poisoned Well

**Reto:** Poisoned Well  
**Oleada:** 2  
**ID de reto:** `82`  
**Estado:** resuelto y validado.

**Flag aceptada:** `POCTF{82.1522.FU3EDJSHVLOZ6CJO.AG7A2IJCFZNBGDOHVIL7FOUZZW}`

## Resolución

La página del reto entrega un token `POISON1...`. Se envía al formulario
`POST /login` del subdominio y se conserva la cookie de lector. Desde esa
sesión, la portada responde con los encabezados `X-Cache` y `Vary: Cookie`;
la verificación del estado del caché se hace en `/verify`.

La respuesta de `/verify` devolvió el nonce y la flag del equipo:

```json
{
  "nonce": "FU3EDJSHVLOZ6CJO",
  "flag": "POCTF{82.1522.FU3EDJSHVLOZ6CJO.AG7A2IJCFZNBGDOHVIL7FOUZZW}"
}
```

El servidor de entrega respondió `Correct.`. Si se contamina la caché con
una prueba incorrecta, `/reset` permite volver a dejarla vacía.

## Reproducción

```bash
python3 solve.py 'POISON1...'
```
