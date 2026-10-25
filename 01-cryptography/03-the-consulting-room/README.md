# Cryptography — The Consulting Room

**Reto:** The Consulting Room  
**Identificador visible:** `crypto3`  
**Oleada:** 3  
**Puntos mostrados:** 125  
**Estado:** resuelto y validado mediante padding oracle.

**Flag:** `POCTF{72.1522.DHQLGVBC7YRF47X3.KEIUBXJ562EKVWXLAOZLVNWNMZ}`

## Enunciado

SecureRecord v2.3 presenta un registro AES cifrado y un endpoint de
verificación de integridad que responde si el padding es válido. El sitio
proporciona un token Bearer específico del equipo y documenta el límite de
1.000 consultas por minuto.

No se guardan el token ni el ciphertext específico de la cuenta en el
repositorio. El solver los recibe mediante `POCTF_CONSULTING_TOKEN` y
`POCTF_CONSULTING_RECORD`.

## Comprobación inicial

La consulta del registro original devolvió:

```json
{"padding":"valid"}
```

Al modificar un byte del registro, el endpoint devolvió HTTP 400 con:

```json
{"padding":"invalid"}
```

Esto confirma el oráculo necesario para recuperar el texto plano bloque a
bloque, sin intentar obtener ni modificar datos de otros equipos.

El ataque recuperó cuatro bloques de texto plano y el padding PKCS#7 final:

```text
POCTF{72.1522.DHQLGVBC7YRF47X3.KEIUBXJ562EKVWXLAOZLVNWNMZ}\x06\x06\x06\x06\x06\x06
```

La flag se envió desde `hackadvisermx` y la plataforma respondió `Correct.`.

## Reproducción

```bash
export POCTF_CONSULTING_TOKEN='[token de la página autenticada]'
export POCTF_CONSULTING_RECORD='[ciphertext hexadecimal de la página]'
python3 solve.py
```

El script respeta el ritmo de consultas documentado. La flag se añadirá aquí
después de recuperar y validar el texto plano en la plataforma.
