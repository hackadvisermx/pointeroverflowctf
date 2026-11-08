# The Tower of Babel
Nonce: `fec9301be1381b49`

Order of application: base3 -> base58 -> transpose(7) -> base85(RFC1924) -> base7(AEIOUYX).
Each stage treats the previous stage's ASCII text as a big-endian integer and re-expresses it in the next base
(no UTF-16 involved). `solve_clean.py` tries all orders and keeps only the one where every
intermediate string fits the next alphabet.
