"""P2 / P3 / P4 / P5 for the (1,5) sharpest-leaf pilot.

For a deterministic random sample of reduced signed weight-5 words at ell=1:
  * exact cyclotomic norm N = Res(X^256+1, P)  (verified engine, control C-c)
  * complete factorization of N (per-class wall guard)
  * P2: constructively verify every prime factor p supports a relation, i.e.
        gcd(P mod p, X^256+1 mod p) has positive degree  ->  a root of exact
        order 512 in F_p-bar annihilating P
  * P5: record v_2(p-1) and bit length of every prime factor
  * P3/P4: distinct-prime yield and wall time per class, for extrapolation

Usage:
  tools/ramguard local -- python3 .../sample_norms.py SEED NCLASSES TIMEOUT_S OUT.json
"""

import json
import random
import signal
import sys
import time

sys.setrecursionlimit(10000)

D = 256          # X^D + 1, root of exact order 512
NBITS_CAP = 256  # official cap q < 2^256
V2_GATE = 41     # official gate v_2(q-1) >= 41


# ------------------------------------------------------------------ norm
def norm_neg(coeffs, d):
    a = list(coeffs)
    while d > 1:
        b = [(-c if (i & 1) else c) for i, c in enumerate(a)]
        prod = [0] * (2 * d - 1)
        for i, ai in enumerate(a):
            if ai:
                for j, bj in enumerate(b):
                    if bj:
                        prod[i + j] += ai * bj
        for i in range(2 * d - 2, d - 1, -1):
            if prod[i]:
                prod[i - d] -= prod[i]
                prod[i] = 0
        a = [prod[2 * i] for i in range(d // 2)]
        d //= 2
    return a[0]


# ------------------------------------------------------------- poly gcd mod p
def poly_trim(a):
    while a and a[-1] == 0:
        a.pop()
    return a


def poly_gcd_mod(a, b, p):
    a = poly_trim([x % p for x in a])
    b = poly_trim([x % p for x in b])
    while b:
        inv = pow(b[-1], p - 2, p)
        db = len(b) - 1
        while len(a) - 1 >= db and a:
            shift = len(a) - 1 - db
            f = (a[-1] * inv) % p
            if f:
                for i, bi in enumerate(b):
                    a[i + shift] = (a[i + shift] - f * bi) % p
            a = poly_trim(a)
            if not a:
                break
        a, b = b, a
    return a


def v2(n):
    n = abs(n)
    k = 0
    while n and n % 2 == 0:
        n //= 2
        k += 1
    return k


# ------------------------------------------------------------------ factoring
SMALL_PRIMES = None


def small_primes(limit=200000):
    global SMALL_PRIMES
    if SMALL_PRIMES is None:
        sieve = bytearray([1]) * limit
        sieve[0] = sieve[1] = 0
        for i in range(2, int(limit ** 0.5) + 1):
            if sieve[i]:
                sieve[i * i:limit:i] = bytearray(len(range(i * i, limit, i)))
        SMALL_PRIMES = [i for i in range(limit) if sieve[i]]
    return SMALL_PRIMES


class Timeout(Exception):
    pass


def _alarm(sig, frm):
    raise Timeout()


def factor_full(n, budget_s):
    """Return (factors dict, complete_bool)."""
    from sympy import factorint, isprime
    fac = {}
    n = abs(n)
    for p in small_primes():
        if p * p > n:
            break
        while n % p == 0:
            fac[p] = fac.get(p, 0) + 1
            n //= p
    if n == 1:
        return fac, True
    if isprime(n):
        fac[n] = fac.get(n, 0) + 1
        return fac, True
    signal.signal(signal.SIGALRM, _alarm)
    signal.alarm(int(budget_s))
    try:
        rest = factorint(n)
        signal.alarm(0)
        for p, e in rest.items():
            fac[p] = fac.get(p, 0) + e
        return fac, True
    except Timeout:
        fac[("COMPOSITE", n.bit_length())] = 1
        return fac, False
    except Exception:
        signal.alarm(0)
        fac[("ERROR", n.bit_length())] = 1
        return fac, False


# ------------------------------------------------------------------ sampling
def random_word(rng):
    """Reduced signed weight-5 word: 5 distinct exponents in [0,256), signs,
    modulo global sign (first sign pinned to +1)."""
    exps = sorted(rng.sample(range(D), 5))
    signs = [1] + [rng.choice((1, -1)) for _ in range(4)]
    return list(zip(signs, exps))


def word_coeffs(word):
    c = [0] * D
    for s, e in word:
        c[e] += s
    return c


def main():
    seed = int(sys.argv[1])
    nclasses = int(sys.argv[2])
    budget = float(sys.argv[3])
    out = sys.argv[4]

    rng = random.Random(seed)
    rows = []
    all_primes = {}
    t_start = time.time()

    for idx in range(nclasses):
        word = random_word(rng)
        c = word_coeffs(word)
        t0 = time.time()
        N = norm_neg(c, D)
        t_norm = time.time() - t0
        t1 = time.time()
        fac, complete = factor_full(N, budget)
        t_fac = time.time() - t1

        prime_recs = []
        p2_ok = True
        for p, e in fac.items():
            if isinstance(p, tuple):
                prime_recs.append({"kind": p[0], "bits": p[1], "exp": e})
                p2_ok = False
                continue
            if p == 2:
                prime_recs.append({"p_bits": 1, "v2": None, "note": "p=2"})
                continue
            # P2: constructive support check
            cyc = [0] * (D + 1)
            cyc[0] = 1
            cyc[D] = 1
            g = poly_gcd_mod(list(c), cyc, p)
            deg = len(g) - 1 if g else -1
            ok = deg >= 1
            p2_ok &= ok
            vv = v2(p - 1)
            prime_recs.append({
                "p_bits": p.bit_length(), "v2": vv, "exp": e,
                "gcd_deg": deg, "p2_ok": ok,
                "official_range": p.bit_length() <= NBITS_CAP,
                "ELIGIBLE": (p.bit_length() <= NBITS_CAP and vv >= V2_GATE),
            })
            all_primes[p] = max(all_primes.get(p, 0), vv)

        rows.append({
            "idx": idx,
            "word": [[int(s), int(e)] for s, e in word],
            "norm_bits": abs(N).bit_length(),
            "complete": complete,
            "n_distinct_primes": sum(1 for r in prime_recs if "p_bits" in r),
            "t_norm": round(t_norm, 4),
            "t_fac": round(t_fac, 4),
            "p2_ok": p2_ok,
            "primes": prime_recs,
        })
        print(f"[{idx+1}/{nclasses}] bits={abs(N).bit_length():>4} "
              f"complete={complete} nfac={len(fac)} "
              f"t_norm={t_norm:.2f}s t_fac={t_fac:.2f}s "
              f"maxv2={max([r.get('v2') or 0 for r in prime_recs] + [0])}",
              flush=True)

    elapsed = time.time() - t_start
    maxv2 = max(all_primes.values()) if all_primes else 0
    eligible = [p for p, v in all_primes.items()
                if v >= V2_GATE and p.bit_length() <= NBITS_CAP]
    summary = {
        "seed": seed, "nclasses": nclasses, "budget_s": budget,
        "elapsed_s": round(elapsed, 2),
        "classes_complete": sum(1 for r in rows if r["complete"]),
        "p2_all_ok": all(r["p2_ok"] for r in rows if r["complete"]),
        "distinct_primes_total": len(all_primes),
        "sum_log2_distinct_primes": sum(p.bit_length() for p in all_primes),
        "max_v2": maxv2,
        "ELIGIBLE_PRIMES": [str(p) for p in eligible],
        "mean_norm_bits": round(sum(r["norm_bits"] for r in rows) / len(rows), 1),
        "mean_t_total": round(sum(r["t_norm"] + r["t_fac"] for r in rows) / len(rows), 3),
        "median_t_total": round(sorted(r["t_norm"] + r["t_fac"] for r in rows)[len(rows) // 2], 3),
    }
    json.dump({"summary": summary, "rows": rows}, open(out, "w"), indent=1)
    print()
    print(json.dumps(summary, indent=1))


if __name__ == "__main__":
    main()
