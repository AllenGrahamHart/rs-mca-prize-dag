# Proof

## The sign product

Changing `r_j` to `-r_j` for `j>=2` permutes the factors in `(USR1)`. For
`j=1`, negate every sign vector after changing `r_1`; each of the 32 factors
acquires a minus sign, whose total product is one. Hence every `r_j` occurs
only to even powers, so `(USR1)` lies in `Z[y_1,...,y_6]`.

The factors are naturally indexed by sign vectors modulo simultaneous global
negation. Permuting the six coordinates permutes these classes. Any
re-normalization that negates a representative factor negates exactly 16
factors, so the total sign is again one. Therefore `Psi_6` is symmetric.
There are 32 linear factors in the `r_i`; replacing even powers `r_i^(2d)`
by `y_i^d` proves homogeneity of degree 16.

In odd characteristic the ambient ring is a field. A product of the 32
linear factors vanishes exactly when one factor vanishes. Distinct `y_i`
mean that no two selected square roots are equal or antipodal, so every
factor is precisely a reduced signed lift. This proves assertions 1 and 2.

## Norm support

The preceding invariance puts `Psi_6` in `K_0`. Multiplicativity of the norm
gives

```text
product_[epsilon] Norm_(K/Q)(S_epsilon)
  = Norm_(K/Q)(product_[epsilon] S_epsilon)
  = Norm_(K/Q)(Psi_6)
  = Norm_(K_0/Q)(Psi_6)^2,
```

because `[K:K_0]=2`. This proves `(USR2)` and equality of rational prime
supports. Every signed sum is nonzero in characteristic zero: after reducing
signs into exponents it is a nonzero polynomial of degree below 256 evaluated
at `zeta_512`, whose minimal polynomial has degree 256. Thus all norm prime
supports in this sentence are well-defined.

## Orbit quotient and sectors

Squaring sends a signed order-512 exponent to an exponent in `Z/256`.
Translation and odd dilation descend to `x -> ax+b`, with
`a in (Z/256)^*`; the two lifts of `a` modulo 512 differ only by sign choices,
which have already been aggregated. Conversely every such affine map lifts,
so this is the exact orbit action.

For a six-subset `S`, the parity of `sum_(x in S)x` is preserved: odd
dilation preserves parity and translation adds `6b`. If the sum is even,
`6b=-sum S mod256` is soluble; if it is odd,
`6b=1-sum S mod256` is soluble. In either case the two solutions differ by
128 and are already in the same translation orbit. Thus the sectors have the
printed product normalizations.

For each of the `128*256=32,768` affine maps, decompose its permutation of
`Z/256` into cycles. An invariant six-subset is a union of cycles. Multiplying
the cycle polynomials while tracking subset size and exponent-sum parity
gives fixed-point totals

```text
even: 197,438,898,176
odd:  184,310,267,904.
```

Division by 32,768 gives `(USR3)`. The primary verifier reconstructs every
cycle record and its digest; the independent audit recomputes the two
Burnside sums with a separate dictionary-valued generating-function
implementation.
