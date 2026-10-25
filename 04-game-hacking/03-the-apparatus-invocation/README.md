# Miscellaneous — The Apparatus, Invocation

**Reto:** The Apparatus, Invocation  
**Identificador visible:** `MISC 100`  
**Oleada:** 1  
**ID de reto:** `3`  
**Estado:** resuelto y validado.

**Flag:** `POCTF{3.1522.TVRVX37X4C3ZIZX4.G3JURK7DUZQDOPMXGINSXPXO3R}`

## Análisis

La página contiene una cuadrícula Lights Out de 7×7. Cada pulsación cambia
la vela elegida y sus cuatro vecinos cardinales; el orden no importa y cada
celda se puede pulsar como máximo una vez en una solución mínima.

El patrón inicial es específico del equipo y aparece en el JavaScript de la
página como `initialBits`, en orden fila-major. Se prueba cada una de las
128 combinaciones posibles de la primera fila. Para cada candidato, la
regla determinista de Lights Out fuerza las pulsaciones de las filas
siguientes: si una vela de la fila anterior sigue encendida, se pulsa la
celda inmediatamente debajo. El candidato válido deja apagada la última
fila.

Para este equipo la solución tiene 12 pulsaciones. El endpoint de la página
acepta la secuencia como `POST .../complete` con un JSON de la forma
`{"clicks":[{"r":0,"c":0}, ...]}` y respondió `Silent. The apparatus speaks.`.
La entrega adicional del marcador respondió `Correct.`.

## Reproducción

Guarda el HTML autenticado de la página del reto y ejecuta:

```bash
python3 solve.py /ruta/al/invocation.html
```

El solver imprime la secuencia de pulsaciones; no guarda cookies ni envía
datos por sí mismo.
