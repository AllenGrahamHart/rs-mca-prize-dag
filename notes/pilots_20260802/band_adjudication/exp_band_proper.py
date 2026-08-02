"""exp_band_proper.py -- can a coset (MC-type) construction reach a BAND
PROPER depth d <= h-2, i.e. produce depth-d band pairs that carry LIVE
slopes?

Mechanism under test.  On the shift pencil v = u/X^j (the only shift for
which the WHOLE MC family stays joint, because X^(M-1) | P_T), the
direction map of every depth-d pair is zeta_P(i) = -x_i^j.  Its fibres on
H are mu_g-cosets with g = gcd(j,n), and T is a union of mu_M-cosets with
g | M, so |zeta_P^{-1}(z) cap T| is 0 or exactly g.  A forced ray therefore
has agreement (k+d) + g, and

    g <  h-d  ->  agreement < A : NO live slope (invisible to occupancy)
    g == h-d  ->  agreement = A : LIVE  (the only productive case)
    g >  h-d  ->  agreement > A : the TANGENT gate breaks (T2/P2 fires and
                                   the pair leaves the generic branch)

so the construction is productive at depth d IFF some j <= M-1 = d-1 has
gcd(j,n) = h-d.  At the six official rows n and k are 2-powers, so d must
be a 2-power (rows.py section 2) and g is a 2-power, while h is ODD, so
h-d is ODD for every even d: g = h-d forces g = 1, i.e. d = h-1.  THE BAND
PROPER IS UNREACHABLE.

PRE-REGISTERED PREDICTIONS:
 S1  h EVEN toy row (h = 6, d = 4 in the band proper [3,4]), j = 2:
     gcd(2,n) = 2 = h-d, so live slopes DO appear and the band proper IS
     reached -- the mechanism is real, the official rows are protected by
     PARITY, not by the mechanism being impossible.
 S2  Even then the slopes CONFINE: Gamma is contained in {-x^j : x in H},
     of size n/gcd(j,n) = n/(h-d), so |Gamma| <= n/(h-d) and (with the
     banked exclusivity) N_d <= n/(2(h-d)) -- LINEAR in n, never n^2.
 S3  Same row, j = 1: agreement k+d+1 < A, ZERO live slopes.
 S4  h ODD toy row (h = 7, d = 4 in the band proper [4,5]): h-d = 3 and
     no j has gcd(j,20) = 3, so NO j is productive -- zero live slopes for
     every j in [1, M-1].  This is the toy analogue of the official rows.
"""

import json
import os
import sys
from math import comb, gcd

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from mclib import INF, Scan, make_domain, mc_c_from_gamma, mc_family, poly_eval

CHK = os.path.join(HERE, "checkpoints")
os.makedirs(CHK, exist_ok=True)

out = {"predictions": __doc__, "fixtures": [], "checks": 0, "fails": []}


def chk(cond, label, extra=None):
    out["checks"] += 1
    if not cond:
        out["fails"].append({"label": label, "extra": str(extra)})
        print("    FAIL", label, extra)
    return cond


def run(n, k, w, M, q, t, j):
    rp = n - k - w
    N, m = n // M, rp // M
    H, beta, omega = make_domain(q, n, beta_exp=0)
    c = mc_c_from_gamma(H, q, n, k, w, M)
    u = [0] * n
    u[n - 1] = 1
    u[k + w - 1] = (u[k + w - 1] + c) % q
    v = [0] * n
    v[n - 1 - j] = 1
    v[k + w - 1 - j] = (v[k + w - 1 - j] + c) % q
    h, A, d = t, k + t, w
    uv = [poly_eval(u, x, q) for x in H]
    vv = [poly_eval(v, x, q) for x in H]
    fam = mc_family(H, q, n, k, w, M, c)
    g = gcd(j, n)
    sc = Scan(H, q, k, uv, vv, A)
    live = sc.live()
    Nd, Nd_any, detail = sc.occupancy()
    img = set((-pow(x, j, q)) % q for x in H)

    band_proper = (-(-h // 2) <= d <= h - 2)
    rec = {"n": n, "k": k, "w": w, "M": M, "q": q, "t": t, "j": j,
           "h": h, "A": A, "d": d, "gcd_j_n": g, "h_minus_d": h - d,
           "d_in_band_proper": band_proper,
           "mc_family": len(fam),
           "band_pairs_at_d": sum(1 for P, dep in sc.band_pairs().items()
                                  if dep == d),
           "pencil_max_agreement": max(sc.max_agr.values()),
           "gate_ok": sc.gate_ok(),
           "n_live": len(live),
           "image_size_n_over_g": n // g,
           "live_inside_image": all(z != INF and z in img for z in live),
           "N_d_selected": Nd.get(d, 0),
           "N_d_any": Nd_any.get(d, 0),
           "productive": g == h - d}

    chk(rec["pencil_max_agreement"] == k + d + g
        or rec["pencil_max_agreement"] == k + d,
        "forced ray agreement = k+d+gcd(j,n)",
        (n, k, w, q, t, j, rec["pencil_max_agreement"], k + d + g))
    chk((g == h - d) == (len(live) > 0),
        "live slopes exist IFF gcd(j,n) = h-d",
        (n, k, w, q, t, j, g, h - d, len(live)))
    chk((g > h - d) == (not sc.gate_ok()),
        "gate breaks IFF gcd(j,n) > h-d",
        (n, k, w, q, t, j, g, h - d, sc.gate_ok()))
    chk(rec["live_inside_image"] or not live,
        "S2 Gamma is confined to {-x^j}",
        (n, k, w, q, t, j, len(live)))
    chk(len(live) <= n // g, "S2 |Gamma| <= n/gcd(j,n)",
        (n, k, w, q, t, j, len(live), n // g))
    chk(Nd.get(d, 0) <= max(1, n // (2 * g)), "S2 N_d <= n/(2 gcd(j,n))",
        (n, k, w, q, t, j, Nd.get(d, 0), n // (2 * g)))

    print("  n=%-3d k=%-2d d=w=%-2d h=%-2d A=%-3d j=%-2d | h-d=%-2d "
          "gcd(j,n)=%-2d productive=%-5s | band-proper d? %-5s | MC=%-3d "
          "pairs@d=%-3d maxagr=%-3d gate=%-5s | |Gamma|=%-3d (<= n/g=%-3d, "
          "confined=%-5s) N_d=%d"
          % (n, k, d, h, A, j, h - d, g, rec["productive"], band_proper,
             len(fam), rec["band_pairs_at_d"], rec["pencil_max_agreement"],
             sc.gate_ok(), len(live), n // g, rec["live_inside_image"],
             Nd.get(d, 0)))
    return rec


print("=== S1/S2/S3: h EVEN (h=6) -- band proper [3,4] contains d=4 ===")
for q in (41, 101, 181):
    for j in (1, 2, 3):
        out["fixtures"].append(run(20, 4, 4, 4, q, t=6, j=j))

print()
print("=== S4: h ODD (h=7) -- band proper [4,5] contains d=4; "
      "h-d=3 and 3 does not divide n=20 ===")
for q in (41, 101, 181):
    for j in (1, 2, 3):
        r = run(20, 4, 4, 4, q, t=7, j=j)
        chk(r["n_live"] == 0, "S4 odd-h band proper: no live slopes",
            (q, j, r["n_live"]))
        out["fixtures"].append(r)

print()
print("=== control: d = h-1 (the cascade tier) on the same shapes ===")
for q in (41, 101, 181):
    out["fixtures"].append(run(20, 4, 4, 4, q, t=5, j=1))

out["verdict"] = "PASS" if not out["fails"] else "FAIL"
with open(os.path.join(CHK, "band_proper.json"), "w") as f:
    json.dump(out, f, indent=1)
print("\nchecks=%d fails=%d -> %s" % (out["checks"], len(out["fails"]),
                                      out["verdict"]))
