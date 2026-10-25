# Reverse Engineering — The Disassembled Mind

**Reto:** The Disassembled Mind  
**Oleada:** 2  
**ID de reto:** `117`  
**Estado:** resuelto y validado.

**Flag aceptada:** `POCTF{117.1522.DLOHMGAUD77LGKP7.EZIK566V6KHWJ24453NTVZKVO5}`

## Artefactos

La página entrega un `program.pyc` específico del equipo y un README. El
SHA-256 publicado para `program.pyc` es:

```text
0c91f2b6ae600230a67a12c9f67698f4fe7936e092b7102420776204faba382a
```

## Resolución

El módulo está compilado con un intérprete reciente de Python 3. El código de
`check()` asigna cinco constantes binarias de igual longitud:

- `enc1`
- `_a` (señuelo, no se indexa)
- `enc2`
- `key2`
- `_b` (señuelo, no se indexa)

El bucle usa únicamente las tres constantes activas y calcula, byte por byte:

```text
expected[i] = enc1[i] XOR enc2[i] XOR key2[i]
```

El valor resultante es la flag completa. Los dos blobs `_a` y `_b` no
participan en ningún acceso posterior, tal como anticipa el enunciado.

La flag se envió al endpoint y respondió `Correct.`.

## Reproducción

```bash
python3 solve.py program.pyc
```

