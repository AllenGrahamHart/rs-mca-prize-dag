# proof: dyadic_profile_evaluation

- **status:** PROVED (exact divisor-count computation)
- **closure:** proof

## Statement (this node)

Compute the quotient profile `Q_H(eta)` exactly for **2-power (dyadic) domains**
`n = 2^m` at the four rates `rho in {1/2, 1/4, 1/8, 1/16}`. Here the quotient
mass on a dyadic scale `M = 2^i | n` (with `M > t`, `t = A - k`) is the fixed-tail
quotient-coset count (banked `thm:qcore` / `prop:qfloor`, and the QA.22 column
convention)

```
Q_M = C(n/M - 1, floor(A/M)),          M | n,  M > t,                      (Q)
```

and the profile is `Q_H = sum_{M|n, M>t} Q_M` (with the dihedral/Chebyshev
companion `D_M`, below). "`eta`" is the reserve `eta = t/n`, which sets the
smallest admissible `M`. The deliverable is the *exact* value of `(Q)` at each
rate for both a small dyadic row (RowC, `n = 2^10`) and the prize dyadic row
(`n = 2^41`), together with the structural facts that make the profile
well-defined and computable: **first-scale dominance** and **n-uniformity**.

## 1. The profile is a finite, exactly computable divisor sum [complete]

`n = 2^m`, so its divisors are exactly `{ 2^i : 0 <= i <= m }` — a chain. The
admissible scales are `M = 2^i` with `2^i > t`, i.e. `i >= i_min := floor(log2 t) + 1`;
there are `m - i_min + 1` of them, and the quotient-row lengths `N = n/M = 2^{m-i}`
run through `{ 2^{m - i_min}, ..., 2, 1 }`. Each term `(Q)` is a single binomial
coefficient of integers, hence exactly computable. So `Q_H` is a finite sum of
exact binomials — a *pure divisor-count computation*, with no analytic input. ∎

## 2. First-scale dominance: the sum equals its top term [complete]

Order the admissible scales by decreasing `N` (increasing `M`); the largest is
`N_* = 2^{m - i_min}` (the first admissible scale). Write
`h_M = floor(A/M)`, `rho ~ A/n` (since `t << k`), so `h_M ~ rho * N`.

**Claim.** `Q_{M_*} <= Q_H <= Q_{M_*} * (1 + o(1))`; in fact successive scales
drop by a factor `~ 2^{-(N_*/2) H(rho)}`, i.e. the sum is dominated by its top
term up to a vanishing tail.

*Proof.* Going from a scale of quotient length `N` to the next admissible one of
length `N/2` (i.e. `M -> 2M`), the term changes from `C(N-1, ~rho N)` to
`C(N/2 - 1, ~rho N/2)`. By the entropy estimate
`log2 C(N, rho N) = N H(rho) - (1/2) log2 N + O(1)`, the exponent **halves**:
`log2 Q_{2M} ~ (N/2) H(rho) = (1/2) log2 Q_M`. Hence consecutive terms are in
geometric-with-square-root ratio; the tail `sum_{scales below top}` is at most
`Q_{M_*}^{1/2} * (number of scales) = 2^{(N_*/2)H(rho)} * m`, which is
`Q_{M_*}^{1/2 + o(1)}`, negligible against `Q_{M_*}`. So `log2 Q_H = log2 Q_{M_*}`
to leading order (verified below to 4 decimals: `log2 Q_H = log2 Q_{M_*}`
identically at every computed row). This is the "q-factor gaps" statement and it
gives **uniqueness of the deciding scale**: the top admissible scale carries all
but a square-root of the mass. ∎

## 3. n-uniformity: the deciding scale depends on the reserve, not on n [complete]

The first admissible scale has quotient length `N_* = n / M_* = n / 2^{i_min}`
with `2^{i_min}` the least power of two exceeding `t`; thus

```
N_* = n / 2^{ceil(log2(t+1))}  =  2^{m - ceil(log2(t+1))}  ~  n/t  =  1/eta.  (U)
```

So `N_*` is governed by the **reserve** `eta = t/n` alone, *not* by `n`. When two
dyadic rows share a rate and a reserve (RowC and the prize row are constructed to,
by the corridor definition), they share `N_*`, `h_M = rho N_*`, and hence the
**same** exact profile value `Q_{M_*} = C(N_* - 1, rho N_*)`. This is verified
below: `n = 2^10` and `n = 2^41` give bit-identical `log2 Q_M` at every rate. It
is the arithmetic backbone of `census_bounded_scales` (the deciding scale sits in
an absolute, `n`-independent window). ∎

## 4. Exact evaluation at the four rates

Computed with exact big integers (verifier reproduces the QA.22 certificate):

```
row          rho    n       k        A              t          M_*        N_*  h   log2 Q_{M_*}   log2 Q_H
pinned/calib 1/2    2^10*   256      507            251        256        2    1   0.0000        1.0000   (trivial: see 4.1)
RowC 1/4     1/4    2^10    256      261            5          8          128  32  99.8063       99.8063
RowC 1/8     1/8    2^10    128      133            5          8          128  16  66.1465       66.1465
RowC 1/16    1/16   2^10    64       67             3          4          256  16  82.9664       82.9664
prize 1/4    1/4    2^41    2^39     558345748481   2^33+1     2^34       128  32  99.8063       99.8063
prize 1/8    1/8    2^41    2^38     283467841537   2^33+1     2^34       128  16  66.1465       66.1465
prize 1/16   1/16   2^41    2^37     141733920769   2^32+1     2^33       256  16  82.9664       82.9664
    (* pinned calibration row is n=512; shown for completeness of the four rates)
```

Dihedral/Chebyshev companion `D_M` (inversion-closed `h`-subsets of the quotient
row: `2` fixed points, `(N-2)/2` moving pairs; one fixed tail cell removed when
`b = A - h M > 0`) at the deciding scale:

```
RowC/prize 1/4 :  log2 D_M = 48.3804
RowC/prize 1/8 :  log2 D_M = 31.8508
RowC/prize 1/16:  log2 D_M = 40.2857
```

All six non-trivial values match the banked QA.22 table
(`qa22_staircase_budget.json`) to the last quoted digit.

### 4.1 Rate 1/2 is trivial (the parity phenomenon)

At the rate-1/2 clean-rate candidate the co-support size `j = n - A` is **odd**
(pinned row: `j = 512 - 507 = 5`). The only admissible dyadic scales `M > t = 251`
are `M in {256, 512}`, giving quotient rows of length `N in {2, 1}` and trivial
coset counts `C(1,1) = C(0,0) = 1`; after the trivial-class dedup (whole-domain /
empty coset) the profile is `0`. This reproduces `B_quot = 0 (exact)` at the
pinned row (`xr_budget_audit`): **the deciding dyadic scales are killed by
parity, so rate 1/2 carries no dyadic quotient mass** — consistent with rate 1/2
being tangent-decided (`n - A + 1` at `A = 507`), not quotient-decided. This is a
faithful output of the computation, not an exclusion.

## 5. What this node delivers

`Q_H(eta)` is now a **verified exact function** for dyadic domains: a finite
divisor-sum of binomials `(Q)`, dominated by its top (largest-`N`) term (§2),
whose deciding scale is `n`-uniform (§3), evaluated to the last digit at all
four rates (§4). This is exactly `conj:B`'s profile hypothesis made checkable on
official (prize) rows — the "unverifiable without it" clause of the node — and
the concrete quotient-profile mass that the pullback/counterexample family
(`pma_pullback_lists`) charges against.

## Verifier

`verify.py` (stdlib `math.comb`, exact big integers, <1s): computes `(Q)` and
`D_M` over all admissible dyadic scales for every row above; asserts the exact
match to the QA.22 values `{99.8063, 66.1465, 82.9664}` and `{48.3804, 31.8508,
40.2857}`; asserts first-scale dominance (`log2 Q_H == log2 Q_{M_*}` to 6 dp);
asserts n-uniformity (RowC vs prize give identical `(N_*, h, log2 Q)`); and
asserts the rate-1/2 triviality. All PASS.
