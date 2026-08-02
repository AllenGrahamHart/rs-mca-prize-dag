"""Reproduce the banked C1 / skew censuses PURELY from the lattice side.

Ground truth being reproduced (all banked, independent code paths):

  A. C1 2N=32, ell=1 (M=32, h=16, U={1}) -- c1_norm_ladder/REPORT.md
       w<=3 census = {97,193,257,353,449}                       (5 of 49)
       w<=4 census = 24 primes (listed there)                   (24 of 259)
       w<=5 census = 160 primes                                 (160 of 1522)
  B. C1 2N=16, ell=1 (M=16, h=8)  = 11 primes <= 881 with minimal weights
  C. skew ell=2 at 2N=32 (M=32, h=16, U={1,3}) -- dli_norm_gate/REPORT.md 3.5
       w<=4 EMPTY; w=5 {97}; w=7 {97,193,257}; w=8 {97,193,257,449,577}

The lattice path shares NO code with either: it builds the q-ary kernel basis,
LLL-reduces it, certifies the reduced basis exactly (det = q^o and membership),
and enumerates ALL lattice points inside a ball by exact Fincke-Pohst, then
filters for ternary coefficient vectors.  Brute force over {0,+-1}^h is never
used (except in the h=8 self-test of lattice_core).
"""
import json, os, sys, time
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lattice_core as lc

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RES = os.path.join(HERE, "results")

# banked maxnorm(h, w) tables, h = M/2  (c1_norm_ladder/REPORT.md)
MAXNORM = {
    8: {1: 1, 2: 16, 3: 81, 4: 196, 5: 529, 6: 1154, 7: 2401, 8: 2176},
    16: {1: 1, 2: 256, 3: 6561, 4: 38416, 5: 279841, 6: 1331716, 7: 5764801,
         8: 14760962, 9: 38950081, 10: 84580802, 11: 184497889,
         12: 342386306, 13: 777684769, 14: 1040410946, 15: 1612931233,
         16: 2311094272},
}


def admissible_primes(M, limit):
    out = []
    q = M + 1
    while q <= limit:
        if lc.is_prime(q):
            out.append(q)
        q += M
    return out


def scan(M, U, qlist, radius_sq, lam_cap=20, log_every=200):
    h = M // 2
    o = len(U)
    rows = []
    t0 = time.time()
    for idx, q in enumerate(qlist):
        B, om = lc.relation_lattice_basis(q, M, U)
        R = lc.fast_lll(B)
        cert = lc.certify_basis(R, q, M, U, om)
        assert cert, ("basis certification failed", q, M, U)
        vs = lc.enumerate_short(R, radius_sq)
        tern = [v for v in vs if lc.is_ternary(v)]
        by_w = {}
        for v in tern:
            by_w[lc.sq_norm(v)] = by_w.get(lc.sq_norm(v), 0) + 1
        # lambda_1^2 : widen by 1 (each empty level is cheap)
        l1 = None
        if vs:
            l1 = min(lc.sq_norm(v) for v in vs)
        else:
            b = radius_sq
            while b < lam_cap:
                b += 1
                w2 = lc.enumerate_short(R, b)
                if w2:
                    l1 = min(lc.sq_norm(v) for v in w2)
                    break
        rows.append({
            "q": q, "M": M, "U": list(U), "h": h, "o": o,
            "det": q ** o,
            "lambda1_sq": l1,
            "amgm_fence": lc.amgm_fence(q, h, o),
            "min_ternary_weight": (min(by_w) if by_w else None),
            "ternary_pairs_by_weight": {str(k): v for k, v in sorted(by_w.items())},
            "n_short_pairs": len(vs),
            "basis_certified": cert,
        })
        if log_every and (idx + 1) % log_every == 0:
            print("  ... %d/%d  q=%d  %.1fs" % (idx + 1, len(qlist), q,
                                                time.time() - t0), flush=True)
    return rows


def main():
    out = {}

    # ---- B: 2N=16, ell=1 -------------------------------------------------
    banked_16 = {17: 3, 97: 4, 113: 5, 193: 5, 241: 5, 337: 7, 353: 6,
                 401: 5, 433: 5, 577: 6, 881: 7}
    qs = admissible_primes(16, MAXNORM[8][8])
    rows = scan(16, (1,), qs, 8, log_every=0)
    got = {r["q"]: r["min_ternary_weight"] for r in rows
           if r["min_ternary_weight"] is not None}
    out["B_2N16_ell1"] = {
        "n_admissible": len(qs), "census": {str(k): v for k, v in sorted(got.items())},
        "banked": {str(k): v for k, v in sorted(banked_16.items())},
        "match": got == banked_16, "rows": rows,
    }
    print("B 2N=16 ell=1: match =", got == banked_16, flush=True)

    # ---- A: 2N=32, ell=1 -------------------------------------------------
    banked_w3 = [97, 193, 257, 353, 449]
    banked_w4 = [97, 193, 257, 353, 449, 577, 641, 673, 929, 1153, 1217, 1249,
                 1409, 2113, 2273, 2593, 2689, 3137, 3457, 4001, 4129, 4993,
                 5857, 7937]
    qs5 = admissible_primes(32, MAXNORM[16][5])
    print("A: %d admissible primes <= %d" % (len(qs5), MAXNORM[16][5]), flush=True)
    rows = scan(32, (1,), qs5, 5)
    cen = {w: sorted(r["q"] for r in rows
                     if r["min_ternary_weight"] is not None
                     and r["min_ternary_weight"] <= w) for w in (2, 3, 4, 5)}
    out["A_2N32_ell1"] = {
        "n_admissible_by_cut": {str(w): len([q for q in qs5 if q <= MAXNORM[16][w]])
                                for w in (2, 3, 4, 5)},
        "census_sizes": {str(w): len(cen[w]) for w in (2, 3, 4, 5)},
        "banked_sizes": {"2": 0, "3": 5, "4": 24, "5": 160},
        "w3_list": cen[3], "w4_list": cen[4],
        "w3_match": cen[3] == banked_w3,
        "w4_match": cen[4] == banked_w4,
        "w5_size_match": len(cen[5]) == 160,
        "w2_empty": cen[2] == [],
        "rows": rows,
    }
    print("A 2N=32 ell=1 sizes:", {w: len(cen[w]) for w in (2, 3, 4, 5)},
          " w3match", cen[3] == banked_w3, " w4match", cen[4] == banked_w4,
          flush=True)

    # ---- C: 2N=32, ell=2 (U={1,3}) ---------------------------------------
    # sieve bound: q^2 <= maxnorm(16,8) = 14760962  ->  q <= 3842
    lim = 0
    while (lim + 1) ** 2 <= MAXNORM[16][8]:
        lim += 1
    qs2 = admissible_primes(32, lim)
    rows2 = scan(32, (1, 3), qs2, 8, log_every=0)
    cen2 = {w: sorted(r["q"] for r in rows2
                      if r["min_ternary_weight"] is not None
                      and r["min_ternary_weight"] <= w) for w in range(2, 9)}
    banked_C = {4: [], 5: [97], 7: [97, 193, 257], 8: [97, 193, 257, 449, 577]}
    out["C_2N32_ell2"] = {
        "sieve_limit": lim, "n_admissible": len(qs2),
        "census": {str(w): cen2[w] for w in cen2},
        "banked": {str(k): v for k, v in banked_C.items()},
        "match": all(cen2[w] == banked_C[w] for w in banked_C),
        "rows": rows2,
    }
    print("C 2N=32 ell=2 census:", {w: cen2[w] for w in cen2},
          " match", all(cen2[w] == banked_C[w] for w in banked_C), flush=True)

    out["all_match"] = (out["B_2N16_ell1"]["match"]
                        and out["A_2N32_ell1"]["w3_match"]
                        and out["A_2N32_ell1"]["w4_match"]
                        and out["A_2N32_ell1"]["w5_size_match"]
                        and out["C_2N32_ell2"]["match"])
    with open(os.path.join(RES, "census_validate.json"), "w") as f:
        json.dump(out, f, indent=1)
    print("ALL MATCH:", out["all_match"])


if __name__ == "__main__":
    main()
