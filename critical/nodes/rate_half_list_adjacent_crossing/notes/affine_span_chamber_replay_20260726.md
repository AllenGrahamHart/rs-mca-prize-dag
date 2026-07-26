# H1/S3 replay: the GF list compilers against the thirteen chambers (2026-07-26)

**Verdict: the affine-span and rank-flat compilers kill NONE of the thirteen
edge-degree chambers. The Convergence Ledger r1 S3 promotion test does not fire;
H1 stays ev-wired.** One positive by-product (the s=1 exclusion) and one banked
artifact (the F_17 witness) are recorded below.

Artifact: `verify_affine_span_chamber_replay.py` (stdlib, exact integers, 8
mutation controls). Upstream read-only at `origin/main = b13de811`.

## 0. Citation repair (forced correction)

The ledger's H1 entry cites the four compilers as `:498 / :439 / :421 / :583`
without naming a file, and the fact-check recorded them as "all verified at pin".
They are **not in `proximity_prize_results_v4.tex`** — none of the four labels
exists in that file. Resolved:

| label | actual location at b13de811 | ledger pin |
|---|---|---|
| `thm:affine-span-list` | `experimental/grande_finale.tex:498` | :498 correct (file unnamed) |
| `thm:fixed-union-list-johnson` | `experimental/grande_finale.tex:439` | :439 correct (file unnamed) |
| `thm:rank-flat-list` | `experimental/grande_finale.tex:583` | :583 correct (file unnamed) |
| `thm:single-mds-circuit-ray` | `RS_MCA_Paving_v9.2.tex:1514` | **:421 wrong** |

## 1. What the compilers say at the official row

`n = 2^41`, `K = 2^40`, `R = n-K = 2^40`, `d = R+1`. Caps
`floor( C(R+s,s) / C(w+s,s) )`, `w = m-K`:

| s | m = 3n/4 | m = 3n/4 − 1 |
|---|---|---|
| 0 | 1 | 1 |
| 1 | 1 | **2** |
| 2 | 3 | **4** |
| 3 | 7 | **8** |

The live question is four codewords at `m = 3n/4 − 1` (`B* = 3` needs
`L_1(3n/4−1) >= 4`). So:

- **s = 1 (collinear): excluded** — cap 2 < 3.
- **s = 2 (coplanar): exactly at the cap** — 4 allowed, zero slack.
- **s = 3: slack 4** — cap 8 against 4.

## 2. The s=1 exclusion, proved directly (independent of the compiler)

Three collinear list members `c_0`, `c_0 + L_1 v`, `c_0 + L_2 v` share ONE
support `S = supp(v)`, because all three pairwise differences are nonzero scalar
multiples of the same `v`. On `S` the three values are pairwise distinct, so at
most one agrees with `u` per position; off `S` all three coincide. Hence

```text
3m <= 3(n - wt(v)) + wt(v) = 3n - 2 wt(v)   =>   wt(v) <= 3(n-m)/2,
```

while MDS gives `wt(v) >= n-K+1`. Contradiction iff `n-K+1 > floor(3(n-m)/2)`.

At the official row this fires with enormous room: it holds for every
`m >= 1,466,015,503,701 = 3n/4 − 183,251,937,963`, i.e. **1.83·10^11 agreement
steps below the razor**, and it also fires on the F_17 row. At `m = 3n/4 − 1` it
reproduces the compiler's s=1 cap exactly. So this bite is real and robust — but
it constrains the *codeword affine span*, not the chambers (see §4).

## 3. Why s=2 does NOT get killed (a correction to a tempting shortcut)

Pinning the generalized Hamming weights at their MDS floor `d_j = R+j` makes
`thm:rank-flat-list` look like it forces `b = 0` exactly at s=2 — which would be
a sharp rigidity statement. **That is an artifact of the pinning.** The theorem
uses the *actual* weights, and the cap is not monotone in `d_2`: scanning the
admissible region (most permissive `d_1 = R+1`),

| `d_2` | `z = n − d_2` | largest `b` with cap ≥ 4 |
|---|---|---|
| `R+2` (minimum support) | 1099511627774 | **0** |
| `R+2 + 10^9` | 1098511627774 | 227167 |
| `3n/4` | 549755813888 | 44606543570 |
| `7n/8` | 274877906944 | 84631211246 |
| `n − 10^6` | 1000000 | 1000000 (capped by `z`, not the compiler) |
| `n` | 0 | 0 (capped by `z`) |

So the `b = 0` rigidity holds **only at minimum support**; the constraint relaxes
as `d_2` grows and is vacuous once `z` is small. At s=3 the budget is
`b <= 142,893,108,331 ≈ 0.2599·2^39`. No chamber is excluded on these grounds.

## 4. The structural blocker (what S3 actually needs)

The thirteen chambers are **edge-degree patterns of the locator pencil** — the
`A_i` block locators, their edge factors `b_ij`, the Plücker gate
`b_01b_23 − b_02b_13 + b_03b_12 = 0`, and the graph types on four vertices
(K_4, K_4−e, cycles, paths, pendant, triangle-plus-singleton). The compilers
constrain a **different object**: the affine span of the four codewords in
`RS[F,D,K]`.

Nothing in the node currently maps one to the other. The ledger's promotion test
— *"ev→req when chamber coordinates are bound to affine spans"* — is therefore
exactly right about what is missing, and **the binding does not exist**, so the
test cannot fire. Concretely, what is owed is a lemma computing the affine rank
`s` (and ideally `d_1, d_2, b`) of the four codewords *from* a chamber's edge
degrees. Until then H1 is evidence, not a requirement edge.

## 5. The F_17 witness, banked as exact integers

`statement.md` cites "an exact `RS[F_17,F_17^*,8]` witness with four codewords at
agreement `11 = 3n/4−1`, realizing the path-plus-singleton chamber at `d=4`" but
never banked its integers. Reconstructed here (12 such triples exist in the
normalized branch `f_0 = 0`, `|Z| = 11`, `|R_i| = 7`; the first is pinned):

```text
D = F_17^* = {1..16},  n = 16,  K = 8,  m = 11
u  = (0,0,0,0,0,0,0,0,0,0,0, 6,15,12, 7,15)
f0 = (0,0,0,0,0, 0, 0,0,0, 0, 0, 0, 0, 0, 0, 0)
f1 = (0,0,0,0,0,10, 7,0,7, 3, 0,12,15,12, 7,15)
f2 = (0,0,0,2,13, 0, 0,0,1, 0,15, 6, 4,12, 7,15)
f3 = (0,4,6,0,0, 0, 0,0,0,10, 6, 6,15,13, 7,15)
```

Measured: all four are codewords (interpolant degree < 8), each at agreement
exactly 11; **every one of the six pairwise agreements is exactly `K−1 = 7`**, so
all six differences are minimum-weight codewords — a maximally tight
configuration. Affine rank `s = 3`; generalized weights `d = (9, 12, 14)` (only
`d_1` sits at the MDS floor, `d_2` and `d_3` are 2 and 3 above it); common-zero
set `z = 2`, `g = 2`, so `b = 0`.

Both compilers give cap **8** against the actual list size **4** — slack 4. So on
the one concrete four-codeword configuration on record, neither compiler is
within a factor of two of tight. Consistent with §1–§3, and it corroborates §2:
**no triple among the four is collinear.**

## 6. Non-claims

- Proves nothing about `L_1(3n/4−1)` at the official row; constructs no official
  counterexample. The F_17 witness is a power-of-two-domain route fence, exactly
  as `statement.md` already says — not a transport to `d = 2^39`.
- `thm:affine-span-list` and `thm:rank-flat-list` are Przemek's theorems; this
  note consumes them and proves neither.
- Kills no chamber, promotes no ev edge, changes no status.
