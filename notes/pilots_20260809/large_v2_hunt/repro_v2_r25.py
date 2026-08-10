#!/usr/bin/env python3
"""STANDALONE reproduction - round 25, large-v_2 window hunt.  No imports from
the pilot's libraries.  Certifies a NON-CYCLOTOMIC TERNARY FOLDED KERNEL
VECTOR at (p, N' = 128) with v_2(p-1) = 26.

The norm is recomputed by the Bareiss determinant of the multiplication
matrix of w in Z[x]/(x^64+1) -- an algorithm INDEPENDENT of the 2-adic tower
recursion that found it.  Prints PASS/FAIL from the literal constants.
"""
W = [2, -2, 2, 2, 2, 2, -1, -2, 2, -2, 2, -2, -2, -1, -2, -2, -2, 2, -2, 2, -2, 2, 2, 2, -2, 2, 2, 2, 2, 2, -2, -2, -2, -1, 2, -2, -2, 2, -2, 2, -2, 2, 2, -2, 2, -2, -2, 2, -2, 2, -2, 2, 2, -2, 2, -2, -2, 2, 2, -2, 2, 2, -2, 2]
P = 744663885017004399638520270460823057367868278950838095881175041
RHO = 242432094911838712720865362272648362300367810894981811276182572
S = 99
V2 = 26


def mr(n, a):
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    x = pow(a, d, n)
    if x in (1, n - 1):
        return True
    for _ in range(s - 1):
        x = x * x % n
        if x == n - 1:
            return True
    return False


def jacobi(a, n):
    a %= n
    r = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                r = -r
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            r = -r
        a %= n
    return r if n == 1 else 0


def lucas(n):
    D = 5
    while jacobi(D, n) != -1:
        D = -(D + 2) if D > 0 else -(D - 2)
    Pp, Q = 1, (1 - D) // 4
    d, s = n + 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    U, V, Qk = 1, Pp % n, Q % n
    for b in bin(d)[3:]:
        U, V = U * V % n, (V * V - 2 * Qk) % n
        Qk = Qk * Qk % n
        if b == "1":
            U, V = (Pp * U + V), (D * U + Pp * V)
            if U % 2:
                U += n
            if V % 2:
                V += n
            U, V = (U >> 1) % n, (V >> 1) % n
            Qk = Qk * Q % n
    if U == 0 or V == 0:
        return True
    for _ in range(s - 1):
        V = (V * V - 2 * Qk) % n
        if V == 0:
            return True
        Qk = Qk * Qk % n
    return False


def norm_bareiss(w):
    """det of the matrix of multiplication by w on Z[x]/(x^h+1), exactly."""
    h = len(w)
    M = [[0] * h for _ in range(h)]
    for j in range(h):
        for i in range(h):
            t = i + j
            M[t % h][j] = w[i] if t < h else -w[i]
    sign, prev = 1, 1
    for k in range(h - 1):
        if M[k][k] == 0:
            for r in range(k + 1, h):
                if M[r][k]:
                    M[k], M[r] = M[r], M[k]
                    sign = -sign
                    break
            else:
                return 0
        for i in range(k + 1, h):
            for j in range(k + 1, h):
                M[i][j] = (M[i][j] * M[k][k] - M[i][k] * M[k][j]) // prev
        prev = M[k][k]
    return sign * M[h - 1][h - 1]


def v2(n):
    return (n & -n).bit_length() - 1


ok = True


def chk(name, cond):
    global ok
    ok = ok and bool(cond)
    print("%-46s %s" % (name, "PASS" if cond else "FAIL"))


chk("w nonzero and inside the box {-2..2}^64",
    any(t != 0 for t in W) and len(W) == 64 and all(-2 <= t <= 2 for t in W))
chk("||w||_1 = %d  (<= 2l' = 130)" % sum(abs(t) for t in W),
    sum(abs(t) for t in W) <= 130)
chk("p is a BPSW + 64-MR probable prime",
    mr(P, 2) and lucas(P) and all(mr(P, a) for a in range(3, 131, 2)))
chk("p = 1 mod 128 (an N'=128 quotient exists)", P % 128 == 1)
chk("v_2(p-1) = %d" % V2, v2(P - 1) == V2)
chk("2^128 < p <= 253^32 (admissible window)", 2 ** 128 < P <= 253 ** 32)
NN = abs(norm_bareiss(W))
chk("independent Norm(w) has %d bits" % NN.bit_length(), NN.bit_length() > 0)
chk("p | Norm(w),  cofactor = %d" % (NN // P if NN % P == 0 else -1),
    NN % P == 0)
chk("rho has exact order 128 mod p", pow(RHO, 64, P) == P - 1)
acc = sum(W[i] * pow(RHO, S * i, P) for i in range(64)) % P
chk("sum_i w_i rho^(%d i) = 0 mod p  (KERNEL MEMBERSHIP)" % S, acc == 0)
chk("s is odd (non-cyclotomic: the vector is not antipodal)", S % 2 == 1)
print("\nOVERALL: %s" % ("PASS" if ok else "FAIL"))
