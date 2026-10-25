# Open-Source Intelligence — Where the Light Fails to Fall

**Reto:** Where the Light Fails to Fall  
**Oleada:** 1  
**ID de reto:** `99`  
**Estado:** resuelto y validado.

**Ciudad:** Baghdad  
**Flag:** `POCTF{99.1522.PIXISB2UWH2DJO7B.43HHX2KQSGMGOOLXA2CAGWGBRC}`

## Análisis

La página proporciona una fotografía de un palomar sobre adoquines, una
flecha que marca el norte verdadero y la hora de observación:

```text
2026-06-06 · 17:40 · UTC+03:00
```

La dirección de la sombra del ave fija el azimut del sol hacia el oeste. Al
comparar el azimut y la elevación solares esperados para ciudades principales
compatibles con UTC+03:00, la combinación coincide con Baghdad. La entrega de
la ciudad respondió `The sun agrees.` y reveló la flag específica del equipo.

## Reproducción

```bash
python3 solve.py
```

El script calcula la posición solar aproximada para Baghdad en la hora dada;
no contiene credenciales ni realiza envíos.
