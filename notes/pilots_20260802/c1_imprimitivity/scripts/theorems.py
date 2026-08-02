#!/usr/bin/env python3
r"""Verification harness for the new statements proved in this pilot, with proofs.

NOTATION.  N = 2M a power of two, R_N = Z[x]/(x^N+1) = Z[zeta], zeta = zeta_2N,
x^N+1 = Phi_2N irreducible.  f ternary of weight w.  Norm(f) = Res(f, x^N+1)
= prod_{j odd mod 2N} f(zeta^j) >= 0.  f* = f(x^-1).  Every f splits uniquely as
f(x) = p(x^2) + x q(x^2) with p, q in R_M ternary, w = w(p) + w(q), and the
field-norm descent gives  Norm_N(f) = Norm_M(p^2 - y q^2)  (y = x^2).
IMPRIMITIVE means supp(f) lies in one coset of 2Z/N, i.e. f = (unit) . iota(g).

-------------------------------------------------------------------------------
T1  LEMMA C  (even-part domination -- "odd autocorrelation mass only hurts").

    For every ternary f in R_N,   Norm_N(f) <= Norm_M(p p* + q q*),
    and p p* + q q* is exactly the EVEN PART of the negacyclic autocorrelation
    A_f = f f* of f, read as an element of R_M.

    Proof.  A_f = f f* = (p p* + q q*)(x^2) + x^-1 (p q*)(x^2) + x (q p*)(x^2),
    so the even part of A_f is iota(p p* + q q*), which is the first claim.
    For the inequality, Norm_N(f) = Norm_M(p^2 - y q^2)
      = |prod_{j odd mod 2M} (p(eta^j)^2 - eta^j q(eta^j)^2)|
      <= prod_j (|p(eta^j)|^2 + |q(eta^j)|^2)          (triangle ineq., |eta^j|=1)
      =  prod_j (p p* + q q*)(eta^j)  =  Norm_M(p p* + q q*).
    Equality iff for every j the complex numbers p(eta^j)^2 and -eta^j q(eta^j)^2
    are non-negative real multiples of one another; in particular equality holds
    whenever q = 0 or p = 0.                                                 QED
    STATUS: proved; verified exhaustively over all 3^8-1 nonzero ternary f at
    N = 8 (0 violations, 672 equalities) and on 3000 random f at N = 16.
    INSUFFICIENT for the imprimitivity conjecture: at M = 8 take p = 1 + y,
    q = 1 + y^7.  Then p p* + q q* = 4 (constant), so the bound is 4^8 = 65536,
    which EXCEEDS maxnorm(8,4)^2 = 196^2 = 38416.  So attack (b) via Lemma C
    alone cannot close even the first non-trivial case.

-------------------------------------------------------------------------------
T2  ROTATION IDENTITY.  For p, q in R_M and 0 <= c < M put
        f_c(x) = p(x^2) + x^(2c+1) q(x^2)  in R_N.
    Each f_c is ternary of the same weight w(p)+w(q) (the even slots carry p,
    the odd slots carry a rotation of q, so no collision ever occurs), and

        prod_{c=0}^{M-1} Norm_N(f_c)  =  Norm_M( p^(2M) + q^(2M) ).

    Proof.  Norm_N(f_c) = Norm_M(p^2 - y^(2c+1) q^2)
                        = prod_{j odd mod 2M} (A_j - eta^{j(2c+1)} B_j),
    with A_j = p(eta^j)^2, B_j = q(eta^j)^2.  Fix j.  j is invertible mod 2M and
    2c+1 runs over all odd residues mod 2M as c runs over 0..M-1, so the
    exponents j(2c+1) run over all odd residues mod 2M exactly once; hence
    {eta^{j(2c+1)}} is exactly the root set of z^M + 1, and
        prod_{z^M = -1} (A - zB) = B^M prod_{z^M=-1}(A/B - z) = A^M + B^M.
    Multiply over j.                                                          QED
    STATUS: proved; verified on 120 random (p,q) at M = 4 and M = 8, 0 failures.
    USE: gives max_c Norm_N(f_c) >= Norm_M(p^2M + q^2M)^(1/M), a constructive
    lower bound, and a new large-move class for the counterexample hunter.
    With q = 0 it degenerates to Norm_M(p)^{2M}, consistent with Lemma A.

-------------------------------------------------------------------------------
T3  NO FLAT TERNARY AT WEIGHT A POWER OF FOUR.
    Let w = 4^t, t >= 1.  Then NO ternary f of weight w in ANY R_N (N a power of
    two) satisfies Norm(f) = w^(N/2).  Consequently maxnorm(N,w) < w^(N/2)
    strictly at every level, and c_w < w^2 strictly; w = 4, 16, 64, ... are
    permanently non-saturating.

    Proof.  Norm(f) = w^(N/2) forces equality in AM-GM, i.e. |f(zeta^j)|^2 = w
    for all odd j, i.e. f f* = w in Z[zeta_2N].  Write w = 2^(2t).  The prime 2
    is totally ramified: (2) = (lambda)^N with lambda = 1 - zeta_2N and
    N(lambda) = Phi_2N(1) = 2, and (lambda) is the UNIQUE prime above 2, hence
    fixed by complex conjugation.  From (f)(f*) = (2)^(2t) = (lambda)^(2tN) we
    get (f) = (lambda)^a with 2a = 2tN, so a = tN and (f) = (lambda)^(tN)
    = (2^t).  Thus f = 2^t u with u a unit; all conjugates of u have modulus
    sqrt(w)/2^t = 1, so by Kronecker's theorem u is a root of unity, u = +-
    zeta^k, i.e. f = +- 2^t x^k in R_N.  Its coefficients are not in {-1,0,1}
    since 2^t >= 2 -- contradiction.                                          QED
    (The argument does NOT extend to w = 2^s with s odd, nor to odd squares:
    there the relevant primes need not be conjugation-stable.)

-------------------------------------------------------------------------------
T4  PARITY.  Norm(f) = w (mod 2) for every ternary f of weight w.
    Proof.  lc(f) = +-1, so reduction mod 2 does not drop degrees and
    Norm(f) = Res(x^N+1, f) = prod over roots of x^N+1 of f.  Mod 2,
    x^N + 1 = (x+1)^N, so Norm(f) = f(-1)^N = f(1)^N = (sum d_i)^N = w^N = w
    (mod 2).                                                                  QED

-------------------------------------------------------------------------------
T5  IMPRIMITIVE => PERFECT SQUARE (arithmetic primitivity certificate).
    If f is imprimitive, f = (unit) . iota(g), then Norm_N(f) = Norm_M(g)^2 is a
    perfect square, and v_2(Norm_N(f)) = 2 v_2(Norm_M(g)) is even.
    CONTRAPOSITIVE: if maxnorm(N,w) is NOT a perfect square then EVERY
    norm-maximising ternary f of weight w is primitive, and the doubling law
    maxnorm(N,w) = maxnorm(N/2,w)^2 FAILS at (N,w) -- proved from the value
    alone, without knowing anything about level N/2.
    Applied to the exhaustive tables this certifies the break arithmetically:
      2N = 8   w = 4 : 8 = 2^3, v_2 odd            -> argmax primitive, law fails
      2N = 16  w = 8 : 2176 = 2^7 . 17, v_2 odd    -> argmax primitive
               w = 6 : 1154 = 2 . 577, v_2 odd     -> argmax primitive
      2N = 32  w = 8 : 14760962 = 2 . 7380481      -> argmax primitive, law fails
               w = 10, 12, 14, 15, 16 likewise non-squares
    and every maxnorm computed in the conjecture's range w <= N/2 - 1, at every
    level up to 2N = 128, IS a perfect square -- as the conjecture requires.
"""
from __future__ import annotations
import json, os, random, sys
from itertools import product as iproduct
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, "/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260802/c1_norm_ladder/scripts")
from norm_core import norm_descent_py, norm_bareiss
from proof_probe import rmul, rstar, radd, rpow, split_eo

def isqrt_exact(n):
    r = int(n ** 0.5)
    for c in (r-2, r-1, r, r+1, r+2):
        if c >= 0 and c*c == n: return c
    return None

TABLES = {
 32: {1:1,2:256,3:6561,4:38416,5:279841,6:1331716,7:5764801,8:14760962,
      9:38950081,10:84580802,11:184497889,12:342386306,13:777684769,
      14:1040410946,15:1612931233,16:2311094272},
 16: {1:1,2:16,3:81,4:196,5:529,6:1154,7:2401,8:2176},
 8:  {1:1,2:4,3:9,4:8},
 64: {1:1,2:65536,3:43046721,4:1475789056,5:78310985281,6:1773467504656,
      7:33232930569601,8:217885999165444,9:1517108809906561},
 128:{2:4294967296,3:1853020188851841,4:2177953337809371136,
      5:6132610415680998648961,6:3145186990070779381678336},
}

def main():
    rng = random.Random(7)
    out = {}

    # ---- T4 parity, exhaustive N=8 and random N=16,32 -----------------------
    bad = 0; n = 0
    for d in iproduct((-1,0,1), repeat=8):
        if not any(d): continue
        w = sum(1 for c in d if c); n += 1
        if norm_descent_py(list(d)) % 2 != w % 2: bad += 1
    r = {"exhaustive_N8": {"tested": n, "violations": bad}}
    for N in (16, 32):
        b = 0
        for _ in range(400):
            d = [0]*N; w = rng.randint(1, N)
            for i in rng.sample(range(N), w): d[i] = rng.choice((-1,1))
            if norm_descent_py(d) % 2 != w % 2: b += 1
        r["random_N%d" % N] = {"tested": 400, "violations": b}
    out["T4_parity_Norm_congruent_w_mod_2"] = r

    # ---- T5 imprimitive => perfect square, and the certified-primitive table -
    b = 0; n = 0
    for _ in range(600):
        M = rng.choice((4, 8, 16)); N = 2*M
        g = [0]*M; w = rng.randint(1, M)
        for i in rng.sample(range(M), w): g[i] = rng.choice((-1,1))
        f = [0]*N
        for k in range(M): f[2*k] = g[k]
        v = norm_descent_py(f); n += 1
        if isqrt_exact(v) is None or v != norm_descent_py(g)**2: b += 1
    cert = {}
    for twoN, tab in sorted(TABLES.items()):
        N = twoN // 2
        row = {}
        for w, v in tab.items():
            s = isqrt_exact(v)
            row[str(w)] = {"maxnorm": str(v), "is_perfect_square": s is not None,
                           "v2": (v & -v).bit_length()-1,
                           "argmax_CERTIFIED_PRIMITIVE_by_nonsquare": s is None,
                           "w_vs_half_ring_N/2": "%d vs %d" % (w, N//2)}
        cert["2N=%d" % twoN] = row
    out["T5_imprimitive_implies_square"] = {
        "random_imprimitive_tested": n, "violations": b,
        "certificate_table": cert}

    # ---- T3 no flat ternary at w = 4 (consistency with the tables) ----------
    t3 = {}
    for twoN, tab in sorted(TABLES.items()):
        N = twoN//2
        if 4 in tab:
            t3["N=%d" % N] = {"maxnorm(N,4)": str(tab[4]), "ceiling_4^(N/2)": str(4**(N//2)),
                              "strictly_below_ceiling": tab[4] < 4**(N//2)}
    out["T3_no_flat_weight_4"] = t3

    # ---- T1/T2 re-run summary (details in proof_probe.json) -----------------
    p = json.load(open(os.path.join(os.path.dirname(HERE), "results", "proof_probe.json")))
    out["T1_lemmaC"] = {k: p[k] for k in ("lemmaC_exhaustive_N8", "lemmaC_random_N16",
                                          "lemmaC_insufficiency_witness")}
    out["T2_rotation_identity"] = p["rotation_identity"]
    print(json.dumps(out, indent=1))

if __name__ == "__main__":
    main()
