# Attack plan

## Exact object

Audit `N_d`, not a raw Reed-Solomon list. Every candidate must pass the
full tangent gate, the ratified strip order, support-wise first-match
selection, `k`-packing, and the requirement of at least two selected
live slopes. The cascade tier `d=h-1` is outside this node.

## Route 1: inverse theorem

Prove that `25N_d>17n^2` forces a large subfamily whose core-complement
locators satisfy the MC vanishing window and are unions of cosets of
`mu_M`, with `M=2^ceil(log2 d)`. The existing depth-quantization and
parity theorem then excludes that subfamily because the official
`h=2^s+1` has no productive structured depth in
`[ceil(h/2),h-2]`. The missing step is finite-characteristic and must
not import the characteristic-zero Lam-Leung classification without a
lifting or norm argument.

## Route 2: windowed projection

For

```text
W_d(z)=#{c in RS_k : k+d <= agr(c,w_z) <= A-2},
beta_d=floor((n-k-d)/(h-d-1)),
```

it is sufficient to prove

```text
25 sum_z W_d(z) <= 17 n^2 (q+1-beta_d).
```

This is stronger than the target because `W_d(z)` includes codewords
which may never assemble into a selected joint pair. A counterexample
to this sufficient inequality is a route cut, not a node falsifier.

## Route 3: finite-characteristic accident ledger

Separate characteristic-zero coset solutions from mod-`p` accidental
solutions. Associate each accidental orbit with a nonzero cyclotomic
obstruction norm divisible by the generated-field prime. Seek either:

1. an orbit bound below `17n/25`, since each multiplicative orbit has
   at most `n` supports; or
2. a low-height common obstruction forced by more than `17n^2/25`
   selected pairs, contradicting the `p>=2^250` field pin.

Any computation must be a bounded falsification pilot on Modal and
must emit partial checkpoints. Toy survival is evidence only because
the known toy regimes are list-subcritical.

## Immediate no-go fences

- Do not use a single-word Johnson bound: the agreement window is far
  below Johnson at the prize rows.
- Do not count raw `(k+d)`-subsets inside deeper agreements: that
  overcounts maximal joint cores exponentially.
- Do not infer `(SL2)` from a slope count; the banked slope-side route
  requires a stronger bound than the program owns.
- Do not call every non-MC support "non-coset" as a theorem. The
  finite-characteristic completeness statement is precisely open.
