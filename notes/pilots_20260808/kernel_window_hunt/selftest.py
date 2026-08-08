#!/usr/bin/env python3
"""Self-tests for klib.  Every check is against an INDEPENDENT source:
banked repo constants, closed-form norms, or a sieve."""
import sys
import time
import random
sys.path.insert(0, "notes/pilots_20260808/kernel_window_hunt")
import klib as K

FAIL = []


def ck(name, cond, extra=""):
    print(("PASS " if cond else "FAIL ") + name + ("  " + extra if extra else ""))
    if not cond:
        FAIL.append(name)


# --- T1  closed form Norm(a + b x) = a^h + b^h  (h even)
ok = True
for h in (4, 8, 16, 64):
    for a, b in ((2, 1), (1, 1), (1, 2), (2, -1), (-2, 1)):
        w = [0] * h
        w[0] = a
        w[1] = b
        if K.tower_norm(w) != a ** h + b ** h:
            ok = False
ck("T1 tower_norm matches a^h+b^h", ok)

# --- T2  banked SCOPE CATCH witness: h=8, w=(-1,-1,-2,-1,2,2,1,-1), Norm=12289
w = [-1, -1, -2, -1, 2, 2, 1, -1]
n = K.tower_norm(w)
ck("T2 banked h=8 witness Norm == 12289", abs(n) == 12289, "Norm=%d" % n)
km = K.kernel_membership(w, 12289, 16)
ck("T2b kernel membership at p=12289, N'=16", km is not None, str(km))

# --- T3  2^64+1 = 274177 * 67280421310721, both = 1 mod 128
w = [0] * 64
w[0], w[1] = 2, 1
n = K.tower_norm(w)
ck("T3 Norm(2+x) at h=64 == 2^64+1", n == 2 ** 64 + 1)
r, fac = K.strip_small(n)
# SELF-CORRECTION: 274177 = 2^18.06 EXCEEDS B_TD = 2^17, so strip_small must
# leave 2^64+1 untouched.  The original assertion here was wrong, not the code.
ck("T3b strip_small leaves 2^64+1 whole (both factors > B_TD)",
   r == n and fac == {}, str(fac))
ck("T3c pollard_brent splits 2^64+1 into the two known primes",
   K.pollard_brent(n, 1 << 20, random.Random(1)) in (274177, 67280421310721))
ck("T3c2 67280421310721 is PRP", K.is_probable_prime(67280421310721, 20))
r = 67280421310721
ck("T3d both factors = 1 mod 128", 274177 % 128 == 1 and r % 128 == 1)
km = K.kernel_membership(w, 274177, 128)
ck("T3e kernel membership (2+x) at p=274177, N'=128", km is not None, str(km))
km = K.kernel_membership(w, 67280421310721, 128)
ck("T3f kernel membership (2+x) at p=67280421310721", km is not None, str(km))

# --- T4  primality vs a sieve up to 200000
sv = set(K._sieve(200000))
bad = [x for x in range(2, 200000) if K.is_probable_prime(x) != (x in sv)]
ck("T4 is_probable_prime == sieve below 200000", not bad, str(bad[:5]))

# --- T5  known 250-bit repo prime (e1_pocklington_250bit_exhibit_field)
P250 = 904625697166646869347790708689937759412227977745095982970820953353127723009
ck("T5 repo 250-bit exhibit prime is PRP", K.is_probable_prime(P250, 64))
ck("T5b = 1 mod 256, 250 bits, < 2^256",
   P250 % 256 == 1 and P250.bit_length() == 250 and P250 < 2 ** 256)
ck("T5c a composite of two 125-bit primes is rejected",
   not K.is_probable_prime((2 ** 127 - 1) * (2 ** 89 - 1)))
# Carmichael + strong pseudoprimes to base 2
for c in (2047, 3277, 29341, 41041, 62745, 1373653, 25326001, 3215031751):
    ck("T5d rejects pseudoprime %d" % c, not K.is_probable_prime(c))

# --- T6  strip_small correctness on random integers
rng = random.Random(7)
ok = True
for _ in range(200):
    m = rng.randrange(1, 10 ** 12)
    r, fac = K.strip_small(m)
    prod = r
    for p, e in fac.items():
        prod *= p ** e
    if prod != m:
        ok = False
    for p in fac:
        if p >= K.B_TD:
            ok = False
    if r > 1:
        for p in K.SMALL_PRIMES:
            if r % p == 0:
                ok = False
                break
ck("T6 strip_small is exact and leaves a B_TD-rough part", ok)

# --- T7  parity law: nodd odd => Norm odd; all even => 2^h | Norm
ok = True
for _ in range(60):
    w = K.fam_B(64, rng)
    if K.nodd(w) % 2 == 1 and abs(K.tower_norm(w)) % 2 == 0:
        ok = False
w2 = [rng.choice((-2, 2)) for _ in range(64)]
n2 = K.tower_norm(w2)
ok = ok and (n2 % (2 ** 64) == 0)
ck("T7 parity law (odd nodd -> odd norm; all-even -> 2^64 | norm)", ok)

# --- T8  AM-GM / PROVED ceiling respected
ok = True
worst = 0
for _ in range(200):
    w = K.fam_B(64, rng)
    n = abs(K.tower_norm(w))
    worst = max(worst, n)
    if n > K.sq(w) ** 32:
        ok = False
ck("T8 |Norm| <= S^32 on FAM-B samples", ok,
   "max sampled log2|Norm|=%.2f, ceiling log2(253^32)=%.4f"
   % (worst.bit_length() - 1 + 0.0, len(bin(K.CEIL253)) - 3))

# --- T9  timing
t = time.time()
NN = 300
for _ in range(NN):
    K.tower_norm(K.fam_B(64, rng))
dt = (time.time() - t) / NN
print("TIMING tower_norm h=64: %.3f ms/eval" % (dt * 1000))
t = time.time()
for _ in range(NN):
    K.strip_small(abs(K.tower_norm(K.fam_B(64, rng))))
dt2 = (time.time() - t) / NN
print("TIMING norm+strip_small h=64: %.3f ms/eval" % (dt2 * 1000))
t = time.time()
for _ in range(30):
    K.is_probable_prime(P250 + 2 * _, 0)
print("TIMING BPSW 250-bit: %.3f ms" % ((time.time() - t) / 30 * 1000))

print("SELFTEST %s (%d failures)" % ("PASS" if not FAIL else "FAIL", len(FAIL)))
