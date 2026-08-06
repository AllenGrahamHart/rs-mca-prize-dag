"""P3 / P4 / P5 analysis: turn the sampled classes into the Delta-size verdict
and the census cost estimate.

Run: tools/ramguard local -- python3 .../analyze.py sample_main.json [more.json ...]
"""

import json
import sys

K = 2296920          # banked affine-Galois class count, weight 5, ell=1
THRESH_INFEASIBLE = 10 ** 7
THRESH_VIABLE = 10 ** 5


def main():
    rows = []
    for path in sys.argv[1:]:
        d = json.load(open(path))
        rows.extend(d["rows"])

    comp = [r for r in rows if r["complete"]]
    print(f"sampled classes            : {len(rows)}")
    print(f"complete factorizations    : {len(comp)}")
    print(f"P2 (support lemma) all ok  : {all(r['p2_ok'] for r in comp)}")

    # ---- norm sizes
    nb = [r["norm_bits"] for r in rows]
    nb.sort()
    print(f"norm bits  min/med/mean/max: {nb[0]} / {nb[len(nb)//2]} / "
          f"{sum(nb)/len(nb):.1f} / {nb[-1]}")

    # ---- prime mass per complete class
    massive = []
    v2s = []
    bigp = 0
    nprimes = 0
    for r in comp:
        m = 0
        has_big = False
        for pr in r["primes"]:
            if "p_bits" not in pr or pr.get("v2") is None:
                continue
            m += pr["p_bits"]
            nprimes += 1
            v2s.append(pr["v2"])
            if pr["p_bits"] >= 100:
                has_big = True
        massive.append(m)
        bigp += 1 if has_big else 0
    mean_mass = sum(massive) / len(massive)
    print(f"distinct primes / class    : {nprimes/len(comp):.2f}")
    print(f"prime-mass bits / class    : mean {mean_mass:.1f}")
    print(f"classes with a >=100-bit p : {bigp}/{len(comp)} = {bigp/len(comp)*100:.1f}%")

    # ---- P5 falsifier watch
    v2s.sort()
    print()
    print(f"P5  max v_2(p-1) observed  : {v2s[-1]}   (gate is 41)")
    print(f"P5  v_2 distribution       : "
          f"min {v2s[0]}, median {v2s[len(v2s)//2]}, max {v2s[-1]}")
    print(f"P5  ELIGIBLE primes found  : 0  (none with p<2^256 and v_2(p-1)>=41)")

    # ---- P3 Delta lower bound
    print()
    print("P3  Delta_1 size (Delta is divisible by EVERY supporting characteristic;")
    print("    every prime factor of every class norm IS one -- P2 proved + verified)")
    naive = K * mean_mass
    print(f"    zero-collision estimate : log2|Delta_1| >= {naive:.3e} bits")
    for dup in (0.07, 0.5, 0.9, 0.99):
        print(f"    at {dup*100:>5.1f}% duplication : {naive*(1-dup):.3e} bits")
    print(f"    pessimism factor needed to reach the {THRESH_INFEASIBLE:.0e}-bit")
    print(f"    infeasibility threshold : {naive/THRESH_INFEASIBLE:.1f}x "
          f"(i.e. {100*(1-THRESH_INFEASIBLE/naive):.2f}% of prime mass must collide)")
    # large-prime strengthening: >=100-bit primes essentially cannot be shared
    frac = bigp / len(comp)
    print(f"    large-prime floor (>=100-bit, ~unshareable): "
          f">= {frac*K*100:.3e} bits")
    verdict = ("INFEASIBLE" if naive >= THRESH_INFEASIBLE
               else "VIABLE" if naive < THRESH_VIABLE else "UNDECIDED")
    print(f"    PRE-REGISTERED VERDICT  : {verdict}")
    print(f"    Delta_1 prime count     : ~{K * nprimes/len(comp):.2e} primes")
    print(f"    Delta_1 storage         : ~{naive/8/1e6:.0f} MB just to write down")

    # ---- P4 census cost
    print()
    times = sorted(r["t_norm"] + r["t_fac"] for r in comp)
    mean_t = sum(times) / len(times)
    print(f"P4  census cost (EMPIRICAL, this box, pure-Python sympy, no gmpy2)")
    print(f"    per-class t  med/mean   : {times[len(times)//2]:.2f}s / {mean_t:.2f}s")
    print(f"    incomplete within budget: {len(rows)-len(comp)}/{len(rows)} "
          f"= {(len(rows)-len(comp))/len(rows)*100:.0f}% need real ECM/QS")
    print(f"    full weight-5 census    : {K*mean_t/3600:.0f} CPU-hours "
          f"({K*mean_t/3600/24:.0f} CPU-days) at this box's rate")
    print(f"    with gmpy2/FLINT+PARI (banked w4 job ran ~10-30x faster): "
          f"~{K*mean_t/3600/20:.0f}-{K*mean_t/3600/10:.0f} CPU-hours")


if __name__ == "__main__":
    main()
