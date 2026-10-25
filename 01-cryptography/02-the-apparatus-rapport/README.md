# Cryptography — The Apparatus, Rapport

**Reto:** The Apparatus, Rapport  
**Identificador visible:** `crypto2`  
**Oleada:** 2  
**Puntos mostrados:** 125  
**Estado:** resuelto y validado en la plataforma.

**Flag:** `POCTF{5.1522.4PJEZSEMFPTYF5SQ.BPATVYCIAFX2ZAGKYBZMEC7NHA}`

## Tablero y clave

El tablero final es:

```text
A·  BO  CX
D·  E·  FX
G·  HO  IX
```

X comienza, los turnos alternan y la partida termina en cuanto X completa una
línea. Por tanto, X gana al colocar `I`, completando la columna `C-F-I`. Las
jugadas posibles que respetan la posición final son cuatro:

```text
CBFHI   CHFBI   FBCHI   FHCBI
```

La segunda cadena se entiende como `CHFBI` (sin espacio): el mensaje
secundario sirve para distinguir el orden de las jugadas de X y O.

## Cifrado

El reto usa la secuencia de casillas como clave y desplaza caracteres dentro
del alfabeto ASCII imprimible de 95 caracteres. Para cada carácter de la
clave, `A` representa desplazamiento 0, `B` desplazamiento 1, …, `I`
desplazamiento 8:

```text
plain = ((cipher - 32) - shift) mod 95 + 32
```

Al probar `CHFBI`, el mensaje secundario se vuelve legible:

```text
By salt and by ash, by the breath drawn but not returned, we open the way.
```

El mismo procedimiento sobre el mensaje primario devuelve la flag:

```text
POCTF{5.1522.4PJEZSEMFPTYF5SQ.BPATVYCIAFX2ZAGKYBZMEC7NHA}
```

La flag se envió desde la cuenta `hackadvisermx` y la plataforma respondió
`Correct. Contact is established.`

## Reproducción

```bash
python3 solve.py
```
