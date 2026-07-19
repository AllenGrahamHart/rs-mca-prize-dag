#!/usr/bin/env python3
"""rh_band_witness_census_modal.py — MODAL LAUNCHER (deliverable; DO NOT LAUNCH
without the maintainer's go). Next-intensity census for the rate-1/2 band
witness lane (rate_half_band_closure, WP7 mechanism 1: new priced family
beyond the n/256 quotient plateau).

Launch (maintainer):  ~/.venvs/modal/bin/modal run rh_band_witness_census_modal.py
App: rs-mca-rh-witness-census

=======================================================================
PRE-REGISTERED READS (write these BEFORE looking at any output)
=======================================================================
Instrument 1 (zero_sum_ladder — the C1/C2 sporadic pricing, quotient level):
  Zero-sum h-subsets of mu_{N2} minus one antipodal pair, exact DP counts,
  q-ladder = 1 mod n crossing INTO the starved regime at N2 = 32
  (starved iff q > C(30,16) = 145,422,675).
  R1a. floor check: count_antipodal == C(N2/2 - 1, h/2) at every q
       (Lam-Leung: char-0 zero-sums of 2-power roots = antipodal pair unions;
        the two-scale coset dressing re-parameterizes the qcore plateau).
  R1b. sporadic(q) = zerosum(q) - floor: expect orbit-quantized rare events
       decaying ~ (#subsets)/q; expect sporadic == 0 at every starved q.
  R1c. KILL LINE (mechanism found): sporadic(q) >= 27 * floor  (the razor
       multiplicative gap x28.4 rounded down, minus the floor itself) at ANY
       starved q. This would be a genuinely new priced family candidate ->
       stop, classify the witnessing subsets, escalate to the maintainer.
  R1d. window-law read: sporadic ledger across the ladder consistent with
       Poisson(lambda ~ C/q) => the first-moment confidence sharpens; a
       SUSTAINED (>= 3 consecutive q) excess in EITHER direction beyond
       Poisson triggers the node's pre-registered falsifier protocol.
Instrument 2 (fiber_census — full moment-map fiber table at n = 128/256):
  Exact CRT-DP over all fibers c in F_q^t of
     #{S subset mu_n, |S| = k + t, series(L_S) = c mod z^(t+1)}
  (= the EXACT full list count of the received word X^k * L_{T0(c)} for
   polynomial words; catches every witness shape at once).
  Cells are fiber-RICH (q^t << C(n,k+t)) — regime label mandatory on every
  readout; these validate the two-column law, they do NOT decide absence.
  R2a. qcore-fiber == C(N-1, h) + background, background ~ C(n,k+t)/q^t
       within Poisson, at n = 128 AND n = 256 (two new scales; with the
       n = 16/32/64 local runs this makes >= 3 scales for the banked
       falsifier's 'sustained' clause).
  R2b. max-fiber argmax is a coset-structured target (an r = 1 word) up to
       background noise. A NON-coset argmax exceeding the plateau target by
       more than Poisson background at BOTH n = 128 and n = 256 is the
       lane's first genuine lead -> classify its S-sets, escalate.
  R2c. generic-core law: fibers of words with core touching r cosets =
       C(N - r, h) + background (in-vivo confirmation at scale).
  R2d. zero-fiber (c = 0): background only (no structural mass at odd sizes).
=======================================================================
BUDGETS: worker RAM stated per function; all counts exact (int64 DP for
instrument 1; 3 x 61-bit-prime CRT for instrument 2). No state local to the
laptop: this file only DEFINES the app.
Catch-ledger context: multi-scale qcore families are NESTED (an order-2M
coset is two order-M cosets), so the deduped plateau at a cell is the finest
admissible scale's C(N-1,h) ALONE — instrument reads use deduped floors.
"""
import modal

app = modal.App("rs-mca-rh-witness-census")
image = modal.Image.debian_slim().pip_install("numpy", "sympy")


def _first_primes_1mod(mod, count, start):
    from sympy import isprime
    out, x = [], start + (mod + 1 - start % mod) % mod
    if x % mod != 1: x += mod - (x - 1) % mod
    while len(out) < count:
        if x % mod == 1 and isprime(x): out.append(x)
        x += mod
    return out


@app.function(image=image, cpu=8.0, memory=65536, timeout=3600 * 4)
def zero_sum_ladder(N2: int, h: int, q_list: list):
    """Exact zero-sum census at quotient scale N2 (mu_{N2} in F_q minus one
    antipodal pair; h-subsets with e1 = 0). DP state: (size <= h) x q int64
    counts — RAM = (h+1) * q * 8 bytes (20 GB at q = 1.5e8, h = 16: OK on the
    64 GB worker). Counts <= C(30,16) = 1.45e8 << 2^63: int64 exact."""
    import numpy as np
    from math import comb
    results = []
    for q in q_list:
        # order-N2 element via cofactor method
        co = (q - 1) // N2
        g = None
        for g0 in range(2, 100000):
            c = pow(g0, co, q)
            if pow(c, N2 // 2, q) != 1:
                g = c; break
        assert g is not None
        pts = [pow(g, i, q) for i in range(N2)]
        assert len(set(pts)) == N2
        b = pts[0]; mb = (q - b) % q
        avail = [x for x in pts if x not in (b, mb)]
        assert len(avail) == N2 - 2
        # DP: T[s] = int64 array over F_q; T[s][v] = #s-subsets with sum v
        T = [np.zeros(q, dtype=np.int64) for _ in range(h + 1)]
        T[0][0] = 1
        for a in avail:
            for s in range(min(h, N2), 0, -1):
                T[s] += np.roll(T[s - 1], a)
        zerosum = int(T[h][0])
        floor = comb(N2 // 2 - 1, h // 2)
        starved = q > comb(N2 - 2, h)
        results.append(dict(q=q, N2=N2, h=h, zerosum=zerosum, floor=floor,
                            sporadic=zerosum - floor, starved=starved,
                            naive_expect=round(comb(N2 - 2, h) / q, 3)))
        del T
    return results


@app.function(image=image, cpu=8.0, memory=32768, timeout=3600 * 6)
def fiber_census(n: int, q: int, t: int, msub: int):
    """Full moment-map fiber table over F_q^t at rate 1/2 (k = n/2,
    s = k + t): CRT-DP over all n domain elements. Table: (s+1) x q^t per
    CRT prime (n=128,q=257,t=3: 68 x 1.7e7 x 8B = 9.2 GB; passes sequential).
    Series update per element a: c'_j = c_j - a*c_{j-1} — an index shear on
    the flat F_q^t array (vectorized gather). Reads R2a-R2d."""
    import numpy as np
    from math import comb
    k = n // 2; s_sz = k + t
    CRT = [(1 << 61) - 1, (1 << 61) - 31, (1 << 61) - 165]  # pairwise coprime
    co = (q - 1) // n
    g = None
    for g0 in range(2, 100000):
        c = pow(g0, co, q)
        if pow(c, n // 2, q) != 1:
            g = c; break
    D = [pow(g, i, q) for i in range(n)]
    assert len(set(D)) == n
    Hm = [pow(g, (n // msub) * i, q) for i in range(msub)]
    T0 = Hm[:t]
    # target fiber label: series of L_T0 mod z^(t+1)
    def series_of(pts):
        ser = [0] * t
        for a in pts:
            prev = 1
            out = []
            for j in range(t):
                out.append((ser[j] - a * prev) % q)
                prev = ser[j]
            ser = out
        return tuple(ser)
    target = series_of(T0)
    Qt = q ** t
    def flat(cvec):
        ix = 0
        for c in cvec: ix = ix * q + c
        return ix
    # index shear for element a: new_index(c) where c'_j = c_j - a*c_{j-1}
    # build once per a as an int64 gather map (vectorized, chunked)
    def shear_map(a):
        idx = np.arange(Qt, dtype=np.int64)
        digs = []
        r = idx
        for _ in range(t):
            digs.append(r % q); r //= q
        digs = digs[::-1]              # c1..ct
        prev = np.full(Qt, 1, dtype=np.int64)
        out = np.zeros(Qt, dtype=np.int64)
        for j in range(t):
            dj = (digs[j] - a * prev) % q
            out = out * q + dj
            prev = digs[j]
        return out
    fiber_mod, maxinfo = [], []
    for p in CRT:
        Tab = [np.zeros(Qt, dtype=np.int64) for _ in range(s_sz + 1)]
        Tab[0][flat((0,) * t)] = 1
        for a in D:
            mp = shear_map(a)
            for s in range(min(s_sz, n), 0, -1):
                contrib = np.zeros(Qt, dtype=np.int64)
                np.add.at(contrib, mp, Tab[s - 1])
                Tab[s] = (Tab[s] + contrib) % p
        final = Tab[s_sz]
        fiber_mod.append(int(final[flat(target)]))
        am = int(np.argmax(final))       # mod-p max is NOT the true max:
        maxinfo.append((am, int(final[am])))  # reconstruct via CRT below
        del Tab
    # CRT reconstruct target fiber (true count < product of primes)
    from sympy.ntheory.modular import crt
    fiber = int(crt(CRT, fiber_mod)[0])
    N = n // msub
    dedup_floor = comb(N - 1, k // msub)
    return dict(n=n, q=q, t=t, msub=msub, target=list(target),
                qcore_fiber=fiber, dedup_floor=dedup_floor,
                background_expect=float(comb(n, s_sz)) / q ** t,
                regime="RICH" if q ** t < comb(n, s_sz) else "STARVED",
                note="max-fiber scan requires a second pass with consistent "
                     "CRT argmax; emitted per-prime argmax for triage",
                per_prime_argmax=maxinfo)


@app.local_entrypoint()
def main():
    import json
    from math import comb
    # ---- Instrument 1: zero-sum ladders (quotient level of n = 128 / 256) --
    # n = 128 -> M2 = 4, N2 = 32, h = 16; starved crossing at q > C(30,16).
    qs_small = _first_primes_1mod(128, 24, 257)          # rich -> transition
    qs_mid = _first_primes_1mod(128, 6, 10 ** 6)         # deep transition
    qs_starved = _first_primes_1mod(128, 4, 2 * 10 ** 8) # STARVED (q > 1.45e8)
    r1 = zero_sum_ladder.remote(32, 16, qs_small + qs_mid + qs_starved)
    print(json.dumps({"instrument1_N2_32": r1}, indent=1))
    # n = 256 -> N2 = 64, h = 32 (starved unreachable: fit-only ladder)
    qs256 = _first_primes_1mod(256, 16, 257) + _first_primes_1mod(256, 4, 10 ** 6)
    r1b = zero_sum_ladder.remote(64, 32, qs256)
    print(json.dumps({"instrument1_N2_64": r1b}, indent=1))
    # ---- Instrument 2: full fiber tables (RICH regime — label mandatory) ---
    jobs = [(128, 257, 2, 4), (128, 257, 3, 4), (128, 769, 2, 4),
            (256, 257, 2, 4), (256, 769, 2, 4)]
    for (n, q, t, msub) in jobs:
        r2 = fiber_census.remote(n, q, t, msub)
        print(json.dumps({"instrument2": r2}, indent=1))
    print("REMINDER: reads R1a-R1d / R2a-R2d are PRE-REGISTERED in the module "
          "docstring; regime labels are mandatory in any banked quote.")
