# Reverse Engineering — Panoptican

**Reto:** Panoptican  
**Oleada:** 3  
**ID de reto:** `120`  
**Estado:** resuelto y validado.

**Flag aceptada:** `POCTF{120.1522.fcc5ee8e157e9a9c.VJRTXDGZVFX4ORJCTP5GBH3NMQ}`

## Artefacto

La página entrega un ZIP específico del equipo con un ELF Linux x86_64
strippeado llamado `panoptican`. El ZIP descargado tuvo SHA-256:

```text
eabd8d1057d453c4c0fa5a4b32437bc9721fb42480f0900d61afb901da669b1c
```

## Resolución

El programa espera una imagen PGM `P5` de `32 × 32` píxeles, carga exactamente
`0x400` bytes y compara la entrada contra una imagen de referencia embebida.
La comparación acepta una distancia cuadrática total de hasta `0x7d0`.

La imagen de referencia comienza en el offset de archivo `0x20f0`. Después de
pasar la comparación, el binario combina sus primeros `0x80` bytes con la
región de máscara en `0x2070` mediante XOR. El resultado termina en una cadena
ASCII con la flag.

El flujo no requiere ejecutar el ELF (el artefacto es Linux y el entorno de
trabajo es macOS); basta con leer las dos regiones del binario y aplicar el
XOR.

La flag se envió al endpoint del reto y respondió `Record recovered.`.

## Reproducción

```bash
python3 solve.py path/to/panoptican
```

