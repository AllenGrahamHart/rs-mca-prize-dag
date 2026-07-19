#!/usr/bin/env python3
"""ENDPOINT-EXC adversarial round (round 1) — the round's checks, replayable.

Attacks the M3 pose (M3_ENDPOINT_EXCEPTION_COVERAGE.md, wave-4 import):
the 6-item per-row endpoint-exception certificate + the soundness implication
    VERIFY_ENDPOINT_EXC(R,pi_R)=ACCEPT ==> q^{-t+H} W_cen(R) <= 2^121
+ the (open) universal coverage obligation ENDPOINT-EXC-COVERAGE.

Toy model = the repo's own exact conventions (A1_PROD_NORM_SIEVE.md,
modal_dli_orbit_census.py): level (n'=2N, L), admissible q = 1 mod n',
pinned omega = g^((q-1)/n') (g = smallest primitive root), kernel
K_q = {ternary d != 0 : D(omega^(2l-1)) = 0 mod q, l = 1..L},
W_cov = sum over kernel d with L+1 <= w(d) <= w_cov of 2^-w(d) (elementwise),
orbit = signed-shift class under t (t^N = -1), quantum 2N.

Cells (pre-registered in eex_findings.md SECTION 1):
  CELL_A   n'=16 (N=8), full exhaustive ground truth, band q<=2000, L=1,2,3
           (includes q=17, 97 — the mission-flagged exceptional pair)
  CELL_B   n'=32 (N=16), grouped-MITM exact ground truth, band q<=10000, L=1,2
  CELL_C   n'=64 (N=32), banked rows q=193, 7937, 110849, 204353 (Modal)
  ABUSE    the 8-certificate abuse battery + fail-closed demos (at q=97 sched)
  MARKOV   A1-PROD weighted-Markov band replay at toy scale (exact)

Kill lines K1/K2/K3a-K3d: see eex_findings.md SECTION 1.
Run:  tools/ramguard tiny -- python3 eex_verify.py CELL_A ABUSE MARKOV
      tools/ramguard tiny -- python3 eex_verify.py CELL_B
      tools/ramguard modal -- ~/.venvs/modal/bin/modal run \
          tools/modal_run_script.py --script <this> --args "CELL_C"
"""
import json
import math
import sys
from fractions import Fraction
from itertools import combinations, product

# ---------------------------------------------------------------- arithmetic
def is_prime(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1 if d == 2 else 2
    return True


def factor(n):
    fs, d = {}, 2
    while d * d <= n:
        while n % d == 0:
            fs[d] = fs.get(d, 0) + 1
            n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        fs[n] = fs.get(n, 0) + 1
    return fs


def smallest_primitive_root(q):
    fs = list(factor(q - 1))
    g = 2
    while True:
        if all(pow(g, (q - 1) // p, q) != 1 for p in fs):
            return g
        g += 1


def pinned_omega(q, nprime):
    return pow(smallest_primitive_root(q), (q - 1) // nprime, q)


def mult_order(x, q, bound):
    for k in range(1, bound + 1):
        if pow(x, k, q) == 1:
            return k
    return None


def band_primes(nprime, qmax):
    return [q for q in range(nprime + 1, qmax + 1, nprime) if is_prime(q)]


# --------------------------------------------------------------- enumeration
def half_vectors(nh, wmax, offset):
    """All ternary vectors on coords offset..offset+nh-1 with weight<=wmax.
    Yields (exponents tuple (absolute), signs tuple, weight)."""
    out = [((), (), 0)]
    for w in range(1, wmax + 1):
        for sup in combinations(range(nh), w):
            asup = tuple(e + offset for e in sup)
            for sgn in product((1, -1), repeat=w):
                out.append((asup, sgn, w))
    return out


def residue(sup, sgn, pw, q):
    s = 0
    for e, c in zip(sup, sgn):
        s += c * pw[e]
    return s % q


def weight_hist_mitm(N, Lmax, q, omega, half_wmax=None):
    """Exact per-weight kernel counts for L = 1..Lmax simultaneously.
    Returns {L: {w: count}} over w <= 2*half_wmax (or full N).
    Grouped meet-in-middle on halves of size N/2."""
    nh = N // 2
    hw = half_wmax if half_wmax is not None else nh
    pw = [pow(omega, e, q) for e in range(N)]
    pwl = [[pow(pw[e], 2 * l - 1, q) for e in range(N)] for l in range(1, Lmax + 1)]
    left = half_vectors(nh, hw, 0)
    right = half_vectors(nh, hw, nh)
    res = {}
    for L in range(1, Lmax + 1):
        dl, dr = {}, {}
        for side, d in ((left, dl), (right, dr)):
            for sup, sgn, w in side:
                key = tuple(residue(sup, sgn, pwl[l], q) for l in range(L))
                d.setdefault(key, [0] * (hw + 1))[w] += 1
        hist = {}
        for key, cl in dl.items():
            nkey = tuple((-r) % q for r in key)
            cr = dr.get(nkey)
            if cr is None:
                continue
            for w1, a in enumerate(cl):
                if a:
                    for w2, b in enumerate(cr):
                        if b:
                            hist[w1 + w2] = hist.get(w1 + w2, 0) + a * b
        hist[0] = hist.get(0, 0) - 1  # remove the zero vector
        res[L] = {w: c for w, c in sorted(hist.items()) if c}
    return res


def kernel_vectors_direct(N, L, q, omega, wmax):
    """All kernel vectors with 1 <= w <= wmax, by direct enumeration."""
    pwl = [[pow(omega, (2 * l - 1) * e, q) for e in range(N)]
           for l in range(1, L + 1)]
    out = []
    for w in range(1, wmax + 1):
        for sup in combinations(range(N), w):
            for sgn in product((1, -1), repeat=w):
                if all(residue(sup, sgn, pwl[l], q) == 0 for l in range(L)):
                    out.append((sup, sgn, w))
    return out


# ------------------------------------------------------------------- orbits
def to_coeffs(sup, sgn, N):
    v = [0] * N
    for e, c in zip(sup, sgn):
        v[e] = c
    return tuple(v)


def shift1(v, N):
    return tuple([-v[N - 1]] + list(v[:N - 1]))


def orbit_of(v, N):
    seen, cur = [], v
    for _ in range(2 * N):
        seen.append(cur)
        cur = shift1(cur, N)
        if cur == v:
            break
    return seen


def orbit_key(v, N):
    return min(orbit_of(v, N))


# ------------------------------------------- the toy 6-item certificate rule
REJECTED_TYPES = {"likely_nonexceptional", "ppt_hardness", "no_known_construction"}


def build_certificate(nprime, q, levels, w_led, w_cov, T, hists, vec_lists):
    """Honest pi_R. hists: {L:{w:count}} exact; vec_lists: {L: kernel vectors
    w<=w_led}. Completeness realized by exhaustive enumeration (toy scale)."""
    N = nprime // 2
    omega = pinned_omega(q, nprime)
    cert = {
        "item1": {"nprime": nprime, "q": q, "omega": omega,
                  "field": "F_q", "generated_field": "F_q",
                  "primality": "trial_division", "order_claim": nprime},
        "item2": {}, "item3": {}, "item4": {},
        "item5": {"owners": {}, "reserve_bits": 21, "reserve_credits": []},
        "item6": {"method": "exact_rational",
                  "T": [T.numerator, T.denominator]},
        "levels": levels, "w_led": w_led, "w_cov": w_cov,
    }
    for L in levels:
        orbs = {}
        for sup, sgn, w in vec_lists[L]:
            if L + 1 <= w <= w_led:
                k = orbit_key(to_coeffs(sup, sgn, N), N)
                if k not in orbs:
                    orbs[k] = (w, len(orbit_of(k, N)))
        cert["item2"][L] = {"orbits": [[list(k), w, s]
                                       for k, (w, s) in sorted(orbs.items())],
                            "completeness": "exhaustive_enumeration_toy"}
        cert["item3"][L] = {"dedup": "orbit_keys_distinct_sizes_exact",
                            "quantum": 2 * N}
        resid = {}
        for w in range(w_led + 1, w_cov + 1):
            c = hists[L].get(w, 0)
            resid[w] = {"U_num": c, "U_den": 2 ** w,
                        "proof_type": "exhaustive_recount_toy"}
        cert["item4"][L] = resid
        for w in range(L + 1, w_cov + 1):
            listed = w <= w_led
            mass_pos = hists[L].get(w, 0) > 0
            owner = "accident" if (w == L + 1 and mass_pos) else "bulk"
            cert["item5"]["owners"][f"L{L}w{w}{'led' if listed else 'res'}"] = owner
    return cert


def _lv(d, L):
    """Level access tolerant of JSON round-trips (int vs str keys)."""
    return d[L] if L in d else d[str(L)]


def verify_certificate(cert, T_check=None):
    """Fail-closed toy VERIFY_ENDPOINT_EXC. Recomputes everything it checks.
    Returns (verdict, fired_clauses, total_certified_Fraction)."""
    fired = []
    nprime, q = cert["item1"]["nprime"], cert["item1"]["q"]
    N = nprime // 2
    # ---- item 1: row key / field / primality-order certificates
    if not is_prime(q):
        fired.append("item1:primality")
    if q % nprime != 1:
        fired.append("item1:splitting q!=1 mod n'")
    if cert["item1"]["omega"] != pinned_omega(q, nprime):
        fired.append("item1:omega_pin")
    if mult_order(cert["item1"]["omega"], q, nprime) != nprime:
        fired.append("item1:omega_order")
    if cert["item1"]["field"] != "F_q" or cert["item1"]["generated_field"] != "F_q":
        fired.append("item1:generated_field_normalization")
    omega = pinned_omega(q, nprime)
    total = Fraction(0)
    for L in cert["levels"]:
        w_led, w_cov = cert["w_led"], cert["w_cov"]
        # independent exhaustive re-enumeration (the completeness check)
        vecs = kernel_vectors_direct(N, L, q, omega, w_led)
        # K3a floor guard: weights <= L must be empty
        if any(w <= L for _, _, w in vecs):
            fired.append(f"item2:L{L}:FLOOR_BREAK_w<=L")
        true_orbs = {}
        for sup, sgn, w in vecs:
            if L + 1 <= w <= w_led:
                k = orbit_key(to_coeffs(sup, sgn, N), N)
                true_orbs.setdefault(k, (w, len(orbit_of(k, N))))
        led = {tuple(k): (w, s) for k, w, s in _lv(cert["item2"], L)["orbits"]}
        if set(led) != set(true_orbs):
            fired.append(f"item2:L{L}:ledger_incomplete_or_spurious")
        for k, (w, s) in led.items():
            if k in true_orbs and true_orbs[k] != (w, s):
                fired.append(f"item3:L{L}:orbit_size_not_exact")
            if len(orbit_of(k, N)) != 2 * N:
                fired.append(f"item3:L{L}:quantum!=2N")
        if len(led) != len({orbit_key(k, N) for k in led}):
            fired.append(f"item3:L{L}:duplicate_orbits")
        # listed mass from the CERT's own ledger (what the cert prices)
        listed_mass = sum(Fraction(s, 2 ** w) for (w, s) in led.values())
        # ---- item 4: residual classes — quantifier + independent check
        resid = _lv(cert["item4"], L)
        want = set(range(w_led + 1, w_cov + 1))
        have = {int(w) for w in resid}
        if have != want:
            fired.append(f"item4:L{L}:unlisted_class_missing")
        rmass = Fraction(0)
        for w in sorted(have & want):
            r = resid[str(w)] if str(w) in resid else resid[w]
            if r["proof_type"] in REJECTED_TYPES:
                fired.append(f"item4:L{L}:rejected_certificate_type")
            U = Fraction(r["U_num"], r["U_den"])
            # independently checkable: exact recount of the class mass
            cnt = count_class_exact(N, L, q, omega, w)
            if U < Fraction(cnt, 2 ** w):
                fired.append(f"item4:L{L}w{w}:residual_bound_false")
            rmass += U
        total += listed_mass + rmass
    # ---- item 5: ownership ledger + reserve charged once
    owners = cert["item5"]["owners"]
    for L in cert["levels"]:
        for w in range(L + 1, cert["w_cov"] + 1):
            tag = f"L{L}w{w}{'led' if w <= cert['w_led'] else 'res'}"
            if sum(1 for k in owners if k == tag) != 1:
                fired.append(f"item5:bucket_{tag}_not_owned_once")
            elif owners[tag] not in ("coset", "bulk", "accident"):
                fired.append(f"item5:bad_owner_{tag}")
    if len(cert["item5"]["reserve_credits"]) > 1:
        fired.append("item5:reserve_charged_more_than_once")
    for c in cert["item5"]["reserve_credits"]:
        total -= Fraction(c[0], c[1])
    # ---- item 6: exact rational final check
    if cert["item6"]["method"] != "exact_rational":
        fired.append("item6:not_exact_rational")
    T = Fraction(cert["item6"]["T"][0], cert["item6"]["T"][1])
    if T_check is not None and T != T_check:
        fired.append("item6:threshold_mismatch")
    if total > T:
        fired.append("item6:endpoint_exceeded")
    return ("ACCEPT" if not fired else "REJECT"), fired, total


_CLASS_CACHE = {}


def count_class_exact(N, L, q, omega, w):
    """Exact count of kernel vectors of weight exactly w (independent path:
    MITM for the whole histogram, cached)."""
    key = (N, L, q)
    if key not in _CLASS_CACHE:
        hw = min(N // 2, max(6, 0)) if N >= 32 else N // 2
        _CLASS_CACHE[key] = weight_hist_mitm(N, L, q, omega, half_wmax=hw)[L]
    return _CLASS_CACHE[key].get(w, 0)


def ground_truth(nprime, q, levels, w_cov, hists):
    N = nprime // 2
    t = Fraction(0)
    for L in levels:
        for w in range(L + 1, w_cov + 1):
            t += Fraction(hists[L].get(w, 0), 2 ** w)
    return t


# --------------------------------------------------------------------- cells
def make_row(nprime, q, levels, w_led, w_cov, half_wmax=None):
    N = nprime // 2
    omega = pinned_omega(q, nprime)
    Lmax = max(levels)
    hists = weight_hist_mitm(N, Lmax, q, omega, half_wmax=half_wmax)
    _CLASS_CACHE.update({(N, L, q): hists[L] for L in levels})
    vecs = {L: kernel_vectors_direct(N, L, q, omega, w_led) for L in levels}
    return omega, hists, vecs


def run_band_cell(name, nprime, qmax, levels, w_led, w_cov):
    """Score every band row at BOTH pre-registered thresholds:
    T = 1 (production analog) and T_mf = 2*MF (mean-field-scaled) —
    pre-run amendment 1 in eex_findings.md."""
    N = nprime // 2
    rows, kill = [], []
    for q in band_primes(nprime, qmax):
        omega, hists, vecs = make_row(nprime, q, levels, w_led, w_cov)
        for L in levels:
            # K3a floor
            floor_ok = all(hists[L].get(w, 0) == 0 for w in range(1, L + 1))
            if not floor_ok:
                kill.append(f"K3a FLOOR BREAK at {name} q={q} L={L}")
            wt = ground_truth(nprime, q, [L], w_cov, hists)
            mf = Fraction(sum(math.comb(N, w)
                              for w in range(L + 1, w_cov + 1)), q)
            verdicts = {}
            for tag, T in (("T1", Fraction(1)), ("Tmf", 2 * mf)):
                cert = build_certificate(nprime, q, [L], w_led, w_cov, T,
                                         hists, vecs)
                verdict, fired, tot = verify_certificate(cert, T_check=T)
                truth_ok = (wt <= T)
                # K2: verdict must match exact truth (honest tight cert)
                if (verdict == "ACCEPT") != truth_ok:
                    kill.append(f"K2 verdict/truth mismatch {name} q={q} "
                                f"L={L} {tag} verdict={verdict} "
                                f"truth={float(wt):.4f}")
                # K1(ii) soundness oracle on every ACCEPT
                if verdict == "ACCEPT" and wt > T:
                    kill.append(f"K1 SOUNDNESS HOLE {name} q={q} L={L} {tag}")
                if tot != wt:
                    kill.append(f"cert-total!=truth {name} q={q} L={L} "
                                f"(honest cert must be tight)")
                verdicts[tag] = verdict
            rows.append({"q": q, "L": L,
                         "W_num": wt.numerator, "W_den": wt.denominator,
                         "W": round(float(wt), 6), "MF": round(float(mf), 6),
                         "verdict": verdicts["T1"],
                         "verdict_mf": verdicts["Tmf"],
                         "min_w": min([w for w in hists[L]] or [None]),
                         "hist": {str(w): c for w, c in hists[L].items()
                                  if w <= w_cov}})
    return rows, kill


def cell_A():
    print("== CELL A: n'=16 (N=8), full exhaustive, band q<=2000, L=1,2,3 ==")
    rows, kill = run_band_cell("A", 16, 2000, [1, 2, 3], 5, 8)
    # cross-validation: direct enumeration vs MITM at two rows
    for q in (17, 97):
        omega = pinned_omega(q, 16)
        direct = {}
        for sup, sgn, w in kernel_vectors_direct(8, 1, q, omega, 8):
            direct[w] = direct.get(w, 0) + 1
        mitm = weight_hist_mitm(8, 1, q, omega)[1]
        ok = all(mitm.get(w, 0) == direct.get(w, 0)
                 for w in range(1, 9))
        print(f"  xval direct==MITM at q={q}: {'PASS' if ok else 'FAIL'}")
        if not ok:
            kill.append(f"XVAL FAIL q={q}")
    for r in rows:
        if r["q"] in (17, 97, 113, 193) or r["verdict"] == "REJECT":
            print(f"  q={r['q']:>5} L={r['L']} W_cov={r['W']:<10} "
                  f"min_w={r['min_w']} verdict={r['verdict']}")
    # exceptionality ranking within the band (per L): where do 17, 97 sit?
    for L in (1, 2, 3):
        sub = sorted((x for x in rows if x["L"] == L),
                     key=lambda x: -Fraction(x["W_num"], x["W_den"]))
        rank17 = [i for i, x in enumerate(sub) if x["q"] == 17]
        rank97 = [i for i, x in enumerate(sub) if x["q"] == 97]
        top = [(x["q"], x["W"]) for x in sub[:3]]
        print(f"  L={L}: band top-3 by W_cov: {top}; rank(q=17)="
              f"{rank17[0] if rank17 else '-'}, rank(q=97)="
              f"{rank97[0] if rank97 else '-'} of {len(sub)}")
    return {"rows": rows, "kill": kill}


def cell_B():
    print("== CELL B: n'=32 (N=16), MITM exact, band q<=10000, L=1,2 ==")
    rows, kill = run_band_cell("B", 32, 10000, [1, 2], 4, 8)
    worst = sorted(rows, key=lambda x: -Fraction(x["W_num"], x["W_den"]))[:5]
    for r in worst:
        print(f"  worst: q={r['q']:>5} L={r['L']} W_cov={r['W']} MF={r['MF']}"
              f" verdict_mf={r['verdict_mf']}")
    for r in rows:
        if r["q"] in (8353,):
            print(f"  banked F2b row q=8353: L={r['L']} W_cov={r['W']} "
                  f"MF={r['MF']} min_w={r['min_w']} "
                  f"verdict={r['verdict']}/{r['verdict_mf']}")
    n_rej = sum(1 for r in rows if r["verdict"] == "REJECT")
    n_rej_mf = sum(1 for r in rows if r["verdict_mf"] == "REJECT")
    print(f"  band rows={len(rows)}, REJECT(T=1)={n_rej}, "
          f"REJECT(Tmf)={n_rej_mf}")
    return {"rows": rows, "kill": kill}


def cell_C():
    """CELL C, K3d checks CORRECTED after the first-run audit (see
    eex_findings.md RUN 4): the banked cluster 'k_indep' counts independent
    components across the WHOLE w<=5 window (band_census_and_clusters.json:
    204353 has n_gens=10 = total w<=5 orbits, z_rank=9, k_indep=7;
    110849 has n_gens=4 = its 4 w5 orbits). The first run's
    'w5 orbits >= k_indep' floor misread that convention and fired
    spuriously; replaced by the audited equalities below. Banked primitive
    counts at 193/7937 from m2_c1prime_level_scaled_results.json."""
    print("== CELL C: n'=64 (N=32), banked rows, w_cov=6, L=1 (Modal) ==")
    banked = {193: {"w3_primitive": 3, "w4_primitive": 46,
                    "w5_primitive": 529, "W_cl": 5763},
              7937: {"w3_primitive": 2, "w4_primitive": 8,
                     "w5_primitive": 31, "W_cl": 236},
              110849: {"n_gens_w_le5": 4},
              204353: {"n_gens_w_le5": 10, "k_indep": 7}}
    rows, kill = [], []
    for q in (193, 7937, 110849, 204353):
        omega, hists, vecs = make_row(64, q, [1], 4, 6, half_wmax=6)
        L = 1
        floor_ok = all(hists[L].get(w, 0) == 0 for w in range(1, L + 1))
        if not floor_ok:
            kill.append(f"K3a FLOOR BREAK C q={q}")
        wt = ground_truth(64, q, [L], 6, hists)
        mf = Fraction(sum(math.comb(32, w) for w in range(2, 7)), q)
        verdicts = {}
        for tag, T in (("T1", Fraction(1)), ("Tmf", 2 * mf)):
            cert = build_certificate(64, q, [L], 4, 6, T, hists, vecs)
            verdict, fired, tot = verify_certificate(cert, T_check=T)
            if tot != wt:
                kill.append(f"cert-total!=truth C q={q} {tag}")
            if (verdict == "ACCEPT") != (wt <= T):
                kill.append(f"K2 verdict/truth mismatch C q={q} {tag}")
            verdicts[tag] = verdict
        verdict = verdicts["T1"]
        # K3d census replay: w=3 orbit count must EQUAL banked primitive count
        orbs3 = {orbit_key(to_coeffs(s, g, 32), 32)
                 for s, g, w in vecs[1] if w == 3}
        orbs4 = {orbit_key(to_coeffs(s, g, 32), 32)
                 for s, g, w in vecs[1] if w == 4}
        b = banked[q]
        checks = {}
        c3, c4, c5 = (hists[1].get(w, 0) for w in (3, 4, 5))
        checks["counts_orbit_quantized"] = all(c % 64 == 0
                                               for c in (c3, c4, c5))
        if not checks["counts_orbit_quantized"]:
            kill.append(f"K3c w<=5 counts not orbit-quantized q={q}")
        if "w3_primitive" in b:
            checks["w3_orbits==banked"] = (len(orbs3) == b["w3_primitive"])
            checks["w4_orbits==banked"] = (len(orbs4) == b["w4_primitive"])
            checks["w5_orbits==banked"] = (c5 // 64 == b["w5_primitive"])
            for nm in ("w3_orbits==banked", "w4_orbits==banked",
                       "w5_orbits==banked"):
                if not checks[nm]:
                    kill.append(f"K3d census mismatch q={q}: {nm}")
        if "n_gens_w_le5" in b:
            tot_le5 = len(orbs3) + len(orbs4) + c5 // 64
            checks["orbits_w<=5==banked_n_gens"] = (tot_le5 == b["n_gens_w_le5"])
            if not checks["orbits_w<=5==banked_n_gens"]:
                kill.append(f"K3d n_gens mismatch q={q}: {tot_le5} vs "
                            f"{b['n_gens_w_le5']}")
            if "k_indep" in b:
                checks["k_indep<=orbits"] = (b["k_indep"] <= tot_le5)
                if not checks["k_indep<=orbits"]:
                    kill.append(f"K3d k_indep exceeds orbit count q={q}")
        # K3c quantum on every LEDGER orbit rep (sizes already exact-checked
        # inside verify_certificate; this is the direct quantum assertion)
        qua = all(s == 64 and len(orbit_of(tuple(k), 32)) == 64
                  for k, w, s in cert["item2"][1]["orbits"])
        if not qua:
            kill.append(f"K3c quantum break q={q}")
        rows.append({"q": q, "W_num": wt.numerator, "W_den": wt.denominator,
                     "W": round(float(wt), 6), "MF": round(float(mf), 3),
                     "verdict": verdicts["T1"], "verdict_mf": verdicts["Tmf"],
                     "hist": {str(w): c for w, c in hists[1].items()
                              if w <= 6},
                     "w3_orbits": len(orbs3), "w4_orbits": len(orbs4),
                     "checks": checks, "quantum_2N": qua})
        print(f"  q={q:>7} W_cov(w<=6)={float(wt):.4f} MF={float(mf):.4f} "
              f"verdicts={verdicts} hist={rows[-1]['hist']} "
              f"w3_orbits={len(orbs3)} checks={checks}")
    return {"rows": rows, "kill": kill}


# ------------------------------------------------------------- abuse battery
def abuse_battery():
    print("== ABUSE battery at q=97, n'=16, schedule L=[1,2,3] ==")
    print("   (two pre-registered configs: T=1 flip-risk / T=4 honest-ACCEPT)")
    nprime, q, levels, w_led, w_cov = 16, 97, [1, 2, 3], 5, 8
    omega, hists, vecs = make_row(nprime, q, levels, w_led, w_cov)
    wt = ground_truth(nprime, q, levels, w_cov, hists)
    results, kill = {}, []
    for tag, T in (("T1", Fraction(1)), ("T4", Fraction(4))):
        r, k = _battery_config(tag, T, nprime, q, levels, w_led, w_cov,
                               omega, hists, vecs, wt)
        results[tag] = r
        kill += k
    return {"results": results, "kill": kill}


def _battery_config(tag, T, nprime, q, levels, w_led, w_cov, omega, hists,
                    vecs, wt):
    honest = build_certificate(nprime, q, levels, w_led, w_cov, T, hists, vecs)
    v0, f0, tot0 = verify_certificate(honest, T_check=T)
    print(f"  [{tag}] honest: verdict={v0} truth={float(wt):.6f} tight="
          f"{tot0 == wt}")
    results = {"honest": {"verdict": v0, "truth": float(wt),
                          "tight": tot0 == wt}}
    kill = []
    if v0 != ("ACCEPT" if wt <= T else "REJECT"):
        kill.append(f"K2 honest verdict wrong at battery row [{tag}]")

    def clone():
        return json.loads(json.dumps(honest))

    battery = {}
    # A1 ledger truncation (blocked by: "complete ... checkable completeness
    # proof, not only exhibited representatives")
    c = clone()
    for L in levels:
        if c["item2"][str(L) if str(L) in c["item2"] else L]["orbits"]:
            c["item2"][str(L) if str(L) in c["item2"] else L]["orbits"].pop()
            break
    battery["A1_ledger_truncation"] = c
    # A2 dedup abuse: halve one listed orbit size (blocked by: "exact
    # multiplier-shadow and lift de-duplication bounds")
    c = clone()
    for L in levels:
        key = str(L) if str(L) in c["item2"] else L
        if c["item2"][key]["orbits"]:
            c["item2"][key]["orbits"][0][2] //= 2
            break
    battery["A2_dedup_halved_orbit"] = c
    # A3 residual-class omission (blocked by: "for every unlisted
    # weight/frequency class")
    c = clone()
    key = str(levels[0]) if str(levels[0]) in c["item4"] else levels[0]
    dropped = sorted(c["item4"][key])[-1]
    del c["item4"][key][dropped]
    battery["A3_residual_class_omitted"] = c
    # A4 residual understatement (blocked by: "independently checkable")
    c = clone()
    key = str(levels[0]) if str(levels[0]) in c["item4"] else levels[0]
    wch = None
    for w in sorted(c["item4"][key]):
        if c["item4"][key][w]["U_num"] > 0:
            wch = w
            break
    if wch is not None:
        c["item4"][key][wch]["U_num"] = 0
    battery["A4_residual_understated"] = c
    # A5 reserve double charge (blocked by: "the aggregate reserve charged
    # once")
    c = clone()
    c["item5"]["reserve_credits"] = [[1, 4], [1, 4]]
    battery["A5_reserve_double_charge"] = c
    # A6 float final check (blocked by: "an exact rational final check")
    c = clone()
    c["item6"]["method"] = "float64"
    # engineered boundary: T' = truth - 2^-80: exact says exceeded, float says ok
    Tp = wt - Fraction(1, 2 ** 80)
    c["item6"]["T"] = [Tp.numerator, Tp.denominator]
    battery["A6_float_boundary"] = c
    float_would_accept = float(wt) <= float(Tp)
    exact_rejects = wt > Tp
    results["A6_boundary_demo"] = {"float_would_accept": float_would_accept,
                                   "exact_rejects": exact_rejects}
    # A7 field/order pin abuse (blocked by: "field presentation,
    # generated-field normalization, and primality/order certificates")
    c = clone()
    c["item1"]["omega"] = pow(omega, 2, q)  # order n'/2
    battery["A7_wrong_order_omega"] = c
    # A8 rejected-type smuggling (blocked by: explicit rejected-type list)
    c = clone()
    key = str(levels[0]) if str(levels[0]) in c["item4"] else levels[0]
    w0 = sorted(c["item4"][key])[0]
    c["item4"][key][w0]["proof_type"] = "likely_nonexceptional"
    battery["A8_rejected_type"] = c

    for name, c in battery.items():
        verdict, fired, tot = verify_certificate(c)
        blocked = verdict == "REJECT"
        # K1: an abuse that ACCEPTs while truth exceeds its own threshold
        Tc = Fraction(c["item6"]["T"][0], c["item6"]["T"][1])
        hole = (verdict == "ACCEPT") and (wt > Tc)
        if hole:
            kill.append(f"K1 SOUNDNESS HOLE [{tag}]: {name} accepted, "
                        f"truth>{float(Tc)}")
        if not blocked:
            kill.append(f"K1/K2 abuse NOT REJECTED [{tag}]: {name}")
        results[name] = {"verdict": verdict, "fired": fired[:3],
                         "blocked": blocked}
        print(f"  [{tag}] {name:<28} -> {verdict} fired={fired[:2]}")
    # fail-closed demo: honest cert vs T' = truth/2 must REJECT
    c = clone()
    Tp = wt / 2
    c["item6"]["T"] = [Tp.numerator, Tp.denominator]
    verdict, fired, _ = verify_certificate(c)
    results["failclosed_T_below_truth"] = {"verdict": verdict,
                                           "fired": fired[:2]}
    print(f"  [{tag}] failclosed T=truth/2            -> {verdict} "
          f"fired={fired[:2]}")
    if verdict != "REJECT":
        kill.append(f"K2 fail-closed demo FAILED [{tag}]")
    return results, kill


# ------------------------------------------------------------- Markov replay
def markov_replay():
    print("== A1-PROD weighted-Markov band replay (exact, toy scale) ==")
    out, kill = [], []
    for nprime, N, kmin, kmax, Lset, w_cov in ((16, 8, 4, 10, (1, 2), 8),
                                               (32, 16, 5, 13, (1,), 8)):
        for k in range(kmin, kmax + 1):
            Qlo, Qhi = 2 ** k, 2 ** (k + 1)
            qs = [q for q in band_primes(nprime, Qhi - 1) if q >= Qlo]
            if not qs:
                continue
            for L in Lset:
                Ws = []
                for q in qs:
                    omega = pinned_omega(q, nprime)
                    h = weight_hist_mitm(N, L, q, omega)[L]
                    Ws.append(sum(Fraction(h.get(w, 0), 2 ** w)
                                  for w in range(L + 1, w_cov + 1)))

                def dcap(w):
                    m = 0
                    while Qlo ** (L * (m + 1)) <= w ** N:
                        m += 1
                    return m

                TOT = sum(math.comb(N, w) * dcap(w)
                          for w in range(L + 1, w_cov + 1))
                for T in (Fraction(1), Fraction(1, 4), max(Ws)):
                    if T == 0:
                        continue
                    cnt = sum(1 for W in Ws if W >= T)
                    ok = cnt <= Fraction(TOT) / T
                    if not ok:
                        kill.append(f"K3b MARKOV BREAK n'={nprime} band "
                                    f"[{Qlo},{Qhi}) L={L} T={T}: "
                                    f"count={cnt} > TOTAL/T={TOT}/{T}")
                    out.append({"nprime": nprime, "band": [Qlo, Qhi], "L": L,
                                "T": str(T), "count": cnt, "TOTAL": TOT,
                                "ok": ok})
        print(f"  n'={nprime}: all band/threshold cells checked")
    bad = [o for o in out if not o["ok"]]
    print(f"  cells={len(out)} violations={len(bad)}")
    return {"cells": out, "kill": kill}


# --------------------------------------------------------------------- main
def main():
    args = sys.argv[1:] or ["CELL_A", "ABUSE", "MARKOV"]
    summary, kills = {}, []
    if "CELL_A" in args:
        r = cell_A()
        summary["CELL_A"] = {"n_rows": len(r["rows"]),
                             "rejects": [x["q"] for x in r["rows"]
                                         if x["verdict"] == "REJECT"]}
        kills += r["kill"]
    if "CELL_B" in args:
        r = cell_B()
        summary["CELL_B"] = {"n_rows": len(r["rows"]),
                             "rejects": [x["q"] for x in r["rows"]
                                         if x["verdict"] == "REJECT"]}
        kills += r["kill"]
    if "CELL_C" in args:
        r = cell_C()
        summary["CELL_C"] = r["rows"]
        kills += r["kill"]
    if "ABUSE" in args:
        r = abuse_battery()
        summary["ABUSE"] = {tag: {k: v.get("verdict")
                                  for k, v in r["results"][tag].items()
                                  if isinstance(v, dict) and "verdict" in v}
                            for tag in r["results"]}
        summary["A6_demo"] = r["results"]["T1"].get("A6_boundary_demo")
        kills += r["kill"]
    if "MARKOV" in args:
        r = markov_replay()
        summary["MARKOV"] = {"cells": len(r["cells"]),
                             "violations": sum(1 for c in r["cells"]
                                               if not c["ok"])}
        kills += r["kill"]
    print("\n==== EEX ROUND SUMMARY ====")
    print(json.dumps(summary, default=str)[:6000])
    print(f"KILL LINES FIRED: {len(kills)}")
    for k in kills:
        print("  KILL:", k)
    print("EEX_VERDICT:", "FALSIFIER_OR_CATCH" if kills else
          "NO_KILL_LINE_FIRED")
    return 1 if kills else 0


if __name__ == "__main__":
    sys.exit(main())
