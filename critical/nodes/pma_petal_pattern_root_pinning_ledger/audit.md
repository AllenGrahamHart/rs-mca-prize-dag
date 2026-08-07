# Audit - PMA petal-pattern root-pinning ledger

## Checked axes

1. The interpolation support is only the exact petal agreement pattern. This
   is intentional: once `(F,W)` is fixed, background roots add no multiplicity.
2. Maximality `b<ell` is load-bearing. It gives `h>d`; without it the base
   polynomial can meet the list threshold using background alone.
3. Exact defect is load-bearing. It gives `deg F=d` and `gcd(F,W)=1`, which
   are required for maximal rank.
4. `e=2d+1-h` has the `+1` forced by the target width
   `w_Y=h-d-1`.
5. `binom(t ell,h)` is an upper bound, not an assertion that every selected
   subset touches all `t` petals or is algebraically realizable.
6. The polynomial corollary requires fixed `E`. It does not turn an
   unbounded exponent into one family-uniform polynomial.
7. The theorem counts codewords, not auxiliary support representatives:
   fixed `(F,Y)` determines `W` because `h>d`.

## Adversarial controls

The verifier exhausts several small maximal sunflower receivers, checks the
fixed-pattern rank and locator counts, and compares every realized
`(d,t,h)` stratum with `(PRP1)`. It also checks:

- a nonmaximal background-only listed word with `h<=d`;
- an unsaturated common-factor pair whose selected-support rank is not
  maximal;
- uniqueness of the codeword attached to every realized `(F,Y)` key.

## Remaining attack

The live residual has unbounded

```text
u+max(0,2d+1-h).
```

It must be assigned to a legitimate natural-scale quotient/field-drop
profile or bounded by an aggregate theorem that uses the smooth-domain
arithmetic. Raw summation of the binomial ledger is not such a theorem.
