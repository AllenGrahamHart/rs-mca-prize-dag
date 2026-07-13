#!/usr/bin/env python3
"""M4 — the dli amber's ASSEMBLY VERIFIER (2026-07-13, fresh-context builder).

Node: dli_prime_weighted_large_block_support (CONJECTURE B-WEAK, the corridor
floor).  M-ledger source: notes/C2PP_POSED_20260710.md 'Path to predicate
status' — M4 = "the assembly verifier (exact-rational: pinned K-prime,
w_max(L), W_cl inputs per zone, R_joint = 21 => q^{-t+H} W_cen <= 2^121),
with the f2b + calibration replays as gates".

WHAT THIS SCRIPT PROVES (and what it does not):
  It machine-verifies, in exact rational arithmetic, the IMPLICATION

    [C1' per-level excess]  AND  [per-row W_cl zone inputs certified by
    ENDPOINT-EXC certificates]  AND  [C2'' 21-bit joint reserve]
        ==>  Sigma_{L=1}^{34} log2 E_L <= 100
        ==>  q^{-t+H} W_cen <= 2^{21+100} = 2^121,

  every step an exact inequality on DECLARED inputs.  The three inputs are
  consumed as NAMED CONDITIONAL PREDICATES with their 1-survived-round
  provenance pinned (F-round state 1/1/1).  NOTHING here proves C1', C2'',
  or ENDPOINT-EXC-COVERAGE; the verdict is therefore
      ASSEMBLY-VERIFIED-CONDITIONAL (on C2'', C1', ENDPOINT-EXC as named
      predicates)
  and can NEVER be an unconditional PASS while any predicate is unproved
  (catch #163: the C2''-instance is an explicit input alongside coverage —
  item-5's soundness display is otherwise secretly conditional).

FAIL-CLOSED: any missing/malformed input -> exit 2 (M4-INPUT-REJECT); any
gate / pin / assembly-step failure -> exit 1 (M4-FAIL); mutation-control
failure (a built-in tamper that does NOT trip) -> exit 1.

Exact arithmetic: every decision-path comparison is on int/Fraction.  Floats
appear only (a) to replay banked binary64 artifacts bit-exactly, and (b) in
display strings.

Repo is READ-ONLY for this script.  Catch ledger: #162 (torn duplicate —
detected and spec'd, deletion owed to the maintainer), #163 (implemented
here), #164 (found by this builder: the 2^(21/33) allowance display "1.555"
in two banked texts is a last-digit slip — true value 1.5544 -> "1.554";
display-only, nothing gates on it; documented in m4_findings.md).

Run:  tools/ramguard tiny -- python3 <scratchpad>/m4_assembly_verifier.py
"""

from __future__ import annotations

import copy
import hashlib
import json
import math
import sys
from fractions import Fraction
from itertools import product
from pathlib import Path

REPO = Path("/home/u2470931/smooth-read-solomin/prize")
NODE_DIR = REPO / "critical/nodes/dli_prime_weighted_large_block_support"
NOTES = NODE_DIR / "notes"

# ---------------------------------------------------------------- constants
LEVELS = 34                # official schedule: 34 levels, Sigma L_j = t
JUNCTIONS = 33             # catch #108: the POSED /33 junction convention
R_JOINT_BITS = 21          # C2'' clause (ii); catch #40 re-pin (22 -> 21)
AGG_BUDGET_BITS = 100      # DLI-AGG: Sigma_L log2 E_L <= 100
ENDPOINT_BITS = 121        # q^{-t+H} W_cen <= 2^121 (catch #40 / #30)
K_PRIME = 4                # C1' pinned constant (exact K' <= 4)
TAU = Fraction(1, 32)      # per-level W_cl zone input: tau_L = 2^-5 (the
                           # A1-PROD threshold trade-off row, adopted as the
                           # per-row bound every pi_R must certify per level)
Q_BOUND_BITS = 256         # admissible q < 2^256, N_L = 256 L (balanced)

CONDITIONAL_VERDICT = (
    "ASSEMBLY-VERIFIED-CONDITIONAL (on C2'', C1', ENDPOINT-EXC as named "
    "predicates)"
)

_failures: list[str] = []


class M4InputReject(Exception):
    """Fail-closed rejection of a missing/malformed input."""


class M4Reject(Exception):
    """Fail-closed rejection inside a gate / pin / assembly step."""


def check(name: str, ok: bool, detail: str = "") -> bool:
    tag = "PASS" if ok else "FAIL"
    print(f"[{tag}] {name}" + (f"  ({detail})" if detail else ""))
    if not ok:
        _failures.append(name)
    return ok


def info(msg: str) -> None:
    print(f"[info] {msg}")


# =========================================================================
# 1. THE INPUT MANIFEST — every input explicit, statuses honest
# =========================================================================

def build_inputs() -> dict:
    """The declared inputs of the assembly.  Statuses are the HONEST current
    statuses; the verdict logic downgrades on any unproved predicate."""
    return {
        # -- (a) the C2''-instance (catch #163: an EXPLICIT named input) --
        "C2PP_INSTANCE": {
            "id": "C2PP-INSTANCE-20260710",
            "name": "C2''",
            "clause": "E_U[prod_j rho_j]_reduced <= 2^R_joint * prod_j "
                      "E_U[rho_j] at every official prize row "
                      "(coset-routed, accident-decomposed; clauses i+iii "
                      "exact accounting)",
            "R_joint_bits": R_JOINT_BITS,
            "junctions": JUNCTIONS,
            "convention": "/33 posed form (catch #108)",
            "theta": 2.0,
            "status": "CONDITIONAL",       # posed + 1 F-round survived
            "rounds_survived": 1,
            "maintainer_token": None,       # no proof exists
            "provenance": [
                "notes/C2PP_POSED_20260710.md",
                "notes/m1_dli_m1_results.json",
                "notes/m1_run_record_20260713.log",
                "notes/M1_RESULT_AUDIT.md",
                "notes/verify_m1_result.py",
            ],
        },
        # -- (b) the C1' ledger (level-scaled) ----------------------------
        "C1P_LEDGER": {
            "id": "C1P-LEVEL-SCALED-20260713",
            "name": "C1'",
            "clause": "E - 1 <= K' * r * (1 + W_cl) with K' <= 4, "
                      "W_cl over primitive orbits of weight in "
                      "[L+1, w_max(L)], w_max(L) = L+5",
            "K_prime_cap": K_PRIME,
            "w_max_rule": "L+5",
            "status": "CONDITIONAL",       # posed + 1 F-round survived (M2)
            "rounds_survived": 1,
            "maintainer_token": None,
            "provenance": [
                "notes/C1PRIME_LEVEL_SCALED_POSE.md",
                "notes/m2_c1prime_level_scaled_results.json",
                "notes/M2_C1PRIME_RESULT_AUDIT.md",
                "notes/verify_m2_c1prime_result.py",
            ],
        },
        # -- (c) ENDPOINT-EXC: certificate rule + COVERAGE ----------------
        "ENDPOINT_EXC": {
            "id": "ENDPOINT-EXC-COVERAGE-20260713",
            "name": "ENDPOINT-EXC",
            "clause": "for every official row R there exists pi_R with "
                      "VERIFY_ENDPOINT_EXC(R, pi_R) = ACCEPT "
                      "(6-item certificate, fail-closed)",
            "items": 6,
            "coverage": "OPEN",            # the pose's own explicit status
            "status": "CONDITIONAL",       # posed + 1 F-round survived
            "rounds_survived": 1,
            "maintainer_token": None,
            "provenance": [
                "notes/M3_ENDPOINT_EXCEPTION_COVERAGE.md",
                "notes/eex_report.md",
                "notes/eex_findings.md",
                "notes/eex_verify.py",
            ],
        },
        # -- (d) the A1-PROD W_cl zone inputs -----------------------------
        # zone tags MUST match the banked a1_prod_norm_sieve_table.json;
        # tau_L is the per-row W_cl bound that every pi_R must certify
        # (items 2-4).  A1-PROD itself is density-only (M3 audit): it never
        # discharges a row, so the per-row bound is ENDPOINT-EXC content.
        "ZONES": {
            "table": "notes/a1_prod_norm_sieve_table.json",
            "levels": {
                L: {
                    "N": 256 * L,
                    "zone": ("covered-full" if L == 1 else
                             "covered-partial" if 2 <= L <= 19 else
                             "uncovered"),
                    "tau_num": TAU.numerator,
                    "tau_den": TAU.denominator,
                    "certified_by": "pi_R items 2-4 (ENDPOINT-EXC)",
                }
                for L in range(1, LEVELS + 1)
            },
        },
        # -- (e) the proved skeleton (green inputs, provenance-pinned) ----
        "SKELETON": {
            "lemma1": "rho_j = q^{L_j} |Z_j| / U (exact reduction; PROVED)",
            "d2": "E_U[rho_j] = (q^L/2^N)(1 + W_j) (exact identity)",
            "d3_floor": "E_U[rho_j] >= 1 (lambda = 0 term of D3)",
            "consumer_face": "q^{-t+H} W_cen = E_U[prod_j rho_j] "
                             "(x4 packet face; half-band count <= 2^121)",
            "status": "PROVED-PINNED",
        },
    }


REQUIRED_SHAPE = {
    "C2PP_INSTANCE": ["id", "R_joint_bits", "junctions", "convention",
                      "status", "rounds_survived", "maintainer_token",
                      "provenance"],
    "C1P_LEDGER": ["id", "K_prime_cap", "w_max_rule", "status",
                   "rounds_survived", "maintainer_token", "provenance"],
    "ENDPOINT_EXC": ["id", "items", "coverage", "status", "rounds_survived",
                     "maintainer_token", "provenance"],
    "ZONES": ["table", "levels"],
    "SKELETON": ["lemma1", "d2", "d3_floor", "consumer_face", "status"],
}


def validate_inputs(inputs: dict) -> None:
    """Fail-closed: every input present with every required field."""
    for top, fields in REQUIRED_SHAPE.items():
        if top not in inputs or not isinstance(inputs[top], dict):
            raise M4InputReject(f"input block missing/malformed: {top}")
        for f in fields:
            if f not in inputs[top]:
                raise M4InputReject(f"input field missing: {top}.{f}")
    zl = inputs["ZONES"]["levels"]
    if sorted(zl) != list(range(1, LEVELS + 1)):
        raise M4InputReject("ZONES.levels must cover exactly L = 1..34")
    for L, z in zl.items():
        for f in ("N", "zone", "tau_num", "tau_den", "certified_by"):
            if f not in z:
                raise M4InputReject(f"zone field missing: L={L}.{f}")
        if z["tau_den"] <= 0 or z["tau_num"] < 0:
            raise M4InputReject(f"zone tau malformed at L={L}")
    for key in ("C2PP_INSTANCE", "C1P_LEDGER", "ENDPOINT_EXC"):
        st = inputs[key]["status"]
        if st not in ("PROVED", "CONDITIONAL", "OPEN"):
            raise M4InputReject(f"{key}.status not in enum: {st}")
        for rel in inputs[key]["provenance"]:
            if not (NODE_DIR / rel).exists():
                raise M4InputReject(f"{key} provenance file missing: {rel}")


# =========================================================================
# 2. PROVENANCE PINS — exact strings/values in the banked record
# =========================================================================

def read(rel: str, base: Path = NODE_DIR) -> str:
    return (base / rel).read_text()


def provenance_pins(inputs: dict) -> None:
    dag = json.loads((REPO / "dag.json").read_text())
    node = next(n for n in dag["nodes"]
                if n["id"] == "dli_prime_weighted_large_block_support")
    stmt = node["statement"]

    check("pin: node statement endpoint 2^121",
          "q^{-t+H} * W_cen <= 2^121" in stmt)
    check("pin: node statement F-round state 1/1/1",
          "C2'' 1 / C1' 1 / ENDPOINT-EXC 1" in stmt)
    check("pin: node statement names catch #163 (C2''-instance input)",
          "#163" in stmt and "C2''-instance" in stmt)

    c2 = read("notes/C2PP_POSED_20260710.md")
    check("pin: C2'' pose R_joint = 21 bits", "R_joint = 21 bits" in c2)
    check("pin: C2'' pose /33 junction display present (catch #108)",
          "2^(21/33)" in c2)
    check("pin: C2'' pose aggregate form primary",
          "the aggregate form is\nprimary" in c2
          or "aggregate form is primary" in c2.replace("\n", " "))
    c2i = inputs["C2PP_INSTANCE"]
    check("pin: manifest R_joint == posed 21",
          c2i["R_joint_bits"] == 21)
    check("pin: manifest junction convention /33 (catch #108)",
          c2i["junctions"] == 33 and "/33" in c2i["convention"])
    # #164 (display-only, non-fatal): the banked "= 1.555" display is a
    # last-digit slip; true 2^(21/33) = 1.5544... -> "1.554".
    disp = round(2 ** (21 / 33), 3)
    if "2^(21/33) = 1.555" in c2:
        info(f"catch #164: banked allowance display '1.555' is a last-digit "
             f"slip; true 2^(21/33) rounds to {disp} (display-only)")
    check("pin: allowance display recomputed (three decimals)",
          disp == 1.554, f"2^(21/33) = {2 ** (21 / 33):.6f}")

    c1 = read("notes/C1PRIME_LEVEL_SCALED_POSE.md")
    check("pin: C1' pose w_max(L) = L+5", "w_max(L) = L+5" in c1)
    check("pin: C1' pose kill line E-1 > 4r(1+W_cl)",
          "E-1 > 4r(1+W_cl)" in c1)
    check("pin: manifest K' cap == 4 and w_max rule == L+5",
          inputs["C1P_LEDGER"]["K_prime_cap"] == 4
          and inputs["C1P_LEDGER"]["w_max_rule"] == "L+5")

    m3 = read("notes/M3_ENDPOINT_EXCEPTION_COVERAGE.md")
    check("pin: M3 soundness display",
          "VERIFY_ENDPOINT_EXC(R,pi_R)=ACCEPT  ==>  q^{-t+H} W_cen(R) "
          "<= 2^121" in m3)
    check("pin: M3 six certificate items", all(
        s in m3 for s in ("primality/order certificates",
                          "complete low-weight orbit ledger",
                          "multiplier-shadow", "residual near-peak",
                          "ownership ledger", "exact rational final check")))
    check("pin: M3 exposes coverage as an input (fail-closed clause)",
          "expose coverage as an input" in m3)

    eexr = read("notes/eex_report.md")
    check("pin: ENDPOINT-EXC round-1 SURVIVED banked",
          "SURVIVED" in eexr and "F-round state becomes 1/1/1" in eexr)
    check("pin: eex report pins catch #163 (C2''-instance input for M4)",
          "#163" in eexr)

    repose = read("REPOSE_B_WEAK.md")
    check("pin: REPOSE catch-#40 addendum 2^121", "2^121" in repose)

    x4 = read("critical/nodes/x4_exactlist_staircase_split/"
              "REDUCTION_PACKET.md", REPO)
    check("pin: consumer face half-band count <= 2^121",
          "equivalently half-band count <= 2^121" in x4)

    check("pin: reserve + aggregate budget == endpoint (21 + 100 = 121)",
          R_JOINT_BITS + AGG_BUDGET_BITS == ENDPOINT_BITS)

    # zone table agreement (banked A1-PROD table vs manifest zone tags)
    tab = json.loads(read(inputs["ZONES"]["table"]))["production_table"]
    trow = {r["L"]: r for r in tab}
    ok = True
    for L in range(1, LEVELS + 1):
        z = inputs["ZONES"]["levels"][L]
        t = trow[L]
        covered = t["w_1"] is not None
        want = ("covered-full" if covered and t["w_1"] == t["w_star"] else
                "covered-partial" if covered else "uncovered")
        if z["zone"] != want or z["N"] != t["N"]:
            ok = False
            info(f"zone mismatch at L={L}: manifest={z['zone']} "
                 f"banked-implies={want}")
    check("pin: manifest zones == banked A1-PROD table "
          "(L=1 full, 2-19 partial, 20-34 uncovered)", ok)
    check("pin: A1-PROD table 34 levels, w*(1) = 55, w_1(1) = 55",
          len(tab) == LEVELS and trow[1]["w_star"] == 55
          and trow[1]["w_1"] == 55)


# =========================================================================
# 3. GATE G1 — the banked f2b 8-row record replays exactly
# =========================================================================

F2B_ROWS = [(2, 97), (2, 193), (2, 8353), (2, 32801),
            (3, 97), (3, 193), (4, 97), (4, 193)]


def gate_f2b() -> None:
    nested = json.loads(read("notes/f2b_nested_correlation.json"))
    perclass = json.loads(read("notes/f2b_replay_perclass_20260710.json"))
    nk = {(r["t"], r["q"]): r for r in nested}
    pk = {(r["t"], r["q"]): r for r in perclass}
    check("G1: f2b row set == the banked 8 rows",
          set(nk) == set(F2B_ROWS) == set(pk))
    ok_ratio = ok_cross = True
    for key in F2B_ROWS:
        r = nk[key]
        # binary64 replay: ratio must equal E_cond/E_uncond bit-exactly
        if r["E_cond"] / r["E_uncond"] != r["ratio"]:
            ok_ratio = False
        # cross-file bit-identity (independent audit run replay_ok'd it)
        if pk[key]["ratio"] != r["ratio"] or not pk[key]["replay_ok"]:
            ok_cross = False
    check("G1: ratio == E_cond/E_uncond bit-exact at all 8 rows", ok_ratio)
    check("G1: perclass replay file bit-identical + replay_ok all rows",
          ok_cross)
    gm = math.exp(sum(math.log(nk[k]["ratio"]) for k in F2B_ROWS) / 8)
    check("G1: raw geometric mean reproduces banked 2.139",
          round(gm, 3) == 2.139, f"gm = {gm:.12f}")
    check("G1: sparse rows stripped mass identically zero "
          "((2,32801), (4,193))",
          pk[(2, 32801)]["stripped_mean_ratio"] == 0.0
          and pk[(4, 193)]["stripped_mean_ratio"] == 0.0)


# =========================================================================
# 4. GATE G2 — the pose-time calibration replays exactly
# =========================================================================

# the 8 bulk ratios cited verbatim in C2PP_POSED (clause-(ii) calibration)
POSE_BULK = [Fraction(998, 1000), Fraction(1010, 1000), Fraction(0),
             Fraction(0), Fraction(1033, 1000), Fraction(1066, 1000),
             Fraction(760, 1000), Fraction(0)]
# the four accident-class masses cited in the pose (orbit-quantized)
POSE_ACCIDENT_MASSES = [128, 128, 64, 128]
ORBIT_QUANTUM_N32 = 32  # 2h at n = 32


def gate_calibration() -> None:
    pose = read("notes/C2PP_POSED_20260710.md")
    check("G2: pose cites the 8 bulk values",
          "0.998 / 1.010 / 0 / 0 / 1.033 /\n  1.066 / 0.760 / 0"
          in pose or "0.998 / 1.010 / 0 / 0 / 1.033" in pose)
    pos = [x for x in POSE_BULK if x > 0]
    gm = math.exp(sum(math.log(float(x)) for x in pos) / len(pos))
    check("G2: bulk GM over positive rows reproduces banked 0.967",
          round(gm, 3) == 0.967, f"gm = {gm:.12f}")
    check("G2: accident masses orbit-quantized (multiples of 32, "
          "128/128/64/128)",
          all(m % ORBIT_QUANTUM_N32 == 0 for m in POSE_ACCIDENT_MASSES)
          and "128/128/64/128" in pose)
    # the naive UNIFORM coset-stripped constant is refuted by the banked
    # record: stripped ratios exceed the /33 allowance.  Exact comparison:
    # x > 2^(21/33)  <=>  x^33 > 2^21 (x > 0), on Fraction(float) exactly.
    perclass = json.loads(read("notes/f2b_replay_perclass_20260710.json"))
    pk = {(r["t"], r["q"]): r for r in perclass}
    refuters = {(2, 8353): 2.752, (4, 97): 2.874}
    ok_disp = ok_exceed = True
    for key, disp in refuters.items():
        x = pk[key]["stripped_mean_ratio"]
        if round(x, 3) != disp:
            ok_disp = False
        if Fraction(x) ** 33 <= Fraction(2) ** 21:
            ok_exceed = False
    check("G2: stripped refuter displays 2.752 / 2.874 reproduce", ok_disp)
    check("G2: refuters exceed the /33 allowance exactly "
          "(x^33 > 2^21) — three-part C2'' shape is forced", ok_exceed)
    check("G2: pose survival text carries both refuter values",
          "2.752" in pose and "2.874" in pose)


# =========================================================================
# 5. GATE G3 — C1' M2 record: full exact-rational replay (12 rows)
# =========================================================================

M2_EXPECTED = {1: {193, 449, 769, 1409, 3137, 5569, 7937, 12289},
               2: {193, 257, 449, 577}}


def gate_m2_replay(inputs: dict) -> None:
    m1 = json.loads(read("notes/m1_dli_m1_results.json"))
    m2 = json.loads(read("notes/m2_c1prime_level_scaled_results.json"))
    check("G3: m2 schema/pose/verdict banked",
          m2["schema"] == "dli-c1prime-m2-v1"
          and m2["pose"] == "w_max(L)=L+5, exact K_prime<=4"
          and m2["killed"] is False
          and m2["verdict"] == "C1_prime_SURVIVES_M2"
          and len(m2["rows"]) == 12)
    source = {((r["t"] + 1) // 2, r["q"]): r for r in m1["rows"]}
    N = 32
    kcap = inputs["C1P_LEDGER"]["K_prime_cap"]
    seen = {1: set(), 2: set()}
    max_k: tuple[Fraction, int, int] | None = None
    positive_control = False
    ok_rows = True
    for row in m2["rows"]:
        L, q = row["level"], row["q"]
        seen[L].add(q)
        if row["weights"] != list(range(L + 1, L + 6)):
            ok_rows = False       # w_max(L) = L+5 window
            continue
        src = source[(L, q)]
        orbs = {int(w): c for w, c in src["V_orbits"].items()}
        prim = {int(w): c for w, c in row["primitive_orbits"].items()}
        if any(not (0 <= prim[w] <= orbs.get(w, 0)) for w in row["weights"]):
            ok_rows = False
        all_weighted = 1 + sum(Fraction(c * 2 * N, 2 ** w)
                               for w, c in orbs.items())
        r_val = Fraction(q ** L, 2 ** N)
        excess = r_val * all_weighted - 1
        ledger = sum(Fraction(prim[w] * 2 * N, 2 ** w)
                     for w in row["weights"])
        if (Fraction(*row["E_minus_1"]) != excess
                or Fraction(*row["r"]) != r_val
                or Fraction(*row["W_cl"]) != ledger
                or row["killed"] is not False):
            ok_rows = False
        if excess > kcap * r_val * (1 + ledger):
            ok_rows = False       # the C1' inequality itself
        k_exact = excess / (r_val * (1 + ledger))
        if max_k is None or k_exact > max_k[0]:
            max_k = (k_exact, L, q)
        if L == 1 and q == 7937 and excess > kcap * r_val:
            positive_control = True   # no-ledger form fails here
    check("G3: all 12 frozen rows replay exactly (E-1, r, W_cl, "
          "C1' inequality)", ok_rows and seen == M2_EXPECTED)
    check("G3: positive control — no-ledger form fails at (L=1, q=7937)",
          positive_control)
    assert max_k is not None
    check("G3: max K' at the preselected accident row, < 1/4, "
          "float pin 0.246909432",
          max_k[1:] == (1, 7937) and max_k[0] < Fraction(1, 4)
          and abs(float(max_k[0]) - 0.246909432) < 1e-9,
          f"max K' = {float(max_k[0]):.9f}")


# =========================================================================
# 6. GATE G4 — C2'' M1 round record pins
# =========================================================================

def gate_m1_record() -> None:
    m1 = json.loads(read("notes/m1_dli_m1_results.json"))
    rows = m1["rows"]
    check("G4: M1 grid — 45 rows, all n = 64, depths t in {2, 3}",
          len(rows) == 45 and all(r["n"] == 64 for r in rows)
          and {r["t"] for r in rows} == {2, 3})
    check("G4: M1 theta == 2.0 (pose convention)", m1["theta"] == 2.0)
    check("G4: F-a NOT fired, F-c NOT fired (banked flags)",
          m1["Fa_fired"] is False and m1["Fc_fired"] is False)
    check("G4: M1 verdict — C2'' survives round 1",
          m1["verdict"].startswith("C2'' SURVIVES"))
    check("G4: no sub-orbit anomaly flags anywhere",
          all(not r["suborbit_flags"] for r in rows))
    log = read("notes/m1_run_record_20260713.log")
    check("G4: full M1 log banked with the survival verdict",
          "M1 VERDICT: C2'' SURVIVES" in log)
    check("G4: M1 log allowance display uses /33 (catch #108)",
          "21/33" in log)


# =========================================================================
# 7. GATE G5 — ENDPOINT-EXC demo: the 6-item certificate, fail-closed,
#    with the C2''-instance linked per catch #163 (toy row, exact)
# =========================================================================

DEMO_Q, DEMO_NPRIME, DEMO_SCHEDULE = 97, 16, (1, 2, 3)
DEMO_W_LED, DEMO_W_COV = 5, 8
DEMO_TRUTH = Fraction(15, 8)   # eex round battery truth, banked


def _is_prime(n: int) -> bool:
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


def _pinned_omega(q: int, nprime: int) -> int:
    fac, m, p = [], q - 1, 2
    while p * p <= m:
        if m % p == 0:
            fac.append(p)
            while m % p == 0:
                m //= p
        p += 1
    if m > 1:
        fac.append(m)
    g = 2
    while any(pow(g, (q - 1) // f, q) == 1 for f in fac):
        g += 1
    return pow(g, (q - 1) // nprime, q)


def _mult_order(x: int, q: int, bound: int) -> int:
    v, k = x % q, 1
    while v != 1 and k <= bound:
        v = v * x % q
        k += 1
    return k if v == 1 else -1


def _enum_kernel(N: int, L: int, q: int, omega: int):
    """Exhaustive ternary kernel enumeration (pass 1: itertools product)."""
    roots = [pow(omega, 2 * l - 1, q) for l in range(1, L + 1)]
    pows = [[pow(r, y, q) for y in range(N)] for r in roots]
    out = []
    for d in product((-1, 0, 1), repeat=N):
        w = sum(1 for x in d if x)
        if w == 0:
            continue
        if all(sum(d[y] * pw[y] for y in range(N)) % q == 0 for pw in pows):
            out.append((d, w))
    return out


def _enum_kernel_pass2(N: int, L: int, q: int, omega: int):
    """Independent second pass: supports x sign patterns (combinations)."""
    from itertools import combinations
    roots = [pow(omega, 2 * l - 1, q) for l in range(1, L + 1)]
    pows = [[pow(r, y, q) for y in range(N)] for r in roots]
    out = []
    for w in range(1, N + 1):
        for sup in combinations(range(N), w):
            for sgn in product((-1, 1), repeat=w):
                d = [0] * N
                for i, y in enumerate(sup):
                    d[y] = sgn[i]
                if all(sum(d[y] * pw[y] for y in sup) % q == 0
                       for pw in pows):
                    out.append((tuple(d), w))
    return out


def _shift1(v: tuple, N: int) -> tuple:
    return (-v[N - 1],) + v[:N - 1]        # negacyclic: x^N = -1


def _orbit(v: tuple, N: int) -> set:
    out, cur = set(), v
    for _ in range(2 * N):
        out.add(cur)
        cur = _shift1(cur, N)
    return out


def _orbit_key(v: tuple, N: int) -> tuple:
    return min(_orbit(v, N))


def build_demo_certificate(inputs: dict) -> tuple[dict, dict]:
    """Honest pi_R at the toy row + the exact per-level truth."""
    q, nprime = DEMO_Q, DEMO_NPRIME
    N = nprime // 2
    omega = _pinned_omega(q, nprime)
    truth, hists, orbits = {}, {}, {}
    for L in DEMO_SCHEDULE:
        vecs = _enum_kernel(N, L, q, omega)
        hist = {}
        for _, w in vecs:
            hist[w] = hist.get(w, 0) + 1
        hists[L] = hist
        truth[L] = sum(Fraction(c, 2 ** w) for w, c in hist.items()
                       if L + 1 <= w <= DEMO_W_COV)
        orbs = {}
        for d, w in vecs:
            if L + 1 <= w <= DEMO_W_LED:
                k = _orbit_key(d, N)
                if k not in orbs:
                    orbs[k] = (w, len(_orbit(k, N)))
        orbits[L] = orbs
    cert = {
        "item1": {"nprime": nprime, "q": q, "omega": omega,
                  "field": "F_q", "generated_field": "F_q",
                  "primality": "trial_division", "order_claim": nprime},
        "item2": {L: {"orbits": sorted(
                          [list(k), w, s] for k, (w, s) in orbits[L].items()),
                      "completeness": "exhaustive_enumeration_toy"}
                  for L in DEMO_SCHEDULE},
        "item3": {L: {"dedup": "orbit_keys_distinct_sizes_exact",
                      "quantum": 2 * N} for L in DEMO_SCHEDULE},
        "item4": {L: {w: {"U_num": hists[L].get(w, 0), "U_den": 2 ** w,
                          "proof_type": "exhaustive_recount_toy"}
                      for w in range(DEMO_W_LED + 1, DEMO_W_COV + 1)}
                  for L in DEMO_SCHEDULE},
        "item5": {"owners": {f"L{L}w{w}": "bulk"
                             for L in DEMO_SCHEDULE
                             for w in range(L + 1, DEMO_W_COV + 1)},
                  "reserve_bits": R_JOINT_BITS, "reserve_credits": [],
                  # catch #163: the joint bridge is the named C2'' input
                  "c2pp_instance": inputs["C2PP_INSTANCE"]["id"]},
        "item6": {"method": "exact_rational", "T": [4, 1]},
        "levels": list(DEMO_SCHEDULE),
        "w_led": DEMO_W_LED, "w_cov": DEMO_W_COV,
    }
    return cert, truth


def verify_certificate(cert: dict, inputs: dict,
                       T_check: Fraction | None = None):
    """Fail-closed toy VERIFY_ENDPOINT_EXC (eex-round semantics) with the
    catch-#163 item-5 pin: the ownership ledger's joint bridge must resolve
    to the manifest's named C2''-instance, else REJECT.  Returns
    (verdict, fired, total)."""
    fired: list[str] = []
    for item in ("item1", "item2", "item3", "item4", "item5", "item6"):
        if item not in cert:
            fired.append(f"{item}:MISSING (fail-closed)")
    if fired:
        return "REJECT", fired, Fraction(0)
    nprime, q = cert["item1"]["nprime"], cert["item1"]["q"]
    N = nprime // 2
    if not _is_prime(q):
        fired.append("item1:primality")
    if q % nprime != 1:
        fired.append("item1:splitting")
    if cert["item1"]["omega"] != _pinned_omega(q, nprime):
        fired.append("item1:omega_pin")
    if _mult_order(cert["item1"]["omega"], q, nprime) != nprime:
        fired.append("item1:omega_order")
    if cert["item1"]["generated_field"] != "F_q":
        fired.append("item1:generated_field_normalization")
    omega = _pinned_omega(q, nprime)
    total = Fraction(0)
    for L in cert["levels"]:
        vecs = _enum_kernel_pass2(N, L, q, omega)   # independent re-count
        if any(w <= L for _, w in vecs):
            fired.append(f"item2:L{L}:FLOOR_BREAK")  # Vandermonde floor
        true_orbs = {}
        for d, w in vecs:
            if L + 1 <= w <= cert["w_led"]:
                k = _orbit_key(d, N)
                true_orbs.setdefault(k, (w, len(_orbit(k, N))))
        led = {tuple(k): (w, s) for k, w, s in cert["item2"][L]["orbits"]}
        if set(led) != set(true_orbs):
            fired.append(f"item2:L{L}:ledger_incomplete_or_spurious")
        for k, (w, s) in led.items():
            if k in true_orbs and true_orbs[k] != (w, s):
                fired.append(f"item3:L{L}:orbit_size_not_exact")
            if len(_orbit(k, N)) != cert["item3"][L]["quantum"]:
                fired.append(f"item3:L{L}:quantum!=2N")
        listed = sum(Fraction(s, 2 ** w) for (w, s) in led.values())
        resid = cert["item4"][L]
        want = set(range(cert["w_led"] + 1, cert["w_cov"] + 1))
        if {int(w) for w in resid} != want:
            fired.append(f"item4:L{L}:unlisted_class_missing")
        rmass = Fraction(0)
        hist2 = {}
        for _, w in vecs:
            hist2[w] = hist2.get(w, 0) + 1
        for w in sorted(want & {int(x) for x in resid}):
            rec = resid[w] if w in resid else resid[str(w)]
            if rec["proof_type"] in ("no_explicit_construction_known",
                                     "likely_nonexceptional",
                                     "ppt_hardness"):
                fired.append(f"item4:L{L}:rejected_certificate_type")
            U = Fraction(rec["U_num"], rec["U_den"])
            if U < Fraction(hist2.get(w, 0), 2 ** w):
                fired.append(f"item4:L{L}w{w}:residual_bound_false")
            rmass += U
        total += listed + rmass
    it5 = cert["item5"]
    for L in cert["levels"]:
        for w in range(L + 1, cert["w_cov"] + 1):
            tag = f"L{L}w{w}"
            if tag not in it5["owners"]:
                fired.append(f"item5:bucket_{tag}_unowned")
            elif it5["owners"][tag] not in ("coset", "bulk", "accident"):
                fired.append(f"item5:bad_owner_{tag}")
    if it5["reserve_bits"] != inputs["C2PP_INSTANCE"]["R_joint_bits"]:
        fired.append("item5:reserve_bits != named C2'' instance")
    if len(it5["reserve_credits"]) > 1:
        fired.append("item5:reserve_charged_more_than_once")
    # ---- catch #163: the joint bridge is NOT consistency-only ----------
    if it5.get("c2pp_instance") != inputs["C2PP_INSTANCE"]["id"]:
        fired.append("item5:c2pp_instance_unresolved (catch #163)")
    for c in it5["reserve_credits"]:
        total -= Fraction(c[0], c[1])
    if cert["item6"]["method"] != "exact_rational":
        fired.append("item6:not_exact_rational")
    T = Fraction(cert["item6"]["T"][0], cert["item6"]["T"][1])
    if T_check is not None and T != T_check:
        fired.append("item6:threshold_mismatch")
    if total > T:
        fired.append("item6:endpoint_exceeded")
    return ("ACCEPT" if not fired else "REJECT"), fired, total


def gate_eex_demo(inputs: dict) -> tuple[dict, dict]:
    cert, truth = build_demo_certificate(inputs)
    check("G5: demo row exact truth replays the banked battery value 15/8",
          sum(truth.values(), Fraction(0)) == DEMO_TRUTH,
          f"per-level {[str(truth[L]) for L in DEMO_SCHEDULE]}")
    v, fired, total = verify_certificate(cert, inputs, Fraction(4))
    check("G5: honest 6-item certificate ACCEPTs at T = 4 "
          "(items verified, C2'' instance linked per #163)",
          v == "ACCEPT" and not fired and total == DEMO_TRUTH,
          f"certified total = {total}")
    tight = copy.deepcopy(cert)
    tight["item6"]["T"] = [1, 1]
    v2, fired2, _ = verify_certificate(tight, inputs, Fraction(1))
    check("G5: fail-closed — same certificate REJECTs at T = 1 "
          "(truth 15/8 > 1)",
          v2 == "REJECT" and any("endpoint_exceeded" in f for f in fired2))
    return cert, truth


# =========================================================================
# 8. THE ASSEMBLY CHAIN — exact inequalities on the declared inputs
# =========================================================================

def assembly(inputs: dict) -> None:
    """Lemma-1/D2/D3 + per-level excess + W_cl zones + aggregate
    Sigma log2 E_j <= 100 + the 21-bit joint reserve
    => q^{-t+H} W_cen <= 2^121."""
    sk = inputs["SKELETON"]
    check("A0: consumer-face identity declared and pinned "
          "(q^{-t+H} W_cen = E_U[prod rho_j])",
          "W_cen" in sk["consumer_face"]
          and sk["status"] == "PROVED-PINNED")
    check("A1: Lemma-1 / D2 / D3 skeleton declared "
          "(E_L >= 1 floor from D3 lambda = 0)",
          all(k in sk for k in ("lemma1", "d2", "d3_floor")))

    # A2: admissibility/balance — r_L = q^L / 2^{256 L} < 1 exactly for
    # every q < 2^256 (integer inequality (2^256 - 1)^L < 2^{256 L}).
    qmax = 2 ** Q_BOUND_BITS - 1
    ok = all(qmax ** L < 2 ** (256 * L) for L in (1, 2, 34))
    check("A2: balance r_L < 1 at every admissible q < 2^256 "
          "(exact integer check, N_L = 256 L)", ok)

    # A3 + A4: per-level excess (C1', named conditional) with the zone
    # inputs (per-row W_cl <= tau_L, certified by pi_R = ENDPOINT-EXC
    # content), aggregated exactly:
    #   E_L <= 1 + K' r_L (1 + tau_L) <= 1 + K'(1 + tau_L)
    #   prod_L E_L <= prod_L (1 + K'(1 + tau_L)) <= 2^100.
    kcap = inputs["C1P_LEDGER"]["K_prime_cap"]
    prod = Fraction(1)
    for L in range(1, LEVELS + 1):
        z = inputs["ZONES"]["levels"][L]
        tau = Fraction(z["tau_num"], z["tau_den"])
        per_level = 1 + kcap * (1 + tau)
        if per_level < 1:
            raise M4Reject(f"A3: per-level bound below the D3 floor at {L}")
        prod *= per_level
    budget = Fraction(2) ** AGG_BUDGET_BITS
    bits = math.log2(float(prod))
    check("A3/A4: aggregate DLI-AGG — prod_L (1 + K'(1 + tau_L)) <= 2^100 "
          "(exact rational)", prod <= budget,
          f"{bits:.4f} bits of 100 used; slack {100 - bits:.4f} bits")

    # A5: the joint reserve (C2'', named conditional):
    #   E_U[prod rho] <= 2^21 * prod E_L  (aggregate form primary, /33
    #   display only).  Exact composition:
    reserve = Fraction(2) ** inputs["C2PP_INSTANCE"]["R_joint_bits"]
    endpoint = Fraction(2) ** ENDPOINT_BITS
    check("A5: joint reserve composes — 2^R_joint * prod_L bound <= 2^121 "
          "(exact rational)", reserve * prod <= endpoint,
          f"2^{R_JOINT_BITS} * 2^{bits:.2f} <= 2^{ENDPOINT_BITS}")
    check("A6: endpoint identity 21 + 100 = 121 (exact)",
          inputs["C2PP_INSTANCE"]["R_joint_bits"] + AGG_BUDGET_BITS
          == ENDPOINT_BITS)
    info("assembly conclusion (CONDITIONAL): q^{-t+H} W_cen <= 2^121, "
         "conditional on C2'' (joint reserve), C1' (per-level excess), "
         "ENDPOINT-EXC (per-row W_cl zone certification + coverage)")


# =========================================================================
# 9. VERDICT LOGIC — never unconditional while a predicate is unproved
# =========================================================================

def compute_verdict(inputs: dict) -> str:
    """The amber wiring consumes exactly this line's verdict."""
    preds = [inputs["C2PP_INSTANCE"], inputs["C1P_LEDGER"],
             inputs["ENDPOINT_EXC"]]
    for p in preds:
        if p["status"] == "PROVED":
            tok = p.get("maintainer_token")
            valid = (isinstance(tok, dict) and "path" in tok
                     and (REPO / tok["path"]).exists()
                     and f"MAINTAINER-COUNTERSIGN: {p['name']} PROVED"
                     in (REPO / tok["path"]).read_text())
            if not valid:
                raise M4Reject(
                    f"predicate {p['name']} claims PROVED without a valid "
                    "maintainer countersign — no silent upgrade "
                    "(catch #163 discipline)")
    unproved = [p["name"] for p in preds if p["status"] != "PROVED"]
    if unproved:
        return CONDITIONAL_VERDICT
    return ("ASSEMBLY-VERIFIED-UNCONDITIONAL (all three predicates "
            "maintainer-countersigned)")


# =========================================================================
# 10. CATCH #162 — read-only detection of the torn duplicate (spec'd
#     surgery is a maintainer edit; presence is a WARNING, not a failure)
# =========================================================================

FRAG_HEAD = "==gridDP PASS; full log banked at notes/m1_run_record_20260713.log)"
FRAG_TAIL = "PROMOTION-ELIGIBLE pending maintainer review. "
FRAG_SHA256_PREFIX = "d60593436da96d99"


def check_catch_162() -> None:
    dag = json.loads((REPO / "dag.json").read_text())
    stmt = next(n for n in dag["nodes"]
                if n["id"] == "dli_prime_weighted_large_block_support"
                )["statement"]
    first = stmt.find(FRAG_HEAD)
    second = stmt.find(FRAG_HEAD, first + 1)
    if second == -1:
        # post-surgery state: exactly one occurrence, inside the original
        ok = (stmt.count("F-a NOT FIRED at either depth") == 1
              and stmt.count("C2''s F-round count: 0 -> 1") == 1
              and "MITM==gridDP PASS" in stmt)
        check("catch #162: statement CLEAN (post-surgery invariants hold)",
              ok)
        return
    end = stmt.find(FRAG_TAIL, second)
    if end == -1:
        raise M4Reject("catch #162: torn duplicate present but MALFORMED "
                       "(tail marker missing) — inconsistent surgery state")
    end += len(FRAG_TAIL)
    frag = stmt[second:end]
    sha = hashlib.sha256(frag.encode()).hexdigest()[:16]
    verbatim = stmt[first:first + len(frag)] == frag
    check("catch #162: torn duplicate matches the banked spec exactly "
          "(verbatim copy, pinned sha256)",
          verbatim and sha == FRAG_SHA256_PREFIX,
          f"offsets [{second}:{end}), {len(frag)} chars, sha256[:16]={sha}")
    info("catch #162: deletion OWED at M4 banking — remove statement chars "
         f"[{second}:{end}) (the duplicate block '==gridDP PASS...pending "
         "maintainer review. ' inside the wave-4 paragraph); full spec in "
         "m4_report.md")


# =========================================================================
# 11. MUTATION CONTROLS — built-in tampers that MUST trip
# =========================================================================

def run_stage(fn, *args) -> tuple[bool, str]:
    """Run a stage against a tampered input set; report whether it fails."""
    global _failures
    saved = _failures
    _failures = []
    trip, why = False, ""
    buf_fail: list[str] = []
    try:
        import io
        import contextlib
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            fn(*args)
        buf_fail = list(_failures)
        if buf_fail:
            trip, why = True, f"checks failed: {buf_fail[:2]}"
    except (M4Reject, M4InputReject) as e:
        trip, why = True, f"{type(e).__name__}: {e}"
    except Exception as e:  # any crash on tampered input is a trip
        trip, why = True, f"crash: {type(e).__name__}: {e}"
    finally:
        _failures = saved
    return trip, why


def mutation_controls(inputs: dict, demo_cert: dict) -> None:
    controls: list[tuple[str, bool, str]] = []

    # MUT-1: tamper the joint reserve 21 -> 22 (catch #40 regression)
    t = copy.deepcopy(inputs)
    t["C2PP_INSTANCE"]["R_joint_bits"] = 22
    trip1a, why1a = run_stage(provenance_pins, t)
    trip1b, why1b = run_stage(assembly, t)
    controls.append(("MUT-1 reserve 21->22", trip1a and trip1b,
                     f"pins: {why1a} | assembly: {why1b}"))

    # MUT-2: broken zone bound — tau_20 = 2^30 blows the 100-bit budget
    t = copy.deepcopy(inputs)
    t["ZONES"]["levels"][20]["tau_num"] = 2 ** 30
    t["ZONES"]["levels"][20]["tau_den"] = 1
    trip2, why2 = run_stage(assembly, t)
    controls.append(("MUT-2 zone bound broken (tau_20 = 2^30)", trip2, why2))

    # MUT-2b: zone tag contradicts the banked A1-PROD table
    t = copy.deepcopy(inputs)
    t["ZONES"]["levels"][20]["zone"] = "covered-partial"
    trip2b, why2b = run_stage(provenance_pins, t)
    controls.append(("MUT-2b zone tag L=20 contradicts banked table",
                     trip2b, why2b))

    # MUT-3: certificate item removed -> fail-closed REJECT
    t = copy.deepcopy(demo_cert)
    del t["item3"]
    v, fired, _ = verify_certificate(t, inputs, Fraction(4))
    controls.append(("MUT-3 certificate item3 removed",
                     v == "REJECT" and any("item3:MISSING" in f
                                           for f in fired),
                     f"verdict={v}, fired={fired[:1]}"))

    # MUT-4a: with C2'' honestly unproved the verdict MUST be CONDITIONAL
    v = compute_verdict(inputs)
    controls.append(("MUT-4a unproved C2'' downgrades verdict to "
                     "CONDITIONAL (never PASS)",
                     v == CONDITIONAL_VERDICT
                     and "UNCONDITIONAL" not in v and "C2''" in v,
                     f"verdict = {v}"))

    # MUT-4b: C2'' flagged PROVED without countersign -> REJECT
    t = copy.deepcopy(inputs)
    t["C2PP_INSTANCE"]["status"] = "PROVED"
    trip4b, why4b = run_stage(compute_verdict, t)
    controls.append(("MUT-4b C2'' claims PROVED without countersign",
                     trip4b, why4b))

    # MUT-5: coverage input absent -> fail-closed INPUT-REJECT
    t = copy.deepcopy(inputs)
    del t["ENDPOINT_EXC"]
    trip5, why5 = run_stage(validate_inputs, t)
    controls.append(("MUT-5 coverage/ENDPOINT-EXC input missing",
                     trip5, why5))

    # MUT-6: junction-convention drift /33 -> /34 (catch #108 regression)
    t = copy.deepcopy(inputs)
    t["C2PP_INSTANCE"]["junctions"] = 34
    t["C2PP_INSTANCE"]["convention"] = "/34 drift"
    trip6, why6 = run_stage(provenance_pins, t)
    controls.append(("MUT-6 junction convention drift to /34", trip6, why6))

    # MUT-7: item-5 unlinked from the named C2'' instance (catch #163)
    t = copy.deepcopy(demo_cert)
    t["item5"]["c2pp_instance"] = None
    v, fired, _ = verify_certificate(t, inputs, Fraction(4))
    controls.append(("MUT-7 item-5 C2'' link severed (catch #163)",
                     v == "REJECT" and any("#163" in f for f in fired),
                     f"verdict={v}"))

    all_ok = True
    for name, tripped, why in controls:
        tag = "TRIPPED" if tripped else "NOT TRIPPED — CONTROL FAILURE"
        print(f"[mutation] {name}: {tag}  ({why[:120]})")
        if not tripped:
            all_ok = False
    check(f"mutation battery: {len(controls)} controls, all tripped",
          all_ok)


# =========================================================================
# 12. M5 status (informational — the maintainer one-liner, catch #40)
# =========================================================================

M5_FILE = NOTES / "M5_CONFIRMATION_2P121.md"
M5_REQUIRED_LINE = (
    "MAINTAINER CONFIRMATION (M5, catch #40): the operative endpoint of "
    "CONJECTURE B-WEAK and of every dli route document is 2^121 "
    "(joint reserve 21 bits); the 2^122 displays are superseded."
)


def m5_status() -> None:
    if M5_FILE.exists() and M5_REQUIRED_LINE in M5_FILE.read_text():
        info("M5: CONFIRMED (maintainer one-liner present)")
    else:
        info("M5: OUTSTANDING — the maintainer one-liner is still owed "
             "(catch #40); required exact text spec'd in m4_report.md; "
             "non-fatal for M4")


# =========================================================================
def main() -> int:
    print("=" * 74)
    print("M4 ASSEMBLY VERIFIER — dli_prime_weighted_large_block_support")
    print("exact-rational; fail-closed; named conditional predicates")
    print("=" * 74)

    try:
        inputs = build_inputs()
        validate_inputs(inputs)
        info("input manifest validated (fail-closed schema): "
             "C2''-instance + C1' ledger + ENDPOINT-EXC(coverage) + "
             "zones + skeleton")
        info(f"named predicates: C2'' [{inputs['C2PP_INSTANCE']['status']}"
             f", {inputs['C2PP_INSTANCE']['rounds_survived']} round], "
             f"C1' [{inputs['C1P_LEDGER']['status']}, "
             f"{inputs['C1P_LEDGER']['rounds_survived']} round], "
             f"ENDPOINT-EXC [{inputs['ENDPOINT_EXC']['status']}, "
             f"{inputs['ENDPOINT_EXC']['rounds_survived']} round, "
             f"coverage {inputs['ENDPOINT_EXC']['coverage']}]")

        print("\n-- provenance pins " + "-" * 50)
        provenance_pins(inputs)
        print("\n-- gate G1: f2b 8-row record replay " + "-" * 33)
        gate_f2b()
        print("\n-- gate G2: pose-time calibration replay " + "-" * 28)
        gate_calibration()
        print("\n-- gate G3: C1' M2 exact replay (12 rows) " + "-" * 27)
        gate_m2_replay(inputs)
        print("\n-- gate G4: C2'' M1 record pins " + "-" * 37)
        gate_m1_record()
        print("\n-- gate G5: ENDPOINT-EXC 6-item demo (exact toy row) --")
        demo_cert, _ = gate_eex_demo(inputs)
        print("\n-- assembly chain " + "-" * 51)
        assembly(inputs)
        print("\n-- catch #162 statement hygiene " + "-" * 37)
        check_catch_162()
        print("\n-- mutation controls " + "-" * 48)
        mutation_controls(inputs, demo_cert)
        print("\n-- M5 " + "-" * 63)
        m5_status()
        verdict = compute_verdict(inputs)
    except M4InputReject as e:
        print(f"\nM4-INPUT-REJECT: {e}")
        return 2
    except M4Reject as e:
        print(f"\nM4-FAIL: {e}")
        return 1

    print("\n" + "=" * 74)
    if _failures:
        print(f"M4-FAIL: {len(_failures)} check(s) failed: {_failures}")
        print("=" * 74)
        return 1
    print(f"M4-VERDICT: {verdict}")
    print("           q^{-t+H} W_cen <= 2^121 follows by exact rational")
    print("           arithmetic from the named-predicate inputs; NO")
    print("           unconditional claim is made (F-round state 1/1/1;")
    print("           promotion requires maintainer countersigns).")
    print("=" * 74)
    return 0


if __name__ == "__main__":
    sys.exit(main())
