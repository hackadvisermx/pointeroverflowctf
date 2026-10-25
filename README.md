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
| 17 | Miscellaneous | Columns of Holes | **Resuelto y validado** | [write-up](05-miscellaneous/02-columns-of-holes/README.md) · [solve.py](05-miscellaneous/02-columns-of-holes/solve.py) |
| 18 | Miscellaneous | A Peculiar Game | **Resuelto y validado** | [write-up](05-miscellaneous/03-a-peculiar-game/README.md) · [solve.py](05-miscellaneous/03-a-peculiar-game/solve.py) |
| 19 | Open-Source Intelligence | Where the Light Fails to Fall | **Resuelto y validado** | [write-up](06-open-source-intelligence/01-where-the-light-fails-to-fall/README.md) · [solve.py](06-open-source-intelligence/01-where-the-light-fails-to-fall/solve.py) |
| 20 | Open-Source Intelligence | A Borrowed Name | **Resuelto y validado** | [write-up](06-open-source-intelligence/02-a-borrowed-name/README.md) · [solve.py](06-open-source-intelligence/02-a-borrowed-name/solve.py) |
| 21 | Open-Source Intelligence | Strings Attached | **Resuelto y validado** | [write-up](06-open-source-intelligence/03-strings-attached/README.md) · [solve.py](06-open-source-intelligence/03-strings-attached/solve.py) |
| 22 | Open-Source Intelligence | The Apparatus, Apport | **Resuelto y validado** | [write-up](06-open-source-intelligence/04-the-apparatus-apport/README.md) |
| 23 | Reverse Engineering | Panoptican | **Resuelto y validado** | [write-up](07-reverse-engineering/01-panoptican/README.md) · [solve.py](07-reverse-engineering/01-panoptican/solve.py) |
| 24 | Reverse Engineering | The Disassembled Mind | **Resuelto y validado** | [write-up](07-reverse-engineering/02-the-disassembled-mind/README.md) · [solve.py](07-reverse-engineering/02-the-disassembled-mind/solve.py) |
| 25 | Reverse Engineering | An Invented Language | **Resuelto y validado** | [write-up](07-reverse-engineering/04-an-invented-language/README.md) · [solve.py](07-reverse-engineering/04-an-invented-language/solve.py) |
| 26 | Steganography | Velocity | **Resuelto y validado** | [write-up](08-steganography/04-velocity/README.md) · [solve.py](08-steganography/04-velocity/solve.py) |
| 27 | Steganography | Commit to Memory | **Resuelto y validado** | [write-up](08-steganography/02-commit-to-memory/README.md) · [solve.py](08-steganography/02-commit-to-memory/solve.py) |
| 28 | Steganography | The Apparatus, The Rapping | **Resuelto y validado** | [write-up](08-steganography/03-the-apparatus-the-rapping/README.md) · [solve.py](08-steganography/03-the-apparatus-the-rapping/solve.py) |
| 29 | Web | The Shape of a Query | **Resuelto y validado** | [write-up](09-web/01-shape-of-query/README.md) · [solve.py](09-web/01-shape-of-query/solve.py) |
| 30 | Web | Poisoned Well | **Resuelto y validado** | [write-up](09-web/02-poisoned-well/README.md) · [solve.py](09-web/02-poisoned-well/solve.py) |
| 31 | Web | The Logic Inside | **Resuelto y validado** | [write-up](09-web/04-the-logic-inside/README.md) · [solve.py](09-web/04-the-logic-inside/solve.py) |
| 32 | Reverse Engineering | Excavation | **Resuelto y validado** | [write-up](07-reverse-engineering/03-excavation/README.md) |
| 33 | Steganography | Invisible Ink | **Resuelto y validado** | [write-up](08-steganography/01-invisible-ink/README.md) · [solve.py](08-steganography/01-invisible-ink/solve.py) |
| 34 | Web | No Structure Required | **Resuelto y validado** | [write-up](09-web/03-no-structure-required/README.md) |

Progreso actual: **34/34 retos resueltos**. La plataforma mostró `CHALLENGE
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
`Columns of Holes` aceptó el nonce `101F31EB65350D9A` con `Correct.` tras
decodificar las punchcards Hollerith del memo PDF.
`A Peculiar Game` aceptó el nonce `D618BBB084981B76` con `The game concludes.`
tras leer las casillas de destino como una rejilla de dos filas.
`Where the Light Fails to Fall` confirmó Baghdad mediante la geometría de la
sombra y aceptó la flag con `Correct.`.
`A Borrowed Name` confirmó `Trusona` y aceptó el marcador específico del
equipo con `Landed.`.
`Strings Attached` confirmó `Wizcorp, LLC` y aceptó el marcador específico del
equipo con `Landed.`.
`The Apparatus, Apport` identificó a Emma Hardinge Britten con `BRITTEN_1870`
y respondió `Identified. The archive is closed.`.
`Panoptican` respondió `Record recovered.` tras reconstruir la imagen PGM
embebida y aplicar el XOR de autorización. `The Disassembled Mind` respondió
`Correct.` al combinar sus tres constantes activas byte a byte. `An Invented
Language` respondió `The interpreter concurs.` tras emular las operaciones
PUSH/XOR/escritura de su VM. `Velocity` aceptó `C268716976238AAD` con
`The signal resolves.` después de decodificar las 64 velocidades MIDI como
bits.
`Commit to Memory` respondió `Correct. Committed.` al convertir las
diferencias de timestamp de los commits a bytes ASCII. `The Apparatus, The
Rapping` aceptó `AAED9D899DD8B64E` con `The signal resolves.` después de
decodificar la temporización Morse de los golpes.
`The Shape of a Query` respondió `Correct.` al consultar la nota privada del
miembro administrador mediante GraphQL. `Poisoned Well` respondió `Correct.`
al verificar la caché con la sesión del equipo. `The Logic Inside` aceptó
`f3ae7967e6c6624c` usando la representación decimal de loopback y el oráculo
de códigos HTTP. `Excavation` aceptó `CNMWEJ37B6ZYULKL` después de descifrar
los saves y leer las iniciales de los 16 items del equipo. `Invisible Ink`
aceptó `POCTF{WPFHZJFKNCCRYYDK}` al extraer ASCII de 7 bits del whitespace
final de las líneas impares. `No Structure Required` respondió `Auditor's
signature verified.` tras usar la inyección NoSQL del login y consultar la
colección oculta `secrets`.

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
│   ├── 01-letters-never-sent/
│   ├── 02-the-apparatus-rapport/
│   ├── 03-the-consulting-room/
│   └── 04-a-map-of-small-things/
├── 02-exploitation/
│   ├── 01-the-sandglass/
│   ├── 02-read-me-my-fortune/
│   ├── 03-thirty-two-steps-down/
│   └── 04-a-few-seconds-either-way/
├── 03-forensics/
│   ├── 01-everything-left-open/
│   ├── 02-a-cabin-worth/
│   ├── 03-what-goes-unwritten/
│   └── 04-a-quiet-home/
├── 04-game-hacking/
│   ├── 01-leap-of-faith/
│   ├── 02-health-is-a-social-construct/
│   └── 03-the-apparatus-invocation/
├── 05-miscellaneous/
│   ├── 01-frequency-and-consequence/
│   ├── 02-columns-of-holes/
│   └── 03-a-peculiar-game/
├── 06-open-source-intelligence/
    ├── 01-where-the-light-fails-to-fall/
    ├── 02-a-borrowed-name/
    ├── 03-strings-attached/
    └── 04-the-apparatus-apport/
└── 07-reverse-engineering/
    ├── 01-panoptican/
    ├── 02-the-disassembled-mind/
    ├── 03-excavation/
    └── 04-an-invented-language/
└── 08-steganography/
    ├── 01-invisible-ink/
    ├── 02-commit-to-memory/
    ├── 03-the-apparatus-the-rapping/
    └── 04-velocity/
└── 09-web/
    ├── 01-shape-of-query/
    ├── 02-poisoned-well/
    ├── 03-no-structure-required/
    └── 04-the-logic-inside/
```

Última revisión de la información visible del sitio: **24 de octubre de
2026**.
