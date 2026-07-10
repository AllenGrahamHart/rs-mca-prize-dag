#!/usr/bin/env python3
"""F2 campaign (Modal): PHASE CANCELLATION MEASUREMENT (cycle 82) —
the first direct test of the census's signed-recovery mechanism.

Objects (from satellite 18's split): W_c = S_c + i Phi_c with
exp(W_c) = prod_{x in mu_n}(1 + psi(c.xbar)).  Facts used:
  * SIGNED SUM EXACT: sum_{c != 0} exp(W_c) = q^j N_total^(j) - 2^n
    (orthogonality; N_total = #subsets of mu_n, any size, with
    p_1 = .. = p_j = 0 — integer DP).
  * j=1 PHASE VANISHING (one line, NEW): for |G| even, x -> -x
    pairs the sawtooth ((cx/q)) with its negative, so Phi_c == 0
    identically at j = 1 — the phase is a genuinely multi-condition
    object (single conditions have a real, positive Fourier side).

MEASUREMENTS (pre-registered reads):
  (A) j=1 vanishing: max |Phi_c| < 1e-9 * n at even-f rows.
  (B) WEYL SUMS of the phase: |E_c e^{i k Phi_c}|, k = 1..4,
      unweighted (sampling is SOUND here — bounded observable,
      unlike exp(S), catch #20) — equidistribution read: values
      ~ N^{-1/2}-scale (report; soft flag at 10x random).
  (C) THE SIGNED-RECOVERY RATIO at exact rows:
        R      = |q^j N_total - 2^n| / sum_{c != 0} exp(S_c)
        R_pred = sqrt(sum_{c != 0} exp(2 S_c)) / sum_{c != 0} exp(S_c)
      (random-phase prediction: E|sum exp(W)|^2 = sum exp(2S) under
      independent uniform phases).  READ: R/R_pred in [0.1, 10] =>
      the random-phase (square-root) saving — exactly the mechanism
      the consumer contract needs — CONFIRMED at these rows;
      R/R_pred > 10 => PHASE ALIGNMENT (the dangerous direction —
      bank loudly, potential falsifier lane); < 0.1 => structured
      super-cancellation (reciprocity visible — bank as lead).
"""
import cmath
import math
import random

import modal

app = modal.App("rs-mca-f2-phase-cancel")
image = modal.Image.debian_slim().pip_install("numpy")

# ("exact", q, n, j, 0, 0) | ("weyl", q, n, j, nsamp, seed)
JOBS = [
    ("exact", 97, 32, 2, 0, 0),
    ("exact", 97, 32, 3, 0, 0),
    ("exact", 193, 64, 2, 0, 0),
    ("weyl", 7681, 512, 2, 20000, 1),
    ("weyl", 12289, 1024, 2, 12000, 2),
]


@app.function(image=image, cpu=2, memory=4096, timeout=280)
def cell(job):
    kind, q, n, j, nsamp, seed = job

    def pf(x):
        out, d = [], 2
        while d * d <= x:
            while x % d == 0:
                out.append(d)
                x //= d
            d += 1
        if x > 1:
            out.append(x)
        return out

    g = next(c for c in range(2, q)
             if all(pow(c, (q - 1) // r, q) != 1 for r in set(pf(q - 1))))
    h = pow(g, (q - 1) // n, q)
    D = [pow(h, i, q) for i in range(n)]
    xbar = [[pow(x, i, q) for i in range(1, j + 1)] for x in D]
    psi = [cmath.exp(2j * math.pi * s / q) for s in range(q)]
    logtab = [0.0] + [math.log(abs(1 + psi[s])) for s in range(1, q)]
    argtab = [cmath.phase(1 + psi[s]) for s in range(q)]
    sawtab = [(s - q if s > q // 2 else s) / q for s in range(q)]
    logtab[0] = math.log(2.0)

    # (A) j=1 phase vanishing at this row (f = n even)
    a_max = 0.0
    for c in range(1, min(q, 500)):
        ph = sum(sawtab[c * x % q] for x in D)
        a_max = max(a_max, abs(math.pi * ph))

    if kind == "exact":
        import numpy as np
        Q = q ** j
        ar = np.arange(Q, dtype=np.int64)
        cdig = [(ar // q ** i) % q for i in range(j)]
        # integer DP for N_total^(j): adding x's moment vector is a
        # bijection on the state space
        counts = np.zeros(Q, dtype=np.int64)
        counts[0] = 1
        for xi in range(n):
            xb = xbar[xi]
            newidx = sum(((cdig[i] + xb[i]) % q) * q ** i
                         for i in range(j))
            tmp = np.zeros_like(counts)
            tmp[newidx] = counts
            counts = counts + tmp
        N_total = int(counts[0])
        signed_exact = q ** j * N_total - 2 ** n

        # full enumeration of (S, Phi) over all c via vectorized tables
        ltab = np.array(logtab)
        atab = np.array(argtab)
        S = np.zeros(Q)
        ph = np.zeros(Q)
        for xi in range(n):
            xb = xbar[xi]
            sidx = sum(cdig[i] * xb[i] for i in range(j)) % q
            S += ltab[sidx]
            ph += atab[sidx]
        S[0] = -1e30  # exclude c = 0
        eS = np.exp(S)
        sum1 = float(eS.sum())
        sum2 = float((eS * eS).sum())
        sgn = complex((eS * np.exp(1j * ph)).sum())
        weyl = []
        mask = np.ones(Q, dtype=bool)
        mask[0] = False
        for k in range(1, 5):
            weyl.append(abs(complex(np.exp(1j * k * ph[mask]).sum())))
        Npop = Q - 1
        R = abs(signed_exact) / sum1
        Rp = math.sqrt(sum2) / sum1
        ident_err = abs(sgn - signed_exact) / max(1.0, abs(signed_exact))
        return {"kind": kind, "q": q, "n": n, "j": j,
                "N_total": N_total, "signed": signed_exact,
                "R": R, "Rp": Rp, "ratio": R / Rp,
                "ident_err": ident_err, "amax": a_max,
                "weyl": [w / Npop for w in weyl],
                "rand": 1 / math.sqrt(Npop)}

    rng = random.Random(seed)
    weyl = [0.0 + 0.0j] * 4
    for _ in range(nsamp):
        c = tuple(rng.randrange(q) for _ in range(j))
        if not any(c):
            continue
        ph = 0.0
        for xi in range(n):
            s = sum(c[i] * xbar[xi][i] for i in range(j)) % q
            ph += argtab[s]
        for k in range(4):
            weyl[k] += cmath.exp(1j * (k + 1) * ph)
    return {"kind": kind, "q": q, "n": n, "j": j,
            "weyl": [abs(w) / nsamp for w in weyl],
            "rand": 1 / math.sqrt(nsamp), "amax": a_max}


@app.local_entrypoint()
def main():
    res = list(cell.map(JOBS, return_exceptions=True))
    fails = 0
    for r in res:
        if not isinstance(r, dict):
            fails += 1
            print("worker error:", str(r)[:300])
            continue
        if r["amax"] > 1e-9 * r["n"]:
            print(f"   !! j=1 phase NON-vanishing at (q={r['q']}): "
                  f"{r['amax']:.2e}")
            fails += 1
        ws = ", ".join(f"{w:.4f}" for w in r["weyl"])
        if r["kind"] == "exact":
            ok = 0.1 <= r["ratio"] <= 10 and r["ident_err"] < 1e-6
            print(f"(q={r['q']}, n={r['n']}, j={r['j']}) EXACT: "
                  f"N_total = {r['N_total']}, signed dev = {r['signed']}, "
                  f"R = {r['R']:.3e}, R_pred = {r['Rp']:.3e}, "
                  f"R/R_pred = {r['ratio']:.2f}, identity err = "
                  f"{r['ident_err']:.1e}; Weyl k=1..4: [{ws}] "
                  f"(random {r['rand']:.4f})  {'OK' if ok else 'FLAG'}")
            if not ok:
                fails += 1
        else:
            print(f"(q={r['q']}, n={r['n']}, j={r['j']}) WEYL sampled: "
                  f"k=1..4: [{ws}] (random scale {r['rand']:.4f}); "
                  f"j=1 phase max = {r['amax']:.1e}")
    if fails:
        raise SystemExit(f"F2_PHASE_CANCEL_FAIL ({fails})")
    print("\nF2_PHASE_CANCELLATION_PASS")
