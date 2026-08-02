#!/usr/bin/env python3
"""C2'' pilot -- what the nullity invariant sees and what it cannot.

At junction j the exact local ratio is

    rho_j(state) = (#admissible skews solving block j) * q^{L_j} / |domain|,

and the character/orthogonality decomposition of that count splits it as

    rho_j = q^{delta_j}  +  Rem_j ,      delta_j = L_j - rank{v_i : i in S_j},

where the q^{delta_j} main term is the contribution of the exact left kernel
K = {y : <y,v_i> = 0 for all i in S_j} and Rem_j collects every dual y outside
K.  This script measures both parts exactly at junction 0 (the archived
skewcount object) and certifies the decomposition in Z[zeta_q].
"""

from __future__ import annotations

import json
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path

from dli_model import block_matrix, blocks, get_zeta

HERE = Path(__file__).resolve().parent


def skewcount_table(q, n, t):
    """sc[Gmask] = #{eps in {+-1}^G : sum_i eps_i v_i = 0}, all G in Z/(n/2)."""
    cols = block_matrix(q, n, t, 0)
    h = n // 2
    o = len(blocks(t)[0])

    def signed(idx):
        st = [((0,) * o, 0)]
        for i in idx:
            v = cols[i]
            bit = 1 << i
            nx = []
            for sv, m in st:
                nx.append((sv, m))
                nx.append((tuple((a + b) % q for a, b in zip(sv, v)), m | bit))
                nx.append((tuple((a - b) % q for a, b in zip(sv, v)), m | bit))
            st = nx
        return st

    L = signed(range(0, h // 2))
    R = signed(range(h // 2, h))
    dL = defaultdict(list)
    for sv, m in L:
        dL[sv].append(m)
    sc = Counter()
    for sv, mR in R:
        key = tuple((-a) % q for a in sv)
        for mL in dL.get(key, ()):
            sc[mL | mR] += 1
    return sc, o


def analyse(q, n, t):
    sc, o = skewcount_table(q, n, t)
    h = n // 2
    by_delta = defaultdict(list)          # delta_0 -> list of rho (Fraction)
    per_k = defaultdict(Counter)          # |G| -> Counter{skewcount}
    for G in range(1 << h):
        k = G.bit_count()
        s = sc.get(G, 0)
        rho = Fraction(s * q**o, 2**k)
        d0 = max(0, o - min(o, k))
        by_delta[d0].append(rho)
        per_k[k][s] += 1
    out = {"n": n, "t": t, "q": q, "o": o, "h": h}
    strata = {}
    for d, lst in sorted(by_delta.items()):
        pred = Fraction(q) ** d
        strata[str(d)] = {
            "n_supports": len(lst),
            "predicted_rho_q^delta": str(pred),
            "min_rho": str(min(lst)), "max_rho": str(max(lst)),
            "mean_rho": str(sum(lst) / len(lst)),
            "n_exactly_predicted": sum(1 for r in lst if r == pred),
            "n_zero": sum(1 for r in lst if r == 0),
            "max_over_pred_float": float(max(lst) / pred),
        }
    out["strata"] = strata
    # profile (|G|) non-constancy: the archived TEST-2 object
    out["per_k_skewcount_values"] = {
        str(k): sorted(per_k[k]) for k in sorted(per_k) if per_k[k]}
    out["profile_constancy_violated_at_k"] = [
        k for k in sorted(per_k) if len(per_k[k]) > 1]
    return out


# --------------------------------------------------------------- exact Z[zeta_q]
def cyclotomic_decomposition_check(q, n, t, Gs):
    """EXACT check, in Z[x]/(x^q-1), of

       q^o * skewcount(G) = q^{o-r} * 2^{|G|}  +  sum_{y not in K} prod_i
                            (x^{a_i(y)} + x^{-a_i(y)})   evaluated at x=zeta_q,

    i.e. that the q^{delta} main term is exactly the left-kernel contribution.
    Both sides are reduced modulo 1+x+...+x^{q-1} (the relation in Z[zeta_q]).
    """
    from itertools import product as iproduct
    cols = block_matrix(q, n, t, 0)
    o = len(blocks(t)[0])
    sc, _ = skewcount_table(q, n, t)
    results = []
    for G in Gs:
        idx = [i for i in range(n // 2) if (G >> i) & 1]
        # exact rank of the support columns
        from nullity import rref_rank
        r = rref_rank([cols[i] for i in idx], q)
        K = []
        rest = []
        for y in iproduct(range(q), repeat=o):
            a = [sum(y[b] * cols[i][b] for b in range(o)) % q for i in idx]
            (K if all(v == 0 for v in a) else rest).append(a)
        assert len(K) == q ** (o - r), (len(K), q, o, r)
        # remainder as an element of Z[x]/(x^q-1)
        acc = [0] * q
        for a in rest:
            poly = [0] * q
            poly[0] = 1
            for v in a:
                nxt = [0] * q
                for e, c in enumerate(poly):
                    if c:
                        nxt[(e + v) % q] += c
                        nxt[(e - v) % q] += c
                poly = nxt
            for e in range(q):
                acc[e] += poly[e]
        # reduce mod 1+x+...+x^{q-1}: subtract acc[q-1]*(all ones)
        shift = acc[-1]
        red = [c - shift for c in acc[:-1]]
        rem_is_integer = all(c == 0 for c in red[1:])
        lhs = q**o * sc.get(G, 0)
        main = q ** (o - r) * 2 ** len(idx)
        ok = rem_is_integer and (lhs - main == red[0])
        results.append({"G": idx, "rank": r, "delta0": o - r,
                        "skewcount": sc.get(G, 0),
                        "kernel_main_term": main,
                        "remainder": red[0] if rem_is_integer else "not integral",
                        "identity_holds": bool(ok)})
        assert ok, results[-1]
    return results


def main():
    out = []
    for (n, t, q) in [(16, 2, 17), (16, 2, 97), (16, 3, 17), (16, 4, 97),
                      (32, 2, 97), (32, 2, 193), (32, 2, 8353), (32, 2, 32801),
                      (32, 3, 97), (32, 4, 97)]:
        a = analyse(q, n, t)
        out.append(a)
        s0 = a["strata"].get("0", {})
        print(f"n={n} t={t} q={q} o={a['o']}: delta0=0 stratum -> "
              f"{s0.get('n_supports')} supports, rho in "
              f"[{s0.get('min_rho')}, {s0.get('max_rho')}], mean "
              f"{float(Fraction(s0.get('mean_rho','0'))):.6g}, "
              f"predicted 1, worst/pred = {s0.get('max_over_pred_float'):.6g}; "
              f"profile-constancy violated at k={a['profile_constancy_violated_at_k']}")
    (HERE / "results" / "junction0_rho.json").write_text(json.dumps(out, indent=1))

    # exact Z[zeta_q] certification of rho = q^delta + remainder
    checks = []
    for (n, t, q) in [(16, 2, 17), (16, 3, 17), (16, 2, 97)]:
        Gs = [0, 1, 0b11, 0b101, 0b10101, 0b1011, 0b11111111, 0b10000001]
        checks.append({"n": n, "t": t, "q": q,
                       "rows": cyclotomic_decomposition_check(q, n, t, Gs)})
    (HERE / "results" / "cyclotomic_split.json").write_text(json.dumps(checks, indent=1))
    ncheck = sum(len(c["rows"]) for c in checks)
    print(f"\nEXACT Z[zeta_q] decomposition rho = q^delta + Rem: {ncheck}/{ncheck} PASS")


if __name__ == "__main__":
    main()
