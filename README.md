# Pointer Overflow CTF 2026

Writeups, scripts y evidencias reproducibles del **Pointer Overflow CTF
(POCTF) 2026**.

Este repositorio es un proyecto hijo de la colección local
[`../ctf-writeups`](../ctf-writeups/). No se guardan credenciales, cookies,
tokens ni otros secretos de la sesión del concurso. Las flags y los artefactos
que dependan del equipo se registran solo después de validarlos y con el
contexto mínimo necesario.

## Evento

- **Sitio oficial:** [pointeroverflowctf.com](https://pointeroverflowctf.com/)
- **Organización:** University of Wisconsin–Stevens Point (UWSP), en honor a
  estudiantes y egresados del programa CIS: Cybersecurity.
- **Organizador/contacto visible:** Prof. C. R. Johnson ·
  [cjohnson@uwsp.edu](mailto:cjohnson@uwsp.edu).
- **Modalidad:** concurso online con participación global.
- **Cuenta usada en esta sesión:** `hackadvisermx`, bracket **Solo**.
- **Estado inicial de la cuenta:** 0/34 retos resueltos; registro completado.

### Calendario publicado

La portada indica que el concurso comenzó el **domingo 27 de septiembre de
2026** y que las oleadas se publican semanalmente. El sitio muestra `09:00
CDT` en el calendario de oleadas y `8:00 AM` en el bloque de datos generales;
se conserva la información tal como aparece publicada.

| Oleada | Publicación visible |
|---|---|
| Wave 1 | 27 de septiembre de 2026 · 09:00 CDT |
| Wave 2 | 4 de octubre de 2026 · 09:00 CDT |
| Wave 3 | 11 de octubre de 2026 · 09:00 CDT |
| Wave 4 | 18 de octubre de 2026 · 09:00 CDT |
| Wave 5 | 25 de octubre de 2026 · 09:00 CDT |
| Wave 6 | 1 de noviembre de 2026 · 09:00 CST |
| Wave 7 | 8 de noviembre de 2026 · 09:00 CST |
| Wave 8 | 15 de noviembre de 2026 · 09:00 CST |

**Cierre publicado:** domingo 6 de diciembre de 2026 · 16:00 CST.

## Reglas y puntuación

- Hay tres brackets: **Solo**, **Team** (de 1 a 6 participantes) y
  **Academic**. Cada persona solo puede competir en un bracket.
- Las flags son específicas del equipo; el texto de algunos retos también
  puede variar por equipo. Las entregas válidas se hacen mediante la página
  oficial del reto.
- Cada reto comienza con un valor base oculto durante una ventana de
  observación. El valor final queda entre **50 y 500 puntos** y se congela al
  alcanzarse el quórum de solves, el quórum de ratings o tras 7 días.
- El primer equipo en resolver recibe un **10 % de first blood** cuando se
  congela el reto. No hay decaimiento posterior.
- Cada reto puede tener hasta tres pistas. Cada pista cuesta **10 puntos
  finalizados**, se compran en orden y no es reembolsable.
- No se permite acceder a datos o instancias de otros equipos, compartir
  flags/soluciones privadas entre equipos ni realizar DoS/DDoS.

## Retos publicados en el tablero

El perfil de la cuenta indica **34 retos** en total. El tablero público los
organiza en estas categorías:

| Categoría | Retos |
|---|---|
| Cryptography | Letters Never Sent · The Apparatus, Rapport · The Consulting Room · A Map of Small Things |
| Exploitation | The Sandglass · Read Me My Fortune · Thirty-Two Steps Down · A Few Seconds Either Way |
| Forensics | Everything Left Open · A Cabin Worth · What Goes Unwritten · A Quiet Home |
| Game Hacking | Leap of Faith · Health Is a Social Construct |
| Miscellaneous | The Apparatus, Invocation · Frequency and Consequence · Columns of Holes · A Peculiar Game |
| Open-Source Intelligence | A Borrowed Name · Strings Attached · Where the Light Fails to Fall · The Apparatus, Apport |
| Reverse Engineering | Panoptican · The Disassembled Mind · Excavation · An Invented Language |
| Steganography | Invisible Ink · The Apparatus, The Rapping · Commit to Memory · Velocity |
| Web | Poisoned Well · The Shape of a Query · No Structure Required · The Logic Inside |

El tablero mostraba solves y puntos globales para los retos ya activos; la
cuenta propia comenzaba sin solves. La fuente de verdad para cada reto es la
página autenticada de ese reto.

## Progreso

| # | Categoría | Reto | Estado | Evidencia |
|---:|---|---|---|---|
| 1 | Cryptography | Letters Never Sent | **Resuelto y validado** | [write-up](01-cryptography/01-letters-never-sent/README.md) · [solve.py](01-cryptography/01-letters-never-sent/solve.py) |
| 2 | Cryptography | The Apparatus, Rapport | **Resuelto y validado** | [write-up](01-cryptography/02-the-apparatus-rapport/README.md) · [solve.py](01-cryptography/02-the-apparatus-rapport/solve.py) |
| 3 | Cryptography | The Consulting Room | **Resuelto y validado** | [write-up](01-cryptography/03-the-consulting-room/README.md) · [solve.py](01-cryptography/03-the-consulting-room/solve.py) |

Progreso actual: **3/34 retos resueltos**. La plataforma mostró `CHALLENGE
SOLVED` para `Letters Never Sent`, desbloqueó el logro `Warm Up`, aceptó
`The Apparatus, Rapport` con el mensaje `Correct. Contact is established.` y
aceptó `The Consulting Room` con `Correct.`.

## Premios publicados

- Certificado digital individual y entrada en el Hall of Fame para todas las
  personas participantes.
- Challenge coin para los puestos 1 y 2 de cada categoría y para cada MVP de
  categoría.
- Premios monetarios: Solo 1.º `$50`; Team 1.º `$100` y 2.º `$50`; Academic
  1.º `$100` y 2.º `$50`; Ghostbuster `$50`.

## Estructura

```text
pointeroverflowctf/
├── README.md
└── 01-cryptography/
    └── 01-letters-never-sent/
        ├── README.md
        └── solve.py
```

Última revisión de la información visible del sitio: **24 de octubre de
2026**.
