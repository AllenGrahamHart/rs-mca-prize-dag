# PROOFS — the Ax-Katz / Chevalley-Warning transfer on (ES)

Round 16, 2026-08-06. Everything here is derived AFTER the registrations
in `PREREG.md` (pilot section P0-P5) were appended. All numbers are
produced by `verify_axkatz.py` (32 checks, 0 failures, exit 0); its
output is `verify_axkatz.out`. Run:

```
tools/ramguard local -- python3 notes/pilots_20260806/es_axkatz_transfer/verify_axkatz.py
```

---

## 0. The mandate and the object, quoted verbatim

`notes/pilots_20260804/mun_anticoncentration/FABLE_AUDIT.md:48-54`:

> - **THE FRONTIER**: the exact zero-count statement (0/1 codewords of
>   the [2^41, 2^41-w+1, w] RS codes = periodic only), with four
>   proved structural constraints on any solution, and **AX-KATZ /
>   CHEVALLEY-WARNING as the untested transfer** — p-divisibility is
>   the one classical family sensitive to defining sets. THE NEXT
>   TERMINAL PILOT ATTACKS AX-KATZ TRANSFER FIRST; the Pro brief (when
>   Pro resumes) targets Deligne-Katz/p-adic people, not coding theory.

The object of record, `notes/pilots_20260804/mun_anticoncentration/PREREG.md:52-59`:

> - **(U1)** The crossing count is exactly a constant-weight count in an
>   explicit p-ary cyclic code:
>   ```text
>   W_w = { x in {0,1}^n <= F_p^n : wt(x) = r',  x in C(n, p, Z_w) }
>   ```
>   where `C(n,p,Z_w)` is the cyclic code of length `n` over `F_p` with
>   defining zero set `Z_w` = the p-cyclotomic closure of `{1,...,w-1}`
>   mod `n`; `dim C = n - |Z_w|`, `w-1 <= |Z_w| <= delta (w-1)`.
>   This is LEMMA Y, BANKED round 14 — cited, not claimed.

The characteristic arithmetic, `notes/pilots_20260804/mun_anticoncentration/PREREG.md:41-48`:

> **Characteristic arithmetic (proved, verify3_prizerow.py R3).** `n = 2^41`,
> `n | p^e - 1`, `p^e = q < 2^256` force `delta := ord_n(p) = 2^j` with
> `j <= 2`, so `delta in {1,2,4}` and `p >= 2^39 + 1`. Consequently
> `p > w` on the whole crossing bracket and `p > 2^33 > d` on every band
> depth: **Newton's identities are invertible at every one of the four
> rows**, so a vanishing PREFIX of elementary symmetric functions is
> equivalent to a vanishing prefix of power sums at all four rows.

LEMMA Z's exact structural count,
`notes/pilots_20260804/mun_anticoncentration/PREREG.md:86-89`:

> is `L`-periodic, hence `T = zeta^S` is a union of cosets of `mu_M`.
> Conversely every such union satisfies the conditions.
> Therefore `W_w^struct` is nonempty iff `M | r'`, and then
> `|W_w^struct| = C(n/M, r'/M)`.

The route cut already proved (not re-litigated),
`notes/pilots_20260804/mun_anticoncentration/FABLE_AUDIT.md:22-31`:

> - **THE ROUTE CUT (the round's main theorem):** two cyclic codes with
>   identical (n, k, p), identical weight enumerators, identical
>   MacWilliams/Delsarte/Krawtchouk data, and DIFFERENT 0/1 counts
>   (32 vs 0) — the terminal is NOT a weight-enumerator function; the
>   entire classical toolkit (LP bounds, dual distance, Sidelnikov,
>   BCH/HT/Roos) cannot decide it EVEN IN PRINCIPLE; Weil/C-U vacuous
>   by 13.5-107 bits at every row; the L2 route loses exactly sqrt(p)
>   ~ 2^128 = the whole budget (measured). A Pro brief asking coding
>   theorists would have been the wrong purchase — this pilot likely
>   paid for itself on that alone.

The band budget, `notes/pilots_20260804/mun_anticoncentration/PREREG.md:35`:

> budget `25 |R_d(u,v)| <= 17 n^2`, i.e. `0.68 n^2 = 3.28670...e24 = 2^81.442`.

---

## 1. (A1) THE ALGEBRAIZATION

Two encodings. Both verified exact at small fixtures in `[K1]`.

### 1.1 ALG-I — the indicator reading

Variables `x_1, ..., x_n` (one per position of `mu_n`). Equations:

| family | count | degree |
|---|---|---|
| `x_i^2 - x_i` (the 0/1 locus) | `n` | 2 |
| window forms | `w-1` (over `F_q`) / `|Z_w|` (over `F_p`) | 1 |
| weight form `sum_i x_i - r'` | 1 | 1 |

- **extension reading** (over `F_q = F_{p^delta}`): the window is the
  `w-1` conditions `sum_i x_i zeta^{is} = 0`, `s = 1..w-1`.
- **base-field reading** (over `F_p`): the same code is cut by exactly
  `|Z_w|` independent `F_p`-linear forms, since `dim C = n - |Z_w|`.
  By the quote above `w-1 <= |Z_w| <= delta(w-1)`.

So `N = n` and `sum_j d_j = 2n + (w-1) + 1 = 2n + w` (extension), resp.
`2n + |Z_w| + 1` (base field).

**CATCH-16A (ALG-I is not exact when `p <= n`).** The weight form pins
`wt(x)` only *modulo p*, so the `F_q`-point count of ALG-I is
`sum_{j = r' mod p} |W_w^{(j)}|`, not `|W_w|`. When `delta = 1` we have
`n | p-1`, hence `p >= n+1 > n`, and there is no aliasing (verified in
96 cells, `[K1c]`). But `delta in {2,4}` admits `p < n = 2^41` (for
`delta = 2`, `p mod 2^41 in {2^41-1, 2^40-1, 2^40+1}`, so `p ~ 2^40` is
admissible), and then ALG-I **overcounts**. Explicit witness (`[K1c]`,
`n = 8`, `p = 7`, `delta = ord_8(7) = 2`, `w = 2`, arithmetic in `F_49`):
the weight profile of `{x in {0,1}^8 : sum x_i zeta^i = 0}` is
`[1, 0, 4, 0, 6, 0, 4, 0, 1]`, so at `r' = 1` the true count is `0` while
the ALG-I system has `1` point (weight 8 aliases onto weight 1 mod 7).
This is why ALG-L below is the load-bearing encoding.

### 1.2 ALG-L — the locator reading (exact at every row)

Variables: the `r'` non-leading coefficients of a monic `E` of degree
`r'`, and the `n - r'` non-leading coefficients of a monic `F` of degree
`n - r'`. Equations: the `n` coefficient identities of `E*F = X^n - 1`,
each bilinear, hence of degree 2; plus the window forms (degree 1) on
`E`'s coefficients.

`X^n - 1` is squarefree over `F_q` (`p` odd, `p ∤ n`) and splits, so a
monic `E` of degree `r'` extends to a solution **iff** `E | X^n - 1`, and
then `F` is unique. Hence the `F_q`-points are in bijection with the
size-`r'` subsets `T <= mu_n` meeting the window — **no weight equation
is needed, because `deg E = r'` is built into the variable set**. This is
exact at every row regardless of `p` vs `n`.

Verified in `[K1b]` at 20 fixtures `(n,p) in {(8,17),(8,41),(4,13)}`,
`w in {2,3}`, every feasible `r'`: **0 mismatches** against the banked
round-15 syndrome DP. (Because the fixtures compare the *elementary-
symmetric* prefix `e_1 = ... = e_{w-1} = 0` against the *power-sum*
prefix, this also re-verifies Newton invertibility at every fixture.)

So `N = n` and `sum_j d_j = 2n + (w-1)`. For a **prefix** window the
`w-1` forced-zero coefficients can be eliminated outright, leaving
`N = n - (w-1)` variables and `sum_j d_j = 2n` with **no linear
equations at all** — the best reading available anywhere, used below.

### 1.3 The band reading

At the band rows the window is "the top `d` coefficients of `u E_T` and
of `v E_T` vanish" — `2d` `F_q`-linear forms on `E`'s coefficients
(linear, since reduction mod `X^n - 1` and multiplication by a fixed `u`
are linear). ALG-L therefore applies verbatim with `nforms = 2d`.

---

## 2. (A2) THE EXPONENT, EXACTLY

### 2.1 The theorems, stated before plugging in (PREREG P0)

- **Ax-Katz** (Katz, *On a theorem of Ax*, Amer. J. Math. 93 (1971)):
  `|V| = 0 mod q^mu` with `mu = ceil((N - sum_j d_j)/max_j d_j)`.
- **Chevalley-Warning**: `sum_j d_j < N  =>  p | |V|`.
- **Warning's second theorem**: `sum_j d_j < N` and `V != {}`
  `=>  |V| >= q^{N - sum_j d_j}`.

Both the exponent formula and Warning-2 are **validated by brute force**
in `[K0]`: 144 random systems over `F_p`, `p in {2,3,5,7}`, `N <= 6`,
degrees `1..3`, **all 144 with `mu >= 1`** — 0 Ax-Katz violations, 0
Warning-2 violations.

### 2.2 The exponents at the four rows of record

Closed forms (verified against the computed values in `[K2]`):

```
ALG-I extension :  mu = -floor((n + nforms + 1)/2)
ALG-L extension :  mu = -floor((n + nforms)/2)
ALG-L prefix    :  mu = -floor((n + nforms)/2)     [N = n - nforms]
```

with `nforms = w-1` (crossing) resp. `2d` (band). At the crossing rows
the ALG-I extension exponent is exactly `-(n+w)/2`.

| row | mu (ALG-I ext) | mu (ALG-L ext) | mu (ALG-L pfx) |
|---|---|---|---|
| crossing w=2^34 | -1108101562368 | -1108101562367 | -1108101562367 |
| crossing w=2^35 | -1116691496960 | -1116691496959 | -1116691496959 |
| crossing w=2^36 | -1133871366144 | -1133871366143 | -1133871366143 |
| crossing w=2^37 | -1168231104512 | -1168231104511 | -1168231104511 |
| crossing w=2^38 | -1236950581248 | -1236950581247 | -1236950581247 |
| crossing w=2^39 | -1374389534720 | -1374389534719 | -1374389534719 |
| band 1/4 d=2^32+1 | -1103806595073 | -1103806595073 | -1103806595073 |
| band 1/4 d=2^33-1 | -1108101562367 | -1108101562367 | -1108101562367 |
| band 1/8 d=2^32+1 | -1103806595073 | -1103806595073 | -1103806595073 |
| band 1/8 d=2^33-1 | -1108101562367 | -1108101562367 | -1108101562367 |
| band 1/16 d=2^31+1 | -1101659111425 | -1101659111425 | -1101659111425 |
| band 1/16 d=2^32-1 | -1103806595071 | -1103806595071 | -1103806595071 |

**Every exponent is negative, in every reading, at every row.**

### 2.3 The Chevalley-Warning baseline and the exact shortfall

CW bites iff `sum_j d_j < N`. Define, in the best reading (ALG-L prefix):

```
DEFICIT := sum d_j - N + 1        (degree that must be REMOVED for CW to bite)
GAP1    := sum d_j - N + max d_j  (removal needed for mu >= 1)
```

| row | CW deficit | log2 | GAP1 |
|---|---|---|---|
| crossing w=2^34 | 2216203124736 | 41.01123 | 2216203124737 |
| crossing w=2^35 | 2233382993920 | 41.02237 | 2233382993921 |
| crossing w=2^36 | 2267742732288 | 41.04439 | 2267742732289 |
| crossing w=2^37 | 2336462209024 | 41.08746 | 2336462209025 |
| crossing w=2^38 | 2473901162496 | 41.16993 | 2473901162497 |
| crossing w=2^39 | 2748779069440 | 41.32193 | 2748779069441 |
| band 1/4 d=2^32+1 | 2207613190147 | 41.00562 | 2207613190148 |
| band 1/4 d=2^33-1 | 2216203124735 | 41.01123 | 2216203124736 |
| band 1/8 d=2^32+1 | 2207613190147 | 41.00562 | 2207613190148 |
| band 1/8 d=2^33-1 | 2216203124735 | 41.01123 | 2216203124736 |
| band 1/16 d=2^31+1 | 2203318222851 | 41.00282 | 2203318222852 |
| band 1/16 d=2^32-1 | 2207613190143 | 41.00562 | 2207613190144 |

**The shortfall is `2^41.003` to `2^41.322` degree-units at every row.**
This is not a near miss: `sum d_j / N > 2` where Ax-Katz needs `< 1`.
The deficit is of the order of `n` itself, because the encoding pays
`2n` in degree for a cube of `n` variables.

### 2.4 The base-field reading and the only defining-set dependence there is

`mu_p = -floor((n + |Z_w| + 1)/2)` genuinely depends on the defining set
— but only through `|Z_w|`, and **monotonically downward**: at
`w = 2^34`, `mu_p = -1108101562368` at `|Z| = w-1` (delta = 1) and
`-1133871366142` at `|Z| = 4(w-1)` (delta = 4). Both ends vacuous; the
only sensitivity that exists points the wrong way.

### 2.5 The sharpest refinements give nothing extra

**Moreno-Moreno** replaces `d_j` by the p-weight degree. Every degree in
play is 1 or 2 and `p >= 2^39 + 1`, so every p-adic digit sum equals the
degree itself (verified `[K3d]`): MM gives **exactly the same mu**.
**Adolphson-Sperber / Wan** sharpen the exponent via the Newton
polyhedron but keep the conclusion's shape `p^mu | count`; §3.2 kills
that shape outright.

---

## 3. (A3) THE DECISION

Three independent mechanisms, each sufficient on its own.

### 3.1 Mechanism 1 — VACUOUS (§2.3)

`mu < 0` at every row in every reading, short by `2^41.0`-`2^41.3`
degree-units. For comparison, the banked round-15 Weil/C-U vacuity at
the same rows is "13.5-107 bits"
(`FABLE_AUDIT.md:27-28`). Ax-Katz is worse.

### 3.2 Mechanism 2 — LOGICALLY MIS-SHAPED (the p-adic unit obstruction)

**THEOREM AK-UNIT.** At every crossing row of record the (ES) target
`|W_w^struct| = C(L, r'/M)` (with `M = w = 2^v`, `L = n/M = 2^{41-v}`)
is a **p-adic unit** for every admissible `p`.

*Proof.* `w = 2^v` with `v in [34,39]`, so `M = w` and `L = 2^{41-v} <= 2^7
= 128`. Every prime `pi` dividing `C(a,b)` satisfies `pi <= a`: for
`pi > a`, `v_pi(a!) = 0`, hence
`v_pi(C(a,b)) = v_pi(a!) - v_pi(b!) - v_pi((a-b)!) = 0`. So every prime
factor of `C(L, r'/M)` is `<= L <= 128`. But `p >= 2^39 + 1`
(`PREREG.md:43`). Hence `p ∤ |W_w^struct|`. No case split on `delta`. ∎

Verified `[K3b]`: the six crossing targets factor completely over primes
`<= L`, largest prime factors `127, 61, 31, 13, 7, 2` respectively.

| row | L | \|W^struct\| | max prime | log2 |
|---|---|---|---|---|
| crossing w=2^34 | 128 | 23582666872052266206656578733667004800 | 127 | 124.1491 |
| crossing w=2^35 | 64 | 1777090076065542336 | 61 | 60.6242 |
| crossing w=2^36 | 32 | 565722720 | 31 | 29.0755 |
| crossing w=2^37 | 16 | 11440 | 13 | 13.4818 |
| crossing w=2^38 | 8 | 56 | 7 | 5.8074 |
| crossing w=2^39 | 4 | 4 | 2 | 2.0000 |

**COROLLARY AK-ACCIDENT (unconditional).** Write
`|W_w| = |W_w^struct| + |W_w^acc|`. If some theorem proves `p | |W_w|`
at a crossing row, then `|W_w^acc| ≡ -|W_w^struct| ≢ 0 (mod p)`, so
`|W_w^acc| > 0`: **accidental (non-periodic) members EXIST.** This needs
no assumption beyond AK-UNIT, which is unconditional.

So in this problem p-divisibility is an **accident-EXISTENCE** theorem.
It is the negation of what (ES) asserts. A non-vacuous Ax-Katz here
would *refute* (ES), never prove it. The whole family
(Chevalley-Warning, Ax, Katz, Ax-Katz, Moreno-Moreno, Adolphson-Sperber,
Wan, McEliece) shares this conclusion shape and is cut in one stroke.

### 3.3 Mechanism 3 — STRUCTURALLY IMPOSSIBLE (the Warning obstruction)

**THEOREM AK-WARN.** Let `f_1..f_m in F_q[x_1..x_N]` be **any** system
whose `F_q`-point count equals `|W_w|` exactly. If `0 < |W_w| < q` then
`N - sum_j d_j <= 0`, hence `mu <= 0`.

*Proof.* If `N - sum_j d_j >= 1` then Warning-2 applies, and `V != {}`
(since `|W_w| > 0`), so `|W_w| >= q^{N - sum d_j} >= q`, contradicting
`|W_w| < q`. Therefore `N - sum d_j <= 0` and
`mu = ceil((N - sum d_j)/max d_j) <= 0`. ∎

Under (ES), `|W_w| = C(L, r'/M) <= C(128,63) = 2^124.1491 < 2^255.900 < q`
at every crossing row (`[K3c]`), and `|W_w| > 0` by LEMMA Z. So:

> **Under (ES), NO exact algebraization of the crossing count — not
> ALG-I, not ALG-L, not any system anyone will ever write down — can
> have a positive Ax-Katz exponent.**

The vacuity measured in §2.3 is therefore not an artefact of our
encoding; it is forced.

**The fibered escape hatch, named and closed.** Suppose an encoding has
`|V| = c * |W_w|` for a known `c` (auxiliary variables, ordered tuples).
Then `q^mu | |V|` is consistent with `mu >= 1`. But by AK-UNIT
`gcd(|W_w|, p) = 1` under (ES), so `q^mu | c`: **all** the divisibility
sits in the fibre, where it says nothing about `|W_w|`. The hatch is
information-free.

### 3.4 Mechanism 4 — INSENSITIVE (the adversarial check)

The audit's hope was that "p-divisibility is the one classical family
sensitive to defining sets" (`FABLE_AUDIT.md:51-52`). Tested directly on
the round-15 separating witness (`n=16, p=17, w=3`, defining sets
`{a, a+1}`), replayed against the banked `verify_transfercut.py`:

| r' | {1,2} | {2,3} | {3,4} | {4,5} | {5,6} | {6,7} | {7,8} |
|---|---|---|---|---|---|---|---|
| 7 | 32 | 32 | 0 | 0 | 16 | 16 | 0 |
| 8 | 54 | 54 | 98 | 98 | 22 | 54 | 276 |

(The `r'=8` row reproduces `verify_transfercut.py`'s `[T4]` exactly; the
`r'=7` row contains the audit's cited "32 vs 0" pair.)

Across this entire family:
- the 0/1 counts **SEPARATE**: `{0, 16, 22, 32, 54, 98, 276}`;
- `mu` is **CONSTANT** at `-9` in both readings;
- `|Z_w|` is **CONSTANT** at `2` (`delta = ord_16(17) = 1`);
- the McEliece exponent `ell - 1` is **CONSTANT** at `0`.

So the Ax-Katz exponent is a function of `(n, #forms, degrees)` only and
is constant on precisely the family that separates the terminal. The
hoped-for defining-set sensitivity is **not realised** in this reading.

Further, **every nonzero count in the family is coprime to `p = 17`**
(`16, 22, 32, 54, 98, 276`) — a direct empirical refutation of any
nontrivial p-divisibility, exactly as registered in P5a.

**PROPOSITION McE-VAC.** McEliece's theorem is vacuous at every row and
for every shifted defining set. *Proof.* McEliece's `ell` is the least
number of nonzeros of the code whose product is 1. The defining set is
`Z_w`, the p-cyclotomic closure of `{1,...,w-1}`; `0 ∉ Z_w`, since
`0 * p^j = 0` and `0 ∉ {1,...,w-1}`. Hence `zeta^0 = 1` is a **nonzero**
of the code and `ell = 1`, giving `p^{ell-1} = p^0 = 1`. Any shift
`{a,...,a+w-2}` with `a >= 1` likewise omits `0`. ∎ (Verified on 6
fixtures, `[K4b]`.) The one classical p-divisibility theorem that *is*
defining-set-sensitive is sensitive through a quantity pinned at its
trivial value on this whole family.

### 3.5 The pre-registered adversarial obligation, discharged

PREREG section 3 clause 2 requires that any claim of (i) survive adding
one accident pair to the periodic count. Run at `n=16, p=17, w=3, r'=8`
(`[K5b]`): `|W_w| = 54`, `|W^struct| = C(4,2) = 6`, so 48 accidental
members; `mu = -9`. The divisibility statement `q^mu | ·` is satisfied
**identically** by `|W^struct|`, by `|W^struct| + 1`, and by the true
count — because `q^0 = 1` divides every integer. It cannot separate
them. By the pre-registered rule this alone forces verdict (iii) over
(i).

### 3.6 VERDICT

> **TRANSFER DEAD.** Not by one mechanism but by four, of which the last
> three are method-level and not repairable by sharpening:
> **(ii) DEAD-VACUOUS** — `mu < 0` at all four rows in all readings,
> short by `2^41.003`-`2^41.322` degree-units (§2.3);
> **(ii+) DEAD-BY-SHAPE** — the target is a p-adic unit, so a
> non-vacuous divisibility would *refute* (ES) rather than prove it, and
> unconditionally would prove accidents EXIST (§3.2);
> **(ii++) DEAD-FOR-ALL-ENCODINGS** — Warning-2 forbids `mu >= 1` for
> any exact algebraization whatsoever, and the fibered hatch is
> information-free (§3.3);
> **(iii) DEAD-INSENSITIVE** — `mu`, `|Z_w|` and McEliece's `ell` are all
> constant on the very family whose 0/1 counts separate (§3.4).

The remaining obligation demanded of verdict (i) is void: there is no
named lemma to state, because the route is closed rather than blocked.

---

## 4. (A4) CALIBRATION

`[K5]`, 34 fixtures over `(n,p) in {(8,17),(8,41),(16,17),(16,97),
(4,13),(16,113)}`, `w in {2,3}`, `r' in {n/4, n/2-1, n/2}`, exact counts
from the banked machinery (which `[K1a]` re-verified against full cube
brute force in 64 cells):

- The Ax-Katz prediction is **never violated** — and never informative:
  at every fixture `mu <= 0`, and `q^0 | N` is true of every integer. It
  is true and **empty**.
- `p | |W_w|` in 11 of 34 fixtures — but **all 11 are the trivial case
  `|W_w| = 0`**. Among the 23 fixtures with a nonzero count, `p` divides
  it in **0**. There is no p-divisibility here to be found, vacuous
  exponent or not.

**Honest scope split (PREREG section 3, clause 3).** The toys sit far
*below* balance (`C(16,8)/p^{|Z|} = 44.5` at `n=16, p=17`), so accidents
abound there, unlike the prize rows. The toys therefore kill the
**row-level** divisibility claim only; the **method** is killed by
§3.2/§3.3, which are proofs, not measurements.

**Regime cross-check.** My `log2 C(128,63) = 124.1491` matches the banked
`verify_rows.py` `[B3]` value `2^124.15`, and my `delta = 1` balance
crossover `w* = 2^33.0` matches its `[B1/B2]` row `log2 q_char = 255.9 ->
log2 w* = 33.0005`. So at the recorded razor row the whole crossing
bracket is **sub-balance**, consistent with the adopted (ES) statement
"sub-balance codimension => no accidental members"
(`FABLE_AUDIT.md:15`).

---

## 5. (P3) THE ONE LIVE SHAPE, TESTED AND CLOSED

If `q^mu | |W|` with `mu >= 1` **and** independently `|W| < q^mu`, then
`|W| = 0`. This is the only shape in which a p-divisibility theorem can
*prove* a suppression statement, and it is the relevant one at the band
rows, because:

**`[K3a]`: at all three band rows the structural family is EMPTY.**
`M = 2^33` (band 1/4, 1/8) resp. `2^32` (band 1/16), and
`r' = (n-k) - d` with `2^33 | (n-k)` resp. `2^32 | (n-k)`, while
`d in [2^32+1, 2^33-1]` resp. `[2^31+1, 2^32-1]` is never `0 mod M`. So
`M ∤ r'` and `|W^struct| = 0`: **the band target is a genuine vanishing
statement**, to which AK-UNIT and AK-WARN do *not* apply.

Both ingredients nevertheless fail:

| row | log2 C(n,r') | mu needed | mu available |
|---|---|---|---|
| crossing w=2^34 | 2.198636e12 | 8591777919 | -1108101562367 |
| band 1/4 d=2^32+1 | 1.790795e12 | 6998025040 | -1103806595073 |
| band 1/8 d=2^32+1 | 1.207313e12 | 4717910394 | -1103806595073 |
| band 1/16 d=2^31+1 | 7.50073e11 | 2931117587 | -1101659111425 |

- ingredient 1 fails by `~2^41` degree-units;
- ingredient 2 needs `mu ~ 8.6e9` (the only unconditional upper bound is
  `U = C(n,r')`, `log2 U ~ 2.2e12`, against `log2 q > 255.9`) while the
  available `mu` is `~ -1.1e12`.

**CATCH-16B (worth banking).** With **only** `mu >= 1` plus the band's
own budget `0.68 n^2 = 2^81.442` as an a priori bound, the route *would*
close, because `2^81.442 < q^1` (`q > 2^255.900`). So the entire gap is
in ingredient 1. **The band rows are the only place in the whole
terminal where a p-divisibility theorem could ever have been decisive,
and there it needs only `mu >= 1`** — which is short by `2^41`.

---

## 6. (A5) WHAT A DECISIVE METHOD MUST SEE

Accumulated exclusions, now four deep:

1. **Not the weight enumerator** (round-15 route cut): identical
   `(n,k,p)`, identical MacWilliams/Delsarte/Krawtchouk data, different
   0/1 counts.
2. **Not the designed distance or `|Z_w|`**: constant at `2` and `-9`
   across the separating family (§3.4) — this also cuts BCH/HT/Roos and
   van Lint-Wilson, as round-15 noted.
3. **Not p-adic / not a congruence**: the target is a **p-adic unit**
   (AK-UNIT). Any congruence method's conclusion has the wrong shape,
   *however sharp its exponent*. This is new and is the strongest of the
   four, because it is indifferent to the method's strength.
4. **Not archimedean-lossy**: Weil/C-U vacuous by 13.5-107 bits, L2 loses
   `2^128`, and the required suppression at the bracket bottom is from
   `log2 C(n,r') ~ 2.2e12` down to `~2^124` — a factor no inequality
   with a `sqrt` loss can supply.

So a decisive method must be an **exact structural (rigidity)** theorem
that sees the defining set as a *subset of `Z/n`*, at a resolution no
coarser than its **divisor profile**
`D(Z) = {n/gcd(n,s) : s in Z}`. That is precisely the invariant LEMMA Z
turns on — `verify_lemmaz.py:136-138`:

```python
    print("  D(n,w) = {n/gcd(n,s)} is exactly the TOP A+1 divisors of n, so")
    print("  the whole condition set collapses to ONE divisibility by")
    print("  (X^n-1)/(X^L-1) = 1 + X^L + ... + X^{n-L}.")
```

and it is exactly what changes under the shift `{1,..,w-1} -> {a,..,a+w-2}`
that separates the counts while leaving every classical invariant fixed.

**The precise ask for the Pro brief (and the next pilot).** LEMMA Z is a
*characteristic-zero* rigidity theorem: over `C`, the interval defining
set forces the solution to be `L`-periodic. In characteristic `p` the
`F_p`-solution space is strictly larger (`dim = n - |Z_w|`) and 0/1
points that do not lift to char-0 solutions ("accidents") are a priori
possible. The open problem is therefore:

> **a characteristic-`p` analogue of vanishing-sums-of-roots-of-unity
> rigidity (Lam-Leung / Conway-Jones) — controlling 0/1 vectors of
> prescribed weight in the `F_p`-reduction of a cyclotomically rigid
> char-0 system, in the SUB-BALANCE regime `C(n,r') < p^{|Z_w|}`.**

That is a `p`-adic/`ell`-adic *geometry* question (Deligne-Katz
equidistribution for the family over the window parameter `a`), not a
divisibility question — which is exactly the audience the round-15 audit
already identified (`FABLE_AUDIT.md:53-54`: "the Pro brief (when Pro
resumes) targets Deligne-Katz/p-adic people, not coding theory"). This
pilot narrows that brief: **ask for rigidity/equidistribution, and state
up front that p-divisibility is excluded by AK-UNIT**, so the
correspondents do not spend their first exchange proposing
Chevalley-Warning.

---

## 7. Residuals (honest)

- **AK-WARN and the "no encoding can work" statement are conditional on
  (ES)** at the crossing rows (they use `|W_w| < q`). Unconditionally we
  know only `|W_w| >= |W^struct| > 0` (LEMMA Z). AK-UNIT and
  COROLLARY AK-ACCIDENT are unconditional.
- **The band rows are not covered by AK-UNIT/AK-WARN**, because their
  structural count is `0` and `0` is divisible by everything. They are
  closed by vacuity (§2.3) and by the ingredient-2 gap (§5) only. If a
  future method ever supplies `mu >= 1` at a band row, CATCH-16B says
  the vanishing follows immediately — that is the one live seam and it
  should stay on the board.
- **`|Z_w|` is not pinned** at the prize rows (it depends on `p mod n`);
  §2.4 brackets it by `[w-1, delta(w-1)]` and both ends are vacuous, so
  nothing turns on the exact value.
- **The `prod T = gamma` clause** of MC-1 (dropped in the round-15 object
  of record) is not folded in. In ALG-L it is one more degree-1 form on
  `E`'s constant coefficient, shifting `mu` by at most 1 — it cannot
  change any verdict here. Reported separately per P5c.
- **`log2 C(n,r')` at `n = 2^41` is computed by `lgamma`** (float);
  absolute error `<< 1` bit on a `2.2e12`-bit quantity. The round-15
  `verify_rows.py` `[S]` calibration measured this same routine's worst
  error at `2.7e-12` bit.
- **Adolphson-Sperber / Wan exponents are not computed numerically.**
  They are excluded by conclusion-shape (§3.2), not by arithmetic. If
  someone wants the numbers, the Newton-polyhedron computation for the
  ALG-L system is a separate (and by §3.2 pointless) exercise.
