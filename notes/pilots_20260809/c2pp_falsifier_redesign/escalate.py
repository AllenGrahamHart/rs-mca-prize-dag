#!/usr/bin/env python3
"""GB-5 ESCALATION + the level law, on EXACT censuses (round 25).

Phases (checkpointed to ckpt.json in THIS directory):
  A  positive control (PR-I, gating) + brute-force n=16 verification of the
     TELESCOPING LEMMA and of R3 itself (PR-A), independent machinery
  B  closed-form verification at saturated cells, every e (PR-B, PR-C)
  C  the LEVEL LAW: exact Zlev(q) across the pre-saturation band (PR-D)
  D  the escalated R3 window grid (GB-5): more shapes, J = 4 exact (PR-E/F/G)

Usage: escalate.py PHASE [PHASE ...]     (stdlib only, run under ramguard)
"""
import json
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from c2lib import (                                            # noqa: E402
    Zinf, Cinf, Binf, LamStar, R3inf_window, R3inf_full, primes_mod,
    cost_Z, Zlev, Csub, Blk, R3_window, blocks, log2_int, sigma,
    positive_control, get_zeta)

CKPT = os.path.join(HERE, "ckpt.json")


def load():
    if os.path.exists(CKPT):
        with open(CKPT) as fh:
            return json.load(fh)
    return {}


def save(st):
    tmp = CKPT + ".tmp"
    with open(tmp, "w") as fh:
        json.dump(st, fh)
    os.replace(tmp, CKPT)


# ============================================================ PHASE A


def brute_tower(n, t, q):
    """Direct enumeration of all 2^n states: block events, level nullity,
    and R3 from its DEFINITION.  Independent of the MITM machinery."""
    B = blocks(t)
    D = len(B)
    zeta = get_zeta(q, n)
    nlev = D                      # levels 0..D-1 carry constraints
    # per-level constraint tables
    lev_tab = {}
    for lev in range(nlev):
        h, T = n // 2 ** lev, t // 2 ** lev
        if T < 1 or h < 1:
            continue
        zh = pow(zeta, 2 ** lev, q)
        lev_tab[lev] = (h, T, [[pow(zh, (r * i) % h, q) for i in range(h)]
                               for r in range(1, T + 1)])
    blk_tab = {}
    for j in range(D - 1):
        hj, hj1 = n // 2 ** j, n // 2 ** (j + 1)
        zj = pow(zeta, 2 ** j, q)
        blk_tab[j] = (hj1, [[pow(zj, (u * i) % hj, q) for i in range(hj1)]
                            for u in B[j]])
    cnt_lev = {lev: 0 for lev in lev_tab}
    cnt_blk = {j: 0 for j in blk_tab}
    cnt_joint = {}
    for x in range(1 << n):
        m = [(x >> i) & 1 for i in range(n)]
        levs = [m]
        for lev in range(1, nlev):
            prev, h = levs[-1], n // 2 ** lev
            levs.append([prev[i] + prev[i + h] for i in range(h)])
        # level nullity
        holds_lev = {}
        for lev, (h, T, tab) in lev_tab.items():
            ml = levs[lev]
            holds_lev[lev] = all(
                sum(ml[i] * row[i] for i in range(h)) % q == 0 for row in tab)
            if holds_lev[lev]:
                cnt_lev[lev] += 1
        # block events
        holds_blk = {}
        for j, (hj1, tab) in blk_tab.items():
            prev, h = levs[j], n // 2 ** (j + 1)
            d = [prev[i] - prev[i + h] for i in range(h)]
            holds_blk[j] = all(
                sum(d[i] * row[i] for i in range(hj1)) % q == 0 for row in tab)
            if holds_blk[j]:
                cnt_blk[j] += 1
        key = tuple(sorted(j for j in blk_tab if holds_blk[j]))
        cnt_joint[key] = cnt_joint.get(key, 0) + 1
    return cnt_lev, cnt_blk, cnt_joint, levs


def phase_A(st):
    print("=" * 78)
    print("PHASE A -- POSITIVE CONTROL (PR-I, gating) and BRUTE FORCE (PR-A)")
    print("=" * 78)
    ok, rows = positive_control()
    for r in rows:
        print(f"  banked n=32 t={r['t']:>2} q={r['q']:>6}: want={r['want']:>7} "
              f"got={r['got']:>7}  {'ok' if r['ok'] else '*** MISMATCH ***'}")
    print(f"  POSITIVE CONTROL: {'PASS 8/8' if ok else 'FAIL'}")
    if not ok:
        raise SystemExit("PR-I failed -- no read is taken.")
    st["A_control"] = ok

    out = []
    for (n, t, q) in [(16, 8, 97), (16, 8, 193), (16, 4, 97), (16, 4, 353)]:
        cl, cb, cj, _ = brute_tower(n, t, q)
        D = len(blocks(t))
        W = list(range(D - 1))
        # census machinery, same row
        Zc, Bc = {}, {}
        r3, terms, raw = R3_window(q, n, t, W, Zc, Bc)
        # 1. level censuses agree
        lev_ok = all(cl[lev] == Zlev(q, n, t, lev)
                     for lev in range(D) if t // 2 ** lev >= 1)
        # 2. block censuses agree
        blk_ok = all(cb[j] == Blk(q, n, t, j) for j in W)
        # 3. R3 from the DEFINITION: log2( P[all E_j | N_{>w1}] / prod P[E_j] )
        all_hold = cj.get(tuple(W), 0)
        # P[all E_j and N_{>w1}] = P[N_{>-1}] = Z_0 ; P[N_{>w1}] = Z_{w1+1}
        r3_def = (log2_int(cl[0]) - log2_int(cl[W[-1] + 1]) + len(W) * n
                  - sum(log2_int(cb[j]) for j in W))
        # 4. the lemma's SECOND form, conditioned:
        #    R3_W = log2( P[ AND_W E_j | N_{>w1} ] / prod_W P[E_j] ).
        #    SELF-CORRECTION: my first version of this check dropped the
        #    conditioning on N_{>w1} and compared against the UNconditional
        #    joint; that check failed while the lemma held.  Both are printed.
        cond_joint = cl[0] / cl[W[-1] + 1]                # P[AND E_j | N_{>w1}]
        r3_joint = math.log2(cond_joint) - sum(log2_int(cb[j]) - n for j in W)
        unc = (log2_int(all_hold) - n
               - sum(log2_int(cb[j]) - n for j in W))     # UNC_W, diagnostic
        ok3 = abs(r3 - r3_def) < 1e-9
        ok4 = abs(r3 - r3_joint) < 1e-9
        print(f"\n  n={n} t={t} q={q}  W={W}")
        print(f"    level censuses match brute force : {lev_ok}")
        print(f"    block censuses match brute force : {blk_ok}")
        print(f"    R3 (MITM)      = {r3:.10f}")
        print(f"    R3 (brute def) = {r3_def:.10f}   match={ok3}")
        print(f"    R3 (joint/marg)= {r3_joint:.10f}   match={ok4}")
        print(f"    UNC_W (unconditional joint excess) = {unc:.10f}  "
              f"[#all-W-blocks-hold={all_hold}, Z_0={cl[0]}: the terminal "
              f"block j={len(blocks(t)) - 1} has no junction]")
        out.append({"n": n, "t": t, "q": q, "lev_ok": lev_ok,
                    "blk_ok": blk_ok, "r3": r3, "r3_def": r3_def,
                    "r3_joint": r3_joint, "unc": unc,
                    "ok": lev_ok and blk_ok and ok3 and ok4})
    st["A_brute"] = out
    print(f"\n  PR-A (telescoping lemma, independent machinery): "
          f"{'PASS' if all(o['ok'] for o in out) else 'FAIL'}")
    return st


# ============================================================ PHASE B

SAT_CELLS = [(16, 8), (16, 4), (16, 2), (32, 16), (32, 8), (32, 4), (32, 2),
             (64, 32), (64, 16), (64, 8), (64, 4), (128, 64), (128, 32),
             (128, 16), (256, 128), (256, 32)]


def phase_B(st):
    """Closed-form verification.  q is chosen PER OBJECT at its own freeze
    scale Lam ~ n/(#constraints) + 4, NOT at the crossover LamStar: the
    first run of this phase used LamStar+3 and produced 29 "failures" that
    were simply unsaturated rows (registered C-4: the onset is later than
    the crossover).  The census cost is q-INDEPENDENT, so this is free."""
    print("=" * 78)
    print("PHASE B -- CLOSED FORMS at saturated cells, every e (PR-B, PR-C)")
    print("=" * 78)
    res = st.get("B", [])
    done = {(r["n"], r["t"], r["lev"], r["kind"]) for r in res}
    print(f"{'n':>5} {'t':>4} {'lev':>3} {'T':>3} {'e':>3} {'kind':>5} "
          f"{'log2 q':>7} {'exact':>24} {'closed form':>24} {'ok':>4}")
    for (n, t) in SAT_CELLS:
        D = len(blocks(t))
        for lev in range(D):
            T, h = t // 2 ** lev, n // 2 ** lev
            if T < 1 or h < 2 or cost_Z(n, lev) > 2 ** 22:
                continue
            for kind in ("Z", "C", "B"):
                if (n, t, lev, kind) in done:
                    continue
                j = lev - 1
                if kind == "B" and (j < 0 or j > D - 2):
                    continue
                ncon = T if kind != "B" else t // 2 ** lev
                lam = n / ncon + 4.0
                if lam > 140 and cost_Z(n, lev) > 2 ** 17:
                    print(f"{n:>5} {t:>4} {lev:>3} {T:>3} {n // (2 * t):>3} "
                          f"{kind:>5}  SKIP: freeze needs log2 q={lam:.0f} at "
                          f"cost {cost_Z(n, lev)} (RAM wall)")
                    continue
                q = primes_mod(n, math.ceil(lam), math.ceil(lam))[0]
                if kind == "Z":
                    got, want = Zlev(q, n, t, lev), Zinf(n, t, lev)
                elif kind == "C":
                    got, want = Csub(q, n, t, lev), Cinf(n, t)
                else:
                    got, want = Blk(q, n, t, j), Binf(n, t, j)
                ok = got == want
                res.append({"n": n, "t": t, "lev": lev, "kind": kind,
                            "q_bits": math.log2(q), "got": str(got),
                            "want": str(want), "ok": ok})
                print(f"{n:>5} {t:>4} {lev:>3} {T:>3} {n // (2 * t):>3} "
                      f"{kind:>5} {math.log2(q):>7.1f} {str(got)[:24]:>24} "
                      f"{str(want)[:24]:>24} {'ok' if ok else 'FAIL':>4}")
                st["B"] = res
                save(st)
    bad = [r for r in res if not r["ok"]]
    print(f"\n  PR-B/PR-C: {len(res)} closed-form checks, "
          f"{len(bad)} failures -> {'PASS' if not bad else 'FAIL'}")
    for r in bad[:10]:
        print(f"    FAIL n={r['n']} t={r['t']} lev={r['lev']} kind={r['kind']}"
              f" got={r['got'][:30]} want={r['want'][:30]}")
    return st


# ============================================================ PHASE C

LCELLS = [(32, 2, 1), (32, 4, 1), (64, 4, 2), (64, 8, 2), (64, 8, 3),
          (128, 16, 4), (32, 2, 0), (32, 4, 0), (64, 16, 3), (128, 32, 4),
          (256, 32, 5)]


def phase_C(st):
    print("=" * 78)
    print("PHASE C -- THE LEVEL LAW on EXACT censuses (PR-D)")
    print("=" * 78)
    res = st.get("C", {})
    for (n, t, lev) in LCELLS:
        key = f"{n}|{t}|{lev}"
        ls = LamStar(n, t, lev)
        T = t // 2 ** lev
        lo = math.ceil(math.log2(n + 1))
        # DENSE across the pre-saturation band and the transition (where the
        # fit lives); then extend the tail ADAPTIVELY and stop as soon as two
        # consecutive scales give Zlev == Zinf exactly (freeze witnessed).
        qs = primes_mod(n, lo, math.ceil(ls) + 3, per_octave=2)
        cur = res.get(key, {})
        zi0 = Zinf(n, t, lev)
        k = math.ceil(ls) + 3
        streak = 0
        while True:
            for q in qs:
                if str(q) in cur:
                    if int(cur[str(q)]) == zi0 and math.log2(q) > ls:
                        streak += 1
                    continue
                cur[str(q)] = str(Zlev(q, n, t, lev))
                res[key] = cur
                st["C"] = res
                save(st)
                if int(cur[str(q)]) == zi0:
                    streak += 1
                else:
                    streak = 0
            if streak >= 2 or k > n / T + 8:
                break
            k += max(1, int(math.ceil((n / T + 8 - k) / 5)))
            qs = [q for q in primes_mod(n, k, k) if q not in cur]
        zi = Zinf(n, t, lev)
        lzi = log2_int(zi)
        print(f"\n  CELL n={n} t={t} lev={lev} T={T} e={n // (2 * t)} "
              f"h={n // 2 ** lev}  LamStar={ls:.3f}  cost={cost_Z(n, lev)}")
        print(f"    {'q':>22} {'Lam':>8} {'log2 Z':>10} {'excess':>10} "
              f"{'log2(Z-Zinf)':>14}")
        for q in qs:
            z = int(cur[str(q)])
            exc = log2_int(z) - lzi
            d = z - zi
            print(f"    {q:>22} {math.log2(q):>8.3f} {log2_int(z):>10.4f} "
                  f"{exc:>10.5f} "
                  f"{(log2_int(d) if d > 0 else float('-inf')):>14.4f}")
    return st


# ============================================================ PHASE D

WCELLS = [
    (32, 16, [0, 1, 2, 3]),          # the GB-5 cell, J=4 (full tower)
    (16, 8, [0, 1, 2]),              # J=3 full tower
    (32, 8, [0, 1, 2]),              # J=3 full tower
    (32, 16, [1, 2, 3]),             # J=3 sub-window (placement control)
    (64, 32, [2, 3, 4]),             # J=3 sub-window at n=64
    (16, 4, [0, 1]),                 # J=2 full tower
    (32, 4, [0, 1]),                 # J=2 full tower, has a pre-sat point
    (64, 16, [2, 3]),                # J=2 sub-window
    (128, 64, [4, 5]),               # J=2 sub-window at n=128
    (32, 2, [0]),                    # J=1 control
    (64, 8, [2]),                    # J=1 control
    # SELF-CORRECTION: (128, 16, W=[4]) was registered in PREREG P6 but is
    # INVALID -- t=16 has blocks j=0..4 and junctions j=0..3 only, so
    # junction 4 would need level 5 with T_5 = 0 (a shift-0 cell, CATCH-19B).
    # Dropped, not filtered post hoc: it never had a junction to measure.
]


def phase_D(st):
    print("=" * 78)
    print("PHASE D -- THE ESCALATED GB-5 GRID (D2)")
    print("=" * 78)
    res = st.get("D", {})
    for (n, t, W) in WCELLS:
        key = f"{n}|{t}|{'-'.join(map(str, W))}"
        J = len(W)
        levs = list(range(W[0], W[-1] + 2))
        top = max(LamStar(n, t, l) for l in levs)
        lo = math.ceil(math.log2(n + 1))
        qs = primes_mod(n, lo, max(lo + 1, math.ceil(top) + 4), per_octave=2)
        cur = res.get(key, {})
        for q in qs:
            if str(q) in cur:
                continue
            r3, terms, raw = R3_window(q, n, t, W)
            cur[str(q)] = {"R3": r3, "terms": terms,
                           "Z": {str(k): str(v) for k, v in raw["Z"].items()},
                           "B": {str(k): str(v) for k, v in raw["B"].items()}}
            res[key] = cur
            st["D"] = res
            save(st)
        r3inf = R3inf_window(n, t, W)
        scaled = 21.0 * J / 33.0
        full = (W == list(range(len(blocks(t)) - 1)))
        print(f"\n  CELL n={n} t={t} W={W} J={J} e={n // (2 * t)} "
              f"{'[FULL TOWER: J of J]' if full else '[sub-window]'}  "
              f"cost={cost_Z(n, W[0])}")
        print(f"    closed-form saturated R3inf = {r3inf:.4f}   "
              f"window-scaled reserve 21*{J}/33 = {scaled:.4f}   "
              f"RATIO_inf = {r3inf / scaled:.3f}")
        print(f"    {'q':>16} {'Lam':>7} {'R3_W':>10} {'RATIO':>8}  terms")
        for q in qs:
            d = cur[str(q)]
            tm = " ".join(f"{x:7.4f}" for x in d["terms"])
            print(f"    {q:>16} {math.log2(q):>7.3f} {d['R3']:>10.4f} "
                  f"{d['R3'] / scaled:>8.3f}  [{tm}]")
    return st


PHASES = {"A": phase_A, "B": phase_B, "C": phase_C, "D": phase_D}

if __name__ == "__main__":
    state = load()
    for ph in (sys.argv[1:] or ["A"]):
        state = PHASES[ph](state)
        save(state)
    print("\ncheckpoint written:", CKPT)
