# Cryptography — Letters Never Sent

**Reto:** Letters Never Sent  
**Identificador visible:** `crypto1`  
**Oleada:** 1  
**Puntos mostrados al abrirlo:** 95  
**Estado:** resuelto localmente; flag pendiente de validación en la plataforma.

## Enunciado y artefactos

La carta está dirigida al almirante Sir Francis Beaufort. El texto menciona
explícitamente un método de “reciprocal tableau” que lleva su nombre. La
imagen se entrega desde la página autenticada del reto:

<https://pointeroverflowctf.com/challenges/letters-never-sent/image/003>

Ciphertext específico de esta sesión:

```text
XQBPP{2.1522.A267IGZCDQZK4673.UO6YFMSMCKJQI3EFOJQPY2FAJY}
```

El marco de la carta contiene palabras en los cuatro lados. Las seis palabras
marcadas con una estrella, leídas alrededor del marco, dan las iniciales
`MEDIUM` (por ejemplo, `Marigold`, `Elder`, `Dove`, `Iris`, …, `Marigold`).
Ese es el indicio para la clave.

## Resolución

1. Identificar **Beaufort** por el destinatario y por la referencia al
   reciprocal tableau.
2. Extraer la clave `MEDIUM` de las palabras marcadas en el borde.
3. Aplicar Beaufort sobre las letras, conservando dígitos, puntos y llaves:

   ```text
   P = K - C (mod 26)
   ```

4. La salida local es:

   ```text
   POCTF{2.1522.M267EYEGRWNU4673.JU6WHAMRGKDWW3ZDGDWPF2DUDO}
   ```

El prefijo `POCTF{` confirma la alineación de la clave. La flag todavía no se
ha enviado desde el navegador en esta sesión; después del envío debe
actualizarse este estado con la respuesta visible del sitio.

## Reproducción

```bash
python3 solve.py
```

El script no necesita red, cookies ni credenciales.
