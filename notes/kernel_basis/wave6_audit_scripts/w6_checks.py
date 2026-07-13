#!/usr/bin/env python3
"""Wave-6 audit replay driver (standalone, read-only on both repos).

Extracts every audited verifier at pin 7e4be37f via `git show`, builds the
scratchpad mini-trees the path-relative verifiers need, and replays them under
tools/ramguard tiny. Also reruns the wave-6 original brute-force validation of
the 9d058055 envelope extrema reduction (w6_envelope_brute.py logic inlined by
import). Expected: every step prints its banked PASS line.

Run:  cd /home/u2470931/smooth-read-solomin/prize && \
      tools/ramguard tiny -- python3 <scratchpad>/w6_checks.py --extract
      # then run each listed replay command (kept separate so no single
      # ramguard envelope has to hold all of them).

This file doubles as the audit record of WHICH commands were run; each was
executed during the wave-6 session with the printed results recorded in
w6_findings.md.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

PIN = "7e4be37f"
WORKTREE = "/home/u2470931/smooth-read-solomin/prize-codex-resolution-v3-20260712"
SCRATCH = Path(
    "/tmp/claude-1000/-home-u2470931-smooth-read-solomin/"
    "d53e6c57-2281-4b35-b085-8a669b4db5f5/scratchpad"
)

# (git path at pin, scratchpad destination)
EXTRACTS = [
    # cluster A
    ("background/nodes/xr_affine_core_cogirth_ray_bound/verify.py",
     "w6_xr_cogirth_verify.py"),
    # cluster B
    ("background/nodes/mca_quadratic_prize_rows/verify.py", "w6_mca_verify.py"),
    # cluster C (path-relative: need mini-tree w6_dli_tree/)
    ("dag.json", "w6_dli_tree/dag.json"),
    ("critical/nodes/dli_prime_weighted_large_block_support/verify.py",
     "w6_dli_tree/critical/nodes/dli_prime_weighted_large_block_support/verify.py"),
    ("critical/nodes/dli_prime_weighted_large_block_support/conditional.md",
     "w6_dli_tree/critical/nodes/dli_prime_weighted_large_block_support/conditional.md"),
    ("critical/nodes/dli_marginal_baseline100_coverage/verify.py",
     "w6_dli_tree/critical/nodes/dli_marginal_baseline100_coverage/verify.py"),
    ("critical/nodes/dli_marginal_baseline100_coverage/conditional.md",
     "w6_dli_tree/critical/nodes/dli_marginal_baseline100_coverage/conditional.md"),
    ("critical/nodes/dli_marginal_baseline100_coverage/statement.md",
     "w6_dli_tree/critical/nodes/dli_marginal_baseline100_coverage/statement.md"),
    ("critical/nodes/dli_c2pp_joint_reserve/statement.md",
     "w6_dli_tree/critical/nodes/dli_c2pp_joint_reserve/statement.md"),
    # cluster D
    ("background/nodes/f3_h3_rich_fiber_norm_cutoff/verify.py",
     "w6_rfnc_verify.py"),
    ("dag.json", "w6_batch_tree/dag.json"),
    ("background/nodes/f3_h3_rich_fiber_ideal_batching/verify.py",
     "w6_batch_tree/background/nodes/f3_h3_rich_fiber_ideal_batching/verify.py"),
    ("experiments/prize_resolution/h3_rich_norm_gcd_result.json",
     "w6_batch_tree/experiments/prize_resolution/h3_rich_norm_gcd_result.json"),
    ("experiments/prize_resolution/h3_parseval_cutoff4_probe.py",
     "w6_cutoff4_probe.py"),
]

# ramguard tiny replay commands, with the PASS lines observed in this session.
REPLAYS = [
    ("w6_xr_cogirth_verify.py",
     "XR_AFFINE_CORE_COGIRTH_RAY_BOUND_PASS matroids=32280 equality=3960 "
     "affine_lines=624 max_pairs=5 rowc-r1_4:ambient_s<=4,PA_s<=4,local_PA_s<=4,"
     "rank4=closed ... prize-r1_16:ambient_s<=10,PA_s<=10,local_PA_s<=10,rank4=closed"),
    ("w6_envelope_brute.py", "W6_ENVELOPE_BRUTE tested=7278 mismatches=0"),
    ("w6_mca_verify.py",
     "MCA_QUADRATIC_PRIZE_ROWS_PASS proof_rows=32654 toy_max=(1, 2) "
     "r1_2:...B=389500552609 r1_4:...B=1210584858040 r1_8:...B=2879806199253 "
     "r1_16:...B=6233898019554"),
    ("w6_dli_tree/critical/nodes/dli_prime_weighted_large_block_support/verify.py",
     "DLI_M4_ASSEMBLY_PASS boundary=2^121 negative_controls=9/9 "
     "premises=baseline100+C2pp21"),
    ("w6_dli_tree/critical/nodes/dli_marginal_baseline100_coverage/verify.py",
     "DLI_BASELINE100_ASSEMBLY_PASS factor=41/8 aggregate_bits=(80,81) "
     "negative_controls=11/11"),
    ("w6_rfnc_verify.py",
     "H3_RICH_FIBER_NORM_CUTOFF_PASS vectors=43434 parity_pairs=130293 "
     "cutoff=19 parseval=6 exponent=n/4"),
    ("w6_batch_tree/background/nodes/f3_h3_rich_fiber_ideal_batching/verify.py",
     "H3_RICH_FIBER_IDEAL_BATCHING_PASS targets=2 pairs=20 norms=18 gcd=4p "
     "mutations=7/7"),
    ("w6_cutoff4_probe.py",
     "H3_PARSEVAL_CUTOFF4_PROBE_PASS (order 16/32/64, matching and "
     "unconstrained 7-cliques all found; order-64 matching witness = the "
     "fence note's pairs)"),
]


def extract() -> None:
    for src, dst in EXTRACTS:
        out = SCRATCH / dst
        out.parent.mkdir(parents=True, exist_ok=True)
        blob = subprocess.run(
            ["git", "-C", WORKTREE, "show", f"{PIN}:{src}"],
            capture_output=True, check=True,
        ).stdout
        out.write_bytes(blob)
        print(f"extracted {src} -> {out}")


def main() -> None:
    if "--extract" in sys.argv:
        extract()
    print("\nReplay commands (each under tools/ramguard tiny from the master repo):")
    for path, expected in REPLAYS:
        print(f"\n  tools/ramguard tiny -- python3 {SCRATCH / path}")
        print(f"  expected: {expected}")


if __name__ == "__main__":
    main()
