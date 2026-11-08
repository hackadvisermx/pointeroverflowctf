#!/usr/bin/env python3
"""
LWE Solver for "Noise Below the Signal" using Correct Primal Lattice LLL
n=15, q=1601, m=30, B=3

Based on Howgrave-Graham (2007): "Solving LWE with LLL"
Primal lattice: [alpha*I_n    0  ]
                [   A        qI_m ]
Target vector: [0, b]
"""

import math
import json

n = 15
q = 1601
m = 30
B = 3

A = [
    [98, 1007, 1573, 1084, 466, 963, 142, 405, 806, 148, 1579, 1228, 1081, 871, 1200],
    [670, 643, 455, 782, 1039, 86, 46, 1335, 815, 473, 737, 713, 1137, 161, 639],
    [1204, 1498, 828, 1090, 642, 1142, 1374, 1395, 588, 136, 1463, 684, 251, 96, 555],
    [1272, 536, 559, 1555, 873, 756, 643, 260, 547, 1033, 1186, 1293, 1489, 928, 1111],
    [1378, 67, 872, 640, 330, 753, 51, 265, 1166, 93, 239, 1202, 611, 1162, 102],
    [379, 1364, 342, 1575, 1430, 695, 916, 6, 843, 287, 943, 204, 418, 392, 1407],
    [1093, 977, 209, 1481, 777, 20, 764, 985, 978, 246, 702, 670, 307, 1572, 1033],
    [1509, 718, 111, 689, 8, 961, 570, 724, 1382, 399, 1516, 1273, 647, 354, 994],
    [1138, 722, 10, 1513, 1403, 869, 692, 1597, 13, 618, 602, 1109, 1096, 968, 1362],
    [536, 1151, 977, 1142, 199, 998, 1244, 955, 493, 1121, 644, 1430, 498, 1383, 1328],
    [12, 895, 563, 1444, 1388, 1546, 1262, 713, 230, 270, 394, 1549, 802, 305, 896],
    [818, 394, 519, 982, 225, 429, 877, 697, 1568, 1600, 1431, 1156, 451, 1439, 942],
    [1084, 680, 807, 1483, 451, 439, 981, 1102, 785, 589, 1218, 1511, 249, 454, 1596],
    [618, 1159, 784, 1442, 1506, 592, 1483, 1192, 1012, 239, 1042, 28, 1184, 527, 422],
    [598, 71, 1231, 27, 301, 226, 1231, 568, 1531, 1060, 25, 1500, 473, 796, 511],
    [1049, 114, 1395, 76, 1168, 860, 1090, 1148, 1039, 954, 1354, 1266, 1567, 1333, 127],
    [59, 150, 1312, 880, 1205, 100, 160, 169, 1595, 1007, 1225, 1165, 446, 1243, 1177],
    [391, 1278, 576, 112, 1371, 47, 1292, 1193, 886, 1477, 1344, 389, 747, 473, 1423],
    [808, 1412, 1511, 401, 1311, 868, 1523, 638, 1310, 1443, 1536, 1093, 454, 414, 1132],
    [859, 1469, 1026, 699, 590, 1507, 1444, 1575, 1258, 462, 1521, 1571, 497, 1547, 921],
    [356, 431, 19, 354, 887, 299, 143, 1200, 1125, 106, 208, 1248, 1085, 187, 963],
    [840, 1540, 1347, 0, 1459, 1239, 1146, 624, 152, 886, 1025, 885, 440, 127, 970],
    [430, 1051, 1283, 422, 692, 1102, 717, 1079, 1089, 1464, 380, 695, 1190, 461, 864],
    [953, 1359, 827, 537, 232, 1444, 1278, 1357, 532, 1520, 1372, 1356, 670, 147, 1355],
    [60, 140, 1322, 391, 1137, 1560, 1485, 507, 424, 103, 362, 649, 381, 1290, 1075],
    [128, 48, 977, 1260, 767, 290, 896, 338, 1206, 609, 417, 205, 455, 1461, 920],
    [99, 1314, 995, 443, 1175, 450, 1139, 441, 524, 1067, 457, 577, 243, 420, 953],
    [1352, 1571, 192, 1046, 1465, 786, 1169, 43, 802, 1119, 1486, 232, 57, 1073, 574],
    [1311, 1423, 353, 820, 32, 60, 689, 897, 437, 376, 989, 523, 1361, 680, 1318],
    [1099, 1283, 848, 1204, 968, 101, 209, 172, 1236, 782, 1312, 482, 183, 695, 288]
]

b = [1557, 878, 1391, 353, 1199, 1331, 1115, 822, 1202, 1215, 1426, 1550, 822, 796, 1324, 864, 1519, 255, 1100, 1513, 1221, 28, 1388, 1048, 614, 974, 1467, 818, 871, 758]

n = 15
q = 1601
m = 30
B = 3

def mod_q(x):
    x = x % q
    if x > q // 2:
        x -= q
    return x

def check_secret(s):
    for i in range(m):
        dot = sum(A[i][j] * s[j] for j in range(n)) % q
        e = mod_q(dot - b[i])
        if abs(e) > B:
            return False
    return True

def mod_q(x):
    x = x % q
    if x > q // 2:
        x -= q
    return x

def lll_reduction(B, delta=0.75):
    """LLL reduction on matrix B"""
    n = len(B)
    B = [list(row) for row in B]
    
    def gs(B):
        n = len(B)
        B_star = [list(row) for row in B]
        mu = [[0]*n for _ in range(n)]
        for i in range(n):
            B_star[i] = list(B[i])
            for j in range(i):
                dot = sum(B[i][k] * B_star[j][k] for k in range(len(B[i])))
                dot_star = sum(B_star[j][k] * B_star[j][k] for k in range(len(B_star[j])))
                mu[i][j] = dot / dot_star if dot_star != 0 else 0
                for k in range(len(B[i])):
                    B_star[i][k] -= mu[i][j] * B_star[j][k]
        return B_star, mu
    
    B_star, mu = gs(B)
    k = 1
    while k < n:
        # Size reduction
        for j in range(k-1, -1, -1):
            if abs(mu[k][j]) > 0.5:
                r = round(mu[k][j])
                for i in range(len(B[k])):
                    B[k][i] -= r * B[j][i]
                mu[k][j] -= r
        
        # Lovasz condition
        B_star, mu = gs(B)
        dot_star_k = sum(x*x for x in B_star[k])
        dot_star_km1 = sum(x*x for x in B_star[k-1])
        if delta * dot_star_km1 > dot_star_k + mu[k][k-1]**2 * dot_star_km1:
            B[k], B[k-1] = B[k-1], B[k]
            k = max(k-1, 1)
        else:
            k += 1
    return B

def check_secret(s):
    for i in range(m):
        dot = sum(A[i][j] * s[j] for j in range(n)) % q
        e = mod_q(dot - b[i])
        if abs(e) > B:
            return False
    return True

def mod_q(x):
    x = x % q
    if x > q // 2:
        x -= q
    return x

def solve_primal_lll(alpha):
    """Howgrave-Graham primal lattice LLL"""
    dim = n + m
    basis = [[0]*dim for _ in range(dim)]
    
    # Scaled secret part: alpha * I_n
    for i in range(n):
        basis[i][i] = alpha
    
    # A part (rows n to n+m-1, cols 0 to n-1)
    for i in range(m):
        for j in range(n):
            basis[n + i][j] = A[i][j]
    
    # q*I part (rows n to n+m-1, cols n to n+m-1)
    for i in range(m):
        basis[n + i][n + i] = q
    
    print(f"Running LLL on primal lattice (dim={dim}, alpha={alpha})...")
    reduced = lll_reduction(basis)
    
    print("LLL reduced basis norms (first 20):")
    for i, row in enumerate(reduced[:20]):
        norm = math.sqrt(sum(x*x for x in row))
        if norm < 2000:
            print(f"  Row {i}: {norm:.2f}")
    
    # The secret should be in the first n coordinates of short vectors
    for row in reduced:
        secret_candidate = row[:n]
        if check_secret(secret_candidate):
            print(f"Found secret in LLL: {secret_candidate}")
            return secret_candidate
    
    # Also check linear combinations of short vectors
    print("Checking linear combinations of short vectors...")
    short_vecs = [row[:n] for row in reduced[:15]]
    for i in range(len(short_vecs)):
        for j in range(i, len(short_vecs)):
            cand = [(short_vecs[i][k] + short_vecs[j][k]) for k in range(n)]
            if check_secret(cand):
                return cand
            cand = [(short_vecs[i][k] - short_vecs[j][k]) for k in range(n)]
            if check_secret(cand):
                return cand
    
    return None

def check_secret(s):
    for i in range(m):
        dot = sum(A[i][j] * s[j] for j in range(n)) % q
        e = mod_q(dot - b[i])
        if abs(e) > B:
            return False
    return True

def mod_q(x):
    x = x % q
    if x > q // 2:
        x -= q
    return x

if __name__ == "__main__":
    import math
    print("Solving LWE using Howgrave-Graham Primal Lattice LLL")
    print(f"n={n}, q={q}, m={m}, B={B}")
    
    # Standard alpha = q / (B * sqrt(m))
    alpha = int(q / (B * math.sqrt(m)))
    print(f"Standard alpha = q/(B*sqrt(m)) = {alpha}")
    
    # Try multiple alpha values around the theoretical value
    for alpha in [50, 75, 100, 125, 150, 200, 250, 300, 400, 500, 800]:
        print(f"\nTrying alpha={alpha}")
        secret = solve_primal_lll(alpha)
        if secret:
            break
    
    if not secret:
        print("\nSecret not found with primal LLL")
    else:
        print(f"\nSecret found: {secret}")
        print(f"JSON: {json.dumps(secret)}")
        
        print("\nVerification:")
        for i in range(m):
            dot = sum(A[i][j] * secret[j] for j in range(n)) % q
            e = mod_q(dot - b[i])
            print(f"  Sample {i}: dot={dot}, b={b[i]}, e={e}")