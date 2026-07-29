# Audit

## Quantifier checks

- Both collision vectors use the same row, primitive quotient root, and
  cofactor `2` before the unit ratio is introduced.
- The strict field floor `p>2^255` yields the printed strict deficit bound.
- All 63 nontrivial entropy side sizes are checked; coordinates equal to one
  may be assigned to the positive side.
- Jensen's inequalities make the two-level calculation a universal extremal
  bound, not an ansatz about collision vectors.
- `Q(v)` has degree dividing `64`; a nontrivial degree is therefore even.
- The Mahler measure lies in `K+` because `K+/Q` is Galois and every signed
  conjugate factor belongs to `K+`.
- Ramification excludes `Q(sqrt(5))` from `K+`; no unproved equality-case
  classification for Schinzel's theorem is used.

## Independent arithmetic

`verify.py` uses the hash-pinned directed-Decimal logarithm engine from the
high-cofactor node. `verify_audit.py` reconstructs every logarithm with exact
rational atanh series and explicit tails. Both check all 63 entropy cases,
the cofactor-`2` deficit, the exact rational signs of Smyth's second
polynomial, and the separation

```text
63.878 < 256 log(1.29).
```

## Scope ruling

The maximum profile now costs at most four shift/sign orbits. This is a
substantial payment, but it does not by itself bound the exact weighted sum
over all lower profiles.

