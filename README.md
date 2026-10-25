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
| 4 | Cryptography | A Map of Small Things | **Resuelto y validado** | [write-up](01-cryptography/04-a-map-of-small-things/README.md) · [solve.py](01-cryptography/04-a-map-of-small-things/solve.py) |
| 5 | Exploitation | The Sandglass | **Resuelto y validado** | [write-up](02-exploitation/01-the-sandglass/README.md) · [solve.lua](02-exploitation/01-the-sandglass/solve.lua) |
| 6 | Exploitation | Read Me My Fortune | **Resuelto y validado** | [write-up](02-exploitation/02-read-me-my-fortune/README.md) · [solve.py](02-exploitation/02-read-me-my-fortune/solve.py) |
| 7 | Exploitation | Thirty-Two Steps Down | **Resuelto y validado** | [write-up](02-exploitation/03-thirty-two-steps-down/README.md) · [solve.py](02-exploitation/03-thirty-two-steps-down/solve.py) |
| 8 | Exploitation | A Few Seconds Either Way | **Resuelto y validado** | [write-up](02-exploitation/04-a-few-seconds-either-way/README.md) · [solve.py](02-exploitation/04-a-few-seconds-either-way/solve.py) |
| 9 | Forensics | Everything Left Open | **Resuelto y validado** | [write-up](03-forensics/01-everything-left-open/README.md) · [solve.py](03-forensics/01-everything-left-open/solve.py) |
| 10 | Forensics | A Cabin Worth | **Resuelto y validado** | [write-up](03-forensics/02-a-cabin-worth/README.md) · [solve.py](03-forensics/02-a-cabin-worth/solve.py) |
| 11 | Forensics | What Goes Unwritten | **Resuelto y validado** | [write-up](03-forensics/03-what-goes-unwritten/README.md) · [solve.py](03-forensics/03-what-goes-unwritten/solve.py) |
| 12 | Forensics | A Quiet Home | **Resuelto y validado** | [write-up](03-forensics/04-a-quiet-home/README.md) · [solve.py](03-forensics/04-a-quiet-home/solve.py) |
| 13 | Game Hacking | Leap of Faith | **Resuelto y validado** | [write-up](04-game-hacking/01-leap-of-faith/README.md) · [solve.py](04-game-hacking/01-leap-of-faith/solve.py) |
| 14 | Game Hacking | Health Is a Social Construct | **Resuelto y validado** | [write-up](04-game-hacking/02-health-is-a-social-construct/README.md) · [solve.py](04-game-hacking/02-health-is-a-social-construct/solve.py) |
| 15 | Miscellaneous | The Apparatus, Invocation | **Resuelto y validado** | [write-up](04-game-hacking/03-the-apparatus-invocation/README.md) · [solve.py](04-game-hacking/03-the-apparatus-invocation/solve.py) |
| 16 | Miscellaneous | Frequency and Consequence | **Resuelto y validado** | [write-up](05-miscellaneous/01-frequency-and-consequence/README.md) · [solve.py](05-miscellaneous/01-frequency-and-consequence/solve.py) |

Progreso actual: **16/34 retos resueltos**. La plataforma mostró `CHALLENGE
SOLVED` para `Letters Never Sent`, desbloqueó el logro `Warm Up`, aceptó
`The Apparatus, Rapport` con el mensaje `Correct. Contact is established.` y
aceptó `The Consulting Room` con `Correct.` y `A Map of Small Things` con el
marcador canónico generado por la página objetivo. `The Sandglass` aparece
como `Solved` y el formulario confirma `Already solved.`. `Read Me My
Fortune` respondió `Correct.`. `Thirty-Two Steps Down` respondió `Correct.`
tras alcanzar el nivel 32 del VM y ejecutar `READ_HOST_FLAG`. `A Few Seconds
Either Way` confirmó `Race won.` después de ganar la carrera entre el
allowlist de lectura y el acceso al valor. `Everything Left Open` respondió
`Correct.` tras recuperar la flag del estado de sesión de Firefox. `A Cabin
Worth` confirmó `ACK :: Correct.` después de recuperar la fila eliminada del
WAL de SQLite y descifrar su nota de Joplin. `What Goes Unwritten` confirmó
`ACK :: Correct.` con el token base32 recuperado del minidump.
`A Quiet Home` confirmó `ACK :: Correct.` tras identificar el serial del
dispositivo ajeno en el tráfico MQTT. `Leap of Faith` devolvió el marcador
del flujo autónomo del cliente y el formulario confirmó `Landed. Nicely done.`
`Health Is a Social Construct` confirmó el mismo mensaje sin exigir progreso
del juego, al reproducir su flujo de cliente.
`The Apparatus, Invocation` confirmó `Silent. The apparatus speaks.` tras
resolver la cuadrícula Lights Out específica del equipo.
`Frequency and Consequence` aceptó el nonce `M6N2OZJ2AGH26YWQ` con `Correct. 73.`.

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
├── 01-cryptography/
    └── 01-letters-never-sent/
        ├── README.md
        └── solve.py
├── 02-exploitation/
    ├── 01-the-sandglass/
    ├── 02-read-me-my-fortune/
    └── 03-thirty-two-steps-down/
        ├── README.md
        └── solve.py
├── 03-forensics/
    ├── 01-everything-left-open/
    ├── 02-a-cabin-worth/
    ├── 03-what-goes-unwritten/
    └── 04-a-quiet-home/
        ├── README.md
        └── solve.py
└── 04-game-hacking/
    ├── 01-leap-of-faith/
    ├── 02-health-is-a-social-construct/
    └── 03-the-apparatus-invocation/
        ├── README.md
        └── solve.py
└── 05-miscellaneous/
    └── 01-frequency-and-consequence/
        ├── README.md
        └── solve.py
```

Última revisión de la información visible del sitio: **24 de octubre de
2026**.
