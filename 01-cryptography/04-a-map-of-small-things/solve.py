#!/usr/bin/env python3
"""Recover the MapCrypt private key with Pohlig-Hellman + BSGS."""

from math import isqrt

from sympy import factorint
from sympy.ntheory.modular import crt


P = 17759930830448937043
A = 1
G = (2, 2130375071143573863)
Q = (9234220756006882062, 13534465947506840651)
INFINITY = None


def negate(point):
    return INFINITY if point is INFINITY else (point[0], (-point[1]) % P)


def add(left, right):
    if left is INFINITY:
        return right
    if right is INFINITY:
        return left

    x1, y1 = left
    x2, y2 = right
    if x1 == x2 and (y1 + y2) % P == 0:
        return INFINITY

    if left == right:
        if y1 % P == 0:
            return INFINITY
        slope = (3 * x1 * x1 + A) * pow(2 * y1, -1, P) % P
    else:
        slope = (y2 - y1) * pow((x2 - x1) % P, -1, P) % P

    x3 = (slope * slope - x1 - x2) % P
    y3 = (slope * (x1 - x3) - y1) % P
    return x3, y3


def multiply(scalar, point):
    result = INFINITY
    while scalar:
        if scalar & 1:
            result = add(result, point)
        point = add(point, point)
        scalar >>= 1
    return result


def baby_step_giant_step(generator, target, order):
    step = isqrt(order) + 1
    table = {}
    current = INFINITY
    for index in range(step):
        table.setdefault(current, index)
        current = add(current, generator)

    giant_step = multiply(step, negate(generator))
    current = target
    for index in range(step + 1):
        if current in table:
            candidate = (table[current] + index * step) % order
            if multiply(candidate, generator) == target:
                return candidate
        current = add(current, giant_step)

    raise ValueError("discrete logarithm not found")


def recover_private_key():
    group_order = P + 1
    residues = []
    moduli = []

    for prime, exponent in factorint(group_order).items():
        modulus = prime**exponent
        subgroup_generator = multiply(group_order // modulus, G)
        subgroup_target = multiply(group_order // modulus, Q)
        residues.append(
            baby_step_giant_step(subgroup_generator, subgroup_target, modulus)
        )
        moduli.append(modulus)

    private_key = int(crt(moduli, residues)[0])
    assert multiply(private_key, G) == Q
    return private_key


if __name__ == "__main__":
    print(recover_private_key())
