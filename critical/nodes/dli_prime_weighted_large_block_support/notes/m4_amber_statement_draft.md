# DRAFT — the dli conditional-close statement (the amber surgery text)

Prepared by the M4 builder (2026-07-13, fresh context). These are DRAFTS for
the maintainer to bank; the repo was read-only for this session. Apply only
after maintainer review of M4 and (independently) the M5 one-liner.

---

## 1. Statement addendum for `dli_prime_weighted_large_block_support`
##    (append to the dag.json `statement` field AFTER the #162 deletion)

> || M4 ASSEMBLY VERIFIER BANKED (2026-07-13): the exact-rational,
> fail-closed assembly implication is machine-verified
> (notes/m4_assembly_verifier.py + m4_run_out.txt):
> [C1' per-level excess, K' <= 4, w_max(L) = L+5] AND [per-row W_cl zone
> inputs, tau_L = 2^-5 at all 34 levels, certified by ENDPOINT-EXC 6-item
> certificates with item 5 consuming the NAMED C2''-instance per catch #163]
> AND [C2'' 21-bit joint reserve, /33 posed junction convention]
> ==> Sigma_L log2 E_L <= 100 (measured exact usage 80.16 bits, slack
> 19.84 bits) ==> q^{-t+H} W_cen <= 2^{21+100} = 2^121.
> Gates replayed at banking: the f2b 8-row record (bit-exact, GM 2.139),
> the pose-time calibration (bulk GM 0.967, refuters 2.752/2.874 exceed the
> /33 allowance exactly), the C1' M2 twelve rows (exact-rational, max
> K' = 0.246909432 at (1,7937), positive control fires), the M1 record pins,
> and a full 6-item ENDPOINT-EXC demo at an exact toy row (truth 15/8,
> ACCEPT/REJECT fail-closed both directions). Ten mutation controls all
> trip (tampered reserve 21->22, broken zone bound, removed certificate
> item, unproved-C2'' verdict downgrade, PROVED-without-countersign reject,
> missing coverage input, /34 drift, severed item-5 link, zone-table
> contradiction, untethered reserve credit). VERDICT CONSUMED BY THIS NODE'S WIRING:
> 'ASSEMBLY-VERIFIED-CONDITIONAL (on C2'', C1', ENDPOINT-EXC as named
> predicates)' — never unconditional while any predicate lacks a maintainer
> countersign. CATCH #164: the banked allowance display '2^(21/33) = 1.555'
> (pose + the #108 pin sentence here) is a last-digit slip — the true value
> 1.5544 rounds to 1.554; display-only, nothing gates on it.

## 2. The route child / conditional-close entry (petal-template shape)

If the maintainer chooses to surface the amber as an explicit route badge
(rather than only the statement addendum), the canonical form is:

> **[CONDITIONAL] dli B-WEAK route close** — q^{-t+H} W_cen <= 2^121 at the
> official rows, CONDITIONAL on exactly three named predicates, each with
> one survived pre-registered adversarial round (F-round state 1/1/1) and
> none proved:
>   (P1) C2'' — the 21-bit joint reserve at the posed /33 junction
>        convention (notes/C2PP_POSED_20260710.md; round M1,
>        notes/m1_run_record_20260713.log);
>   (P2) C1' — the level-scaled per-level excess E-1 <= 4r(1+W_cl),
>        w_max(L) = L+5 (notes/C1PRIME_LEVEL_SCALED_POSE.md; round M2);
>   (P3) ENDPOINT-EXC — per-row 6-item certificate coverage of every
>        official row, item 5 consuming P1 as a named instance (catch #163)
>        (notes/M3_ENDPOINT_EXCEPTION_COVERAGE.md; round banked at
>        notes/eex_report.md); COVERAGE IS OPEN — this is the widest gap.
> Green skeleton (PROVED, not conditions): Lemma 1 exact reduction, D2/D3
> identities + the E >= 1 floor, the A1-PROD norm-sieve theorem (density
> only — it discharges NO individual row), moment transfer, the dual kills.
> Pins: P-CONS (endpoint 2^121 = 21 + 100, catch #40, M5 one-liner),
> P-FIELD (generated-field normalization, catch #13), P-ROWS (official
> rows only), P-CONV (/33 junction display, catch #108; corrected display
> 1.554, catch #164).
> Machine-verified assembly: notes/m4_assembly_verifier.py (exit 0 = the
> implication + all gates + all mutation controls).
> The conjecture node B-WEAK itself KEEPS its user-posed CONJECTURE/TARGET
> status and its pre-registered falsifier — the amber is a route-level
> close, not a truth upgrade.

## 3. The M5 line — exact required maintainer text (catch #40)

File: `critical/nodes/dli_prime_weighted_large_block_support/notes/M5_CONFIRMATION_2P121.md`
containing exactly this line (the M4 verifier greps for it verbatim and
flips its M5 display from OUTSTANDING to CONFIRMED):

```
MAINTAINER CONFIRMATION (M5, catch #40): the operative endpoint of CONJECTURE B-WEAK and of every dli route document is 2^121 (joint reserve 21 bits); the 2^122 displays are superseded.
```

## 4. Re-surgery criteria (pre-registered: when the amber must come back off)

Downgrade the conditional close (CONDITIONAL -> the pre-amber state) if ANY
of the following occurs; none is discretionary:

1. Any of P1/P2/P3 is REFUTED in a later adversarial round (F-round rule
   is symmetric: survivals promote, kills demote).
2. The endpoint constant is re-pinned again (any change to 2^121, to the
   21-bit reserve, or to the 100-bit aggregate split) — the assembly must
   be re-run and re-banked; the M4 verifier fails closed on the current
   pins by construction.
3. The consumer face changes what it consumes (x4 REDUCTION_PACKET's
   'equivalently half-band count <= 2^121' line, or the E_U[prod rho_j]
   identity) — pin A0 breaks.
4. An official row is shown to have NO accepting 6-item certificate
   (coverage refuted, not merely open) — P3 dies as a predicate, and with
   it the per-row W_cl zone inputs.
5. The /33 junction convention or theta = 2 accident convention is revised
   in a way that re-prices the banked calibration (gates G2/G4 fail).
6. Any silent status upgrade is detected (a predicate marked PROVED without
   the countersign file) — the M4 verifier already rejects this; treat a
   bypass as a custody incident (#104/#120 discipline).

Re-promotion after a downgrade requires: the repaired predicate to survive
a NEW pre-registered round, plus a fresh M4 run (green + all mutations
tripping) banked alongside.
