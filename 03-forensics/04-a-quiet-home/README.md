# Forensics — A Quiet Home

**Reto:** A Quiet Home  
**Identificador visible:** `forensics4`  
**Oleada:** 4  
**Puntos mostrados:** 137  
**Artefacto:** `marchetti-2026-14-elena-ha.zip`  
**SHA-256 publicado:** `4adb0eeec2e8e190e4fff39e62328026a682d261c876928639c27e56560eab6d`  
**Estado:** resuelto y validado.

**Token/serial:** `6SOGN7PZUD7XQPTW`

## Análisis

La configuración de HomeAssistant identifica el slot 04 de la cerradura como
`M.H.`. En el log MQTT, a las 14:47, la puerta se desbloquea con
`keypad_04`. En el tráfico inmediatamente posterior aparece un cliente no
habitual, `zwave_c4pf5`, que publica sus atributos.

El payload de `zwave/rf_key_c4pf5/attributes` contiene:

```json
{"node_id":47,"product_id":"0x0037","product_type":"0x0217",
 "product_serial":"6SOGN7PZUD7XQPTW","manufacturer":"Aeotec",
 "model":"MiniMote Key Fob (ZW088)"}
```

El `product_serial` es el token de 16 caracteres base32. La página objetivo
confirmó el envío con `ACK :: Correct.`.

## Reproducción

```bash
python3 solve.py marchetti-2026-14-elena-ha.zip
```

El solver requiere `tshark` para decodificar los paquetes MQTT. El ZIP es
específico del equipo y no se conserva en el repositorio.
