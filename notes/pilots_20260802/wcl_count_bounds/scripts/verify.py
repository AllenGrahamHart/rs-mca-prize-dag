"""Cheap independent replay of every headline claim of this pilot.
Exit 0 iff all checks pass.  Runs in well under a minute under ramguard local.
"""
import json, os, sys
from fractions import Fraction
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lattice_core as lc
import official_witness as ow

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RES = os.path.join(HERE, "results")
checks = []


def ck(name, cond, detail=""):
    checks.append({"check": name, "pass": bool(cond), "detail": str(detail)})


# T1 determinant of the relation lattice
for (q, M, U) in [(97, 32, (1,)), (97, 32, (1, 3)), (449, 32, (1, 3, 5)),
                  (641, 64, (1, 3))]:
    B, om = lc.relation_lattice_basis(q, M, U)
    ck("T1 det L_{%d,%d,%s} = q^%d" % (q, M, U, len(U)),
       abs(lc.det_int(B)) == q ** len(U), abs(lc.det_int(B)))

# T2 minima law: all successive minima equal (shift orbit is independent)
q, M, U = 193, 32, (1,)
B, om = lc.relation_lattice_basis(q, M, U)
R = lc.fast_lll(B)
ck("T2a reduced basis certified", lc.certify_basis(R, q, M, U, om))
l1 = min(lc.sq_norm(v) for v in lc.enumerate_short(R, 4))
v0 = [v for v in lc.enumerate_short(R, l1) if lc.sq_norm(v) == l1][0]
orb, s = [v0], v0
for _ in range(15):
    s = lc.negacyclic_shift(s)
    orb.append(s)
ck("T2b lambda_h = lambda_1 (16 independent minimal vectors)",
   lc.det_int(orb) != 0 and all(lc.sq_norm(o) == l1 for o in orb), l1)
mins = [v for v in lc.enumerate_short(R, l1) if lc.sq_norm(v) == l1]
ck("T2c #minimal points is a multiple of 2h = 32", (2 * len(mins)) % 32 == 0,
   2 * len(mins))

# T3 doubling sublattice index = q^o
q, M, U = 257, 32, (1,)
omp = lc.element_of_exact_order(q, 2 * M)
om2 = pow(omp, 2, q)
Bl, _ = lc.relation_lattice_basis(q, M, U, omega=om2)
Bh, _ = lc.relation_lattice_basis(q, 2 * M, U, omega=omp)
S = []
for b in Bl:
    e = [0] * 32
    o_ = [0] * 32
    for i in range(16):
        e[2 * i] = b[i]
        o_[2 * i + 1] = b[i]
    S += [e, o_]
ck("T3a iota(L) + x.iota(L) inside L^(2h)",
   all(lc.in_lattice(v, q, 2 * M, U, omp) for v in S))
ck("T3b index = q^o", abs(lc.det_int(S)) // abs(lc.det_int(Bh)) == q ** len(U),
   abs(lc.det_int(S)) // abs(lc.det_int(Bh)))

# T4 AM-GM (kappa >= 1) is TIGHT: the flat weight-7 ternary generates kappa = 1
f = [1, 1, 1, -1, -1, 1, -1, 0]
rows, s = [f[:]], f[:]
for _ in range(7):
    s = lc.negacyclic_shift(s)
    rows.append(s)
det = abs(lc.det_int(rows))
R = lc.fast_lll(rows)
l1 = min(lc.sq_norm(v) for v in lc.enumerate_short(R, 7))
ck("T4 flat weight-7 ideal has N = 7^4 and lambda_1^2 = 7, i.e. kappa = 1",
   det == 2401 and l1 == 7 and l1 ** 4 == det, (det, l1))

# T5 the official-scale separation witness
a = [0] * 256
for (e, sg) in ow.EXPONENTS:
    a[e] = sg
N = ow.norm_negacyclic(a)
q0 = N // 2
ck("T5a recomputed norm matches the banked engineered witness", N == ow.BANKED_NORM)
ck("T5b q0 is a 256-bit prime", lc.is_prime(q0) and q0.bit_length() == 256)
ck("T5c v_2(q0-1) = 9 < 41 (not official)", lc.v2(q0 - 1) == 9)
ck("T5d q0 < 2^256", q0 < (1 << 256))
kap = Fraction(6 ** 128, q0)
ck("T5e kappa(I)^128 = 6^128/q0 gives kappa < 1.508",
   Fraction(1508, 1000) ** 128 > kap and Fraction(1507, 1000) ** 128 <= kap)

# T6 slot arithmetic identities
ck("T6a 4^128 = 2^256 exactly", 4 ** 128 == 1 << 256)
ck("T6b w^128 > 2^256 for every w >= 5", all(w ** 128 > 1 << 256 for w in range(5, 12)))
ck("T6c conditional fence c_5^64 = 23^64 = 279841^16 > 2^256",
   279841 ** 16 == 23 ** 64 and 23 ** 64 > 1 << 256)
QMIN = 3 * (1 << 41) + 1
ck("T6d q_min = 3*2^41+1 is prime with v_2 = 41", lc.is_prime(QMIN) and lc.v2(QMIN - 1) == 41)
ck("T6e at q_min slot (1,5) needs kappa > 3.9",
   Fraction(39, 10) ** 128 * QMIN < 5 ** 128)

# T7 census spot checks against the banked lists
for (q, M, U, w) in [(97, 32, (1,), 3), (193, 32, (1,), 3), (17, 16, (1,), 3),
                     (97, 32, (1, 3), 5), (577, 32, (1, 3), 8)]:
    B, om = lc.relation_lattice_basis(q, M, U)
    R = lc.fast_lll(B)
    vs = [v for v in lc.enumerate_short(R, w) if lc.is_ternary(v)]
    ck("T7 banked minimal weight %d at q=%d M=%d U=%s" % (w, q, M, U),
       vs and min(lc.sq_norm(v) for v in vs) == w,
       min([lc.sq_norm(v) for v in vs], default=None))

ok = all(c["pass"] for c in checks)
with open(os.path.join(RES, "verify.json"), "w") as f:
    json.dump({"checks": checks, "n": len(checks),
               "n_pass": sum(1 for c in checks if c["pass"]), "all_pass": ok}, f, indent=1)
for c in checks:
    print("%-4s %s   %s" % ("PASS" if c["pass"] else "FAIL", c["check"], c["detail"]))
print("\n%d/%d PASS" % (sum(1 for c in checks if c["pass"]), len(checks)))
sys.exit(0 if ok else 1)
