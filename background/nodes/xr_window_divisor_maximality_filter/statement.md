# XR window-divisor maximality filter

- **status:** PROVED
- **purpose:** prevent the raw-subset count from replacing selected
  maximal occupancy

For a received pair `(u,v)`, let `MAX_e` be the number of distinct
codeword pairs whose full joint agreement set has size exactly `k+e`.
Let `RAW_d` count `(k+d)`-sets on which both received words interpolate
to degree-`<k` codewords, equivalently the degree-`n-k-d` locators
satisfying both window systems. Then

```text
RAW_d = sum_{e>=d} MAX_e binom(k+e,k+d).                  (F)
```

More generally, let `Pi` be any predicate of the uniquely reconstructed
maximal pair, such as selected liveness plus survival of the fixed strip
order. Let `MAX_e^Pi` count maximal depth-`e` pairs satisfying `Pi`, and let
`RAW_d^Pi` count their raw `(k+d)`-subsets. Then

```text
RAW_d^Pi=sum_(e>=d) MAX_e^Pi binom(k+e,k+d),             (PF)
```

and finite binomial inversion gives

```text
MAX_d^Pi=sum_(j>=0)(-1)^j binom(k+d+j,k+d) RAW_(d+j)^Pi. (INV)
```

For `L>=0` define the truncated sieve

```text
S_L^Pi(d)=sum_(j=0)^L(-1)^j
          binom(k+d+j,k+d) RAW_(d+j)^Pi.                 (S)
```

Then the exact Bonferroni inequalities are

```text
S_(2a+1)^Pi(d)<=MAX_d^Pi<=S_(2a)^Pi(d).                 (BON)
```

Thus the target maximal selected occupancy has a support-moment interface
that retains first-match and strip semantics. A closing application must
bound one even truncated sum as a whole, or provide the signed lower and
upper moment controls needed by it. Substituting unrelated upper bounds for
every `RAW` term is invalid because `(S)` has negative coefficients.

The identity remains true before any selected-live-slope filter. A
selected maximal depth-`d` pair contributes exactly one locator to
`N_d`; a deeper pair contributes zero to `N_d` but
`binom(k+e,k+d)` locators to `RAW_d`. Therefore a bound on all divisors
in the affine window intersection is not equivalent to SL-2 and is in
general false at its `17n^2/25` threshold.

The exact residual object must impose both:

1. **maximality:** the reconstructed pair disagrees in at least one
   coordinate at every point of `T`, so its full joint core is `H\T`;
2. **selection/liveness:** that maximal pair has `L_P>=2` under the
   support-wise first-match selector.

The two single-word window matrices each have rank `d`, but this also
does not imply joint codimension `2d`; their row spaces can intersect.

## Falsifier

A raw locator not lying over a unique maximal joint pair, or failure of
the fiber identity `(F)`, predicate-filtered inversion `(INV)`, or either
parity in `(BON)`.
