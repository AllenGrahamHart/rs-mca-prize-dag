# Audit - L1 polarized petal-entropy ledger

## Checked axes

1. Untouched and full petals both have polarized cost zero but are retained
   as two separate orientations; this is the load-bearing `2^M` factor.
2. `binom(ell,a_i)=binom(ell,ell-a_i)` justifies charging the smaller side.
3. The exact support choices factor over disjoint petals; no global
   `binom(t ell,h)` relaxation is used.
4. The root-pinning factor is charged after the exact pattern is fixed.
5. The sum over defects costs one factor `k<=n`; no uniqueness in `d` is
   assumed.
6. The polynomial conclusion fixes `E` before the row varies.

## Remaining attack

The live support entropy is `p+e->infinity`. A sparse petal is no longer
expensive merely because its deficit from fullness is large; a counterexample
must carry growing sparse/full description length or growing root excess.
