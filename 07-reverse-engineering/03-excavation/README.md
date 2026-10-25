# Reverse Engineering — Excavation

**Reto:** Excavation  
**Oleada:** 1  
**ID de reto:** `119`  
**Estado:** resuelto y validado.

**Flag aceptada:** `CNMWEJ37B6ZYULKL`

## Artefactos

La página entrega tres saves canónicos y un save específico del equipo. Los
cuatro encabezados comparten el magic `9e e1 c7 21`, la versión `02 00 02 00`
y un tamaño little-endian. Los SHA-256 publicados coinciden con los archivos
descargados:

| Archivo | SHA-256 |
|---|---|
| `sample1.sav` | `6ed4defc4ca96b9f28086375ca2f0d690a6af708c51e78746a67dc49ce9ac1a2` |
| `sample2.sav` | `d2660f5a5d0577daa30c0e57264434b8be0267dcd496bd6afbe9fc00f6c8582c` |
| `sample3.sav` | `1bd1418716899948646b314d48c01dd16ab5d4720501ef582a7392a61378e1b` |
| `team.sav` | `41b344a64f7253bfa838613123c204043182b363fc6f17fdce4d1e649b2ef173` |

## Resolución

El cuerpo empieza después de los 12 bytes iniciales y usa una máscara XOR
periódica de 8 bytes. Las claves recuperadas por texto conocido son:

```text
sample1  bff366a0192308a7
sample2  8ee28d4183df8c1b
sample3  e62903e8dcf7b038
team     271c348acb5f8ecb
```

Tras aplicar la máscara, aparecen registros de inventario y notas de sesión.
Los tres saves canónicos producen acrósticos de los primeros nombres de item:
`TORCH`, `SILVERMOON` y `NIGHTENDSSOON`, lo que confirma la lectura del
formato.

El save del equipo contiene 16 nombres de item. Tomando la inicial de cada
nombre, en el orden almacenado, se obtiene:

```text
Cracked Séance Disc       C
Needle of the Bureau      N
Marrow Quill Pen          M
Widow's Brass Compass    W
Ember in Glass            E
Jarful of Teeth           J
3-Pronged Rowan Fork      3
7-Day Candle              7
Blackbone Flute           B
6-Ward Amulet             6
Zinc Etched Sigil Plate   Z
Yew Stem Staff             Y
Uncoiling Rope             U
Lead Bound Envelope       L
Knotted Willow Charm       K
Lead Bound Envelope       L
```

El token resultante es `CNMWEJ37B6ZYULKL`. La entrega al reto respondió
`Correct.`.

