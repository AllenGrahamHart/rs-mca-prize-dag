#!/usr/bin/env python3
"""c2pp_gb_probe -- independent verification of the three structural claims.

V1  BRUTE FORCE: at n=16 enumerate all 2^16 indicator vectors x and rebuild
    C_j, Z_j and omega_j from scratch; must equal the MITM machinery.
    Independent-machinery cross-check of the whole instrument.
V2  P[coset column] is q-INDEPENDENT: P_U[S_j = empty] = 2^{h-n} exactly.
V3  THE CEILING THEOREM: omega_j <= 2^{n - h_{j+1}} for EVERY q, because
    the numerator is a probability and the denominator has no q in it.
    Checked against every measured row.
V4  THE SATURATION CLOSED FORM at the T = h/2 cells (n/t = 2):
    Z_j^inf = sum_{c=0}^{u} C(u,c)^h   (the constant states c*1 are the ONLY
    T-null level states), C_j^inf = 2, so
    log2 omega_j^inf = (n - h + 1) - log2( sum_c C(u,c)^h ), q-free.
"""
import json
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from gb_probe import (level_vectors, mitm_null_count, binom_alpha,   # noqa: E402
                      subset_alpha, get_zeta, log2_int)

fail = []


def check(name, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}  {detail}")
    if not ok:
        fail.append(name)


# ------------------------------------------------------- V1 brute force n = 16
print("V1  BRUTE FORCE at n=16 (all 2^16 x enumerated, independent machinery)")
for (n, t, q, j) in [(16, 4, 97, 0), (16, 4, 193, 0), (16, 8, 97, 0),
                     (16, 4, 97, 1), (16, 8, 193, 1), (16, 8, 97, 2)]:
    lev = j + 1
    h = n // 2 ** lev
    T = t // 2 ** lev
    if T < 1 or h < 2:
        continue
    zeta_h = pow(get_zeta(q, n), 2 ** lev, q)
    u = 2 ** lev
    tab = [[pow(zeta_h, (r * i) % h, q) for i in range(h)]
           for r in range(1, T + 1)]
    cellof = [i % h for i in range(n)]
    Cb = Zb = 0
    for x in range(1 << n):
        M = [0] * h
        y = x
        i = 0
        while y:
            if y & 1:
                M[cellof[i]] += 1
            y >>= 1
            i += 1
        if all(sum(M[i] * row[i] for i in range(h)) % q == 0 for row in tab):
            Zb += 1
            if all(v == 0 or v == u for v in M):
                Cb += 1
    _, _, vecs = level_vectors(q, n, t, lev)
    Cm = mitm_null_count(vecs, subset_alpha(), q, T)
    Zm = mitm_null_count(vecs, binom_alpha(u), q, T)
    check(f"n={n} t={t} q={q} j={j}: brute(C,Z)=({Cb},{Zb}) vs "
          f"MITM=({Cm},{Zm})", (Cb, Zb) == (Cm, Zm))

# --------------------------------------------- V2 coset probability, q-free
print("\nV2  P_U[coset column] = 2^(h-n), with NO q in it")
for (n, lev) in [(12, 1), (16, 1), (16, 2), (16, 3)]:
    h = n // 2 ** lev
    u = 2 ** lev
    cnt = 0
    for x in range(1 << n):
        M = [0] * h
        for i in range(n):
            if (x >> i) & 1:
                M[i % h] += 1
        if all(v == 0 or v == u for v in M):
            cnt += 1
    check(f"n={n} level={lev}: |coset|={cnt} == 2^h={2 ** h}", cnt == 2 ** h)
print("     (closed form 2^h/2^n; the coset column is a SUPPORT condition on "
      "the\n      unconditional measure -- q does not enter its definition "
      "or its value.)")

# --------------------------------- V3 + V4 against every banked measured row
with open(os.path.join(HERE, "gb_results.json")) as fh:
    ST = json.load(fh)

print("\nV3  CEILING THEOREM  log2 omega_j <= n - h_{j+1}, every q, every cell")
worst = []
for key, rec in ST["rows"].items():
    n = rec["n"]
    for u_ in rec["junctions"]:
        ok = u_["log2_omega"] <= u_["ceiling_bits"] + 1e-9
        if not ok:
            fail.append(f"ceiling violated {key} j={u_['j']}")
        worst.append((u_["log2_omega"] / u_["ceiling_bits"], key, u_["j"],
                      u_["log2_omega"], u_["ceiling_bits"]))
worst.sort(reverse=True)
check(f"{len(worst)} (row, junction) pairs all satisfy the ceiling",
      not [f for f in fail if "ceiling" in f])
for w in worst[:3]:
    print(f"      tightest: {w[1]} j={w[2]}: {w[3]:.4f} of {w[4]} bits "
          f"({100 * w[0]:.2f}% of the ceiling)")

print("\nV4  SATURATION CLOSED FORM at the n/t = 2 cells")
for key, rec in sorted(ST["rows"].items()):
    cell = key.split("|")[0]
    n, t = rec["n"], rec["t"]
    if n / t != 2 or rec["q"] < 1000:
        continue
    for u_ in rec["junctions"]:
        h, uu = u_["h"], u_["u"]
        pred = sum(math.comb(uu, c) ** h for c in range(uu + 1))
        ok = (u_["Z_j"] == pred) and (u_["C_j"] == 2)
        lw = (n - h + 1) - log2_int(pred)
        ok &= abs(lw - u_["log2_omega"]) < 1e-9
        if not ok:
            fail.append(f"closed form {key} j={u_['j']}")
    if rec["q"] < 5000:
        js = "  ".join(
            f"j={u_['j']}: Z={u_['Z_j']} == sum_c C({u_['u']},c)^{u_['h']}"
            for u_ in rec["junctions"])
        print(f"    {cell} q={rec['q']}: {js}")
check("closed form Z_j = sum_c C(u,c)^h and C_j = 2 at every n/t=2 row",
      not [f for f in fail if "closed form" in f])

# ------------------------------------------------- the official-scale ceiling
N_OFF, JUNC = 2 ** 41, 33
ceil_off = sum(N_OFF - N_OFF // 2 ** (j + 1) for j in range(JUNC))
print(f"\nOFFICIAL-SCHEDULE CEILING of the G-b functional (n=2^41, 33 junctions):"
      f"\n    sum_j (n - h_(j+1)) = {ceil_off} = 2^46 + 256 bits"
      f"  [{ceil_off == 2 ** 46 + 256}]"
      f"\n    -- finite and q-FREE, so 'growing without bound in q' is "
      "impossible;\n       but it exceeds the 21-bit reserve by a factor "
      f"{ceil_off / 21:.3e}, so the\n       non-firing carries no information "
      "about C2''-r3.  SCOPE: this ceiling is\n       a property of the "
      "SCHEDULE, not a measurement, and is not a reserve bound.")

print("\n" + ("ALL CHECKS PASS" if not fail else f"FAILURES: {fail}"))
sys.exit(1 if fail else 0)
