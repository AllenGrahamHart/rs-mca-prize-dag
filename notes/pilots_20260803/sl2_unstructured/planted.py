#!/usr/bin/env python3
"""SL-2 pilot, route (3): PLANT a SUB-DEPTH coset family (M < d).

PROFILE: local.   Run:  tools/ramguard local -- python3 <this>

BP(1) (banked, xr_mc_depth_quantization) concludes "structured => d is a
power of two" only for the scale PINNED by definitions item 10,
M = 2^ceil(log2 d) >= d.  The coset structure itself forces only M | d.
This file realizes the M < d case CONCRETELY, in a toy, by DESCENT:

  * take an MC shift pencil (U, V) for the QUOTIENT instance
    RS_{k/M} on mu_{n/M} at depth d' (banked MC-1/MC-5),
  * LIFT it:  u(X) = X^{rho_u} U(X^M),  v(X) = X^{rho_v} V(X^M),
  * the entire quotient family lifts to depth d = M d' upstairs, with
    core complements that are mu_M-coset unions and M < d.

Measured, exhaustively:
  L1  the lifted family is EXACTLY the set of scale-M cores upstairs
      (bijection with the quotient joint cores),
  L2  the upstairs depth is d = M d' with M < d  (item-10 "structured"
      would demand M = 2^ceil(log2 d) >= d -- this family is NOT of that
      form, so BP(1) does not apply to it),
  L3  the upstairs excess h (max agreement over the pencil minus k)
      satisfies  d = h - M,  i.e. the QUOTIENT CASCADE TIER d' = h'-1
      lifts to a BAND-PROPER depth upstairs whenever 2 <= M <= (h+2)/4,
  L4  P3 EVASION: with rho_u != rho_v no pencil member w_z is
      M-quotient-periodic (its syndrome window meets two classes mod M),
      yet every member still admits the whole family -- so a per-word
      quotient-periodicity test does not see this adversary,
  L5  KEY LEMMA: every joint core has A(Z) = B(Z) = 0, so all q+1
      members interpolate to codewords on it.

This is an ALGEBRA/MECHANISM demonstration, not a count claim: by SL-3
sub-criticality a toy cannot exhibit the blow-up.
"""
import json
from itertools import combinations

from algebra import (cyc, direct_core, evalpoly, inv, lemmaW, locator,
                     pmul, root_of_unity)

# -------------------------------------------------------------- fixture
Q = 97
N_UP, K_UP, M = 16, 4, 2          # upstairs row
NQ, KQ = N_UP // M, K_UP // M     # quotient: N=8, k'=2
DQ = 2                            # quotient depth d'
D_UP = M * DQ                     # upstairs depth d = 4  (M = 2 < d = 4)
MPRIME = 2                        # MC scale downstairs (M' | N, M' | m)
RHO_U, RHO_V = 0, 1               # DIFFERENT classes mod M  -> P3 evasion

checks = []


def ck(name, ok, extra=None):
    checks.append(dict(check=name, ok=bool(ok), extra=extra))
    return ok


def maxagr(u_poly, n, k, q, rmax):
    """max agreement of any codeword (deg < k) with u, by LEMMA W."""
    for rr in range(0, rmax + 1):
        d = n - k - rr
        if d < 0:
            continue
        g = root_of_unity(n, q)
        H = [pow(g, i, q) for i in range(n)]
        for T in combinations(range(n), rr):
            ok, _ = lemmaW(u_poly, [H[i] for i in T], n, k, d, q)
            if ok:
                return n - rr
    return None


def main():
    q = Q
    n, k, d = N_UP, K_UP, D_UP
    rp = n - k - d
    m = rp // M
    g = root_of_unity(n, q)
    H = [pow(g, i, q) for i in range(n)]
    gN = pow(g, M, q)
    HQ = [pow(gN, i, q) for i in range(NQ)]
    mq = NQ - KQ - DQ                       # quotient r'  (= m)
    ck("quotient r' == m", mq == m, dict(mq=mq, m=m))

    # ---- quotient MC word U = Y^{N-1} + c' Y^{k'+d'-1}, c' from a valid
    #      mu_{M'}-coset union (MC-1/MC-3, banked)
    NP, mp = NQ // MPRIME, mq // MPRIME
    A0 = [i + j * NP for i in range(mp) for j in range(MPRIME)]
    prod0 = 1
    for i in A0:
        prod0 = prod0 * HQ[i] % q
    cprime = ((-1) ** (mq + 1) * prod0) % q
    U = [0] * NQ
    U[NQ - 1] = 1
    U[KQ + DQ - 1] = cprime
    # ---- MC-5 shift pencil downstairs: V = U / Y  (j = 1 <= M'-1)
    V = [U[(s + 1) % NQ] for s in range(NQ)]

    U_vec = [evalpoly(U, y, q) for y in HQ]
    V_vec = [evalpoly(V, y, q) for y in HQ]

    # ---- quotient joint cores (exhaustive)
    qcores = []
    for A in combinations(range(NQ), mq):
        Ap = [HQ[i] for i in A]
        a, _ = lemmaW(U, Ap, NQ, KQ, DQ, q)
        b, _ = lemmaW(V, Ap, NQ, KQ, DQ, q)
        a2 = direct_core(U_vec, HQ, A, NQ, KQ, DQ, q)[0]
        b2 = direct_core(V_vec, HQ, A, NQ, KQ, DQ, q)[0]
        ck("quotient lemmaW == direct", a == a2 and b == b2)
        if a and b:
            qcores.append(A)
    ck("quotient joint family NON-EMPTY", len(qcores) > 0,
       dict(count=len(qcores)))

    # ---- LIFT
    u = [0] * n
    v = [0] * n
    for s in range(NQ):
        u[(RHO_U + s * M) % n] = U[s]
        v[(RHO_V + s * M) % n] = V[s]
    u_vec = [evalpoly(u, x, q) for x in H]
    v_vec = [evalpoly(v, x, q) for x in H]

    # ---- L1: exhaustive upstairs census at depth d
    up_u, up_v, up_joint, up_coset = [], [], [], []
    for T in combinations(range(n), rp):
        Tp = [H[i] for i in T]
        a, _ = lemmaW(u, Tp, n, k, d, q)
        b, _ = lemmaW(v, Tp, n, k, d, q)
        a2 = direct_core(u_vec, H, T, n, k, d, q)[0]
        b2 = direct_core(v_vec, H, T, n, k, d, q)[0]
        if a != a2 or b != b2:
            ck("upstairs lemmaW == direct", False, dict(T=T))
        if a:
            up_u.append(T)
        if b:
            up_v.append(T)
        if a and b:
            up_joint.append(T)
            cnt = {}
            for i in T:
                cnt[i % NQ] = cnt.get(i % NQ, 0) + 1
            if all(x == M for x in cnt.values()):
                up_coset.append(T)
    lifted = set()
    for A in qcores:
        lifted.add(tuple(sorted(i + j * NQ for i in A for j in range(M))))
    ck("L1: upstairs joint cores == LIFTED quotient joint cores",
       set(up_joint) == lifted,
       dict(upstairs=len(up_joint), lifted=len(lifted),
            coset_unions=len(up_coset)))
    ck("L1b: every upstairs joint core is a mu_M-coset union",
       len(up_coset) == len(up_joint))
    ck("L1c: E_T(X) = G(X^M) for every upstairs joint core",
       all(all(c == 0 for i, c in enumerate(locator([H[i] for i in T], q))
               if i % M) for T in up_joint))

    # ---- L2: the scale is SUB-DEPTH
    item10_M = 1 << (d - 1).bit_length()          # 2^ceil(log2 d)
    ck("L2: M < d  (BP(1)/item-10 scale would be 2^ceil(log2 d) >= d)",
       M < d and M != item10_M,
       dict(M=M, d=d, item10_scale=item10_M, M_divides_d=(d % M == 0)))

    # ---- L3: the induced excess h upstairs, and the band-proper test
    rmax = rp - 1
    ag_u = maxagr(u, n, k, q, rmax)
    ag_v = maxagr(v, n, k, q, rmax)
    ag_z = {}
    for z in [1, 2, 3, 5, 7, 11, 13]:
        wz = [(u[i] + z * v[i]) % q for i in range(n)]
        ag_z[z] = maxagr(wz, n, k, q, rmax)
    A_gate = max([x for x in [ag_u, ag_v] + list(ag_z.values())
                  if x is not None])
    h_up = A_gate - k
    band_lo, band_hi = -(-h_up // 2), h_up - 2
    # L3 AS PRE-REGISTERED WAS MIS-SPECIFIED and is recorded as FAILED:
    # it predicted d = h - M and a band-proper landing using the toy's
    # MEASURED ceiling as h.  h is an AMBIENT ROW parameter (the tangent
    # gate A = k+h), not the word's own ceiling; a toy has no independent
    # gate, so its measured h necessarily sits just above the planted
    # family.  The band-proper landing is ROW ARITHMETIC and is decided
    # in descent.py, not here.  Both readings are reported.
    l3_prereg = dict(predicted_d=h_up - M, actual_d=d,
                     prereg_ok=(d == h_up - M),
                     band_proper_measured=[band_lo, band_hi],
                     landed=("band-proper" if band_lo <= d <= band_hi
                             else ("cascade tier" if d == h_up - 1
                                   else "outside")))
    ck("L3 [PREREG, MIS-SPECIFIED -- recorded as failed]: d = h-M with h "
       "the toy's MEASURED ceiling", l3_prereg["prereg_ok"], l3_prereg)
    ck("L3': d = M * d' exactly (the descent depth relation)",
       d == M * DQ, dict(d=d, M=M, dprime=DQ))
    ck("L3'': relative to the toy's own measured ceiling the lifted "
       "family sits at the CASCADE tier d = h-1", d == h_up - 1,
       dict(h_measured=h_up, d=d))
    ck("L3''': d is NOT a power of two is NOT required -- d = 4 IS a "
       "power of two here; what matters is M != 2^ceil(log2 d)",
       M != item10_M, dict(d=d, M=M, item10=item10_M))

    # ---- L4: P3 evasion
    per = {}
    for name, w in (("u", u), ("v", v)):
        cls = {p % M for p in range(k, n) if w[p]}
        per[name] = sorted(cls)
    ev = {}
    for z in [1, 2, 3, 5]:
        wz = [(u[i] + z * v[i]) % q for i in range(n)]
        cls = {p % M for p in range(k, n) if wz[p]}
        ev[z] = sorted(cls)
    ck("L4: u, v each 1-class; every member w_z meets 2 classes mod M",
       all(len(per[x]) == 1 for x in per)
       and all(len(c) == M for c in ev.values()),
       dict(classes_u=per["u"], classes_v=per["v"], classes_wz=ev))
    # and the family still lives on every member
    memb_ok = True
    for z in [1, 2, 3, 5]:
        wz = [(u[i] + z * v[i]) % q for i in range(n)]
        for T in up_joint:
            if not lemmaW(wz, [H[i] for i in T], n, k, d, q)[0]:
                memb_ok = False
    ck("L4b: every member w_z admits the WHOLE family", memb_ok)

    # ---- L5: KEY LEMMA
    key_ok = True
    for T in up_joint:
        Z = [i for i in range(n) if i not in T]
        for z in [0, 1, 2, 3, 5, 7]:
            wz = [(u[i] + z * v[i]) % q for i in range(n)]
            wv = [evalpoly(wz, x, q) for x in H]
            if not direct_core(wv, H, T, n, k, d, q)[0]:
                key_ok = False
    ck("L5: KEY LEMMA -- all members interpolate to codewords on Z",
       key_ok)

    bad = [c for c in checks if not c["ok"]]
    print(f"checks: {len(checks)}   failures: {len(bad)}")
    for b in bad:
        print("  FAIL", b)
    print()
    print(f"upstairs row: n={n} k={k} q={q}   scale M={M}   depth d={d}")
    print(f"quotient:     N={NQ} k'={KQ} d'={DQ} m={mq}  (MC scale M'="
          f"{MPRIME}) -> {len(qcores)} joint cores")
    print(f"upstairs:     {len(up_joint)} joint cores at depth {d}, "
          f"{len(up_coset)} of them mu_{M}-coset unions")
    print(f"single-word:  |cores(u)|={len(up_u)}  |cores(v)|={len(up_v)}")
    print(f"induced gate: A = {A_gate}, h = {h_up}, band proper = "
          f"[{band_lo},{band_hi}], d = {d} -> "
          f"{'BAND-PROPER' if band_lo <= d <= band_hi else 'outside'}")
    print(f"item-10 scale 2^ceil(log2 d) = {item10_M} != M = {M}: BP(1) "
          f"does not apply")
    print(f"P3: classes(u)={per['u']} classes(v)={per['v']} "
          f"classes(w_z)={ev}")

    with open(__file__.replace(".py", ".json"), "w") as fh:
        json.dump(dict(row=dict(n=n, k=k, q=q, M=M, d=d, h=h_up,
                                band_proper=[band_lo, band_hi],
                                A_gate=A_gate, item10_scale=item10_M),
                       quotient=dict(N=NQ, k=KQ, d=DQ, m=mq,
                                     Mprime=MPRIME, cores=len(qcores)),
                       upstairs=dict(joint=len(up_joint),
                                     coset=len(up_coset),
                                     u=len(up_u), v=len(up_v)),
                       classes=dict(u=per["u"], v=per["v"], wz=ev),
                       checks=checks, n_checks=len(checks),
                       n_fail=len(bad),
                       verdict="PASS" if not bad else "FAIL"), fh, indent=1)


if __name__ == "__main__":
    main()
