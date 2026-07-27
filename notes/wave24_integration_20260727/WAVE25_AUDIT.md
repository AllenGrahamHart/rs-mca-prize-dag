# Wave-25 audit — Codex's DSP8 / H3 batch

**Date:** 2026-07-27. **Planner:** Fable. **Range:** `9ef1680d..0124bcb9`
(four commits, 08:51–09:11). **Verdict: CLEAN — integrated in full.**

**Shape: 3 new PROVED background nodes, ZERO status changes, 33 files.** After a
day of unwinding over-claims, this batch is the opposite: additive, verified,
and fenced. Nothing on the critical surface moved; the census is unchanged at
`241 = 177/39/25`.

| node | what it proves |
|---|---|
| `f3_affine_coset_pair_prime_subfield_descent` | the extension-field count IS the prime-field count (PSD1) |
| `f3_h3_norm_one_torus_affine_quotient_cap` | `I_(a,b) <= 2` on the norm-one torus (NT1) |
| `f3_h3_dsp8_smooth_quotient_cap_compiler` | removes the quotient weight, at the price of an `n^(4/3)` estimate it does NOT prove |

All six verifiers (`verify.py` + `verify_audit.py` on each) **PASS**.

## What I checked independently

**1. The prime-subfield descent resolves the fence I raised at the Mattarei
import.** I had flagged Codex's own caveat — "the theorem is prime-field only,
not transported to a deployed extension-field row" — as the live risk, since
KoalaBear is `p^6`. This node closes it correctly, and by the honest route:

> If `x in F_q` and `L_1(x) in K <= F_p^*` with `a_1, b_1 in F_p`, then
> `x = a_1^{-1}(L_1(x) - b_1) in F_p`.

So the extension-field count is **literally the prime-field count** — the proof
says exactly that: *"not an extension of Mattarei's theorem."* No transport is
claimed; none is needed.

**KoalaBear numerics re-computed by me, all confirmed:** `p - 1 = 2^24 * 127`;
`n = 2^21` divides it; `d = (p-1)/n = 1016 = 8*127`; `d^3 = 1048772096 > 4n =
8388608`; `d >= 4`; `p = 2 mod 3` so `gcd(3, p-1) = 1` and cubing is an
automorphism of `F_p^*`. The hypotheses hold.

**And the exclusion is stated, not hidden:** for Mersenne-31,
`v_2(p_M - 1) = 1`, so an order-`2^21` subgroup is NOT in `F_(p_M)` — the node
says so and claims nothing there.

**2. The norm-one bound — I re-derived it before reading the proof, and it
matches.** For `z in T`, `bar(z) = z^{-1}`; if `az + b in T` too then
`1 = (az+b)(bar(a) z^{-1} + bar(b))`, and multiplying by `z` gives
`a bar(b) z^2 + (a bar(a) + b bar(b) - 1) z + bar(a) b = 0` — a genuine
quadratic (both outer coefficients nonzero since `a, b in E^*`), hence at most
two roots. `(NT1)` follows.

Its `audit.md` carries seven fences, and the load-bearing ones are exactly the
right ones: **#2** "the norm-one premise is load-bearing — a prime-subfield
multiplicative group can meet a nondegenerate affine image in far more than two
points"; **#5** the Mersenne-characteristic subgroup descends to `F_(p_M^2)`,
not `F_(p_M)`, keeping this route separate from the Mattarei descent; **#6**
the deployed M31 line round is the `chi`-projection of a twin coset, is NOT
this instance, and **no adapter is supplied**.

**3. The compiler states its own limitation.** `(SQC6)` reduces the uniform
smooth target to `U_sm^0 + U_sm^A < 44.926 n^(4/3)`, and the node closes:
*"This compiler removes the quotient weight only at the price of a strong
`n^(4/3)` unweighted smooth-SP estimate. **It proves no such estimate**."* A
reduction presented as a reduction.

## Contrast worth recording

Every failure mode this day's audit exposed — typicality standing in for a
per-row claim, a named-exhibit certificate read as a family result, a
neighbouring zone's proof read as covering the node, an auto-discharge through
a `conditional.md` that did not exist — is **absent** here. The batch names its
hypotheses, verifies its numerics, and disclaims what it has not proved. This is
the standard the re-graded surface should be held to going forward.

## Integrated

3 nodes + 3 edges into `dag.json` (canon guard + atomic replace), folders
copied, `UPSTREAM_IMPORT_LEDGER.md` and `PRIZE_RESOLUTION_ROADMAP.md` synced
from Codex, manifest refreshed (1195 scripts). All six repo validators PASS;
census unchanged.
