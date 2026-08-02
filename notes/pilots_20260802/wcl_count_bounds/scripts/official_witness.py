"""The official-scale separation witness, verified from scratch.

`dli_wcl_engineered_terminal_scope` (PROVED, background) banks a reduced signed
weight-SIX relation at root order 512:

    P(z) = 1 - z^33 + z^40 - z^136 - z^143 + z^145,

whose cyclotomic norm is 2 * q0 with q0 a 256-bit prime and v_2(q0 - 1) = 9.

This script recomputes the norm by an independent field-norm descent in
Z[x]/(x^256+1), re-certifies q0, and then builds the RELATION LATTICE
L_{q0,512,{1}} -- an ideal lattice with h = 256 and det = q0, i.e. exactly the
shape of an official ell=1 WCL row -- and exhibits P inside it.

Consequence (report section 6): every Minkowski / transference / ball-counting
/ normalized-first-minimum bound is a function of (h, det) only.  This lattice
has the official (h, det) profile and lambda_1^2 <= 6.  So no such bound can
prove any WCL slot whose closure needs lambda_1^2 > 6 -- and none can be proved
at strength kappa > 6 / q0^{1/128} without USING v_2(q-1) >= 41.
"""
import json, os, sys
from fractions import Fraction
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lattice_core as lc

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RES = os.path.join(HERE, "results")

BANKED_NORM = 122312418397310579415219240127455896396372121843316076135243835573788121252866
BANKED_Q0 = 61156209198655289707609620063727948198186060921658038067621917786894060626433
EXPONENTS = [(0, 1), (33, -1), (40, 1), (136, -1), (143, -1), (145, 1)]


def norm_negacyclic(a):
    """Res(f, x^h+1) for f given by coefficient list a (len h a power of two),
    by the field-norm descent  f(x) f(-x) = g(x^2)."""
    h = len(a)
    cur = list(a)
    while h > 1:
        ev = cur[0::2]                     # even part  e(y),  y = x^2
        od = cur[1::2]                     # odd part   o(y)
        # f(x) f(-x) = e(y)^2 - y o(y)^2   in Z[y]/(y^{h/2}+1)
        m = h // 2
        g = [0] * m
        # e^2
        for i, u in enumerate(ev):
            if not u:
                continue
            for j, v in enumerate(ev):
                if not v:
                    continue
                k, s = i + j, 1
                if k >= m:
                    k -= m
                    s = -1
                g[k] += s * u * v
        # - y o^2
        for i, u in enumerate(od):
            if not u:
                continue
            for j, v in enumerate(od):
                if not v:
                    continue
                k, s = i + j + 1, -1
                if k >= m:
                    k -= m
                    s = 1
                g[k] += s * u * v
        cur, h = g, m
    return cur[0]


def main():
    h, M = 256, 512
    a = [0] * h
    for (e, s) in EXPONENTS:
        assert e < h, e
        a[e] = s
    out = {"P_exponents": EXPONENTS, "h": h, "M": M,
           "weight": sum(1 for t in a if t)}

    N = norm_negacyclic(a)
    out["norm_recomputed"] = str(N)
    out["norm_matches_banked"] = (N == BANKED_NORM)
    out["norm_over_2"] = str(N // 2)
    q0 = N // 2
    out["q0"] = str(q0)
    out["q0_matches_banked"] = (q0 == BANKED_Q0)
    out["q0_bits"] = q0.bit_length()
    out["q0_is_prime"] = lc.is_prime(q0)
    out["q0_v2"] = lc.v2(q0 - 1)
    out["q0_lt_2_256"] = q0 < (1 << 256)
    out["official_v2_threshold"] = 41
    out["q0_official_admissible"] = (out["q0_v2"] >= 41)

    # omega of exact order 512 in F_{q0}, and P(omega) = 0
    om = lc.element_of_exact_order(q0, M)
    val = sum(a[i] * pow(om, i, q0) for i in range(h)) % q0
    out["exists_omega_order_512"] = True
    out["P_vanishes_at_some_order_512_root"] = None
    # P vanishes at SOME primitive 512-th root; find the dilation that works
    hit = None
    for u in range(1, M, 2):
        omu = pow(om, u, q0)
        if sum(a[i] * pow(omu, i, q0) for i in range(h)) % q0 == 0:
            hit = u
            break
    out["P_vanishes_at_some_order_512_root"] = hit is not None
    out["vanishing_dilation_u"] = hit
    out["P_value_at_base_omega"] = str(val)

    if hit is not None:
        omh = pow(om, hit, q0)
        B, _ = lc.relation_lattice_basis(q0, M, (1,), omega=omh)
        out["lattice_det_eq_q0"] = (abs(lc.det_int(B)) == q0)
        out["P_in_lattice"] = lc.in_lattice(a, q0, M, (1,), omh)
        out["lambda1_sq_upper_bound"] = 6
        # kappa upper bound: kappa <= 6 / q0^{1/128}, exactly
        # kappa^{128} = (lambda1^2)^{128} / q0
        kap_pow = Fraction(6 ** 128, q0)
        lo, hi = 1, 4000
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if Fraction(mid, 1000) ** 128 <= kap_pow:
                lo = mid
            else:
                hi = mid - 1
        out["kappa_upper_bound_milli"] = lo
        out["kappa_pow128_num"] = str(kap_pow.numerator)
        out["kappa_pow128_den"] = str(kap_pow.denominator)

    # which open slots are refuted for any v_2-blind kappa bound
    need = {"(1,5)": Fraction(5, 4), "(1,6)": Fraction(6, 4), "(1,7)": Fraction(7, 4),
            "(1,8)": Fraction(8, 4), "(2,7)": Fraction(7, 4), "(2,8)": Fraction(8, 4),
            "(2,9)": Fraction(9, 4), "(4,10)": Fraction(10, 4), "(4,11)": Fraction(11, 4)}
    kb = Fraction(out.get("kappa_upper_bound_milli", 0), 1000)
    out["kappa_cap_from_witness"] = str(kb)
    out["slots_beyond_v2_blind_kappa"] = sorted(k for k, v in need.items() if v > kb)
    out["slots_still_reachable_in_principle"] = sorted(k for k, v in need.items()
                                                       if v <= kb)

    with open(os.path.join(RES, "official_witness.json"), "w") as f:
        json.dump(out, f, indent=1)
    for k in ("norm_matches_banked", "q0_matches_banked", "q0_bits", "q0_is_prime",
              "q0_v2", "q0_official_admissible", "P_vanishes_at_some_order_512_root",
              "lattice_det_eq_q0", "P_in_lattice", "kappa_upper_bound_milli",
              "kappa_cap_from_witness", "slots_beyond_v2_blind_kappa",
              "slots_still_reachable_in_principle"):
        print("%-38s %s" % (k, out.get(k)))


if __name__ == "__main__":
    main()
