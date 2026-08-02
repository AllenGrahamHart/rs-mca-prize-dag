"""Structure of the relation lattice: the minima law, the doubling sublattice
index, and the official/non-official separation test.

S1  MINIMA LAW.  L is an ideal, hence stable under multiplication by x, which
    is a negacyclic shift = an isometry of Z^h.  For any nonzero alpha in L the
    h vectors x^j alpha are in L, all of length ||alpha||, and Q-linearly
    independent (Z[zeta] is a domain).  Hence
        lambda_1(L) = lambda_2(L) = ... = lambda_h(L).
    Corollary: Minkowski's SECOND theorem carries no information beyond the
    first for these lattices; and the number of lattice points of any given
    length is a multiple of 2h (free +/- x^j action), so the number of weight-w
    ternary relations is 0 or >= 2h.

S2  DOUBLING.  iota: Z[y]/(y^h+1) -> Z[x]/(x^{2h}+1), y -> x^2, with
    omega = omega'^2.  Then iota(L^{(h)}) and x.iota(L^{(h)}) both sit inside
    L^{(2h)}, and
        [ L^{(2h)} : iota(L^{(h)}) (+) x.iota(L^{(h)}) ] = q^o    exactly.
    Consequences: lambda_1(L^{(2h)}) <= lambda_1(L^{(h)}) and the census is
    monotone under doubling.

S3  SEPARATION.  Everything a Minkowski/transference/counting argument can see
    is a function of (h, det) = (256 ell, q^ell).  Official and non-official q
    of the same size have identical (h, det).  We exhibit explicit same-bit-size
    pairs where one carries a weight-w relation and the other does not.
"""
import json, os, sys, time
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lattice_core as lc

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RES = os.path.join(HERE, "results")


def minima_law(cases):
    rows = []
    for (q, M, U) in cases:
        h = M // 2
        B, om = lc.relation_lattice_basis(q, M, U)
        R = lc.fast_lll(B)
        assert lc.certify_basis(R, q, M, U, om)
        l1 = None
        b = 0
        while l1 is None and b < 40:
            b += 1
            vs = lc.enumerate_short(R, b)
            if vs:
                l1 = min(lc.sq_norm(v) for v in vs)
        mins = [v for v in lc.enumerate_short(R, l1) if lc.sq_norm(v) == l1]
        v0 = mins[0]
        orb, s = [v0], v0
        for _ in range(h - 1):
            s = lc.negacyclic_shift(s)
            orb.append(s)
        d = lc.det_int(orb)
        # count of minimal vectors, counting +/- pairs -> 2*len(mins) points
        rows.append({
            "q": q, "M": M, "U": list(U), "h": h, "det": q ** len(U),
            "lambda1_sq": l1,
            "orbit_same_length": all(lc.sq_norm(o) == l1 for o in orb),
            "orbit_independent_det": str(d), "orbit_rank_full": d != 0,
            "lambda_h_eq_lambda_1": d != 0,
            "n_minimal_points": 2 * len(mins),
            "minimal_points_multiple_of_2h": (2 * len(mins)) % (2 * h) == 0,
            "minimal_points_over_2h": (2 * len(mins)) // (2 * h),
            "amgm_fence": lc.amgm_fence(q, h, len(U)),
            "amgm_slack": l1 - lc.amgm_fence(q, h, len(U)),
        })
    return rows


def doubling(cases):
    rows = []
    for (q, M, U) in cases:
        h = M // 2
        o = len(U)
        # omega' of exact order 2M; omega = omega'^2 has exact order M
        omp = lc.element_of_exact_order(q, 2 * M)
        om = pow(omp, 2, q)
        Bl, _ = lc.relation_lattice_basis(q, M, U, omega=om)
        Bh, _ = lc.relation_lattice_basis(q, 2 * M, U, omega=omp)
        # S = iota(L) (+) x.iota(L)
        S = []
        for b in Bl:
            e = [0] * (2 * h)
            for i in range(h):
                e[2 * i] = b[i]
            S.append(e)
            odd = [0] * (2 * h)
            for i in range(h):
                odd[2 * i + 1] = b[i]
            S.append(odd)
        inside = all(lc.in_lattice(v, q, 2 * M, U, omp) for v in S)
        dS = abs(lc.det_int(S))
        dH = abs(lc.det_int(Bh))
        rows.append({
            "q": q, "M_low": M, "M_high": 2 * M, "U": list(U),
            "h_low": h, "h_high": 2 * h,
            "S_inside_L_high": inside,
            "det_S": str(dS), "det_L_high": str(dH),
            "det_L_low_squared": str((q ** o) ** 2),
            "index": str(dS // dH) if dH else None,
            "index_eq_q_pow_o": (dH != 0 and dS // dH == q ** o and dS % dH == 0),
        })
    return rows


def separation(rows_A):
    """From the completed 2N=32 ell=1 sweep: same-bit-size prime pairs, one with
    a weight-w relation, one without; plus the v_2(q-1) profile of the census."""
    out = {}
    have = {r["q"]: r for r in rows_A}
    for w in (3, 4, 5):
        cen = [q for q, r in have.items()
               if r["min_ternary_weight"] is not None and r["min_ternary_weight"] <= w]
        non = [q for q, r in have.items()
               if q <= max(cen) and (have[q]["min_ternary_weight"] is None
                                     or have[q]["min_ternary_weight"] > w)]
        pairs = []
        for q0 in sorted(cen):
            bl = q0.bit_length()
            cand = [q1 for q1 in non if q1.bit_length() == bl]
            if cand:
                pairs.append({"bits": bl, "q_with_relation": q0,
                              "q_without_relation": min(cand),
                              "det_equal_bitlength": True,
                              "v2_with": lc.v2(q0 - 1),
                              "v2_without": lc.v2(min(cand) - 1)})
            if len(pairs) >= 6:
                break
        out["w%d" % w] = {
            "n_census": len(cen),
            "max_v2_census": max(lc.v2(q - 1) for q in cen),
            "v2_histogram_census": _hist([lc.v2(q - 1) for q in cen]),
            "v2_histogram_all": _hist([lc.v2(q - 1) for q in have
                                       if q <= max(cen)]),
            "same_bitlength_pairs": pairs,
        }
    return out


def _hist(xs):
    d = {}
    for x in xs:
        d[str(x)] = d.get(str(x), 0) + 1
    return dict(sorted(d.items(), key=lambda kv: int(kv[0])))


def admissible_near(M, target, count=1, below=False):
    """`count` primes q = 1 mod M nearest to `target` (deterministic)."""
    out, k = [], 0
    while len(out) < count and k < 100000:
        for cand in ([target - k * M] if below else [target + k * M, target - k * M]):
            if cand > M and (cand - 1) % M == 0 and lc.is_prime(cand) and cand not in out:
                out.append(cand)
                if len(out) == count:
                    break
        k += 1
    return out


def main():
    out = {}
    # every case is machine-checked prime and admissible (a composite modulus is
    # NOT an ideal lattice; an earlier hand-written case list contained
    # 279809 = 73 * 3833 and the orbit-multiplicity invariant below caught it)
    big32 = admissible_near(32, 279841, 1, below=True)[0]
    cases = [(97, 32, (1,)), (193, 32, (1,)), (257, 32, (1,)), (577, 32, (1,)),
             (7937, 32, (1,)), (32801, 32, (1,)), (big32, 32, (1,)),
             (97, 32, (1, 3)), (193, 32, (1, 3)), (577, 32, (1, 3)),
             (449, 32, (1, 3, 5)), (17, 16, (1,)), (881, 16, (1,)),
             (193, 64, (1,)), (257, 64, (1,)), (641, 64, (1,))]
    for (q, M, U) in cases:
        assert lc.is_prime(q) and (q - 1) % M == 0, (q, M)
    out["minima_law"] = minima_law(cases)
    out["minima_law_all_equal"] = all(r["lambda_h_eq_lambda_1"] for r in out["minima_law"])
    out["minima_law_orbit_multiplicity"] = all(
        r["minimal_points_multiple_of_2h"] for r in out["minima_law"])
    print("S1 minima law: lambda_h = lambda_1 on all %d cases: %s ; point counts "
          "multiples of 2h: %s" % (len(cases), out["minima_law_all_equal"],
                                   out["minima_law_orbit_multiplicity"]), flush=True)

    # doubling needs q = 1 mod 2M so that omega' of exact order 2M exists
    dcases = [(193, 32, (1,)), (257, 32, (1,)), (449, 32, (1,)), (641, 32, (1,)),
              (193, 32, (1, 3)), (257, 32, (1, 3)), (577, 32, (1, 3)),
              (97, 16, (1,)), (193, 16, (1,)), (257, 16, (1,)), (641, 16, (1, 3)),
              (12289, 32, (1,)), (12289, 32, (1, 3))]
    for (q, M, U) in dcases:
        assert lc.is_prime(q) and (q - 1) % (2 * M) == 0, (q, M)
    out["doubling"] = doubling(dcases)
    out["doubling_all_ok"] = all(r["S_inside_L_high"] and r["index_eq_q_pow_o"]
                                 for r in out["doubling"])
    print("S2 doubling index = q^o on all %d cases: %s"
          % (len(dcases), out["doubling_all_ok"]), flush=True)

    cv = os.path.join(RES, "census_validate.json")
    if os.path.exists(cv):
        with open(cv) as f:
            A = json.load(f)["A_2N32_ell1"]["rows"]
        out["separation"] = separation(A)
        print("S3 separation computed", flush=True)
    else:
        print("S3 skipped: census_validate.json not present yet", flush=True)

    with open(os.path.join(RES, "structure.json"), "w") as f:
        json.dump(out, f, indent=1)


if __name__ == "__main__":
    main()
