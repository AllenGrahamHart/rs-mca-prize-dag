# Rate-half MCA two-anchor reserve repricing

- **status:** PROVED
- **closure:** proof
- **scope:** deployed KoalaBear and Mersenne-31 MCA adjacent rows

## Statement

Put the proved near-rational first-match owner before the residual exception
set.  If its charge is `2w` and the residual exception cap remains `31`, the
large rational-owner target in the active conditional MCA assembly must be

```text
B_owner^(2w)(g) <= B*-(2w+31)-(n-g).                 (RR1)
```

It cannot retain the printed `B*-31-(n-g)` target by placing near-rational
slopes inside the exception set, because `2w>31` on both rows.  With `(RR1)`,
the conditional assembly arithmetic is exact: the near-rational owner,
exception set, crossing slopes, and owner-contained slopes sum to at most
`B*` in the large-owner branch.  Every smaller-owner or global-affine branch
retains a positive margin.

The exact revised targets are

| row | `2w+31` | `g_min=2m-K+1` target | full-owner target |
|---|---:|---:|---:|
| KoalaBear | 134,975 | 274,980,728,110,346,481 | 274,980,728,111,260,112 |
| Mersenne-31 | 134,927 | 15,728,609 | 16,642,288 |

Using the proved exact average ceilings, the full-owner targets retain
integer factors at least `4,807,520` and `9`, respectively.  Thus the probe
does not arithmetically falsify the direct S/A/E route, but it prices the
route honestly: the large-owner input and source interface must be reissued
at a target smaller by exactly `2w`.

## Nonclaims

No revised large-owner bound, spread theorem, exception-routing theorem,
whole-line selector, safe row, or prize threshold is proved.  The Mersenne
row is an arithmetic stress row outside the official smooth-domain
quantifier.

## Falsifier

An incorrect source pin, row parameter, target, branch margin, or exact-sum
identity; or a proof that the `2w` set can be absorbed in the same set whose
cardinality is bounded by `31` without a separate owner or containment
theorem.
