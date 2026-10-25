# Web — The Logic Inside

**Reto:** The Logic Inside  
**Oleada:** 3  
**ID de reto:** `79`  
**Estado:** resuelto y validado.

**Nonce aceptado:** `f3ae7967e6c6624c`

## Resolución

El servicio de preview bloquea literalmente `127.0.0.1` y `localhost`, pero
el cliente HTTP acepta la representación decimal de la misma dirección:

```text
http://2130706433:9001/flag?guess=
```

El campo `upstream_status` funciona como oráculo: `200` significa que el
prefijo enviado coincide y `404` que no coincide. Probando cada carácter del
alfabeto hexadecimal y conservando el prefijo correcto se recupera:

```text
f3ae7967e6c6624c
```

La plataforma aceptó el nonce y respondió `Flag accepted.`.

## Reproducción

El script recibe el valor de la cookie de sesión del sitio principal para no
guardar credenciales en el repositorio:

```bash
python3 solve.py "$POCTF_SESSION"
```
