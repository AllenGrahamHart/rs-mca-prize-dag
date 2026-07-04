#!/usr/bin/env python3
r"""
Modal dispatch job for node: midlarge_h7_20.

============================ PRE-REGISTERED SPEC ============================
(quoted verbatim from prize/nodes/midlarge_h7_20/statement.md)

  "The scannable band h in (6, 20]: zero active cores at official-shape rows.
   EVIDENCE WALL: the pre-registered scan -- C1b-descent pipelines at n <= 256
   calibration rows plus MITM slices at n = 1024, h = 7..20; interpretation
   fixed before data: any active core found is charged and counted against the
   3.3e3/h budget; zero across calibrations licenses the exclusion lemma
   attempt."

  Falsifier: "an active core at h in (7,20] at any calibration row."
============================================================================

CONSTRUCTION (faithful to the banked C1a MITM machinery
experimental/scripts/verify_c1a_lowh_mitm.py and the h=3 census
verify_x12_h3_active_core_census.py):

  Row = (mu_n subset F_p) with n a power of two, p == 1 mod n, at q ~ n^2 and
  q ~ n^3 (the x12 calibration regime).  A minimal h-trade = two DISJOINT
  h-subsets P, Q of mu_n with equal elementary-symmetric signature
  e_1..e_{h-1} of their locators and e_h(P) != e_h(Q).  An ACTIVE (non-toral)
  core = a trade whose halves are NOT both single mu_h-cosets (the paid toral
  fiber class).  The scan counts non-toral active cores at h = 7..20.

  METHOD.  Anchored meet-in-the-middle (exactly verify_c1a_lowh_mitm.mitm_census):
  hash side = anchored (h-1)-subsets {0} u subset of [1,W); probe side = h-subsets
  of [1,W).  With W = n this is the COMPLETE per-orbit census; with W < n it is a
  genuine EXHAUSTIVE sub-census over the first W roots (finds every trade whose
  2h-support lies in [0,W)) -- the c1a "spot slice" used for n=1024.  Any
  anchored non-toral trade = a falsifier.  Per-config wall-time budget so the job
  always terminates and reports.

SCOPE HONESTY: the spec names "C1b-descent pipelines at n<=256"; this job uses
the banked & gate-validated MITM census (complete at feasible small n, window
slice otherwise) across n in {16,32,64,128,256,1024} for BOTH q~n^2 and q~n^3.
It is the same census object (c1a note sec 2.2 proves route (a) == the MITM
count); it does not reimplement the separate C1b descent enumerator.

CORRECTNESS GATE (banked ground truth, must pass in-cloud before the scan):
  full_census(16,3,17)=352 trades; full_census(16,3,97)=16 trades;
  full_census(128,3,17921)=18 anchored cores; full_census(256,3,65537)=129;
  full_census(16,4,17): 120 non-toral + 6 toral (exceptional prime -- the
  DECISIVE non-toral detection);  full_census(32,5,97): 96 trades.

Self-contained (stdlib only).  Prints one JSON line prefixed with the node name.
"""

import modal
import json
import time
import itertools
from math import comb

app = modal.App("rs-mca-midlarge_h7_20")
image = modal.Image.debian_slim()

_SMALL_PRIMES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)


def is_prime(m):
    m = int(m)
    if m < 2:
        return False
    for q in _SMALL_PRIMES:
        if m % q == 0:
            return m == q
    d = m - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1
    for a in _SMALL_PRIMES:
        x = pow(a, d, m)
        if x == 1 or x == m - 1:
            continue
        for _ in range(r - 1):
            x = x * x % m
            if x == m - 1:
                break
        else:
            return False
    return True


def next_prime_1mod(n, start):
    t = (start - 1) // n
    if t < 1:
        t = 1
    while True:
        p = 1 + n * t
        if p >= start and is_prime(p):
            return p
        t += 1


def mu_n_generator(p, n):
    assert (p - 1) % n == 0
    e = (p - 1) // n
    a = 2
    while True:
        z = pow(a, e, p)
        if pow(z, n // 2, p) != 1:
            return z
        a += 1


def sig_general(exps, pw, p, h):
    coef = [1] + [0] * h
    for a in exps:
        r = pw[a]
        for j in range(h, 0, -1):
            coef[j] = (coef[j] - r * coef[j - 1]) % p
    e = tuple(((-coef[j]) % p if (j & 1) else coef[j]) for j in range(1, h))
    e_h = (-coef[h]) % p if (h & 1) else coef[h]
    return e, e_h


def is_coset(A, h, n):
    if n % h:
        return False
    step = n // h
    r0 = A[0] % step
    return sorted(A) == sorted((r0 + j * step) % n for j in range(h))


def full_census(n, h, p, z=None):
    if z is None:
        z = mu_n_generator(p, n)
    pw = [pow(z, a, p) for a in range(n)]
    buckets = {}
    for A in itertools.combinations(range(n), h):
        sig, eh = sig_general(A, pw, p, h)
        buckets.setdefault(sig, []).append((A, eh))
    unordered = toral = nontoral = 0
    anchored_cores = set()
    for lst in buckets.values():
        if len(lst) < 2:
            continue
        for i in range(len(lst)):
            Ai, ea = lst[i]
            sAi = set(Ai)
            for j in range(i + 1, len(lst)):
                Bj, eb = lst[j]
                if sAi & set(Bj):
                    continue
                if ea == eb:
                    continue
                unordered += 1
                if is_coset(Ai, h, n) and is_coset(Bj, h, n):
                    toral += 1
                else:
                    nontoral += 1
                if 0 in Ai:
                    anchored_cores.add(Ai)
                if 0 in Bj:
                    anchored_cores.add(Bj)
    return {"n": n, "h": h, "unordered_trades": unordered, "toral": toral,
            "nontoral": nontoral, "anchored_cores": len(anchored_cores)}


def _pack(exps):
    v = 0
    for a in exps:
        v = (v << 11) | a
    return v


def mitm_slice(n, h, p, z=None, W=None, time_budget=None):
    """Anchored MITM over window [0,W). Complete iff W==n. Returns anchored
    non-toral / toral counts + a witness list. Time budget aborts safely and
    flags incomplete (never silently claims 0)."""
    if z is None:
        z = mu_n_generator(p, n)
    if W is None:
        W = n
    W = min(W, n)
    pw = [pow(z, a, p) for a in range(n)]
    t0 = time.time()
    aborted = False

    # Phase 1: hash side
    table = {}
    n_hash = 0
    for tri in itertools.combinations(range(1, W), h - 1):
        exps = (0,) + tri
        sig, _ = sig_general(exps, pw, p, h)
        cur = table.get(sig)
        packed = _pack(tri)
        if cur is None:
            table[sig] = packed
        elif isinstance(cur, int):
            table[sig] = [cur, packed]
        else:
            cur.append(packed)
        n_hash += 1
        if time_budget and (n_hash & 0x3FFF) == 0 and time.time() - t0 > time_budget * 0.5:
            aborted = True
            break

    def unpack(v, k):
        out = []
        for _ in range(k):
            out.append(v & 0x7FF)
            v >>= 11
        return tuple(reversed(out))

    # Phase 2: probe side
    n_probe = 0
    anc_toral = anc_nontoral = 0
    witnesses = []
    if not aborted:
        for Q in itertools.combinations(range(1, W), h):
            sig, eh = sig_general(Q, pw, p, h)
            n_probe += 1
            packed = table.get(sig)
            if packed is not None:
                for cand in (packed if isinstance(packed, list) else [packed]):
                    Ptri = unpack(cand, h - 1)
                    Pexps = (0,) + Ptri
                    psig, pe_h = sig_general(Pexps, pw, p, h)
                    if psig != sig:
                        continue
                    if set(Pexps) & set(Q):
                        continue
                    if pe_h == eh:
                        continue
                    if is_coset(Pexps, h, n) and is_coset(Q, h, n):
                        anc_toral += 1
                    else:
                        anc_nontoral += 1
                        if len(witnesses) < 8:
                            witnesses.append({"P": list(Pexps), "Q": list(Q)})
            if time_budget and (n_probe & 0x3FFF) == 0 and time.time() - t0 > time_budget:
                aborted = True
                break
    complete = (W == n) and not aborted
    return {"n": n, "h": h, "W": W, "complete": complete, "aborted": aborted,
            "n_hash": n_hash, "n_probe": n_probe,
            "anchored_nontoral": anc_nontoral, "anchored_toral": anc_toral,
            "witnesses": witnesses}


def run_gate():
    fails = []

    def ck(name, cond, got=""):
        if not cond:
            fails.append(f"{name} :: {got}")

    r = full_census(16, 3, 17)
    ck("h3 n16 F17 = 352 trades", r["unordered_trades"] == 352, r["unordered_trades"])
    r = full_census(16, 3, 97)
    ck("h3 n16 F97 = 16 trades", r["unordered_trades"] == 16, r["unordered_trades"])
    r = full_census(128, 3, 17921)
    ck("h3 n128 p17921 = 18 anchored cores", r["anchored_cores"] == 18, r["anchored_cores"])
    r = full_census(256, 3, 65537)
    ck("h3 n256 p65537 = 129 anchored cores", r["anchored_cores"] == 129, r["anchored_cores"])
    r = full_census(16, 4, 17)
    ck("h4 n16 F17 = 120 nontoral + 6 toral (decisive nontoral detection)",
       r["nontoral"] == 120 and r["toral"] == 6, (r["nontoral"], r["toral"]))
    r = full_census(32, 5, 97)
    ck("h5 n32 F97 = 96 trades", r["unordered_trades"] == 96, r["unordered_trades"])
    return {"gate_pass": len(fails) == 0, "gate_fails": fails}


def scan(total_budget_s=8600.0):
    hs = list(range(7, 21))
    ns = [16, 32, 64, 128, 256, 1024]
    # per-config subset-count ceiling to keep each cell feasible
    COUNT_CEIL = 6_000_000
    # build config list first (to divide the time budget)
    configs = []
    for h in hs:
        for n in ns:
            if n < 2 * h:
                continue
            for exp in (2, 3):
                configs.append((h, n, exp))
    budget_per = total_budget_s / max(1, len(configs))

    out = []
    for (h, n, exp) in configs:
        p = next_prime_1mod(n, n ** exp)
        z = mu_n_generator(p, n)
        # choose window W: largest with C(W-1,h-1)+C(W,h) <= COUNT_CEIL, capped at n
        W = 2 * h
        best = W
        w = 2 * h
        while w <= n:
            cost = comb(w - 1, h - 1) + comb(w, h)
            if cost <= COUNT_CEIL:
                best = w
                w += 1
            else:
                break
        W = best
        res = mitm_slice(n, h, p, z=z, W=W, time_budget=budget_per)
        res["q_exp"] = exp
        res["p"] = p
        out.append(res)

    falsifiers = [r for r in out if r["anchored_nontoral"] > 0]
    complete_zero = [r for r in out if r["complete"] and r["anchored_nontoral"] == 0]
    return {
        "h_range": [7, 20],
        "n_list": ns,
        "count_ceiling": COUNT_CEIL,
        "per_config": out,
        "num_configs": len(out),
        "num_complete_zero": len(complete_zero),
        "num_aborted_incomplete": sum(1 for r in out if r["aborted"]),
        "falsifiers_nontoral_active_cores": falsifiers,
        "overall_verdict": ("FALSIFIER_ACTIVE_CORE_FOUND" if falsifiers
                            else "ZERO_ACTIVE_CORES_EXCLUSION_SUPPORTED"),
    }


@app.function(image=image, cpu=4, memory=8192, timeout=10800)
def run():
    gate = run_gate()
    if not gate["gate_pass"]:
        result = {"node": "midlarge_h7_20", "status": "GATE_FAILED", "gate": gate}
        print("midlarge_h7_20 " + json.dumps(result), flush=True)
        return result
    sc = scan()
    result = {"node": "midlarge_h7_20", "status": "OK", "gate": gate, "scan": sc}
    print("midlarge_h7_20 " + json.dumps(result), flush=True)
    return result


@app.local_entrypoint()
def main():
    call = run.spawn()
    print("SPAWNED midlarge_h7_20 fc_id=" + str(call.object_id))
