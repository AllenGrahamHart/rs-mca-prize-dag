# Wave-46 audit — THE BAND FLIP: xr_graded_tangent_band_charge TARGET -> CONDITIONAL on SL-2 alone

**Date:** 2026-08-04. **Planner:** Fable. **Range:** codex-v11w..codex-v11x
(head 88238fd0; 20 worker commits). **Verdict: CLEAN — integrated in
full. THE FIRST STATUS FLIP OF A CRITICAL RED BY THE WORKER, and it is
SOUND.**

Codex consumed our rounds 7-12 (SL-1 windowed reduction, the spectral/
parity exclusions, the consolidation updates) and built the DAG
structure our pilots left banked: xr_band_windowed_projection_reduction
(SL-1's theorems, minted PROVED), xr_window_system_descent (their own
proof of the L-content — the power-of-two liveness argument written
properly, superseding the draft we HELD for gaps),
xr_band_high_window_exclusion (SL-2 as a CONDITIONAL node), the
re-decomposition of SL-2-RES into TWO SHARPER REDS
(xr_band_fullrank_window_divisor_count +
xr_band_forced_commonroot_syzygy_count), and 13 PROVED
xr_deficient_window_* payment/router nodes discharging the
rank-deficient branches. 22 nodes + 72 edges; drift on 3 shared
critical nodes = the flip + Route-T exact-budget statement corrections.

THE FLIP: conditional.md assumes EXACTLY ONE leaf (SL-2: 25 N_d <=
17 n^2 on ceil(h/2) <= d <= h-2 at the prize rows); everything else is
banked/proved (RowC vacuous; low depths under the envelope; cascade
tier N <= n/2; MC excluded by depth quantization). BUDGET CORRECTION
ACCEPTED: H_band(C) = s_lo(C) - 16n^3 (exact identity; "13n^3" was a
floored description, H_band/n^3 ~ 13.857 at the prize rows — a
correction IN the ratified route's favor, consistent with its intent).
Provenance preserved verbatim (ratification header, rounds 7-11
parentheticals, heart section, falsifier).

CENSUS REPRICE: math 242(179/38/25) -> 246(179/41/26); submission
257 -> 261(191/43/27). One red retired (the band charge), two sharper
reds enter, +3 conditionals. The unified mystery's SL-2 leaf is now
DAG-front-and-center as the promotion trigger: proving it flips the
band charge with no further mathematical premise.

Verification: their full chain green in their tree (manifests, prize
dag, census) + 17 node verifiers replayed (0 failures) + our post-merge
chain green (compile CONTENT stable at 1817/5070). Merge trivial under
the shared manifest convention (our graph was a strict subset). New
pin: 88238fd0.

Watches: the two new reds are the next-round anchors alongside OV;
export batch (cells 3/6/14 + possibly the flip narrative) pending;
Scott #1149 closes two more 112 cells upstream.
