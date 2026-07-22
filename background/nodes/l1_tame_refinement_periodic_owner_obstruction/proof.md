# Proof - L1 tame-refinement periodic-owner obstruction

## 1. Complete tame fibers

The involution preserving `P=X^2+3X` is

```text
iota(x)=-3-x.
```

It pairs `(1,13)`, `(2,12)`, and `(3,11)`. Direct substitution gives the
three distinct values in `(PO2)`. Since `P-a` is monic of degree two and has
the displayed two distinct roots, each pair is a complete polynomial fiber.
Their union is `T`, and `17` is coprime to `ell/2=3`, so the refinement is in
the tame scope of `l1_tame_fixed_petal_refinement_census`.

## 2. Exact listed support

The sets in `(PO1)` are disjoint, with

```text
|C|=7=k-1,       |T|=6=ell,       |R|=3<ell.
```

By `(PO3)`, the zero polynomial agrees with `U` exactly on `A=C union T`.
Its agreement count is `7+6=13=k+sigma`, so it is an exact listed codeword in
the relevant source-petal chart datum.

## 3. Trivial multiplicative stabilizer

Because `A=H\R`, the multiplicative stabilizers of `A` and `R` are equal.
Suppose `aR=R`. Since `4a` belongs to `{4,5,6}`, one has

```text
a in {1,14,10} mod 17.
```

The candidate `a=14` fails because `5a=2`, and `a=10` fails because
`5a=16`. Therefore `a=1`, proving `(PO4)`. In particular `-1=16` does not
stabilize `A`, so this is not the intrinsic degree-two antipodal quotient.

The exact-periodic owner requires stabilizer size greater than one. It cannot
own this contributor even though the source petal is a union of complete tame
fibers. This proves the claimed route obstruction.
