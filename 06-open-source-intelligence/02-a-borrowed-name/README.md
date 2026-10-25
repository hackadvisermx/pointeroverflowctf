# Open-Source Intelligence — A Borrowed Name

**Reto:** A Borrowed Name  
**Oleada:** 2  
**ID de reto:** `92`  
**Estado:** resuelto y validado.

**Respuesta:** `Trusona`  
**Flag:** `POCTF{92.1522.0efa181beb09b64a.LSP4XUDSJ3IKCFGEHIXEQQQRCV}`

## Resolución

El sujeto es Frank Abagnale Jr. La pregunta cita su frase “Passwords are for
treehouses” y pide identificar la empresa de autenticación sin contraseñas a
la que se acercó como asesor. La investigación de la propia empresa y de
entrevistas contemporáneas identifica a **Trusona**, fundada por Ori Eisen.

Se envió `Trusona` al endpoint de respuesta, que devolvió el marcador
`POCTF{92.1522.0efa181beb09b64a.LSP4XUDSJ3IKCFGEHIXEQQQRCV}`. El formulario de
flag respondió `Landed.`.

## Reproducción

```bash
python3 solve.py
```

El script registra la respuesta de investigación y no realiza envíos.
