#!/usr/bin/env python3
"""P-A1 widening cost: exact row arithmetic.

Compares every banked numeric close at the CURRENT pairwise-core cap
kappa = k against the WIDENED cap kappa = A-2 forced by repair R2
(cores in [k, A-2]; the A-2 ceiling is supplied by xr_pencil_cascade).

Run under: tools/ramguard tiny -- python3 <this>
"""
from math import comb
import json

ROWS = []
for name, n, rate, scale in [
    ("RowC 1/4", 1024, 4, 256),
    ("RowC 1/8", 1024, 8, 256),
    ("RowC 1/16", 1024, 16, 512),
    ("prize 1/4", 2**41, 4, 256),
    ("prize 1/8", 2**41, 8, 256),
    ("prize 1/16", 2**41, 16, 512),
]:
    k = n // rate
    A = k + n // scale + 1
    ROWS.append(dict(name=name, n=n, k=k, A=A, h=A - k, r=n - A, R=n - k,
                     budget=8 * n**3, half=4 * n**3))

out = {}

print("=== 1. row constants and the widened band ===")
print(f"{'row':<11}{'n':>14}{'k':>14}{'A':>14}{'h':>13}{'r':>14}{'R':>14}"
      f"{'band [k,A-2] width':>20}")
for row in ROWS:
    w = row["A"] - 2 - row["k"] + 1
    print(f"{row['name']:<11}{row['n']:>14}{row['k']:>14}{row['A']:>14}"
          f"{row['h']:>13}{row['r']:>14}{row['R']:>14}{w:>20}")
out["rows"] = ROWS

print()
print("=== 2. collapsed-face exclusion (xr_higher_rank_collapsed_face_exclusion) ===")
print("CFE derives a common zero set of size k+2 and contradicts it against the")
print("cap.  Under widening the only available cap is A-2 = k+h-2.")
print("CFE SURVIVES iff k+2 > A-2, i.e. iff h < 4.")
print(f"{'row':<11}{'h':>13}{'k+2 > A-2 ?':>14}{'verdict':>12}")
cfe = {}
for row in ROWS:
    ok = row["k"] + 2 > row["A"] - 2
    cfe[row["name"]] = ok
    print(f"{row['name']:<11}{row['h']:>13}{str(ok):>14}"
          f"{('SURVIVES' if ok else 'BREAKS'):>12}")
out["cfe_survives"] = cfe

print()
print("=== 3. uniform split-pencil reduction: transported block cap ===")
print("post-puncture block cap  a (kappa=k)  ->  a+h-2 (kappa=A-2)")
print("(HR) rank-one exclusion needs a common support of size >= a+1 to exceed")
print("the cap: survives iff a+1 > a+h-2, i.e. iff h < 3.")
print("(HR7) union lower bound 2(a+1)-cap = a+2 becomes a+4-h: informative iff h<4.")
print(f"{'row':<11}{'h':>13}{'rank1 excl':>12}{'union lb 2(a+1)-cap':>22}")
for row in ROWS:
    h = row["h"]
    print(f"{row['name']:<11}{h:>13}{('SURVIVES' if h < 3 else 'BREAKS'):>12}"
          f"{'a+' + str(4 - h) if h <= 4 else 'a-' + str(h - 4):>22}")

print()
print("=== 4. pencil / collision-line population cap L(kappa)=floor((n-kappa)/(A-kappa)) ===")
print("(CLB2 in xr_highcore_collision_line_basis_ledger; L in")
print(" xr_rs_flat_nullity_basis_charge (FN3); (PSP) in xr_poststrip_affine_pencil_charge)")
print(f"{'row':<11}{'L(k)=floor(R/h)':>18}{'L(A-2)=floor((r+2)/2)':>24}{'blow-up':>16}")
Ltab = {}
for row in ROWS:
    n, k, A, h, r = row["n"], row["k"], row["A"], row["h"], row["r"]
    Lk = (n - k) // (A - k)
    LA = (n - (A - 2)) // (A - (A - 2))
    Ltab[row["name"]] = (Lk, LA)
    print(f"{row['name']:<11}{Lk:>18}{LA:>24}{LA / Lk:>16.4g}")
out["line_cap"] = Ltab

print()
print("=== 4b. L(kappa) across the whole band (RowC rows, exact) ===")
for row in ROWS[:3]:
    n, k, A = row["n"], row["k"], row["A"]
    vals = [(w, (n - w) // (A - w)) for w in range(k, A - 1)]
    print(f"  {row['name']:<11} " + "  ".join(f"w={w}:L={L}" for w, L in vals))

print()
print("=== 5. (PSP) post-strip affine-pencil charge: paid full-domain selector ranks ===")
print("|P| C(h+a,a) <= C(n,a) * L(kappa);  paid rank s=a+1 while RHS/C(h+a,a) <= 8n^3")


def psp_max_a(row, kappa, budget):
    n, A, h = row["n"], row["A"], row["h"]
    L = (n - kappa) // (A - kappa)
    best = 0
    for a in range(1, 80):
        if comb(n, a) * L // comb(h + a, a) <= budget:
            best = a
        else:
            break
    return best, L


print(f"{'row':<11}{'kappa=k: max a':>16}{'-> paid rank s':>16}"
      f"{'kappa=A-2: max a':>18}{'-> paid rank s':>16}")
psp = {}
for row in ROWS:
    a1, _ = psp_max_a(row, row["k"], row["budget"])
    a2, _ = psp_max_a(row, row["A"] - 2, row["budget"])
    psp[row["name"]] = (a1 + 1, a2 + 1)
    print(f"{row['name']:<11}{a1:>16}{a1 + 1:>16}{a2:>18}{a2 + 1:>16}")
out["psp_paid_rank"] = psp

print()
print("=== 6. (ACG) affine-core cogirth ray bound: CORE-AGNOSTIC ===")
print("|P| C(h+a,a) <= C(n,a)(n-a) -- no core hypothesis anywhere in the statement")


def acg_max_a(row, budget):
    n, h = row["n"], row["h"]
    best = 0
    for a in range(1, 80):
        if comb(n, a) * (n - a) // comb(h + a, a) <= budget:
            best = a
        else:
            break
    return best


print(f"{'row':<11}{'max a':>10}{'paid rank s':>14}{'paid rank s at 4n^3':>22}")
for row in ROWS:
    a1 = acg_max_a(row, row["budget"])
    a2 = acg_max_a(row, row["half"])
    print(f"{row['name']:<11}{a1:>10}{a1 + 1:>14}{a2 + 1:>22}")

print()
print("=== 7. (SEL) all-LineRay affine-core bound: CORE-AGNOSTIC ===")
print("|Gamma| <= C(sigma+r,sigma); largest sigma paid at 8n^3 and at 4n^3")
print(f"{'row':<11}{'sigma@8n^3':>12}{'sigma@4n^3':>12}{'C(3+r,3)/n^3':>16}")
for row in ROWS:
    r, b, hb = row["r"], row["budget"], row["half"]
    s8 = max(s for s in range(1, 12) if comb(s + r, s) <= b)
    s4 = max(s for s in range(1, 12) if comb(s + r, s) <= hb)
    print(f"{row['name']:<11}{s8:>12}{s4:>12}"
          f"{comb(3 + r, 3) / row['n']**3:>16.6f}")

print()
print("=== 8. (FN4) persistent-root packing, p=0: |P| C(A,t) <= C(n,t), t=kappa+1 ===")
print(f"{'row':<11}{'kappa=k -> |P| bound':>26}{'kappa=A-2 -> |P| bound':>28}{'8n^3':>26}")
for row in ROWS[:3]:
    n, A, k = row["n"], row["A"], row["k"]
    t1 = k + 1
    b1 = comb(n, t1) // comb(A, t1)
    t2 = (A - 2) + 1
    b2 = comb(n, t2) // comb(A, t2) if t2 <= A else None
    print(f"{row['name']:<11}{b1:>26}{str(b2):>28}{row['budget']:>26}")
print("  (prize rows omitted: C(n,k+1) with k=2^39 is not representable)")

print()
print("=== 9. Maxwell core-size cap L_max = floor((2R+h-1)/h)  [(PB1)] ===")
print("derived from (HR2), whose derivation uses the KERNEL dimension a, not the")
print("pairwise cap -- so it is expected to be unchanged by the widening.")
for row in ROWS[3:]:
    Lm = (2 * row["R"] + row["h"] - 1) // row["h"]
    print(f"  {row['name']:<11} L_max = {Lm}   (statement (PB2) prints 384/448/960)")

print()
print("=== 10. GRK atlas: union size under widening ===")
print("core w in [k,A-2]  =>  |E union E'| = n-w in [r+2, R]; d_C = |U_C|-R can go")
print("NEGATIVE (down to 2-h).  Padding U_C up to R gives d=0 and |Z_C| <= R.")
print(f"{'row':<11}{'R (=|Z_C| cap at d=0)':>24}{'min union r+2':>16}{'min d_C':>10}")
for row in ROWS:
    print(f"{row['name']:<11}{row['R']:>24}{row['r'] + 2:>16}{2 - row['h']:>10}")

with open("notes/pilots_20260802/p_a1_widening_cost/row_arith.json", "w") as fh:
    json.dump(out, fh, indent=1, default=str)
print()
print("checkpoint written: row_arith.json")
