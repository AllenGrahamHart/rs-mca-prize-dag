# PRE-REGISTRATION — SL-1b (mystery 2): the base-3 first-moment dimension threshold

Round 16, 2026-08-06. Coordinator-authored brief; the pilot appends its
own registrations BEFORE any computation.

## 0. The target (verbatim, FABLE_AUDIT of f2_sl1_powersums)

> ... the named SL-1b (dim L >= m log_p 3 — the base-3 first-moment
> threshold, exactly log2 3 from LEMMA 3's) ...

SL-1b is one of mystery 2's three remaining obligations (with the t/q
pin — running as a SIBLING pilot this round, do not duplicate it — and
the |K1| seam, assigned to that sibling).

## 1. Source surfaces (read ALL first; quote verbatim)

- `notes/pilots_20260804/f2_sl1_powersums/PROOFS.md` — SL-1's full
  proof (the diagonal-times-Vandermonde mechanism applied locally to
  minors; weight >= ceil(t/2)+1 characteristic-free; the true law
  min(2R+1, max(p, R+1)) sharp in both branches; the Z(L) mass bounds;
  the discharge criterion t >= 1.2263m; SL-1b's exact statement and
  why it was named). QUOTE SL-1b's statement verbatim from this file
  before any work — if the statement there differs from the audit's
  one-line gloss above, the PROOFS.md form governs and the discrepancy
  is your first reported item.
- `notes/pilots_20260804/f2_sl1_powersums/FABLE_AUDIT.md` — the
  banked context: what SL-1 subsumes (THEOREM A), the DLI/WCL stronger
  sibling (w >= 2R+1 under char > w, with 6 counterexamples showing
  char > w is NECESSARY), and the cross-lane scope facts.
- `notes/pilots_20260804/f2_opening/PROOFS.md` — LEMMA 3 (the
  necessary condition SL-1b's constant is calibrated against) and the
  rung ladder.

## 2. Pre-registered claims

- **(B1)** PROVE or REFUTE SL-1b as stated in PROOFS.md. First test:
  does SL-1's own mechanism (diagonal-times-Vandermonde on minors)
  extend to the dimension statement, and if not, name the exact
  obstruction.
- **(B2)** Sharpness: if proved, exhibit the extremal family attaining
  (or approaching) dim L = m log_p 3; if the truth is a different
  constant c != log_p 3, prove the true law and state which side the
  discharge criterion moves.
- **(B3)** Small-field search for counterexamples BEFORE investing in
  proof: exhaustive L over small p and m at ramguard-tiny scale, with
  the search space and its boundaries pre-registered in your appended
  section. A counterexample ends the pilot with a REFUTED verdict and
  the witness.
- **(B4)** The consequence, stated exactly: what does SL-1b (proved or
  refuted or re-constanted) do to mystery 2's discharge chain at each
  rung — independent of the t-pin question, which the sibling pilot
  owns. If your result INTERACTS with the t-pin (e.g., the criterion
  t >= 1.2263m moves), flag the interaction for the coordinator; do
  not resolve it yourself.

## 3. Pre-registered falsifiers / honesty clauses

- A single counterexample in (B3) refutes SL-1b as stated; report the
  witness and stop proving.
- If SL-1b's statement in PROOFS.md is ambiguous (e.g., which L, which
  m), the ambiguity is a reported defect, not a licence to pick the
  provable reading. State both readings and address the one LEMMA 3's
  calibration needs.
- No silent strengthening: if you prove a weaker threshold that still
  serves the discharge criterion, label it SL-1b-WEAK and say exactly
  what gap remains.

## 4. Rules of engagement

- DRAFT ONLY: write only inside `notes/pilots_20260806/f2_sl1b/`.
  Never touch dag.json, node shards, tools/, or push.
- COMPUTE LAW: never bare python3; `tools/ramguard tiny -- python3 ...`
  (256M/60s) or `tools/ramguard local -- python3 ...` (1G/5min);
  literal `--`; run from repo root
  `/home/u2470931/smooth-read-solomin/prize`.
- Verbatim quotes for every statement you rely on (file:line).
- Do NOT write REPORT.md — return the full report as your final
  message; the coordinator persists it verbatim.

---

# APPENDED PRE-REGISTRATION (pilot, 2026-08-06, before any computation)

## A. The target statement, quoted verbatim

`notes/pilots_20260804/f2_sl1_powersums/PROOFS.md:316-319`:

> **SL-1b (the named residual, replacing SL-1 on the obligation list):** prove
> a **lower** bound `dim_{F_p} L >= m · log_p 3` (or a second-moment /
> anti-concentration step for `Z(L)`). This is a counting statement about the
> deployed `L`; SL-1 (distance) is now discharged and is not the obstruction.

and the threshold it is calibrated against,
`notes/pilots_20260804/f2_sl1_powersums/PROOFS.md:296-299`:

> ```text
>    E[Z] = O(1)          iff  p^d >~ 2^m   iff  d >= m / log2 p     <-- LEMMA 3
> ```
> ```text
>   L^perp ∩ T = {0}     iff  p^d >~ 3^m   iff  d >= m · log_p 3    <-- existence
> ```

**Recorded discrepancy vs the audit gloss** (`PREREG.md:8-9` above, from
`FABLE_AUDIT.md:19-22`): the audit calls SL-1b "the base-3 first-moment
threshold, exactly log2 3 from LEMMA 3's". PROOFS.md:296-299 labels the
base-2 line "LEMMA 3" (a *mass* threshold, `E[Z]=O(1)`) and the base-3
line "existence" (`L^perp ∩ T = {0}`). These are two DIFFERENT
conclusions, not one threshold at two constants. PROOFS.md governs.

## B. The two readings I am obliged to separate (honesty clause §3)

- **(R-A) LITERAL.** `dim_{F_p} L >= m · log_p 3` for the deployed `L`,
  full stop — a statement about one integer.
- **(R-B) INTENDED.** The consequence PROOFS.md:298 attaches to it:
  `L^perp ∩ T = {0}` for the deployed `L` (hence `Z(L)=1` and (O1)).

I will report a verdict on BOTH, and state explicitly whether (R-A)
implies (R-B).

## C. Pre-registered proof attempt (B1)

**PA-1.** dim L = m − dim L^perp, and `L^perp` is the F_p-kernel of the
`|Lambda| × m` matrix `A = (y_i^l)`. SL-1's own diag×Vandermonde minor
argument shows some `R × R` minor of `A` is invertible over `F_q`,
whence `dim_{F_p} L^perp <= m − R` and

```text
        dim_{F_p} L  >=  min(m, R),     R = longest consecutive odd run.
```

Registered prediction: PA-1 succeeds, and (R-A) therefore reduces to the
purely numerical `ceil(t/2) >= m log_p 3`, i.e. `t >= 2 m log_p 3`.

**PA-1 falsifiers** (any one kills PA-1):
- (F1) a configuration in the B3 grid with `dim L < min(m, R)`;
- (F2) a configuration where `A` has NO invertible `R × R` minor
  although `Lambda` contains `R <= m` consecutive odd exponents;
- (F3) an F_p-subspace of `F_p^m` of F_p-dimension `> m − R` contained
  in the F_q-kernel (i.e. the base-change step is wrong).

## D. Pre-registered small-field search grid (B3), fixed now

Field: `F_q`, `q = p^k`. Window `W <= mu_n`, `n` even, closed under
`x -> -x`; `m = |W|/2`; `Lambda = {2a+1, 2a+3, ..., 2a+2R-1}`.

- `p in {3, 5, 7, 11, 13, 17, 19}`
- `k in {1, 2, 3}` with `n | p^k − 1` and `k = ord_n(p)` minimal
- `n` even, `4 <= n <= 48`
- windows: **(W-full)** `W = mu_n` (`m = n/2`); **(W-ord)**
  `W = {x : ord(x) = n}` (`m = phi(n)/2`)
- `R = 1 .. min(m+1, 8)`; shifts `a in {0, 1, 2}`
- ternary sweep over all `3^m` vectors only when `m <= 10`
  (`3^10 = 59049`); rank-only rows allowed up to `m <= 12`
- exact arithmetic in `F_p[X]/(f)`, `f` irreducible of degree `k`; no
  floating point anywhere in a decision

Boundaries (declared, so no post-hoc widening): nothing with `m > 12`,
`n > 48`, `p > 19`, `k > 3`, `R > 8`. If a falsifier is not found inside
this box I report "not found in the declared box", never "does not
exist".

**Search falsifiers, in priority order:**
- **(S-F1)** any row with `R <= m` and `dim L < min(m, R)` → PA-1 dead,
  SL-1b's proof route dead.
- **(S-F2)** any row with `dim L >= m log_p 3` AND a nonzero ternary
  vector in `L^perp` → **(R-B) is REFUTED**: the literal SL-1b does not
  imply what PROOFS.md:298 attaches to it. (Rows with `p = 3` are
  excluded from S-F2 as degenerate: `log_3 3 = 1` makes the threshold
  `dim L >= m`, i.e. `L^perp = 0`, so the implication is vacuously true
  there. Declared before running.)
- **(S-F3)** any row with `dim L > min(m, k|Lambda|)` → the upper bound
  used for the rung-16/`t*` verdict is wrong.

## E. Pre-registered official-row arithmetic (B4)

Constants used, all quoted from the repo, none invented:
`p = 2^31 − 2^24 + 1`, `log2 p = 30.988685`,
`m_j = 2^{22+j}` (`f2_opening/PROOFS.md:15`), `m_16 = 2^38` vs `2^39`
ambiguity carried, `t in {7e10, 2^36, 2^41/log2 p, t* = 8,592,912,739}`
(`f2_sl1_powersums/PROOFS.md:386-391`).

Registered predictions (recorded before computing):
- (P1) (R-A) holds at rungs 14-16 under `t = 7e10` with margin > 2x.
- (P2) (R-A) FAILS at rung 16 under `t*`, and fails by an upper bound
  (`dim L <= k·|Lambda|`), i.e. it is REFUTED there, not merely open.
- (P3) The `t*` refutation and CATCH-4's own sign flip both depend on
  `k = 2`; I will report the `k` at which each evaporates. **I will NOT
  pin `k` or `t`** — that is the sibling pilot `f2_tq_pin`'s. Any
  interaction is flagged upward, not resolved.

## F. Honesty clauses added by the pilot

- If PA-1 proves only `dim L >= min(m, R)` and this suffices for (R-A)
  only under a hypothesis on `t`, the result is labelled
  **SL-1b-CONDITIONAL(t)**, never "SL-1b PROVED" unqualified.
- Anything I find that is already in the repo goes in the subtraction
  ledger and is cited, not claimed.
- No status flip is proposed for any minted node; DRAFT ONLY.
