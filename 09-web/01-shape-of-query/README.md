# Web — The Shape of a Query

**Reto:** The Shape of a Query  
**Oleada:** 1  
**ID de reto:** `81`  
**Estado:** resuelto y validado.

**Flag aceptada:** `POCTF{81.1522.N5OPK5ZZWAAM25PV.AYOYW5KOWNXKVHBPTB5RKZGZH5}`

## Resolución

La página autenticada entrega un token temporal `SHAPE1...` para el equipo.
Se canjea en `/session/exchange` del portal externo y se obtiene una sesión
para su API GraphQL.

La introspección está habilitada. El tipo `User` expone `team` y
`privateNotes`; la consulta a `me` permite ver también los miembros del
equipo. El usuario `admin_1522` tenía la flag en su nota privada:

```graphql
{
  me {
    team {
      members { username privateNotes }
    }
  }
}
```

La entrega respondió `Correct.`.

## Reproducción

```bash
python3 solve.py 'SHAPE1...'
```
