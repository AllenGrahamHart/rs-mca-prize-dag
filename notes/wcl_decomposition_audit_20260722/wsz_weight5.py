#!/usr/bin/env python3
"""Shared exact helpers for the WCL weight-five and powered-screen audits.

The screen records primality as probable primality.  Norm computations are
exact integer resultants against a power-of-two cyclotomic polynomial.
"""

from math import isqrt


_MR_BASES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43)


def is_probable_prime(n):
    """Return whether ``n`` is a strong probable prime to the fixed bases."""
    if n < 2:
        return False
    for p in _MR_BASES:
        if n % p == 0:
            return n == p
    limit = isqrt(n)
    if limit * limit == n:
        return False

    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in _MR_BASES:
        if a >= n:
            continue
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def _schoolbook_mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                if y:
                    out[i + j] += x * y
    return out


def _max_bits(values):
    return max((abs(value).bit_length() for value in values), default=0)


def _packed_mul(a, b):
    """Exact dense convolution via balanced Kronecker substitution."""
    la, lb = len(a), len(b)
    ba, bb = _max_bits(a), _max_bits(b)
    if ba == 0 or bb == 0:
        return [0] * (la + lb - 1)

    digit_bits = ba + bb + min(la, lb).bit_length() + 2
    digit_bytes = (digit_bits + 7) // 8
    digit_bits = 8 * digit_bytes
    half = 1 << (digit_bits - 1)

    def pack(values):
        positive = bytearray(digit_bytes * len(values))
        negative = bytearray(digit_bytes * len(values))
        for i, value in enumerate(values):
            start = i * digit_bytes
            end = start + digit_bytes
            if value > 0:
                positive[start:end] = value.to_bytes(digit_bytes, "little")
            elif value < 0:
                negative[start:end] = (-value).to_bytes(
                    digit_bytes, "little")
        return int.from_bytes(positive, "little") - int.from_bytes(
            negative, "little")

    count = la + lb - 1
    offset = int.from_bytes(
        half.to_bytes(digit_bytes, "little") * count, "little")
    product = pack(a) * pack(b) + offset
    assert product >= 0
    raw = product.to_bytes(digit_bytes * count + 8, "little")
    assert raw[digit_bytes * count:] == b"\x00" * 8
    return [
        int.from_bytes(raw[i * digit_bytes:(i + 1) * digit_bytes], "little")
        - half
        for i in range(count)
    ]


def _norm_rec(coefficients, multiply):
    current = list(coefficients)
    width = len(current)
    if width == 0 or width & (width - 1):
        raise ValueError("coefficient length must be a positive power of two")
    while width > 1:
        next_width = width // 2
        even = current[0::2]
        odd = current[1::2]
        even_square = multiply(even, even)
        odd_square = multiply(odd, odd)
        paired = [0] * width
        for i, value in enumerate(even_square):
            paired[i] += value
        for i, value in enumerate(odd_square):
            paired[i + 1] -= value
        current = [
            paired[i] - paired[i + next_width]
            for i in range(next_width)
        ]
        width = next_width
    return current[0]


def norm_rec(coefficients):
    """Independent schoolbook resultant used by ``wscr_screens selfcheck``."""
    return _norm_rec(coefficients, _schoolbook_mul)


def norm_of_set(exponents, order):
    """Return ``|Res(X^(order/2)+1, sum(X^e))|`` with signs reduced."""
    if order < 2 or order & (order - 1):
        raise ValueError("order must be a power of two")
    half = order // 2
    coefficients = [0] * half
    for exponent in exponents:
        exponent %= order
        if exponent >= half:
            coefficients[exponent - half] -= 1
        else:
            coefficients[exponent] += 1
    return abs(_norm_rec(coefficients, _packed_mul))
