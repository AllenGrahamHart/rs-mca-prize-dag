# U1 official-row norm-gate extraction

## Status and purpose

This is the first-work-item audit for roadmap candidate U1.  It extracts the
actual lower and upper norm currencies used by the banked WCL, HGE4, and C36
proofs.  It is a scope correction, not a new closure and not a claim that a
lane-uniform U1 theorem has been proved.

The roadmap's former schematic phrase

```text
2^f(w) divides Norm(u)
```

is not the common arithmetic statement proved in these packets.  The sound
common envelope is the following elementary norm gate.

Let `K` be a number field, `u` a nonzero algebraic integer, and `p` a row
characteristic.  If `r` distinct prime ideals of `O_K` above `p` divide
`(u)`, then

```text
p^r divides |Norm_(K/Q)(u)|.                         (NG1)
```

Thus a row lower bound `p>=P_0` and an archimedean ceiling
`|Norm(u)|<=G` exclude the witness when

```text
P_0^r>G.                                            (NG2)
```

When `(NG2)` fails, a complete factorization or ideal-support sieve can
still exclude the row primes by testing their congruence, size, and field
conditions.  In particular, `v_2(p-1)>=41` is a filter on an odd prime
factor `p`; it does **not** imply that `2^41` divides `Norm(u)`.  For example,
the norm of the rational integer `p` in any number field is a power of the
odd integer `p`, and is therefore odd.

For comparisons below, define the logarithmic norm headroom

```text
F=r log_2(P_0),       H=F-log_2(G).                 (NG3)
```

Positive `H` proves emptiness.  This `F` is a lower-bound exponent, not a
2-adic valuation of the norm.

## Extracted table

| lane and proved packet | nonzero obstruction | prime-ideal multiplicity `r` | proved ceiling `G` | row gate | actual endpoint |
|---|---|---:|---:|---|---|
| WCL Newton short window, `dli_wcl_newton_short_window_exclusion` | none | n/a | n/a | `char=0` or `char>w` | Newton identities exclude `w<=2ell`; this is not a norm argument |
| WCL terminal weights 3 and 4, `dli_wcl_weight{3,4}_ambient_exclusion` | `P(zeta_512)` | 1 | `w^256` by the conjugate triangle bound | `p<2^256`, `v_2(p-1)>=41` | exact resultant factorization finds no admissible prime; the size inequality alone does not close |
| WCL `(2,5)`, `dli_wcl_ell2_weight5_norm_gcd_exclusion` | pair-router ideal index / two norm gcd | 1 support condition | no uniform closing ceiling used | same official prime filter | all 1,514 pair orbits are factored; maximum factor depth is 18 |
| WCL `(2,6)`, `dli_wcl_ell2_weight6_recursive_norm_exclusion` | saturated pair of cubic-router norms | 1 support condition | no uniform closing ceiling used | same official prime filter | all 404,740 candidates are factored or removed by the vanishing-sum lemma; maximum factor depth is 18 |
| WCL `(1,5)`, `(1,6)`, `(2,7)` descents | Nullstellensatz integer `Delta` | 1 support condition once `Delta` is certified | unknown until a certificate is computed | same official prime filter | finite certificate route only; no `Delta` is yet banked for these slots |
| HGE4 quarter-width, `f3_hge4_cyclotomic_norm_quarter_width_exclusion` | signed support sum `z` | `floor(h/2)` | `(4h)^(m/4)` | `p>m^2` | `(m^2)^r>G` deletes `m/4<=h<m/3` |
| HGE4 ambient-level contraction, `f3_hge4_ambient_norm_level_contraction` | signed support sum `z`; defect split `q` | `floor(h/2)` | `(4h-v_h)^(m/4)` when `q!=0`; `h^(m/4)` on the swap branch, where `v_h=floor((h-1)/2)+2` | official `p>n^2`, retained while `m|n` | exact per-width gate `n^(2 floor(h/2))>=(4h-v_h)^(m/4)`; its closed-form corollary deletes every proper-level width `h>=2 ceil(m log_2(m)/(8 log_2(n)))` and `55,050,457,488` additional official cells |
| HGE4 multiscale Haar product, `f3_hge4_multiscale_haar_m64_level_close` | odd signed sum plus every nonzero dyadic fold of the even defect | all `h-1` moment indices, partitioned by 2-adic valuation | `D^(m/4) product_a Delta_a^(N_a/4)` under the shared Haar budget; zero folds contribute exact powers of two | official `p>n^2`; complete endpoint replay at `m=64` | pays the entire exact level `m=64` at zero debit on every official ambient row; surviving exact levels start at `m=128` |
| HGE4 odd swap, `f3_hge4_swap_norm_haar_band_exclusion` | one-side support sum `z` | `(h-1)/2` | `h^(m/4)` | `p>m^2` | `m^(h-1)>=h^(m/4)` deletes the printed near-quarter band |
| C36 rich fiber, `f3_h3_rich_fiber_norm_cutoff` | one collision `beta_E-beta_F` | 1 | `6^(n/4)` | `p>=n^2` | deletes only `p>6^(n/4)` |
| C36 ideal star, `f3_h3_low_distance_ideal_star_router` | normalized two-generator collision ideal | 1 | `6^(n/4)/4` | `p>=n^2` | finite candidate-prime sieve; it does not delete every prime in the open corridor |

The WCL and C36 ideal packets use divisibility by an ideal norm in places.
For this table that is still a one-prime support condition.  Adding more
generators can shrink the ideal norm and improve candidate filtering, but it
does not manufacture distinct primes above `p` in `(NG1)`.

## DSP8 transfer verdict

The desired satellite is

```text
P(t)<=24
```

at every official row.  A counterexample to it would have `P(t)>=25`, hence
excess `e=P-18>=7`.  The banked multistar ladder then gives a higher-degree
same-target collision ideal, but all its generators vanish at the **same**
prime ideal above `p`.  The proved uniform arithmetic remains

```text
r=1,       p>=n^2,       |N(K)|<=6^(n/4)/4.        (D1)
```

At the first official order `n=8192`, the lower-bound exponent is only

```text
log_2(n^2)=26,
```

whereas the printed upper ceiling has logarithm

```text
(n/4)log_2(6)-2 > 5292.
```

Consequently the existing C36 norm-size argument has no analytic route to
`P<=24`.  The stronger star degree improves the finite sieve but does not
improve the proved `r` or the worst-case `G`.

A norm-gate proof of the DSP8 satellite therefore needs at least one genuinely
new item:

1. a completeness theorem producing many **distinct Galois prime ideals**
   above `p`, so that `r` grows with the complexity;
2. a normalized common-ideal ceiling below `n^2` for every `P>=25` fiber;
3. or a complete engineered-prime factor sieve for the official corridor.

The current cutoff-2 Taylor screen and the richer multistar selectors supply
candidate compression for item 3, not either analytic input 1 or 2.  They
must not be cited as a proof of the satellite.  CR-001 records the exact
outbound computation only after its structural generator and cost gate are
met.

## U1 disposition

The corrected norm gate `(NG1)--(NG2)` is a real shared lemma, but its useful
power comes from lane-specific production of `r` and `G`.  The extraction
currently separates the examples into:

1. a field-uniform Newton mechanism;
2. genuine size contradictions with several conjugate prime ideals (HGE4);
3. one-prime candidate-support sieves (WCL and C36).

The ambient-level HGE4 contraction is the first explicit transfer win from
this audit: it preserves the official row lower bound while descending the
exact-ratio tower, rather than resetting the prime scale to the smaller
level. It remains a broom result because it deletes widths but gives no bound
on the surviving orbit fibers.

Accordingly U1 should remain a roadmap candidate rather than a DAG lemma.
Its DSP8 flagship pose is not proof-ready until a Sidon-strip or other
preprocessing theorem produces one of the three missing items above.  This
does not refute the desired `P<=24` statement; it rules out deriving it from
the currently banked C36 norm inequalities alone.
