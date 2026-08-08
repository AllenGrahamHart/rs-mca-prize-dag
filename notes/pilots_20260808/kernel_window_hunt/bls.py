#!/usr/bin/env python3
"""Brillhart-Lehmer-Selfridge n-1 primality PROOF (BLS75 Thm 5, cube-root form)
with fail-closed controls.  Upgrades a witness prime from PROBABLE to PROVEN."""
import glob
import json
import random
import sys
from math import gcd, isqrt
sys.path.insert(0, "notes/pilots_20260808/kernel_window_hunt")
import klib as K
from hunt import verify_hit

TD = [q for q in K.SMALL_PRIMES if q < 10 ** 5]


def factor_part(n, primes=TD):
    """(F, R, {q: e}) with F the fully-removed part over `primes`, R = n/F."""
    m, F, fac = n, 1, {}
    for q in primes:
        if m % q == 0:
            e = 0
            while m % q == 0:
                m //= q
                e += 1
            fac[q] = e
            F *= q ** e
    return F, m, fac


def bls_prove(n, extra_primes=()):
    """Return (True, cert) if BLS Thm 5 PROVES n prime; (False, reason) else.

    n-1 = F*R, F completely factored, gcd(F,R)=1, F > n^(1/3);
    for each prime q | F an a_q with a_q^(n-1) = 1 mod n and
    gcd(a_q^((n-1)/q) - 1, n) = 1;  R = 2*F*s + r, 0 <= r < 2F;
    then n is prime iff s == 0 or r^2 - 8s is not a perfect square.
    """
    if n < 3 or n % 2 == 0:
        return False, "n even or too small"
    F, R, fac = factor_part(n - 1, list(TD) + list(extra_primes))
    if gcd(F, R) != 1:
        return False, "gcd(F,R) != 1"
    if F ** 3 <= n:
        return False, "F = 2^%d is not > n^(1/3)" % (F.bit_length() - 1)
    bases = {}
    for q in fac:
        found = None
        for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47):
            if pow(a, n - 1, n) != 1:
                return False, "a^(n-1) != 1 for a=%d (n is composite)" % a
            if gcd(pow(a, (n - 1) // q, n) - 1, n) == 1:
                found = a
                break
        if found is None:
            return False, "no base for q=%d" % q
        bases[q] = found
    s, r = divmod(R, 2 * F)
    if s == 0:
        return True, {"F": F, "R": R, "fac": fac, "bases": bases, "s": s, "r": r,
                      "branch": "s == 0"}
    d = r * r - 8 * s
    if d >= 0 and isqrt(d) ** 2 == d:
        return False, "r^2-8s = %d is a perfect square (inconclusive)" % d
    return True, {"F": F, "R": R, "fac": fac, "bases": bases, "s": s, "r": r,
                  "branch": "r^2-8s not a square"}


# ------------------------------------------------------- fail-closed controls
def controls():
    rng = random.Random(20260808)
    bad = 0
    proved = 0
    checked = 0
    for _ in range(4000):
        n = rng.randrange(3, 10 ** 7) | 1
        ok, _c = bls_prove(n)
        truth = K.is_probable_prime(n)          # exact below 3.2e18
        checked += 1
        if ok:
            proved += 1
            if not truth:
                bad += 1
    print("CONTROL: %d odd n tested, BLS proved %d, FALSE CERTIFICATES: %d"
          % (checked, proved, bad))
    # a hostile control: Carmichael numbers and strong pseudoprimes
    for c in (561, 1105, 1729, 2465, 2821, 6601, 8911, 41041, 62745, 825265,
              3215031751, 2152302898747):
        ok, _c = bls_prove(c)
        if ok:
            print("FALSE CERTIFICATE on %d" % c)
            bad += 1
    # repo-banked proven prime must certify
    P250 = 904625697166646869347790708689937759412227977745095982970820953353127723009
    ok, cert = bls_prove(P250)
    print("CONTROL: repo Pocklington exhibit prime certified by BLS: %s (%s)"
          % (ok, cert["branch"] if ok else cert))
    return bad == 0 and ok


if __name__ == "__main__":
    assert controls(), "BLS CONTROLS FAILED"
    print()
    best = None
    for f in sorted(glob.glob(
            "notes/pilots_20260808/kernel_window_hunt/state/proofhunt_*.json")):
        st = json.load(open(f))
        if st.get("rec") and (best is None or st["rec"]["frac"] > best["frac"]):
            best = st["rec"]
    p = int(best["p"])
    print("candidate: %d bits, PM1FRAC %.4f" % (p.bit_length(), best["frac"]))
    ok, cert = bls_prove(p)
    print("BLS VERDICT:", "PROVEN PRIME" if ok else "not proven: %s" % cert)
    if ok:
        print("  F = 2^%.1f, F^3/n = 2^%.1f, branch = %s, #primes in F = %d"
              % (cert["F"].bit_length() - 1,
                 (cert["F"] ** 3 // p).bit_length() - 1,
                 cert["branch"], len(cert["fac"])))
        rep = verify_hit(best["w"], p, 128)
        print("  witness verification ok =", rep["ok"], " l1 =", rep["l1"],
              " cof =", rep["cofactor"], " v2(p-1) =", rep["v2_p_minus_1"],
              " km s =", rep["kernel_membership"][1])
        json.dump({"w": best["w"], "p": best["p"],
                   "bls": {"F": str(cert["F"]), "R": str(cert["R"]),
                           "fac": {str(k): v for k, v in cert["fac"].items()},
                           "bases": {str(k): v for k, v in cert["bases"].items()},
                           "s": str(cert["s"]), "r": str(cert["r"]),
                           "branch": cert["branch"]}},
                  open("notes/pilots_20260808/kernel_window_hunt/state/"
                       "best_witness_proven.json", "w"))
        print("  written to state/best_witness_proven.json")
