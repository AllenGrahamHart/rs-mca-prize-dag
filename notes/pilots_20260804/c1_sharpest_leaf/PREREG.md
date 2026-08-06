# PRE-REGISTRATION — round 14, mystery 3 (junction-0 / C1-C2'' sparse-certificate lane)

Written BEFORE any computation in this pilot. Date 2026-08-06.

## Leaf selected

`critical/nodes/dli_wcl_slot_1_5_emptiness` (status TARGET), the smallest of the
ten WCL slot leaves that `dli_wcl_zone_coverage` requires.

## Subtraction already performed (do not re-derive)

| banked fact | source |
|---|---|
| exact affine-Galois class counts w=3/4/5/6 = 254 / 24,979 / 2,296,920 / 185,569,028 | `critical/nodes/dli_wcl_zone_coverage/weight5_orbit_route_fence.md:32-35` |
| reduced signed word counts 11,054,080 / 1,398,341,120 / 140,952,784,896 / 11,793,049,669,632 | same, :32-35 |
| 256-row weight-5 norm sample: 722 factor records, 670 distinct primes, max v_2(p-1)=17, slowest factorization 15.95 s | same, :44-48 |
| "The direct norm census ... is not the next closure route" (resource call, 2026-07-13) | same, :50-56 |
| (1,5) has an exact 3-unknown fixed-divisor classifier: `G(Y)=Y A(Y)^2-(bY+1)^2 | Y^256-1`, `deg A = 2` | `background/nodes/dli_wcl_odd_next_boundary_square_divisor_descent/statement.md:65` |
| the remainder ideal `I_1=(R_0..R_4)` has no char-0 point; nonzero integer `Delta_1` exists; "computing, factoring, and applying the official field constraints ... can close both slots" | same, :69-87 |
| straight-line lift for (1,5): 52 variables, 54 equations, total degree <= 3 | `background/nodes/dli_wcl_fixed_divisor_straight_line_lift/statement.md` |
| max-norm gates cannot reach ANY open slot (all w>=5; 23^64 = 2^289.5 > 2^256) | `notes/pilots_20260802/dli_norm_gate/REPORT.md:63-69` |
| count / Minkowski-second-minimum bounds cannot reach any open slot (LAT1 minima law; 256-bit cap; kappa achieved <= 1.507 vs needed [3.97, 8.73]) | `notes/pilots_20260802/wcl_count_bounds/REPORT.md:6-42` |
| standing lane law: "slots need v_2-aware certificates (the sparse-certificate route) — not max-norm gates AND not count bounds" | `notes/pilots_20260802/wcl_count_bounds/FABLE_AUDIT.md:15-21` |
| engineered weight-6 order-512 witness: Norm(1 - z^33 + z^40 - z^136 - z^143 + z^145) = 2q, q prime, 256-bit, v_2(q-1)=9 | `background/nodes/dli_wcl_engineered_terminal_scope/statement.md` |

The *only* route the lane law leaves alive for the ten slots is the
v_2-aware sparse certificate, i.e. the `Delta` route. This pilot tests that
route at its smallest instance.

## Claims registered

**P1 (coefficient identity).** Writing `A = Y^2 + a1 Y + a0` and
`G(Y) = Y A(Y)^2 - (bY+1)^2 = Y^5 - s1 Y^4 + s2 Y^3 - s3 Y^2 + s4 Y - s5`
with `s_i` the elementary symmetric functions of the five roots, the five
coefficient equations are exactly

```text
2 a1 = -s1;   a1^2 + 2 a0 = s2;   2 a0 a1 - b^2 = -s3;   a0^2 - 2b = s4;   s5 = 1.
```

FALSIFIER: symbolic expansion disagrees in any coefficient.

**P2 (supporting-prime lemma).** For a reduced signed weight-5 `P` at
`ell=1`, EVERY odd prime `p` dividing `Res(X^256+1, P(X))` is a supporting
characteristic of slot (1,5): there is `w` of exact order 512 in `F_p-bar`
with `P(w)=0`.

FALSIFIER: a sampled class and a prime factor `p` of its resultant for which
no root of `P` in `F_p-bar` has exact order 512. Tested constructively on
every prime factor of every sampled class.

**P3 (Delta infeasibility test).** Any valid `Delta_1` is divisible by every
supporting characteristic (banked, `...odd_next_boundary...:84-86`). Hence
`log2|Delta_1| >= sum over DISTINCT supporting primes of log2 p`. I will
measure distinct-prime yield per class on my own sample and extrapolate to
the banked 2,296,920 classes.

PRE-REGISTERED DECISION THRESHOLDS (fixed now):
- if extrapolated `log2|Delta_1| >= 10^7` bits ==> the "compute and factor one
  integer Delta per slot" route is declared INFEASIBLE at the smallest slot,
  and therefore at all ten;
- if `< 10^5` bits ==> route viable, this pilot's thesis is REFUTED;
- in between ==> undecided, report as such.

**P4 (census cost, EMPIRICAL).** Measure mean/median wall time of
`Res(X^256+1,P)` plus complete factorization on a random weight-5 class
sample; extrapolate to 2,296,920 classes. Labeled empirical throughout.

**P5 (falsifier watch).** Record `max v_2(p-1)` over all primes seen. If any
prime `p < 2^256` has `v_2(p-1) >= 41`, slot (1,5) is REFUTED and the
junction-0 ten-slot program dies. Banked comparanda: max v_2 = 18 (w=3),
29 (w=4), 17 (banked w=5 256-row sample).

## Controls (run must be void if any fails)

- **C-a** Burnside orbit counts must reproduce 254 (w=3), 24,979 (w=4),
  2,296,920 (w=5).
- **C-b** reduced signed word counts must reproduce 11,054,080 /
  1,398,341,120 / 140,952,784,896.
- **C-c** my norm routine must reproduce the banked engineered weight-6
  value exactly:
  `Norm = 122312418397310579415219240127455896396372121843316076135243835573788121252866 = 2q`,
  `q = 61156209198655289707609620063727948198186060921658038067621917786894060626433`
  prime, `v_2(q-1) = 9`.

## Compute discipline

All runs via `tools/ramguard local -- python3 ...` from the repo root. No
Modal, no network. Anything larger is filed as a COMPUTE REQUEST, not run.
