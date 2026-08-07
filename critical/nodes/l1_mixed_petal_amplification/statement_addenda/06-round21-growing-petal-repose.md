# Round-21 growing-petal diagnosis

**The growth parameter of this bucket is petal size `ell`, not `n`.**
For a maximal-source chart (`|C| = k-1`, `t` petals of size `ell`,
background `b < ell`, `t*ell + b = n-k+1`), the floor band plus the
agreement threshold force (verified at 45 cells)

```text
#core kept a <= Lambda := 2*ell + b - 2,   #petal lost om <= Lambda + 1 - sigma
=>  the bucket is EMPTY when sigma > Lambda, and otherwise
    BOX = Theta(C(k-1,Lambda) * C(t*ell,Lambda)) = Theta(n^{2*Lambda}).
```

At `ell = 2, b = 1` (the only cell the N10 census ever ran):
`Lambda = 3`, `BOX = Theta(n^6)` with exact leading term `n^6/2304`.
Thus the census's registered super-polynomial falsifier could never fire
there, for any received word, as a counting fact. The retained counts are the
random-word law `BOX/q` to 0.4-2% at `n = 32, 64`.

**Consumer contract quantified** (`imgfib` plus the `petal_growth` budget):
the mixed bucket must fit inside 719 columns of `C(n+6,6)` at exponent 6; at
`ell = 2` it occupies 0.31 columns, discharged by counting unconditionally
for every received word. By the listing inequality
`k-1+ell >= k+sigma`, a contributor at the corrected reserve
(`sigma = Theta(n/log n)` at official rows) needs
`ell = Omega(n/log n)`, where `BOX = n^{Theta(n/log n)}`. The census regime
and the consumer regime are separated by `Theta(n/log n)` in the one
parameter that controls the object.

## Re-pose of record (L1-MPA-w)

- **Clause (a), proved by unconditional counting:** the contribution is zero
  when `sigma > 2*ell+b-2`, and otherwise is at most `BOX(ell,b)`.
- **Clause (b), the open target:** for charts with growing `ell`, namely
  `ell >= sigma+1` and hence `ell = Omega(n/log n)` at official rows, the
  contribution is `n^B` for an absolute `B`. This clause carries the entire
  open content; it is not a counting fact.
- Pre-registered falsifiers are **(F-w1)** an `ell`-sweep word whose retained
  count exceeds `10*BOX(ell)/q`, and **(F-w2)** any mixed floor-band
  contributor with `sigma > 2*ell+b-2`.

## Adversarial evidence at fixed `ell`

The mandatory attempt failed. Exhaustion over all 830,490 legal chart words
at `n = 16` gave maximum 66 versus mean 32.1 (2.05x). At `n = 32`, the best
found was 3,273 (the minimal-degree word `deg U = k+1`, a consistent 16%
structural excess, +11 sigma) versus mean 2,805. Both pre-registered escape
tests remained silent.

The observed mechanism is exact-shell suppression: adversarial degeneracy
spikes the linear-algebra filter (268,026, or 69x its mean), but exact
agreement collapses the spike (122, or 22x below its mean). Degenerate words
make codewords agree on larger sets, promoting them out of this bucket into
higher-agreement strata. At fixed `ell` the exact-agreement bucket is
self-limiting. The measured danger is the growing-petal direction: increasing
`ell` by one buys more than doubling `n` (17.1x at `ell=2 -> 3`, and 44.1x at
`ell=2 -> 4`, with `n=24` fixed).

## Cross-lane audit

No current band-lane instrument applies. The routes
`xr_pencil_forcing_t0`, cascade, L-A, L-B, and Lemma R fail at hypothesis
level because petal agreement sets meet in `|C|=k-1<k+1` and petal points
have multiplicity one. The exact ambient match
`pma_arbitrary_petal_source_realizability` is a route cut: maximality does not
force a common pencil. The ternary object matches the ambient half-system of
`mu_n` in odd characteristic but has no `Lambda`, so no `tau` can be formed.

Census evidence is not proof. The BOX identities and closed form are
derivations, machine-checked by `d2_growth_law.py`, `d2_danger_map.py`,
`d3_ell_sweep.py`, `a3_exhaustive_exact.py`, and `a5_scale32.py`; all were
coordinator-replayed. Full provenance is in
`notes/pilots_20260807/l1_pma_diag/`.
