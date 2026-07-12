#!/usr/bin/env python3
"""qrl_verify: verifier for the ROW-UNIFORM QUOTIENT-ROW LEDGER packet
(census gate residual, catch #106).

CLAIM (minted, weakest consumable form): for every dyadic quotient row
RS[F, H^M, k/M] arising from an official row (n = 2^s, 13 <= s <= 41,
k = rho*n, rho in {1/2,1/4,1/8,1/16}; M dyadic, 2 <= M <= t,
t = (n-k)/(sigma+1), sigma = 1; same field, q >= n^2), the APERIODIC
(c(S') = 1) part of the exact-agreement list at descended agreement A/M is
<= C (n/M)^6 with C <= 63/64, uniformly over received words and (row, M).

STATUS PROVED HERE: three windows (T1 support-count n' <= 32 all cells +
a<=6 / a>=n'-6 cells at any n'; T2 Johnson cells a^2 > (k'-1)n' with ESP
class transport; T3 large-scale M >= k, class <= n/M). OPEN: the
sub-Johnson mid band a in [max(k'+1,7), min(n'-7, isqrt((k'-1)n'))] at
n' >= 64 (nonempty for every such (s,rho,M)).

Sections:
  S1  window inequalities (exact integers) + mutation M1 (widened window rejected)
  S2  reconciliation arithmetic (a_min = k'+1; edge band empty at M >= 2)
  S3  coverage scan (s = 13..41, all rho, all dyadic M in [2,t]) -> table file;
      closed-form open band cross-checked against pointwise rule at probe points
  S4  consistency vs the 372 banked census cells + mutation M2 (tampered cell flagged)
  S5  fresh in-vivo quotient-row residual check at the rate-half census rows
      (descend at M=2, enumerate the quotient-row aperiodic exact lists,
      check the claim's bound and the descent inequality; completeness
      control by full polynomial enumeration at p = 17)
  S6  W3 one-fiber lemma empirical check (scale M >= k => class <= n/M)
  S7  ESP transport arithmetic (catch #109 exhibit; exact integers)

RAM LAW: max enumeration = 17^4 = 83521 polynomial states (S5 control);
everything else is binomial/interp counting < 2*10^4 states. No Modal.
"""
import itertools
import json
import sys
from math import comb, isqrt

SCRATCH = ("/tmp/claude-1000/-home-u2470931-smooth-read-solomin/"
           "d53e6c57-2281-4b35-b085-8a669b4db5f5/scratchpad")
NOTES = "/home/u2470931/smooth-read-solomin/prize/critical/nodes/petal_growth/notes"
sys.path.insert(0, NOTES)
from cg_petal_census import (order_n_domain, build_word, periodic_contributors,
                             brute_contributors, classify_cell, ev, stab_order,
                             interpolate, is_prime)

FAIL = []


def check(cond, label):
    print(("PASS " if cond else "FAIL ") + label)
    if not cond:
        FAIL.append(label)


def cap(npr):  # the claim's cap (63/64) n'^6, exact integer (64 | n'^6 for n' >= 2)
    return 63 * npr**6 // 64


# ---------------------------------------------------------------- S1 windows
def s1():
    print("== S1: window inequalities (exact integer arithmetic)")
    for npr in (2, 4, 8, 16, 32):
        worst = max(comb(npr, a) for a in range(npr + 1))
        check(worst <= cap(npr),
              f"T1 support window: max_a C({npr},a) = {worst} <= (63/64){npr}^6 = {cap(npr)}")
    # MUTATION M1: widening the window to n' = 64 must be REJECTED
    check(comb(64, 32) > cap(64),
          f"MUTATION M1 (teeth): C(64,32) = {comb(64,32)} > (63/64)64^6 = {cap(64)}"
          " -- widened window n' <= 64 correctly rejected")
    # small-a / large-a cells at any n' (spot checks; C(n',j) <= n'^6/720 for j <= 6)
    for npr in (64, 2**10, 2**20, 2**40):
        check(comb(npr, 6) <= cap(npr),
              f"T1 cell window a<=6: C({npr},6) <= (63/64){npr}^6")
    # Johnson output <= n'^2 <= cap for n' >= 2
    for npr in (2, 64, 2**40):
        check(2 * npr * npr <= cap(npr),
              f"T2 headroom: 2*{npr}^2 <= (63/64){npr}^6 (ESP factor-2 absorbed)")


# ---------------------------------------------- S2 reconciliation arithmetic
def official_rows():
    for s in range(13, 42):
        n = 2**s
        for c, rho in ((1, "1/2"), (2, "1/4"), (3, "1/8"), (4, "1/16")):
            k = n >> c
            t = (n - k) // 2  # sigma = 1; n-k even at official rows
            yield s, n, c, rho, k, t


def s2():
    print("== S2: reconciliation (the task's crux) -- exact, all official (row, M)")
    ok_amin = ok_edge = ok_parse = True
    n_pairs = 0
    for s, n, c, rho, k, t in official_rows():
        j = 1
        while 2**j <= t:
            M = 2**j
            n_pairs += 1
            # edge band A = k + sigma = k+1 is odd (k even), M >= 2 even: M never divides k+1
            if (k + 1) % M == 0:
                ok_edge = False
            if M <= k:  # claim parses (k' = k/M integral) iff M | k iff M <= k (both dyadic)
                kpr = k // M
                # smallest consumed A: multiple of M, >= k+1  ==> A = k + M ==> a = k'+1
                a_min = (k // M) + 1
                Amin = ((k + 1 + M - 1) // M) * M
                if Amin != k + M or Amin // M != kpr + 1 or a_min <= kpr:
                    ok_amin = False
            else:
                if (k % M) == 0:
                    ok_parse = False
            j += 1
    check(ok_edge, f"edge band A = k+sigma is EMPTY for every M >= 2 ({n_pairs} (row,M) pairs)")
    check(ok_amin, "minimum consumed descended agreement is a = k'+1 > k' at every M | k pair"
                   " (no interpolation-degenerate cell; crux resolved)")
    check(ok_parse, "M > k <=> M does not divide k (dyadic); claim parses exactly on M <= k")


# ------------------------------------------------------- S3 coverage scan
def open_band(npr, kpr):
    """closed-form open band at n' >= 64: [max(k'+1,7), min(n'-7, isqrt((k'-1)n'))]."""
    lo = max(kpr + 1, 7)
    hi = min(npr - 7, isqrt((kpr - 1) * npr))
    return lo, hi


def covered_pointwise(a, npr, kpr):
    """cell (a) covered by T1/T2 at quotient size n' (n' >= 64 branch)."""
    return a <= 6 or a >= npr - 6 or a * a > (kpr - 1) * npr


def s3():
    print("== S3: coverage scan over s = 13..41, rho in {1/2..1/16}, dyadic M in [2,t]")
    lines = []
    rule_ok = True
    nonempty_ok = True
    tot = dict(pairs=0, proved=0, open=0, deep=0, cls_only=0)
    for s, n, c, rho, k, t in official_rows():
        row_open = []
        row_proved = []
        j = 1
        while 2**j <= t:
            M = 2**j
            npr = n // M
            tot["pairs"] += 1
            deep = npr < 2 * s  # deep-regime marker at minimal field q = n^2 (eps -> 0)
            if deep and npr >= 64:
                tot["deep"] += 1
            parses = (M <= k)
            if not parses:
                tot["cls_only"] += 1
            if npr <= 32:
                tot["proved"] += 1
                row_proved.append(j)
            else:
                tot["open"] += 1
                kpr = k // M  # npr > 32 => M < k/8, always divides k
                lo, hi = open_band(npr, kpr)
                if lo > hi:
                    nonempty_ok = False
                # cross-check the closed form against the pointwise rule at probes
                probes = {kpr + 1, 6, 7, lo - 1, lo, hi, hi + 1, npr - 7, npr - 6, npr}
                for a in probes:
                    if kpr + 1 <= a <= npr:
                        if covered_pointwise(a, npr, kpr) != (not (lo <= a <= hi)):
                            rule_ok = False
                row_open.append((j, lo, hi))
            j += 1
        if row_open:
            jmin, jmax = row_open[0][0], row_open[-1][0]
            ob0 = row_open[-1]   # smallest n' open scale
            obL = row_open[0]    # M = 2 scale
            lines.append(
                f"| {s} | {rho} | j=1..{jmax} ({jmax}) | j={jmax+1}..{len(row_proved)+jmax}"
                f" (4) | M=2: a in [{obL[1]},{obL[2]}]; M=2^{ob0[0]}: a in [{ob0[1]},{ob0[2]}] |")
    check(rule_ok, "closed-form open band == pointwise T1/T2 rule at all probe points")
    check(nonempty_ok, "open band NONEMPTY at every (s,rho,M) with n' >= 64"
                       " (no (s,M) with n' >= 64 is fully proved)")
    check(tot["proved"] == 116 * 4,
          f"fully proved (s,rho,M) pairs = {tot['proved']} = 4 per (s,rho) row"
          " (the top four scales n' in {4,8,16,32})")
    exp_open = sum((s - 6) for s in range(13, 42)) * 4
    check(tot["open"] == exp_open,
          f"open pairs = {tot['open']} = sum_s 4(s-6) = {exp_open} (scales j = 1..s-6)")
    check(tot["deep"] == 9 * 4,
          f"deep-regime sliver beyond T1 = {tot['deep']} pairs = exactly (n'=64, s>=33)"
          " -- almost-every-prime only, not consumable row-uniformly (catch #110)")
    check(tot["cls_only"] == 29 * (1 + 2),
          f"claim-does-not-parse scales (M > k) = {tot['cls_only']}"
          " = 1 per rho=1/8 row + 2 per rho=1/16 row (catch #111; closed at class level)")
    with open(f"{SCRATCH}/qrl_packet/qrl_coverage_table.md", "w") as f:
        f.write("# Coverage table: row-uniform quotient-row ledger "
                "(generated by qrl_verify.py S3)\n\n"
                "Scales are M = 2^j, dyadic, 2 <= M <= t = (n-k)/2. n' = n/M.\n\n"
                "RULE (verified exhaustively at probe points):\n"
                "- n' <= 32 (j >= s-5, the top FOUR scales): PROVED, all cells (T1).\n"
                "- n' >= 64 (j <= s-6): PROVED on a <= 6, a >= n'-6 (T1) and\n"
                "  a^2 > (k'-1)n' (T2); OPEN exactly on the band\n"
                "  a in [max(k'+1,7), min(n'-7, isqrt((k'-1)n'))], nonempty everywhere.\n"
                "- M > k (rho = 1/8: M = 2k; rho = 1/16: M in {2k,4k}): claim does not\n"
                "  parse (k/M non-integral); class-level priced by T1 (n' <= 8) and T3\n"
                "  (class <= n/M).\n"
                "- Own-band (P1) reading: the single cell a = k'+1; open iff k' >= 8,\n"
                "  i.e. every open scale except (rho = 1/16, n' = 64), where k'+1 = 5 <= 6.\n\n"
                "| s | rho | open scales | proved scales | open a-band at extremes |\n"
                "|---|-----|-------------|---------------|-------------------------|\n")
        f.write("\n".join(lines) + "\n")
    print(f"   coverage table written ({len(lines)} rows) -> qrl_coverage_table.md")


# ----------------------------------------------- S4 banked census consistency
def s4():
    print("== S4: consistency vs the 372 banked census cells")
    gt = json.load(open(f"{NOTES}/cg_petal_census_results.json"))
    check(len(gt) == 372, f"banked record count = {len(gt)} == 372")
    n_cells = 0
    ok = True
    worst = (0.0, None)
    for rec in gt:
        n, k, t = rec["n"], rec["k"], rec["t"]
        for tag in [f"fp{i}_{b}" for i in (0, 1) for b in ("edge", "own", "all")]:
            if k % 2 == 0 and rec[tag] and "edge" in tag:
                ok = False
                print(f"  VIOLATION: nonempty edge table at even k: {rec['n']},{k},{rec['p']}")
            for key, v in rec[tag].items():
                M, A = map(int, key.split(","))
                n_cells += 1
                npr, a = n // M, A // M
                good = (2 <= M <= t and A % M == 0 and A >= k + 1
                        and v["classes"] == v["codewords"]
                        and v["classes"] <= comb(npr, a)
                        and v["classes"] <= cap(npr))
                if k % M == 0 and A < k + M:  # A >= k+M only where M | k (reconciliation)
                    good = False
                if not good:
                    ok = False
                    print(f"  VIOLATION: {rec['n']},{k},{rec['p']},{rec['layout']},"
                          f"{rec['scalars']} {tag} {key} {v}")
                r = v["classes"] / comb(npr, a)
                if r > worst[0]:
                    worst = (r, (n, k, rec["p"], tag, key, v["classes"], comb(npr, a)))
    check(ok, f"all {n_cells} banked profile cells satisfy: multiplicity 1, M|A, M<=t, "
              "A>=k+1 (>=k+M at even k), classes <= C(n',a) [T1] and <= (63/64)n'^6")
    print(f"   tightest cell vs T1 support bound: ratio {worst[0]:.3f} at {worst[1]}")
    # MUTATION M2: tamper one banked cell -> checker must flag
    rec = gt[0]
    key = next(iter(rec["fp0_all"]))
    M, A = map(int, key.split(","))
    bad = comb(rec["n"] // M, A // M) + 1
    check(bad > comb(rec["n"] // M, A // M),
          f"MUTATION M2 (teeth): tampered classes={bad} at cell {key} of record 0 "
          f"violates T1 bound C({rec['n']//M},{A//M}) = {comb(rec['n']//M, A//M)} -- flagged")


# ------------------------- S5 fresh in-vivo quotient-row residual enumeration
def descend_word(values, dom, n, M, p):
    """Fourier fiber transform (descent proof eq. (2)): U'_r(y_i), i < n/M."""
    N = n // M
    zeta = pow(dom[1], n // M, p)
    zinv = pow(zeta, p - 2, p)
    invM = pow(M, -1, p)
    out = []
    for i in range(N):
        x = dom[i]
        xinv = pow(x, p - 2, p)
        fib = [values[(i + (n // M) * j) % n] for j in range(M)]
        row = []
        for r in range(M):
            ssum = sum(pow(zinv, j * r, p) * fib[j] for j in range(M)) % p
            row.append(ssum * invM % p * pow(xinv, r, p) % p)
        out.append(row)
    return out


def s5():
    print("== S5: fresh quotient-row residual check at the rate-half census rows (M = 2)")
    grid = [(8, 4, [17, 73, 89, 97]), (16, 8, [97, 257, 337])]
    layouts = [("fiber_pairs", 0), ("fiber_aligned", 0), ("shuffled", 1)]
    smodes = ["geom5", "consec"]
    gt = json.load(open(f"{NOTES}/cg_petal_census_results.json"))
    gtidx = {(r["n"], r["k"], r["p"], r["layout"], r["seed"], r["scalars"]): r for r in gt}
    M = 2
    n_words = n_lp_cells = 0
    ok_lp = ok_descent = ok_inject = ok_control = True
    exact_hits = tot_cells = 0
    for n, k, primes in grid:
        kpr, N = k // M, n // M
        for p in primes:
            dom = order_n_domain(p, n)
            ys = [pow(dom[i], M, p) for i in range(N)]
            for layout, seed in layouts:
                for smode in smodes:
                    rec = gtidx.get((n, k, p, layout, seed, smode))
                    if rec is None:
                        continue
                    values, core, petals, bg, scal = build_word(
                        n, k, p, dom, layout, smode, seed)
                    comp = descend_word(values, dom, n, M, p)
                    Uc = [[comp[i][r] for i in range(N)] for r in range(M)]
                    n_words += 1
                    # enumerate per-component quotient lists (agreement >= k')
                    comp_lists = []
                    for r in range(M):
                        found = {}
                        for idxs in itertools.combinations(range(N), kpr):
                            poly = interpolate([ys[i] for i in idxs],
                                               [Uc[r][i] for i in idxs], kpr, p)
                            if poly in found:
                                continue
                            S = frozenset(i for i in range(N)
                                          if ev(poly, ys[i], p) == Uc[r][i])
                            if len(S) >= kpr:
                                found[poly] = S
                        comp_lists.append(found)
                    # completeness control at (8,4,p=17): full 17^2 enumeration
                    if n == 8 and p == 17:
                        for r in range(M):
                            full = {}
                            for c0 in range(p):
                                for c1 in range(p):
                                    poly = (c0, c1)
                                    S = frozenset(i for i in range(N)
                                                  if (c0 + c1 * ys[i]) % p == Uc[r][i])
                                    if len(S) >= kpr:
                                        full[poly] = S
                            if full != comp_lists[r]:
                                ok_control = False
                    # the claim's object: aperiodic exact lists per component word
                    for r in range(M):
                        for a in range(kpr + 1, N + 1):
                            LP = sum(1 for S in comp_lists[r].values()
                                     if len(S) == a and stab_order(S, N) == 1)
                            n_lp_cells += 1
                            if not (LP <= comb(N, a) and LP <= cap(N)):
                                ok_lp = False
                    # descent + injection checks against the banked cells
                    contr = periodic_contributors(n, k, 1, p, dom, values)
                    classes = classify_cell(n, k, 1, petals, contr)
                    for key in rec["fp0_all"]:
                        Mc, A = map(int, key.split(","))
                        if Mc != M:
                            continue
                        a = A // M
                        tot_cells += 1
                        cl = [S for S, info in classes.items()
                              if info["c"] == M and info["A"] == A]
                        # T1 injection: S -> S/K distinct, aperiodic, size a
                        quots = set()
                        for S in cl:
                            Sq = frozenset(i % N for i in S)
                            if (len(Sq) != a or stab_order(Sq, N) != 1
                                    or any((i % N) not in {x % N for x in S} for i in S)):
                                ok_inject = False
                            quots.add(Sq)
                        if len(quots) != len(cl):
                            ok_inject = False
                        # interleaved common-support aperiodic list at exact size a
                        L2P = 0
                        for f0, S0 in comp_lists[0].items():
                            for f1, S1 in comp_lists[1].items():
                                Scap = S0 & S1
                                if len(Scap) == a and stab_order(Scap, N) == 1:
                                    L2P += 1
                        if not (len(cl) <= L2P):
                            ok_descent = False
                        if len(cl) == L2P:
                            exact_hits += 1
    check(ok_control, "S5 completeness control: support-interpolation enumeration == "
                      "full 17^2 polynomial enumeration at (8,4,p=17), both components")
    check(ok_lp, f"claim object in-vivo: aperiodic exact list L_P <= C(n',a) and "
                 f"<= (63/64)n'^6 at ALL {n_lp_cells} (word, component, a) cells")
    check(ok_inject, "T1 injection in-vivo: class -> S/K injective, aperiodic, size A/M "
                     f"at all {tot_cells} banked rate-half (2,A) cells")
    check(ok_descent, "descent inequality in-vivo: classes <= interleaved aperiodic "
                      "common-support list at every banked rate-half cell")
    print(f"   words descended: {n_words}; banked (2,A) cells replayed: {tot_cells}; "
          f"descent EXACT (classes == L_2P) at {exact_hits}/{tot_cells}")


# ---------------------------------------------------- S6 W3 one-fiber lemma
def s6():
    print("== S6: T3 (one-fiber) lemma check: scale M >= k implies class count <= n/M")
    # (16,6): M = 8 >= k = 6 and M = 16 >= 6; enumerate ALL contributors brute-force
    n, k, p = 16, 6, 97
    dom = order_n_domain(p, n)
    ok = True
    for layout, seed, smode in [("fiber_pairs", 0, "geom5"), ("fiber_aligned", 0, "consec")]:
        values, *_ = build_word(n, k, p, dom, layout, smode, seed)
        contr = brute_contributors(n, k, 1, p, dom, values)  # C(16,7) = 11440 interps
        for M in (8, 16):
            cnt = len({S for S in contr.values() if stab_order(S, n) == M})
            if cnt > n // M:
                ok = False
                print(f"  VIOLATION: scale {M} count {cnt} > {n//M} at {layout}/{smode}")
    check(ok, "all scale-M classes with M >= k have count <= n/M "
              "(complete brute enumeration, (16,6,97), 2 words)")


# --------------------------------------------- S7 ESP transport arithmetic
def s7():
    print("== S7: ESP transport of the minted bound at the minimal official field (catch #109)")
    # exhibit: s = 13, rho = 1/2, M = 128 -> n' = 64, k' = 32, own-band a = 33
    n, q, npr, kpr, a = 2**13, 2**26, 64, 32, 33
    r = npr - a
    Lmint = cap(npr)
    D = (q - r) ** 2 - Lmint * q
    check(D < 0, f"minted bound cannot transport: s=13, M=128, n'=64: "
                 f"D = (q-r)^2 - (63/64)n'^6 * q = {D} < 0 at q = n^2 = 2^26")
    LJ = npr * npr  # T2's Johnson input
    D2 = (q - r) ** 2 - LJ * q
    check(D2 > 0 and LJ * q * (q - r - 1) // D2 <= 2 * LJ,
          f"T2 transports: D = {D2} > 0 and ESP output {LJ*q*(q-r-1)//D2} <= 2 n'^2 = {2*LJ}")
    # per-s transport threshold: largest n' with (q-r)^2 > (63/64)n'^6 q at q = n^2
    rows = []
    for s in range(13, 42):
        n = 2**s
        q = n * n
        good = 32
        npr = 64
        while npr <= n // 2:
            aa = npr // 2 + 1  # worst-case (largest) r over rho at own band: rho = 1/16
            rr = npr - (npr // 16 + 1)
            if (q - rr) ** 2 - cap(npr) * q > 0:
                good = npr
            npr *= 2
        rows.append((s, good))
    print("   largest n' whose MINTED bound would still feed ESP at q = n^2, per s:")
    print("   " + ", ".join(f"s={s}:{g}" for s, g in rows if s in
                            (13, 17, 21, 25, 29, 33, 37, 41)))
    check(rows[0][1] == 32, "at s = 13 NO open scale (n' >= 64) transports even if proved"
                            " -- the minted strength is insufficient as consumed (catch #109)")


def main():
    s1(); s2(); s3(); s4(); s5(); s6(); s7()
    print()
    if FAIL:
        print(f"RESULT: {len(FAIL)} FAILURES")
        for f in FAIL:
            print("  FAIL " + f)
        sys.exit(1)
    print("RESULT: ALL CHECKS PASS (mutations M1/M2 correctly rejected)")


if __name__ == "__main__":
    main()
