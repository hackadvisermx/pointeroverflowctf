# Cryptography — A Map of Small Things

**Reto:** A Map of Small Things  
**Identificador visible:** `crypto4`  
**Oleada:** 4  
**Puntos mostrados:** 137  
**Estado:** resuelto y validado en la página objetivo.

**Flag:** `POCTF{73.1522.5MSC5CBIFNN5TTAP.QFKR7L3E5SBZ6B74GT4LICMI32}`

## Parámetros

La curva entregada por el reto es:

```text
y² = x³ + x  (mod p)
p  = 17759930830448937043
G  = (2, 2130375071143573863)
Q  = (9234220756006882062, 13534465947506840651)
```

Se pide recuperar `k` tal que `Q = k·G`. La página acepta el entero decimal
crudo, una variante `POCTF{...}` o el marcador canónico.

## Resolución

Como `p ≡ 3 (mod 4)` y la curva tiene `j = 1728` (`a=1`, `b=0`), el orden
del grupo es `#E(Fp) = p + 1`:

```text
17759930830448937044 = 2² · 38603 · 121123 · 949584469
```

El punto base tiene el orden completo `p+1`. Se aplicó Pohlig–Hellman y
BSGS en cada componente:

```text
k mod 4         = 0
k mod 38603     = 1888
k mod 121123    = 88202
k mod 949584469 = 899141831
```

El CRT da:

```text
k = 2251441649768399336
```

La verificación local `k·G == Q` fue positiva. El formulario genérico del reto
rechazó el entero y la variante simple `POCTF{...}`; la página objetivo aceptó
el entero mediante `key-input` y devolvió el marcador canónico:

```text
POCTF{73.1522.5MSC5CBIFNN5TTAP.QFKR7L3E5SBZ6B74GT4LICMI32}
```

## Reproducción

```bash
python3 solve.py
```
