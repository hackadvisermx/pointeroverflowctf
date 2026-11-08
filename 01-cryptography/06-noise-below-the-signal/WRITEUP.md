# Noise Below the Signal
Answer (JSON): `[1,1,2,1,3,1,-2,-2,-3,2,0,-3,-3,0,2]`
(mod q=1601: `[1,1,2,1,3,1,1599,1599,1598,2,0,1598,1598,0,2]`)

Statement: secret is drawn from the same small distribution as the noise (|s_i|<=3), noise B=3, n=15, m=30, q=1601.
Method: Kannan embedding of the q-ary lattice of A's column space (basis [I|C] / qI), LLL, shortest vector
(b - A s, +-3) gives the error; solve A s = b - e mod q. All 30 residuals are within [-3,3].
Earlier attempt failed because it assumed a uniform secret (wrong) and had reduction bugs.
`solve_clean.py` needs numpy.
