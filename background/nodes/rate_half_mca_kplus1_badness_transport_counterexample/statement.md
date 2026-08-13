# Rate-half MCA K-to-K+1 badness-transport counterexample

- **status:** PROVED
- **closure:** construction
- **scope:** one actual deployed KoalaBear received-line record

## Statement

There is an explicit received line and support on the deployed KoalaBear row
whose slope `0` is support-wise MCA-bad for `RS[F,D,k]` but is not
support-wise MCA-bad after silently replacing the code dimension by `k+1`.

Take the deployed subgroup `D=<zeta>` of order `n=2^21`, put

```text
e=67473,
E={zeta^i: 0<=i<e},
S={zeta^i: e<=i<e+m},
u=1_E,
v(x)=x^k.
```

Then `|S|=m`, `u=0` on `S`, and `h=0` is an actual slope-zero explanation.
For dimension `k`, no polynomial of degree less than `k` agrees with `v` on
`S`, so the pair is not simultaneously explained there.  For dimension
`k+1`, the pair `(0,X^k)` is a valid simultaneous explanation on the same
support.  Hence badness and first-owner semantics are not invariant under the
dimension substitution.

## Consequence

Any `K=k+1` prefix-envelope adapter used for the actual `degree<k` MCA
problem must explicitly preserve or recheck the degree-`<k` explanation and
pair-noncontainment guards.  A numerical shifted-profile match or an
inclusion of code spaces is insufficient.  This is the hostile regression
required by condition 4 of the proposed `SEM-QBC` interface and by any direct
S/A/E whole-line selector using the same witness substrate.

## Nonclaims

This does not refute an adapter that retains the original degree guard.  It
does not assign the pole-line `d1=67473` record to Q or BC, prove an endpoint
relation, bound a slope set, or close any row.

## Falsifier

Failure of the deployed subgroup or support arithmetic, existence of a
degree-less-than-`k` polynomial agreeing with `X^k` on `m>k` points, or
failure of `(0,X^k)` to belong to the dimension-`k+1` code.
