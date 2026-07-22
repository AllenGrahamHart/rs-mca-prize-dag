#!/usr/bin/env python3
"""wscr_screens.py -- goal item 6: powered falsifier-sampling screens.

Four pre-registered survival screens over the open WCL slot cells:
  screen15  (1,5) irreducible-core sample (400 orbits)
  screen27  (2,7) router-orbit sample (sharded; doubles as timing pilot)
  screen16  (1,6) uniform sample (256 supports)
  screen17  (1,7) uniform sample (128 supports)

Conventions (audited, notes/wcl_decomposition_audit_20260722/wcl_audit_findings.md):
cell (ell,w): reduced signed weight-w support = antipodal-free w-subset R of
Z_{512*ell} (r encodes s*omega^e, e = r mod 256*ell, s = +1 if r < 256*ell
else -1); omega EXACT order 512*ell; event iff P(omega^(2j-1)) = 0 for
j = 1..ell has its obstruction integer divisible by an OFFICIAL prime
(q < 2^256, v_2(q-1) >= 41).

ell=1 obstruction: Norm = Res(X^256+1, P) (or the descended-order norm for
coset-supported rows; identical prime support by the proved descent identity
Norm_512 = Norm_256^2).  ell=2 (router, mirrors the audited (2,6) cert +
wclp_b_sample_modal.py reference): selected quadruple {1,x,y,z} + complement
triple with product d=zeta^c; cleared cubic sigma_1=-u^2, theta_1=u*w,
e3=u^3*d, w=u*e2-e3-d; ten doublings; F=sigma_1024-3u^1024,
G=theta_1024-3u^2048; obstruction = gcd(Norm F, Norm G), Norm(u)-saturated,
PLUS (route (a), wclp finding #9) the u-shared part gcd(g0, Norm u).

CAUTION (banked catch): prime factors of norms are NOT all == 1 mod n; no
progression-based shortcuts anywhere.  Full factoring with a time cap;
probable-prime classification (labeled).  Powered tail: boosted p-1 stage 1
with exponent (order << 260) * smooth(B1) is a DIRECT detector of official-
admissible primes whose odd part of q-1 is B1-powersmooth, run on every
unresolved cofactor.

All runs: cd <repo> && tools/ramguard local -- python3 <this file> <cmd>
"""
import json
import os
import random
import sys
import time
from math import gcd, isqrt

sys.set_int_max_str_digits(0)

SCRATCH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRATCH)

from wsz_weight5 import is_probable_prime, norm_of_set, norm_rec  # noqa: E402

BASE_SEED = "wscr-20260722"
V2_GATE = 41
Q_BOUND = 1 << 256
B1 = 60_000

# ----------------------------------------------------------------------
# small primes
# ----------------------------------------------------------------------

_SP = []


def small_primes():
    global _SP
    if not _SP:
        limit = 1_000_000
        bs = bytearray([1]) * (limit + 1)
        bs[0:2] = b"\x00\x00"
        for i in range(2, isqrt(limit) + 1):
            if bs[i]:
                bs[i * i:: i] = b"\x00" * len(bs[i * i:: i])
        _SP = [i for i in range(limit + 1) if bs[i]]
    return _SP


_PM1_E = {}


def pm1_exponent(order):
    """E = (order << 260) * prod_{p <= B1} p^floor(log_p B1).
    A prime q divides gcd(base^E - 1, n) iff q-1 | E, i.e. iff the odd part
    of q-1 is B1-powersmooth AND v_2(q-1) <= 260 + v_2(order).  Since
    official primes have q < 2^256 (v_2(q-1) <= 255), the 2-part is FULLY
    covered: this is a direct detector of official-admissible primes with
    B1-powersmooth odd part."""
    if order not in _PM1_E:
        e = order << 260
        for p in small_primes():
            if p > B1:
                break
            pe = p
            while pe * p <= B1:
                pe *= p
            e *= pe
        _PM1_E[order] = e
    return _PM1_E[order]


def pm1_boosted(n, order):
    """Returns (factor_or_None, smooth_clear). smooth_clear=True certifies:
    NO prime q | n has q-1 | E (in particular no admissible prime with
    B1-powersmooth odd part)."""
    e = pm1_exponent(order)
    for base in (2, 3, 5, 7, 11):
        g = gcd(pow(base, e, n) - 1, n)
        if 1 < g < n:
            return g, False
        if g == 1:
            return None, True
        # g == n: all primes clumped; retry with next base
    return None, False


def brent_rho_timed(n, deadline, seed=1):
    if n % 2 == 0:
        return 2
    rng = random.Random(seed * 0x9E3779B97F4A7C15 + n % 0xFFFFFFFB)
    while time.monotonic() < deadline:
        y = rng.randrange(1, n)
        cc = rng.randrange(1, n)
        m = 256
        g = r = q = 1
        x = ys = y
        while g == 1:
            x = y
            for _ in range(r):
                y = (y * y + cc) % n
            k = 0
            while k < r and g == 1:
                ys = y
                for _ in range(min(m, r - k)):
                    y = (y * y + cc) % n
                    q = q * abs(x - y) % n
                g = gcd(q, n)
                k += m
                if time.monotonic() >= deadline and g == 1:
                    return None
            r *= 2
        if g == n:
            g = 1
            while g == 1:
                ys = (ys * ys + cc) % n
                g = gcd(abs(x - ys), n)
        if g != 1 and g != n:
            return g
    return None


def iroot(n, k):
    if n < 2:
        return n
    x = 1 << -((-n.bit_length()) // k)
    while True:
        y = ((k - 1) * x + n // pow(x, k - 1)) // k
        if y >= x:
            return x
        x = y


_PP_KS = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61)


def perfect_power(c):
    for k in _PP_KS:
        if (1 << k) > c:
            break
        r = iroot(c, k)
        if pow(r, k) == c:
            return r, k
    return None, None


def timed_factor_screen(N, order, deadline, rho_seed=1):
    """Split |N| into (probable-)prime factors within the wall deadline.
    Returns (factors {p: mult}, unresolved [(composite, smooth_clear)]).
    Every unresolved composite has been pm1-boost-checked (smooth_clear
    records the powered-detector verdict)."""
    N = abs(N)
    assert N != 0
    factors = {}
    unresolved = []
    while N % 2 == 0:
        factors[2] = factors.get(2, 0) + 1
        N //= 2
    for p in small_primes()[1:]:
        if p * p > N:
            break
        while N % p == 0:
            factors[p] = factors.get(p, 0) + 1
            N //= p
    if N == 1:
        return factors, unresolved
    stack = [N]
    while stack:
        c = stack.pop()
        if c == 1:
            continue
        if is_probable_prime(c):
            factors[c] = factors.get(c, 0) + 1
            continue
        r, k = perfect_power(c)
        if r is not None:
            stack.extend([r] * k)
            continue
        f, smooth_clear = pm1_boosted(c, order)
        if f is None and time.monotonic() < deadline:
            f = brent_rho_timed(c, deadline, rho_seed)
        if f is None:
            unresolved.append((c, smooth_clear))
            continue
        stack.append(f)
        stack.append(c // f)
    return factors, unresolved


def v2(q):
    t = q - 1
    return (t & -t).bit_length() - 1


def classify(factors, gate=V2_GATE, bound=Q_BOUND):
    """max v_2(q-1) over primes; list of admissible (alarm) primes."""
    maxv2 = 0
    alarms = []
    for q in factors:
        if q == 2:
            continue
        v = v2(q)
        maxv2 = max(maxv2, v)
        if v >= gate and q < bound:
            alarms.append(q)
    return maxv2, alarms


# ----------------------------------------------------------------------
# ell = 1 sampling machinery
# ----------------------------------------------------------------------

def draw_support(rng, w, half=256):
    """Uniform reduced signed support: w exponents in [0,half), anchor sign
    + on the smallest exponent (global-sign quotient), free signs on the
    rest.  Returned as antipodal-free w-subset of Z_{2*half}."""
    exps = sorted(rng.sample(range(half), w))
    R = [exps[0]]
    for e in exps[1:]:
        R.append(e if rng.random() < 0.5 else e + half)
    return sorted(R)


def is_symmetric(R, M=512):
    S = set(R)
    for c in range(M):
        if all((c - r) % M in S for r in R):
            return True
    return False


def in_coset4(R):
    return len({r & 3 for r in R}) == 1


def canon_ell1(R, M=512):
    """Orbit-invariant canonical form: descend while parity-uniform (proved
    coset-descent bijection), then min over affine maps sending an
    odd-difference ordered pair to (0,1)."""
    cur = sorted(R)
    m = M
    depth = 0
    while len({r % 2 for r in cur}) == 1:
        p = cur[0] % 2
        cur = sorted((r - p) // 2 for r in cur)
        m //= 2
        depth += 1
    best = None
    for u in cur:
        for vv in cur:
            d = (vv - u) % m
            if d % 2 == 0:
                continue
            a = pow(d, -1, m)
            T = tuple(sorted((a * (x - u)) % m for x in cur))
            if best is None or T < best:
                best = T
    return depth, m, best


def run_ell1_row(R, deadline, rho_seed):
    """Norm at the descended (primitive) order + timed factor screen."""
    depth, m, key = canon_ell1(R)
    t0 = time.monotonic()
    n = norm_of_set(list(key), m)
    t_norm = time.monotonic() - t0
    assert n != 0, (R, "zero norm impossible (Lam-Leung + antipodal-free)")
    row = {"R": list(R), "canon": [depth, m, list(key)],
           "norm_bits": abs(n).bit_length(), "t_norm": round(t_norm, 4)}
    if abs(n) == 1:
        row.update(verdict="SURVIVED_UNIT", maxv2=0, factors=[],
                   unresolved=[], t_row=round(time.monotonic() - t0, 4))
        return row
    fs, unres = timed_factor_screen(n, m, deadline, rho_seed)
    mv, alarms = classify(fs)
    verdict = ("EVENT" if alarms else
               "SURVIVED_CERTIFIED" if not unres else "SURVIVED_PARTIAL")
    row.update(
        verdict=verdict, maxv2=mv,
        factors=[[str(p), e, v2(p), p.bit_length()] for p, e in
                 sorted(fs.items())],
        unresolved=[[str(c), c.bit_length(), sc] for c, sc in unres],
        alarms=[str(q) for q in alarms],
        t_row=round(time.monotonic() - t0, 4))
    return row


def screen_ell1(name, w, n_target, row_budget, seed_tag, reject_core=False,
                global_budget=250.0):
    t_start = time.monotonic()
    hard_stop = t_start + global_budget
    rows = []
    seen_keys = {}
    rej = {"coset4": 0, "symmetric": 0, "dup": 0}
    overall_max = 0
    alarms_all = []
    for i in range(n_target):
        if time.monotonic() > hard_stop:
            print(f"  soft deadline hit at row {i}; stopping honestly")
            break
        rng = random.Random(f"{BASE_SEED}:{seed_tag}:{i}")
        R = None
        for _ in range(10_000):
            cand = draw_support(rng, w)
            if reject_core:
                if in_coset4(cand):
                    rej["coset4"] += 1
                    continue
                if is_symmetric(cand):
                    rej["symmetric"] += 1
                    continue
            key = canon_ell1(cand)
            if key in seen_keys:
                rej["dup"] += 1
                continue
            R = cand
            seen_keys[key] = i
            break
        assert R is not None, f"sampler starved at row {i}"
        deadline = min(time.monotonic() + row_budget, hard_stop)
        row = run_ell1_row(R, deadline, rho_seed=i + 1)
        row["i"] = i
        rows.append(row)
        overall_max = max(overall_max, row["maxv2"])
        if row["verdict"] == "EVENT":
            alarms_all += row["alarms"]
            print(f"!! EVENT at row {i}: R={R} alarms={row['alarms']}")
            with open(os.path.join(SCRATCH, "wscr_EVENT_witness.json"),
                      "w") as fh:
                json.dump(row, fh, indent=1)
    wall = time.monotonic() - t_start
    times = sorted(r["t_row"] for r in rows)
    nn = len(times)
    summary = {
        "screen": name, "cell": [1, w], "seed_base": BASE_SEED,
        "seed_tag": seed_tag, "n_registered": n_target, "n_run": nn,
        "sample_measure": "uniform over reduced signed supports "
                          "(orbit-size-weighted over orbits)",
        "rejections": rej,
        "events": sum(1 for r in rows if r["verdict"] == "EVENT"),
        "alarms": alarms_all,
        "unit_rows": sum(1 for r in rows if r["verdict"] == "SURVIVED_UNIT"),
        "certified_rows": sum(1 for r in rows
                              if r["verdict"] in ("SURVIVED_CERTIFIED",
                                                  "SURVIVED_UNIT")),
        "partial_rows": sum(1 for r in rows
                            if r["verdict"] == "SURVIVED_PARTIAL"),
        "partial_smooth_clear": sum(
            1 for r in rows if r["verdict"] == "SURVIVED_PARTIAL"
            and all(u[2] for u in r["unresolved"])),
        "max_v2": overall_max,
        "row_seconds": {"med": times[nn // 2] if nn else None,
                        "p95": times[int(nn * 0.95)] if nn else None,
                        "max": times[-1] if nn else None},
        "row_budget_s": row_budget,
        "wall_seconds": round(wall, 2),
        "python": sys.version.split()[0],
        "rows": rows,
    }
    out = os.path.join(SCRATCH, f"wscr_screen_{name}.json")
    with open(out, "w") as fh:
        json.dump(summary, fh)
    print(f"SCREEN {name}: n={nn}/{n_target} events={summary['events']} "
          f"unit={summary['unit_rows']} certified={summary['certified_rows']} "
          f"partial={summary['partial_rows']} "
          f"(smooth-clear {summary['partial_smooth_clear']}) "
          f"max_v2={overall_max} wall={wall:.1f}s "
          f"med={summary['row_seconds']['med']}s "
          f"p95={summary['row_seconds']['p95']}s")
    print(f"  rejections: {rej}")
    return summary


# ----------------------------------------------------------------------
# (2,7) router pipeline: Z[X]/(X^512+1) via Kronecker substitution
# ----------------------------------------------------------------------

DEG = 512
ORDER2 = 1024


def _maxbits(c):
    mb = 0
    for x in c:
        if x:
            b = x.bit_length() if x > 0 else (-x).bit_length()
            if b > mb:
                mb = b
    return mb


def poly_mul(a, b):
    """Exact product of int-coefficient polys (dense lists), via signed
    Kronecker substitution + balanced-digit unpack."""
    la, lb = len(a), len(b)
    ba, bb = _maxbits(a), _maxbits(b)
    if ba == 0 or bb == 0:
        return [0] * (la + lb - 1)
    bits = ba + bb + min(la, lb).bit_length() + 2
    nb = (bits + 7) // 8
    bpack = nb * 8
    half = 1 << (bpack - 1)

    def pack(c):
        pos = bytearray(nb * len(c))
        neg = bytearray(nb * len(c))
        for i, x in enumerate(c):
            if x > 0:
                pos[i * nb:(i + 1) * nb] = x.to_bytes(nb, "little")
            elif x < 0:
                neg[i * nb:(i + 1) * nb] = (-x).to_bytes(nb, "little")
        return int.from_bytes(bytes(pos), "little") - int.from_bytes(
            bytes(neg), "little")

    C = pack(a) * pack(b)
    count = la + lb - 1
    off_digit = half.to_bytes(nb, "little")
    H = int.from_bytes(off_digit * count, "little")
    C += H
    assert C >= 0
    raw = C.to_bytes(nb * count + 8, "little")
    assert raw[nb * count:] == b"\x00" * 8, "Kronecker digit overflow"
    out = [int.from_bytes(raw[i * nb:(i + 1) * nb], "little") - half
           for i in range(count)]
    return out


def ring_mul(a, b):
    """Product in Z[X]/(X^DEG + 1)."""
    c = poly_mul(a, b)
    out = c[:DEG] + [0] * (DEG - min(DEG, len(c)))
    for k in range(DEG, len(c)):
        out[k - DEG] -= c[k]
    return out


def ring_add(a, b):
    return [x + y for x, y in zip(a, b)]


def ring_sub(a, b):
    return [x - y for x, y in zip(a, b)]


def ring_scal(k, a):
    return [k * x for x in a]


def monomial(e):
    e %= ORDER2
    c = [0] * DEG
    if e >= DEG:
        c[e - DEG] = -1
    else:
        c[e] = 1
    return c


def recursive_norm(c):
    """|Res(X^DEG + 1, P)| by even/odd halving (mirrors the audited flint
    reference in wclp_b_sample_modal.py)."""
    cur = list(c)
    width = DEG
    while width > 1:
        nw = width // 2
        even = cur[0::2]
        odd = cur[1::2]
        pe = poly_mul(even, even)
        po = poly_mul(odd, odd)
        co = [0] * width
        for k, x in enumerate(pe):
            co[k] += x
        for k, x in enumerate(po):
            co[k + 1] -= x
        cur = [co[i] - co[i + nw] if i + nw < width else co[i]
               for i in range(nw)]
        width = nw
    return abs(cur[0])


def run_candidate_27(selected, c_exp, factor_deadline_s=2.5, rho_seed=1):
    """One (2,7) router orbit: selected = exponents of the 3 non-1 selected
    roots; complement triple has product zeta^c_exp.  Mirrors the audited
    pipeline; obstruction screen = saturated gcd + u-shared part (route (a))."""
    t0 = time.monotonic()
    one = [0] * DEG
    one[0] = 1
    e1 = one
    e2 = [0] * DEG
    e3 = [0] * DEG
    for v in selected:
        r = monomial(v)
        e3 = ring_add(e3, ring_mul(e2, r))
        e2 = ring_add(e2, ring_mul(e1, r))
        e1 = ring_add(e1, r)
    d_val = monomial(c_exp)
    u = e1
    w_val = ring_sub(ring_sub(ring_mul(u, e2), e3), d_val)
    u2 = ring_mul(u, u)
    sigma = ring_scal(-1, u2)
    theta = ring_mul(u, w_val)
    prod = ring_mul(ring_mul(u2, u), d_val)
    upow = u
    power = 1
    while power < ORDER2:
        s_, t_, p_ = sigma, theta, prod
        sigma = ring_sub(ring_mul(s_, s_), ring_scal(2, t_))
        theta = ring_sub(ring_mul(t_, t_), ring_scal(2, ring_mul(p_, s_)))
        prod = ring_mul(p_, p_)
        upow = ring_mul(upow, upow)
        power *= 2
    F = ring_sub(sigma, ring_scal(3, upow))
    G = ring_sub(theta, ring_scal(3, ring_mul(upow, upow)))
    t_rec = time.monotonic() - t0

    fz = all(x == 0 for x in F)
    gz = all(x == 0 for x in G)
    t1 = time.monotonic()
    n1 = 0 if fz else recursive_norm(F)
    t_n1 = time.monotonic() - t1
    t1 = time.monotonic()
    n2 = 0 if gz else recursive_norm(G)
    t_n2 = time.monotonic() - t1
    t1 = time.monotonic()
    nu = recursive_norm(u)
    assert nu != 0, "char-zero weight-4 selected-sum vanisher (impossible)"
    t_nu = time.monotonic() - t1

    row = {"selected": list(selected), "c": c_exp,
           "zero_F": fz, "zero_G": gz,
           "n1_bits": n1.bit_length(), "n2_bits": n2.bit_length(),
           "nu_bits": nu.bit_length(),
           "t_recurrence": round(t_rec, 3), "t_norm_F": round(t_n1, 3),
           "t_norm_G": round(t_n2, 3), "t_norm_u": round(t_nu, 3)}
    if fz and gz:
        row.update(verdict="STRUCTURAL_ZERO", maxv2=0,
                   t_row=round(time.monotonic() - t0, 3))
        return row
    if fz or gz:
        row.update(verdict="SINGLE_ZERO_UNRESOLVED", maxv2=0,
                   t_row=round(time.monotonic() - t0, 3))
        return row
    t1 = time.monotonic()
    g0 = gcd(n1, n2)
    t_gcd = time.monotonic() - t1
    t1 = time.monotonic()
    common = g0
    while common > 1:
        rem = gcd(common, nu)
        if rem == 1:
            break
        common //= rem
    gsat = common
    ushare = gcd(g0, nu)
    t_sat = time.monotonic() - t1

    t1 = time.monotonic()
    deadline = time.monotonic() + factor_deadline_s
    fs = {}
    unres = []
    if gsat > 1:
        f1, u1 = timed_factor_screen(gsat, ORDER2, deadline, rho_seed)
        for p, e in f1.items():
            fs[p] = fs.get(p, 0) + e
        unres += u1
    if ushare > 1:
        f2, u2_ = timed_factor_screen(ushare, ORDER2, deadline,
                                      rho_seed + 7_777)
        for p, e in f2.items():
            fs[p] = fs.get(p, 0) + e
        unres += u2_
    t_fac = time.monotonic() - t1
    mv, alarms = classify(fs)
    verdict = ("EVENT_CANDIDATE" if alarms else
               "SURVIVED_CERTIFIED" if not unres else "SURVIVED_PARTIAL")
    row.update(
        g0_bits=g0.bit_length(), gsat_bits=gsat.bit_length(),
        ushare_bits=ushare.bit_length(), verdict=verdict, maxv2=mv,
        factors=[[str(p), e, v2(p), p.bit_length()] for p, e in
                 sorted(fs.items())],
        unresolved=[[str(c), c.bit_length(), sc] for c, sc in unres],
        alarms=[str(q) for q in alarms],
        t_gcd=round(t_gcd, 3), t_saturate=round(t_sat, 3),
        t_factor=round(t_fac, 3), t_row=round(time.monotonic() - t0, 3))
    return row


def canon_27(Q, c):
    """Canonical invariant of the router orbit of (Q, c) under
    H = {(t,r): t odd}: (Q,c) -> (tQ+r, tc+3r).  Complete enumeration of
    orbit members with 0 in the support: r = -t*q0."""
    best = None
    for t in range(1, ORDER2, 2):
        for q0 in Q:
            key = (tuple(sorted((t * (x - q0)) % ORDER2 for x in Q)),
                   (t * (c - 3 * q0)) % ORDER2)
            if best is None or key < best:
                best = key
    return best


def legal_tuple(values):
    if any(v % ORDER2 in (0, ORDER2 // 2) for v in values):
        return False
    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            if (values[i] - values[j]) % ORDER2 in (0, ORDER2 // 2):
                return False
    return True


def draw_27(rng):
    while True:
        a, b, e = (rng.randrange(1, ORDER2) for _ in range(3))
        if legal_tuple((a, b, e)):
            return (a, b, e), rng.randrange(ORDER2)


def screen_27_shard(shard, of, n_total, factor_budget=2.5,
                    global_budget=245.0):
    t_start = time.monotonic()
    hard_stop = t_start + global_budget
    rows = []
    for i in range(n_total):
        if i % of != shard:
            continue
        if time.monotonic() > hard_stop:
            print(f"  soft deadline hit before index {i}; stopping honestly")
            break
        rng = random.Random(f"{BASE_SEED}:27:{i}")
        sel, c = draw_27(rng)
        row = run_candidate_27(sel, c, factor_budget, rho_seed=i + 1)
        row["i"] = i
        row["canon"] = [list(canon_27((0,) + sel, c)[0]),
                        canon_27((0,) + sel, c)[1]]
        rows.append(row)
        if row["verdict"] == "EVENT_CANDIDATE":
            print(f"!! EVENT_CANDIDATE at index {i}: sel={sel} c={c} "
                  f"alarms={row['alarms']}")
            with open(os.path.join(SCRATCH, "wscr_EVENT_witness.json"),
                      "w") as fh:
                json.dump(row, fh, indent=1)
    out = {"shard": shard, "of": of, "n_total_registered": n_total,
           "rows": rows, "wall_seconds": round(time.monotonic() - t_start, 2)}
    path = os.path.join(SCRATCH, f"wscr_screen_27router_shard{shard}.json")
    with open(path, "w") as fh:
        json.dump(out, fh)
    done = len(rows)
    ev = sum(1 for r in rows if r["verdict"] == "EVENT_CANDIDATE")
    print(f"SHARD {shard}/{of}: rows={done} events={ev} "
          f"wall={out['wall_seconds']}s")


def merge_27(of, n_total):
    rows = []
    for shard in range(of):
        path = os.path.join(SCRATCH,
                            f"wscr_screen_27router_shard{shard}.json")
        with open(path) as fh:
            d = json.load(fh)
        assert d["of"] == of and d["n_total_registered"] == n_total
        rows += d["rows"]
    rows.sort(key=lambda r: r["i"])
    keys = {}
    for r in rows:
        k = (tuple(r["canon"][0]), r["canon"][1])
        assert k not in keys, f"orbit collision {r['i']} vs {keys[k]}"
        keys[k] = r["i"]
    times = sorted(r["t_row"] for r in rows)
    nn = len(times)

    def phase(key):
        vals = sorted(r.get(key, 0.0) for r in rows)
        return {"med": vals[nn // 2], "p95": vals[int(nn * 0.95)],
                "max": vals[-1]}

    overall_max = max((r["maxv2"] for r in rows), default=0)
    summary = {
        "screen": "27router", "cell": [2, 7], "seed_base": BASE_SEED,
        "seed_tag": "27", "n_registered": n_total, "n_run": nn,
        "sample_measure": "uniform over legal normalized router "
                          "presentations ({1,x,y,z}, c) "
                          "(orbit-size-weighted over router orbits)",
        "events": sum(1 for r in rows if r["verdict"] == "EVENT_CANDIDATE"),
        "alarms": sum((r.get("alarms", []) for r in rows), []),
        "zero_rows": sum(1 for r in rows if r["verdict"] in
                         ("STRUCTURAL_ZERO", "SINGLE_ZERO_UNRESOLVED")),
        "trivial_gcd_rows": sum(1 for r in rows
                                if r.get("gsat_bits", 99) <= 1
                                and r.get("ushare_bits", 99) <= 1),
        "certified_rows": sum(1 for r in rows
                              if r["verdict"] == "SURVIVED_CERTIFIED"),
        "partial_rows": sum(1 for r in rows
                            if r["verdict"] == "SURVIVED_PARTIAL"),
        "partial_smooth_clear": sum(
            1 for r in rows if r["verdict"] == "SURVIVED_PARTIAL"
            and all(u[2] for u in r["unresolved"])),
        "max_v2": overall_max,
        "bits": {"n1_med": sorted(r["n1_bits"] for r in rows)[nn // 2],
                 "n2_med": sorted(r["n2_bits"] for r in rows)[nn // 2],
                 "g0_med": sorted(r.get("g0_bits", 0)
                                  for r in rows)[nn // 2],
                 "gsat_med": sorted(r.get("gsat_bits", 0)
                                    for r in rows)[nn // 2],
                 "gsat_max": max(r.get("gsat_bits", 0) for r in rows)},
        "timing_pilot": {k: phase(k) for k in
                         ("t_recurrence", "t_norm_F", "t_norm_G", "t_norm_u",
                          "t_gcd", "t_saturate", "t_factor", "t_row")},
        "python": sys.version.split()[0],
        "note": "pure-Python local rates (no flint); banked Modal+flint "
                "rate was 1.25 s/orbit with gcd+saturation 1.095 s",
        "rows": rows,
    }
    out = os.path.join(SCRATCH, "wscr_screen_27router.json")
    with open(out, "w") as fh:
        json.dump(summary, fh)
    print(f"SCREEN 27router: n={nn}/{n_total} "
          f"events={summary['events']} zero={summary['zero_rows']} "
          f"certified={summary['certified_rows']} "
          f"partial={summary['partial_rows']} "
          f"(smooth-clear {summary['partial_smooth_clear']}) "
          f"max_v2={overall_max}")
    print(f"  bits: {summary['bits']}")
    for k, vals in summary["timing_pilot"].items():
        print(f"  {k}: med={vals['med']:.3f} p95={vals['p95']:.3f} "
              f"max={vals['max']:.3f}")


# ----------------------------------------------------------------------
# selfcheck + pilots
# ----------------------------------------------------------------------

def cmd_selfcheck():
    ok = True
    rng = random.Random(20260722)

    # SC1: Kronecker poly_mul vs schoolbook
    def school(a, b):
        out = [0] * (len(a) + len(b) - 1)
        for i, x in enumerate(a):
            if x:
                for j, y in enumerate(b):
                    out[i + j] += x * y
        return out
    for trial, (la, lb, mag) in enumerate(
            [(7, 5, 10), (64, 64, 1 << 30), (128, 128, 1 << 200),
             (512, 512, 3), (33, 200, 1 << 999)]):
        a = [rng.randrange(-mag, mag + 1) for _ in range(la)]
        b = [rng.randrange(-mag, mag + 1) for _ in range(lb)]
        if poly_mul(a, b) != school(a, b):
            print(f"SC1 FAIL trial {trial}")
            ok = False
    print("SC1 Kronecker mul vs schoolbook:", "PASS" if ok else "FAIL")

    # SC2: recursive_norm vs wsz norm_rec (independent audited impl) at 512
    ok2 = True
    for _ in range(3):
        c = [0] * DEG
        for e in rng.sample(range(DEG), 7):
            c[e] = rng.choice((1, -1))
        if recursive_norm(c) != abs(norm_rec(c[:])):
            ok2 = False
    # and vs sympy resultant at width 16
    import sympy
    X = sympy.symbols("x")
    for _ in range(3):
        cc = [rng.randrange(-5, 6) for _ in range(16)]
        want = abs(int(sympy.resultant(X ** 16 + 1,
                                       sum(v * X ** i
                                           for i, v in enumerate(cc)))))
        cur, width = list(cc), 16

        def rn(cur, width):
            while width > 1:
                nw = width // 2
                pe = poly_mul(cur[0::2], cur[0::2])
                po = poly_mul(cur[1::2], cur[1::2])
                co = [0] * width
                for k, x in enumerate(pe):
                    co[k] += x
                for k, x in enumerate(po):
                    co[k + 1] -= x
                cur = [co[i] - co[i + nw] if i + nw < width else co[i]
                       for i in range(nw)]
                width = nw
            return abs(cur[0])
        if rn(cur, width) != want:
            ok2 = False
    print("SC2 recursive_norm vs norm_rec/sympy:", "PASS" if ok2 else "FAIL")
    ok &= ok2

    # SC3: EXACT mod-q validation over F_q, q = 12289 (1024 | q-1):
    # (a) when the cleared cubic splits over F_q, the ring-computed
    #     sigma_k/theta_k/pi_k evaluated at z must equal the symmetric
    #     functions of the scalar roots' 2^k-th powers, k = 1..10;
    # (b) recursive_norm(F/G/u) mod q must equal (+-) the direct product
    #     of F(z^k) over odd k — an independent full-size norm check.
    q = 12289
    z = pow(11, (q - 1) // ORDER2, q)
    zo = z
    o = 1
    while zo != 1:
        zo = zo * z % q
        o += 1
    assert o == ORDER2, "z must have exact order 1024"
    powz = [1] * ORDER2
    for j in range(1, ORDER2):
        powz[j] = powz[j - 1] * z % q

    def ev_q(poly, k=1):
        return sum(coef * powz[(i * k) % ORDER2] for i, coef in
                   enumerate(poly) if coef) % q

    ok3 = True
    rng3 = random.Random("wscr:selfcheck:27")
    split_done = False
    for _try in range(40):
        sel, c_exp = draw_27(rng3)
        one = [0] * DEG
        one[0] = 1
        e1, e2, e3 = one, [0] * DEG, [0] * DEG
        for vv in sel:
            r = monomial(vv)
            e3 = ring_add(e3, ring_mul(e2, r))
            e2 = ring_add(e2, ring_mul(e1, r))
            e1 = ring_add(e1, r)
        d_val = monomial(c_exp)
        u = e1
        w_val = ring_sub(ring_sub(ring_mul(u, e2), e3), d_val)
        u2 = ring_mul(u, u)
        sigma = ring_scal(-1, u2)
        theta = ring_mul(u, w_val)
        prod = ring_mul(ring_mul(u2, u), d_val)
        s_q, t_q, p_q = ev_q(sigma), ev_q(theta), ev_q(prod)
        # find roots of x^3 - s_q x^2 + t_q x - p_q over F_q by scan
        roots_q = []
        cubic = (1, (-s_q) % q, t_q % q, (-p_q) % q)
        for x in range(q):
            v = 0
            for co in cubic:
                v = (v * x + co) % q
            if v == 0:
                roots_q.append(x)
                if len(roots_q) == 3:
                    break
        # multiplicity handling: accept only clean 3-distinct-root splits
        if len(roots_q) != 3:
            if split_done:
                break
            continue
        split_done = True
        upow = u
        power = 1
        rr = list(roots_q)
        while power < ORDER2:
            s_, t_, p_ = sigma, theta, prod
            sigma = ring_sub(ring_mul(s_, s_), ring_scal(2, t_))
            theta = ring_sub(ring_mul(t_, t_), ring_scal(2, ring_mul(p_, s_)))
            prod = ring_mul(p_, p_)
            upow = ring_mul(upow, upow)
            power *= 2
            rr = [x * x % q for x in rr]
            en1 = sum(rr) % q
            en2 = (rr[0] * rr[1] + rr[0] * rr[2] + rr[1] * rr[2]) % q
            en3 = rr[0] * rr[1] * rr[2] % q
            if (ev_q(sigma), ev_q(theta), ev_q(prod)) != (en1, en2, en3):
                ok3 = False
        F = ring_sub(sigma, ring_scal(3, upow))
        G = ring_sub(theta, ring_scal(3, ring_mul(upow, upow)))
        # (b) norm consistency at full size, mod q
        for poly in (F, G, u):
            direct = 1
            for k in range(1, ORDER2, 2):
                direct = direct * ev_q(poly, k) % q
            nq = recursive_norm(poly) % q
            if nq != direct and nq != (-direct) % q:
                ok3 = False
        break
    ok3 &= split_done
    print("SC3 exact mod-q recurrence + full-size norm consistency:",
          "PASS" if ok3 else "FAIL", "(split found:", split_done, ")")
    ok &= ok3

    # SC4: canonical invariance
    ok4 = True
    rng4 = random.Random("wscr:selfcheck:canon")
    for _ in range(15):
        sel, c = draw_27(rng4)
        Q = (0,) + sel
        k0 = canon_27(Q, c)
        t = rng4.randrange(1, ORDER2, 2)
        r = rng4.randrange(ORDER2)
        Q2 = tuple((t * x + r) % ORDER2 for x in Q)
        c2 = (t * c + 3 * r) % ORDER2
        if canon_27(Q2, c2) != k0:
            ok4 = False
    for _ in range(15):
        R = draw_support(rng4, 5)
        k0 = canon_ell1(R)
        a = rng4.randrange(1, 512, 2)
        b = rng4.randrange(512)
        R2 = sorted((a * x + b) % 512 for x in R)
        if canon_ell1(R2) != k0:
            ok4 = False
    print("SC4 canonicalization orbit-invariance:", "PASS" if ok4 else "FAIL")
    ok &= ok4

    # SC5: powered pm1 detector positive control (official-admissible prime)
    q0 = 3 * 2 ** 41 + 1
    assert is_probable_prime(q0) and v2(q0) == 41
    p_r = 0
    rng5 = random.Random(5)
    while not is_probable_prime(p_r):
        p_r = rng5.getrandbits(100) | (1 << 99) | 1
    f, sc = pm1_boosted(q0 * p_r, 512)
    ok5 = f is not None and f % q0 == 0
    mv, al = classify({q0: 1, p_r: 1})
    ok5 &= al == [q0] and mv == 41
    # detector-path control at a lowered gate: 12289 (v2 = 12)
    mv2, al2 = classify({12289: 1}, gate=10)
    ok5 &= al2 == [12289] and classify({12289: 1})[1] == []
    print("SC5 pm1 admissible-prime detector + classifier:",
          "PASS" if ok5 else "FAIL")
    ok &= ok5

    # SC6: timed factor screen reassembly on a real (1,5) norm
    n = abs(norm_of_set([0, 3, 50, 301, 511], 512))
    fs, un = timed_factor_screen(n, 512, time.monotonic() + 20)
    prod_chk = 1
    for p, e in fs.items():
        prod_chk *= p ** e
    for c, _ in un:
        prod_chk *= c
    ok6 = prod_chk == n
    print(f"SC6 factor screen reassembly ({len(fs)} primes, "
          f"{len(un)} unresolved):", "PASS" if ok6 else "FAIL")
    ok &= ok6

    print("SELFCHECK:", "PASS" if ok else "FAIL")
    sys.exit(0 if ok else 1)


def _odd_pps():
    """Odd prime powers p^floor(log_p B1) for p <= B1, ascending p."""
    out = []
    for p in small_primes()[1:]:
        if p > B1:
            break
        pe = p
        while pe * p <= B1:
            pe *= p
        out.append((p, pe))
    return out


def declump_split(c, deadline):
    """Staged p-1 on a composite where plain pm1 clumped (g == n for all
    bases, i.e. every prime factor q has q-1 | E).  Steps the 2-part one
    squaring at a time and the odd smooth part one prime power at a time,
    over several bases, catching the first point where the factors' orders
    diverge.  Returns a nontrivial factor or None."""
    pps = _odd_pps()
    for base in (2, 3, 5, 7, 11, 13, 17):
        if time.monotonic() > deadline:
            return None
        # odd smooth part first, then stepped 2-part
        a = base % c
        for _, pe in pps:
            a = pow(a, pe, c)
        for _ in range(300):
            g = gcd(a - 1, c)
            if 1 < g < c:
                return g
            if g == c:
                break
            a = a * a % c
        # 2-part first, then stepped odd part (order of stages swapped)
        a = pow(base, 1 << 300, c)
        clumped_pp = None
        for p, pe in pps:
            an = pow(a, pe, c)
            g = gcd(an - 1, c)
            if 1 < g < c:
                return g
            if g == c:
                clumped_pp = (p, pe)
                break
            a = an
        if clumped_pp is not None:
            p, pe = clumped_pp
            while pe > 1:
                an = pow(a, p, c)
                g = gcd(an - 1, c)
                if 1 < g < c:
                    return g
                if g == c:
                    break  # same flip point; next base
                a = an
                pe //= p
    return None


def cmd_declump():
    """POST-HOC labeled pass: split the clumped unresolved cofactors
    (smooth_clear == False) recorded by the four registered screens.
    Does NOT modify the registered screen JSONs."""
    targets = []
    for name, order in (("15core", 512), ("16", 512), ("17", 512),
                        ("27router", 1024)):
        path = os.path.join(SCRATCH, f"wscr_screen_{name}.json")
        with open(path) as fh:
            d = json.load(fh)
        for r in d["rows"]:
            for cs, bits, sc in r.get("unresolved", []):
                if not sc:
                    targets.append((name, r["i"], int(cs), bits, order))
    print(f"declump targets: {len(targets)} clumped cofactors")
    out_rows = []
    new_alarms = []
    overall_max = 0
    resolved = 0
    t0 = time.monotonic()
    for name, i, c, bits, order in targets:
        deadline = time.monotonic() + 4.0
        found = {}
        stack = [c]
        gaveup = []
        while stack:
            x = stack.pop()
            if x == 1:
                continue
            if is_probable_prime(x):
                found[x] = found.get(x, 0) + 1
                continue
            r_, k_ = perfect_power(x)
            if r_ is not None:
                stack.extend([r_] * k_)
                continue
            f = declump_split(x, deadline)
            if f is None:
                f = brent_rho_timed(x, min(deadline,
                                           time.monotonic() + 1.0),
                                    seed=i + 31)
            if f is None:
                gaveup.append(x)
                continue
            stack.append(f)
            stack.append(x // f)
        mv, al = classify(found)
        overall_max = max(overall_max, mv)
        new_alarms += al
        status = "RESOLVED" if not gaveup else (
            "PARTIAL" if found else "UNSPLIT")
        if not gaveup:
            resolved += 1
        out_rows.append({
            "screen": name, "i": i, "cofactor_bits": bits,
            "status": status, "maxv2": mv,
            "factors": [[str(p), e, v2(p), p.bit_length()]
                        for p, e in sorted(found.items())],
            "still_unresolved_bits": [x.bit_length() for x in gaveup],
            "alarms": [str(q) for q in al]})
        if al:
            print(f"!! DECLUMP ALARM screen {name} row {i}: {al}")
    summary = {"pass": "post-hoc declump (labeled; registered screen JSONs "
                       "untouched)",
               "targets": len(targets), "fully_resolved": resolved,
               "max_v2_new": overall_max, "alarms": new_alarms,
               "wall_seconds": round(time.monotonic() - t0, 2),
               "rows": out_rows}
    with open(os.path.join(SCRATCH, "wscr_declump.json"), "w") as fh:
        json.dump(summary, fh, indent=1)
    print(f"DECLUMP: {resolved}/{len(targets)} fully resolved; "
          f"max v_2 among newly certified primes = {overall_max}; "
          f"alarms = {new_alarms}; wall {summary['wall_seconds']}s")


def cmd_pilot_ell1():
    """Calibration pilot on NON-registered seed streams (:pilotW:)."""
    for w, count, budget in ((5, 8, 3.0), (6, 6, 3.0), (7, 4, 3.0)):
        print(f"--- pilot (1,{w}) x{count}, rho budget {budget}s/row")
        for i in range(count):
            rng = random.Random(f"{BASE_SEED}:pilot{w}:{i}")
            R = draw_support(rng, w)
            t0 = time.monotonic()
            row = run_ell1_row(R, time.monotonic() + budget, rho_seed=900 + i)
            print(f"  i={i} m={row['canon'][1]} bits={row['norm_bits']} "
                  f"{row['verdict']} maxv2={row['maxv2']} "
                  f"unres={[u[1] for u in row['unresolved']]} "
                  f"t={time.monotonic() - t0:.2f}s (norm {row['t_norm']}s)")


def cmd_pilot27(count):
    print(f"--- pilot (2,7) x{count} (seed stream :pilot27:)")
    for i in range(count):
        rng = random.Random(f"{BASE_SEED}:pilot27:{i}")
        sel, c = draw_27(rng)
        row = run_candidate_27(sel, c, factor_deadline_s=3.0,
                               rho_seed=800 + i)
        print(f"  i={i} sel={sel} c={c} -> {row['verdict']} "
              f"n1={row['n1_bits']}b n2={row['n2_bits']}b "
              f"nu={row['nu_bits']}b g0={row.get('g0_bits')}b "
              f"gsat={row.get('gsat_bits')}b ushare={row.get('ushare_bits')}b "
              f"maxv2={row['maxv2']}")
        print(f"    t: rec={row['t_recurrence']} nF={row['t_norm_F']} "
              f"nG={row['t_norm_G']} nu={row['t_norm_u']} "
              f"gcd={row.get('t_gcd')} sat={row.get('t_saturate')} "
              f"fac={row.get('t_factor')} row={row['t_row']}")


def main():
    cmd = sys.argv[1]
    if cmd == "selfcheck":
        cmd_selfcheck()
    elif cmd == "pilot_ell1":
        cmd_pilot_ell1()
    elif cmd == "pilot27":
        cmd_pilot27(int(sys.argv[2]))
    elif cmd == "screen15":
        screen_ell1("15core", 5, 400, 0.45, "15core", reject_core=True)
    elif cmd == "screen16":
        screen_ell1("16", 6, 256, 0.75, "16")
    elif cmd == "screen17":
        screen_ell1("17", 7, 128, 1.5, "17")
    elif cmd == "screen27":
        screen_27_shard(int(sys.argv[2]), int(sys.argv[3]),
                        int(sys.argv[4]), factor_budget=2.0)
    elif cmd == "merge27":
        merge_27(int(sys.argv[2]), int(sys.argv[3]))
    elif cmd == "declump":
        cmd_declump()
    else:
        raise SystemExit("unknown subcommand")


if __name__ == "__main__":
    main()
