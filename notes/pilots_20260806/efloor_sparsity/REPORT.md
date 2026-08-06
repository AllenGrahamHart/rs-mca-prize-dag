(Coordinator-persisted verbatim from the pilot's final message, 2026-08-06.)

# ROUND 18 — E_floor SPARSITY (hybrid): the small-prime end of CC-sparsity is now a theorem, and the conjecture's shape is not what round 17 thought

**Verdict in one line: the sparsity half of CC now has its first unconditional theorem — for every fixed odd `p`, `p | N(I_S)` with `strat(S)=0` forces `p > sqrt(w+1)`, so `p=3` is excluded outright for all `w >= 6` at every `n` — but the same work shows `E_floor` is a *tautology* given THEOREM CS, that CC-sparsity is a self-similar copy of (ES) rather than a lemma beneath it, and that the official row gate `v_2(q-1) >= 41` is exactly the blind spot of the mechanism that works.**

## 0. What was run

All from `/home/u2470931/smooth-read-solomin/prize` under the ramguard law. Files, all inside my directory, nothing else touched (verified: `find -newermt '-3 hours'` outside my dir returns empty):

- `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260806/efloor_sparsity/PREREG.md` — coordinator brief + my registrations **E0–E9, appended before any computation**
- `.../efloor_sparsity/PROOFS.md` — the derivations
- `.../efloor_sparsity/sp_lib.py` — new machinery: per-prime splitting of the banked census identity + **exact meet-in-the-middle census**, reusing `cop_lib.py`'s HNF ideal norm as an independent oracle
- `.../efloor_sparsity/verify_sp.py` — stages `self / cover / tern / floor / dense / n64 / n64all / prize / failclosed`
- outputs `verify_{self,cover,tern,floor,dense,n64_a,n64_b,n64all,n128,prize,failclosed}.out`

**56,542 checks, 0 failures, every stage exit 0.** Fail-closed proven not asserted: `failclosed` injects a false check and exits 1.

**The methodological gain that made everything else possible.** Round 17 censused ~21k *orbits* at `r' <= 8`. Splitting the census identity prime-by-prime makes each condition `F_p`-**linear**, so a syndrome meet-in-the-middle censuses **all 2^32 subsets at n=32 exactly, by weight** — and reaches `n=64` and `n=128`. Validated against the banked HNF ideal norm and the banked `F_p[X]`-gcd census on 52,510 checks.

## 1. (S1) SMALL-PRIME EXCLUSION — PROVED

> **THEOREM SP-COVER.** If every coset of `<p>` in `(Z/n)^*` contains an odd `s <= w-1`, then `p | N(I_S)` forces `strat(S) >= 1`.

Proof in three lines (`PROOFS.md` §3): Frobenius closes the window, full coset coverage makes `f_S` vanish at *every* primitive `n`-th root, so `Phi_n | f_S` mod `p`; writing `f_S = A + X^{n/2}B` gives `A - B = 0` in `F_p` with 0/1 coefficients, hence `A = B` **as integers** — periodicity. The engine is **LEMMA AB**: `A-B` is a *ternary* vector, and `{-1,0,1} = F_3` is exactly why `p=3` is the extremal prime.

> **LEMMA COS.** `w_cov(p,2^m)` is **independent of `m`** for `m >= v_2(p^2-1)`, and `w_cov <= 2^{v_2(p^2-1)} <= p^2-1`.
>
> **THEOREM SP-UNIFORM.** `p | N(I_S)` with `strat(S)=0` implies `2^{v_2(p^2-1)} > w`, hence **`p > sqrt(w+1)`**.

| p | 3 | 5 | 7 | 11 | 13 | 17 |
|---|---|---|---|---|---|---|
| `w_cov` (all `n`) | **6** | **4** | **12** | 8 | 4 | **16** |

**This is the first sparsity theorem, and it is stronger than "p=3 alone" as the mandate hoped:** the bad-prime range at stratum `a=0`, previously unbounded below, is now **two-sided** — `sqrt(w+1) < p <= r'^{n/(4·ceil((w-1)/2))}`, the upper end being round 17's CS-EXCL.

**Exhaustive verification** (all `2^32` subsets, `n=32`, `p=3`): `a=0` bad sets = 3072 (w=3,4), **64** (w=5), **0** (w>=6) — `w_cov(3,32)=6`, sharp. Every SP-COVER emptiness check passes at `n in {16,32,64,128}`, `p in {3,5,7,17}`. Registered predictions P1, P3, P4 all held.

**Second mechanism found (THEOREM SP-TERNARY).** For `p >= 5` the ternary constraint bites on its own: at `n=32, p=5` the code has **zero** nonzero ternary codewords already at `w=2`, so `p=5` is excluded far below `w_cov`. Verified exactly, cross-checked against the census in all 56 cells.

**The honest half of (S1): the union bound does NOT close.** I proved the registered density theorem SPD (character sums + a self-contained BCH bound) and then proved it **vacuous in every regime** — it needs dual distance `~p^2 log n` and BCH only delivers `~n/|Z_w|`. **The theorem shape the brief proposed — a union bound over the finite CS3-alive range — cannot be closed by the standard tool.** Both *ends* of the prime range are theorems; the middle is untouched. This is exactly what I pre-registered as the expected outcome (E9.3), so it is not a retrofit.

## 2. (S2) DENSEST FLOOR FAMILIES — no refutation, one strong find

> **LEMMA QS.** For `S = T u (T + n/4)` (disjoint), `x_s = 0` for **every** `s = 2 mod 4`.

At `n=32, r'=6, w=3`, measured exactly over all characteristics:

| | size | in `E_floor` | internal density | share of total `a=0` floor mass |
|---|---|---|---|---|
| baseline, all `C(32,6)` | 906192 | 6528 | 0.00721 | 100% |
| **F1 quarter-shift** | **3808** | **3200** | **0.84034** | **49.0%** |

**0.42% of the sets carry 49% of the entire floor mass**, at 116x the baseline density — the densest family found, and exact (unsampled). Its mechanism is condition-annihilation: at `w=3` it is a `w=2` instance in disguise, the same phenomenon as round 17's CATCH-17C. **It dies completely at `w=4`.** F2/F3/F5 give exactly zero; F4/F6/F7 were subsample-measured and are reported as estimates (their zeros are *not* exact zeros).

**The pre-registered falsifier was NOT triggered.** Every family is exponentially small in `n` (F1 has `~7^{n/4}` members against `2^n`), so contributions vanish. Measured trade-off law: F1 pays `2^-7.9` in size to gain `2^+6.9` in density — **net negative, and one step of `w` erases the gain**.

## 3. (S3) THE n-ASYMPTOTIC — round 16's flag is CLOSED

Round 16 recorded (`es_boundary_adversary/REPORT.md:106`): *"**n=64 was registered in my grid and never executed.**"* Executed, two independent ways, and `n=128` reached as a bonus:

- **All-characteristic exact census at n=64** (banked HNF norm + full factorisation, affine orbits): at `r' in {3,4}`, the `a=0` exceptional class is **EMPTY for every `w >= 3`** (density 0.906/0.861 at the degenerate `w=2`). 874 checks, 0 failures — including a check that every bad prime found satisfies **both** the CS floor and SP-UNIFORM.
- **Per-prime exact census**: `n=64`, `r'<=6`, `w<=12`, `p in {3,5,7,17}`; `n=128`, `r'<=4`, `w<=8`. Last `a=0` witness: `w=3` at `n=64` (p=7,17), **none at all for `w>=3`** at `n=128`.

Every `a=0` count at every `n` is a multiple of `n`, independently reproducing the banked quantization law.

## 4. (S4) THE u2c CONVERSION STATEMENT

> **(CONV)** The 1440-trial credit at `critical/nodes/u2c_giant_tnull_dichotomy/node.json:8` becomes mathematics iff one proves: *at official row parameters, for every `S` with `strat(S)=0`, `q` does not divide `N(I_S)`.*

How far this pilot gets: SP-UNIFORM proves (CONV) for all `q <= sqrt(w+1)` (i.e. `q <= 2^17.00` at `w=2^34`, up to `2^19.50` at `w=2^39`); CS-EXCL proves it above the CS3 floor. **The official `q` sits in neither end, provably.**

## 5. Catches

- **CATCH E-1 (proved).** Given THEOREM CS, `E_floor = {S : N_odd(I_S) > 1}` **exactly** on `strat(S)=0` — CS *derives* the floor inequality for every bad prime. The round-17 decomposition `E = E_strat u E_floor` is a **restatement, not a reduction**; CC-sparsity is precisely as hard as the original open lemma. Machine-confirmed in every cell at `n=32` and `n=64`. THEOREM CS and its prize-row content are untouched.
- **CATCH E-2 (structural).** LEMMA AB shows `E_floor`-sparsity = counting **{0,±1} vectors in a `p`-ary cyclic code of length `n/2`**, while (ES) is counting **{0,1} vectors in a `p`-ary cyclic code of length `n`**. Same shape. **CC-sparsity is not a lemma below (ES) — it is (ES) again, at half length over a ternary alphabet.** Anyone planning to close the residual 28.84% of the crossing bracket via CC-sparsity should read this first.
- **CATCH E-3 (campaign-relevant).** The official row gate `v_2(q-1) >= 41` — *required* by the construction — forces `j_q >= 42`, so SP-COVER needs `w >= 2^42` while the bracket caps at `w = 2^39`. **The row primes are the worst possible primes for the mechanism that works.** CS-EXCL closes `w > 2^37.3131` (independently reproduced); the gap to SP-COVER is `2^4.6869` in `w` and the two exclusions do not meet.
- **My own registered prediction (P2) MISSED, 5 of 6 cells.** I predicted `w_cov` would be sharp; it is sharp only at `(n=32,p=3)`. SP-COVER's hypothesis is sufficient, not necessary — SP-TERNARY explains why. Reported, not buried; the theorem passed all its own checks, my claim about its tightness did not.

## 6. Honest residuals

1. **The middle of the prime range is untouched**, and §7 of PROOFS proves the natural character-sum route cannot reach it.
2. **CC-sparsity is not proved**, and by CATCH E-2 is not easier than the problem it was invoked to solve.
3. **SP-TERNARY has no `n`-uniform form** — a certified per-`(n,p,w)` criterion, not a theorem in `n`.
4. **Unexplained anomaly / lead:** at `n=32, p=5, w=2` a flat model predicts ~110 nonzero ternary codewords; the exact count is **0**.
5. **Even-window conditions are used in none of the proofs**, yet the census shows they matter (`p=7` at `n=32` empties at `w=7` while odd conditions alone never suffice). An even-condition SP-COVER would lower every threshold — the most obvious next step.
6. **`w=3` still has no proof**, as in round 17.
7. **Scale:** exhaustive at `n in {16,32}`; `n=64` at `r'<=4` (all characteristics) and `r'<=6` (four primes); `n=128` at `r'<=4`. Prize-row statements are deductions from theorems proved for all `n`, not extrapolations.
8. **COMPUTE LAW: no breaches.** Every `python3` invocation — including all file patching and peeking — went through `tools/ramguard tiny|local -- python3` with a literal `--`. No `git` write, no file written outside my directory, `crossing_low_w/` never read.
