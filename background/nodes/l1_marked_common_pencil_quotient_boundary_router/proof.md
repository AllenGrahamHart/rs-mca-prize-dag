# Proof - L1 marked common-pencil quotient-boundary router

## 1. Canonical locator factorization

The fibers in `(QB1)` are disjoint. Every fiber contained in `D` is therefore
selected by `A_full(D)`, and removing their union leaves a unique set `B_D`.
By maximality of `A_full(D)`, this boundary contains no complete fiber.

The locator of a disjoint union is the product of its monic locators. Since
`L_(T_a)=P-a`, one obtains

```text
L_D=L_(B_D) product_(a in A_full(D)) L_(T_a)
   =L_(B_D) product_(a in A_full(D))(P-a).
```

This proves existence in `(QB3)`. Its set-theoretic construction also proves
uniqueness. Alternatively, the complete fiber factors `P-a` have disjoint
root sets, and the remaining squarefree factor has no complete such root
set, so no fiber factor can move between the two terms.

Taking degrees in the disjoint union gives

```text
d=beta+ell |A_full(D)|,
```

which proves `(QB4)`.

## 2. Counting fixed-boundary fibers

Fix the support/mark chart and a boundary `B`. A full-label set `A_0` counted
by `Q(B)` determines `D`, hence the monic squarefree locator `F_D`, uniquely
by `(QB3)`. Conversely every defect locator with this boundary supplies one
such label set. Thus there is no locator multiplicity over the pair
`(B,A_0)`.

The proved `l1_marked_common_pencil_crt_fiber_bound` applies to the selected
Forney stratum. For fixed supports, marks, and `F_D`, it gives at most one
numerator above the lower endpoint and at most `q^(2p)` numerators at the
endpoint. The latter bound is valid uniformly throughout the window, so the
number of codewords over fixed `B` is at most

```text
q^(2p) Q(B).
```

Summing over all admissible boundaries of size `beta` proves the first part
of `(QB5)`. There are at most `binom(|C|,beta)` such boundaries, and
`p<=P_0`, which proves the second part.

For fixed `B_0`, summing over `beta<=B_0` introduces at most

```text
sum_(beta=0)^B_0 binom(|C|,beta) <= (B_0+1)n^B_0.
```

Since `q=poly(n)` and `P_0,B_0` are fixed, this and `q^(2P_0)` are
polynomial factors with fixed exponents. A super-polynomial family that
remains in the box can therefore only come from a super-polynomial value of
one of the quotient-core counts `Q(B)`. If no fixed boundary box contains
such a quotient census, the boundary size must escape every fixed `B_0`.

## 3. Why no quotient payment is inferred

Factorization of the missed-core locator through `P` is not factorization of
the received word or of the listed codeword. The full agreement set can have
trivial stabilizer. This is exactly the scope distinction proved in
`pma_quotient_closure_scope`; consequently `(QB5)` is a router into the
quotient-core census, not a charge to `pma_exact_periodic_owner`.

