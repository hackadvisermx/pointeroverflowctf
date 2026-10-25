# Reverse Engineering — An Invented Language

**Reto:** An Invented Language  
**Oleada:** 4  
**ID de reto:** `123`  
**Estado:** resuelto y validado.

**Flag aceptada:** `POCTF{123.1522.aa143f2d7e1bf811.ZFKNZNGQU2TXVYFFDLURUM7G7W}`

## Artefactos

La página entrega `prog.bin`, `vm.c` y `README.txt` dentro de un ZIP
específico del equipo. El programa es una VM de pila pequeña. El bytecode no
imprime nada: escribe valores en la memoria `m[]` y termina.

## Resolución

Las operaciones relevantes son `PUSH` (`0x01`), XOR (`0x07`) y escritura en
memoria (`0x0b`). Cada bloque del programa calcula un byte mediante XOR y lo
guarda en una posición consecutiva. Al emular los bloques, las posiciones
`m[0]` a `m[58]` forman directamente:

```text
POCTF{123.1522.aa143f2d7e1bf811.ZFKNZNGQU2TXVYFFDLURUM7G7W}
```

La flag se envió y el endpoint respondió `The interpreter concurs.`.

## Reproducción

```bash
python3 solve.py prog.bin
```

