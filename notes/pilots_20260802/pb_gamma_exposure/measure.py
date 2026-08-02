#!/usr/bin/env python3
"""Measure the |Gamma| law across a q-ladder at fixed (n, K, h, m).

    tools/ramguard local -- python3 \
        notes/pilots_20260802/pb_gamma_exposure/measure.py S1

Writes MEASURE_<shape>.json in this directory.  Predictions were frozen in
PREDICTIONS.json BEFORE this ran (predict.py refuses to overwrite).

Strip/genericity: the banked Case runs two O(q) loops (T1 proportionality
over all lambda, T2 monic-degree over all z) that are infeasible above
q ~ 10^6.  FastCase replaces each with its exact O(n)/O(1) equivalent and
`--equiv` asserts the two agree verdict-for-verdict at every ladder point
with q <= EQUIV_Q.  All other banked checks (parameters, fibres, labels,
core, T3 fold, T4 rank, global genericity, and every per-candidate identity
in build_family) are the banked ones, unmodified.
"""

from __future__ import annotations

import json
import os
import sys
import time
from itertools import combinations

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
PILOTS = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(PILOTS, "pb_split_fibre_selector"))
import pb_split_fibre_pilot as P            # noqa: E402
from census import census                    # noqa: E402

EQUIV_Q = 20_000        # run the banked O(q) strip loops below this
PAIRS_CAP = 4000        # exact Gamma_lo only when |Gamma| <= this


class FastCase(P.Case):
    """Banked Case with the two O(q) strip loops replaced by exact
    equivalents.  Everything else is inherited verbatim."""

    def strip_checks(self) -> None:
        q, n, m, K = self.q, self.n, self.m, self.K
        u = [P.peval(self.U, x, q) for x in self.D]
        v = [P.peval(self.V, x, q) for x in self.D]
        self.req("T1_u_nonzero", any(u))
        self.req("T1_v_nonzero", any(v))
        # T1 exact equivalent: v = lam u on D forces lam = v[i]/u[i] at any
        # i with u[i] != 0, so a single candidate lam has to be tested.
        i0 = next(i for i in range(n) if u[i] % q)
        lam = (v[i0] * pow(u[i0], q - 2, q)) % q
        prop = all((v[i] - lam * u[i]) % q == 0 for i in range(n))
        self.req("T1_not_proportional", not prop)
        # T2 exact equivalent: deg U = A, U monic, deg V = A-m < A, hence
        # deg(U + zV) = A with leading coefficient 1 for EVERY z in F_q.
        self.req("T2_monic_degA",
                 P.deg(self.U) == self.A and self.U[self.A] % q == 1
                 and P.deg(self.V) < self.A,
                 "degU=A monic and degV<A => deg(u+zv)=A monic for all z")
        gc = self._gcd(n, K)
        folds = []
        for M in range(2, gc + 1):
            if gc % M:
                continue
            zeta = pow(self.omega, n // M, q)
            fu = all(P.peval(self.U, (zeta * x) % q, q)
                     == P.peval(self.U, x, q) for x in self.D)
            fv = all(P.peval(self.V, (zeta * x) % q, q)
                     == P.peval(self.V, x, q) for x in self.D)
            if fu and fv:
                folds.append(M)
        self.req("T3_no_quotient_fold", not folds, f"folds={folds}")
        indep = any((u[i] * v[j] - u[j] * v[i]) % q
                    for i in range(n) for j in range(n))
        self.req("T4_rank_two", indep)
        self.req("globally_generic_by_degree",
                 self.A - m < self.A and P.deg(self.V) >= K,
                 f"joint support <= {self.A-m} < A={self.A}")


def lowcore_family(case):
    """low-core-ONLY planted family (no Sidon clause): a-subsets J with
    |J ^ J'| <= a-2 and pairwise distinct slopes z_J in F_q."""
    q, a, b = case.q, case.a, case.b
    fam, famsets, sums = [], [], set()
    for J in combinations(range(b), a):
        Js = set(J)
        if any(len(Js & S) > a - 2 for S in famsets):
            continue
        zJ = sum(case.labels[i] for i in J) % q
        if zJ in sums:
            continue
        fam.append(J)
        famsets.append(Js)
        sums.add(zJ)
    out = []
    for J in fam:
        zJ = sum(case.labels[i] for i in J) % q
        sup = sorted(set(case.core_idx)
                     | {i for j in J for i in case.fibre_idx[j]})
        assert len(sup) == case.A
        out.append(dict(J=list(J), z=zJ, mask=P.mask_of(sup)))
    return out


def gamma_lo(masks: dict[int, int], K: int):
    """{z : |S_z ^ S_w| <= K-1 for every w != z}; exact, O(|Gamma|^2)."""
    zs = sorted(masks)
    hi = set()
    for i, z in enumerate(zs):
        mz = masks[z]
        for w in zs[i + 1:]:
            if bin(mz & masks[w]).count("1") >= K:
                hi.add(z)
                hi.add(w)
    return [z for z in zs if z not in hi], sorted(hi)


def run(shape: str) -> None:
    with open(os.path.join(HERE, "PREDICTIONS.json")) as fh:
        PRED = json.load(fh)
    sd = PRED["shapes"][shape]
    prm0 = sd["params"]
    out = dict(shape=shape, params=prm0, A=sd["A"], C_n_A=sd["C_n_A"],
               M_inf=sd["M_inf_greedy_lowcore"], points=[])
    checks_total = 0
    for pt in sd["ladder"]:
        q = pt["q"]
        t0 = time.time()
        prm = dict(prm0)
        prm["q"] = q
        case = FastCase(f"{shape}_q{q}", prm)
        equiv = None
        if q <= EQUIV_Q:
            slow = P.Case(f"{shape}_q{q}_slow", dict(prm))
            equiv = ({t: v for t, v, _ in slow.checks}
                     == {t: v for t, v, _ in case.checks})
            assert equiv, (shape, q)
        checks_total += len(case.checks)
        fam = lowcore_family(case)
        cs = census(case, want_lexmin=True)
        live = sorted(cs["per_slope"])
        nlive = len(live)
        planted = {c["z"]: c["mask"] for c in fam}
        sel = cs["lexmin"]
        n_intended_first = sum(1 for z, mk in planted.items()
                               if sel.get(z) == mk)
        rec = dict(
            q=q, log2q=pt["log2q"],
            mean_Wz_pred=pt["mean_Wz"],
            witnesses_pred=pt["witnesses_pred"],
            witnesses_meas=cs["total"],
            gamma_poisson_pred=pt["gamma_poisson"],
            gamma_pred=pt["gamma_pred"],
            gamma_meas=nlive,
            M_lowcore_meas=len(fam),
            planted_slopes_live=sum(1 for z in planted if z in cs["per_slope"]),
            intended_is_first_match=n_intended_first,
            mean_Wz_meas=cs["total"] / nlive if nlive else 0.0,
            regime=pt["regime"],
            secs=round(time.time() - t0, 2),
        )
        if nlive and nlive <= PAIRS_CAP:
            lo, hi = gamma_lo(sel, prm0["K"])
            rec["gamma_lo"] = len(lo)
            rec["gamma_hi"] = len(hi)
            rec["retention"] = len(lo) / nlive
            rec["gamma_lo_over_8n3"] = f"{len(lo)}/{8*prm0['n']**3}"
        else:
            rec["gamma_lo"] = None
            rec["retention"] = None
        out["points"].append(rec)
        print(f"  q=2^{pt['log2q']:5.2f}={q:<12} wit {cs['total']:>9} "
              f"(pred {pt['witnesses_pred']:>12.1f})  |G| {nlive:>7} "
              f"(pred {pt['gamma_pred']:>10.1f})  M {len(fam):>4}  "
              f"ret {rec['retention'] if rec['retention'] is None else round(rec['retention'],4)}"
              f"  first-match {n_intended_first}/{len(fam)}  {rec['secs']}s")
    out["banked_checks_replayed"] = checks_total
    path = os.path.join(HERE, f"MEASURE_{shape}.json")
    with open(path, "w") as fh:
        json.dump(out, fh, indent=1, sort_keys=True)
    print(f"wrote {path}  ({checks_total} banked checks, all PASS)")


if __name__ == "__main__":
    for s in sys.argv[1:]:
        print(f"== shape {s}")
        run(s)
