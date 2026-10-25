# Web — The Apparatus, Levitation

**Reto:** The Apparatus, Levitation
**Oleada:** 5
**ID de reto:** `80`
**Estado:** resuelto y validado.

**Flag aceptada:** `POCTF{80.1522.RGGZ3FDN3FEU2H4I.5CFJ37UZRGKFQJYUXOYJSICZEZ}`

## Resolución

El portal remoto abre una sesión `MEDIUM` con el token específico del equipo.
El endpoint de transcripciones solo expone el registro de asistencia para ese
rol. El portal publica una clave RSA y valida los JWT con `RS256`, pero acepta
el mismo `kid` con `HS256`; al usar el PEM público como secreto HMAC se puede
forjar un token con `role: spirit`.

El token forjado permite consultar `/api/transcript`, que devuelve el marcador
específico del equipo:

```text
POCTF{80.1522.RGGZ3FDN3FEU2H4I.5CFJ37UZRGKFQJYUXOYJSICZEZ}
```

La entrega al endpoint oficial respondió `Correct.`.

## Reproducción

1. Abrir una sesión `MEDIUM` con el token de la página autenticada.
2. Descargar la clave pública PEM del portal.
3. Decodificar el JWT legítimo y conservar `team_id` y `nonce`.
4. Cambiar el algoritmo a `HS256`, establecer `role` en `spirit` y firmar con
   el texto PEM de la clave pública.
5. Consultar `/api/transcript` con el JWT forjado y enviar el marcador devuelto.

No se guardan en este repositorio el token temporal, la cookie ni el JWT
forjado.
